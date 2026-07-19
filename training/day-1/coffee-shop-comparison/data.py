"""Load and aggregate coffee shop review CSV data."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

CSV_PATH = Path(__file__).resolve().parent / "coffee_shop_reviews.csv"

RATING_COLUMNS = (
    "overall_rating",
    "coffee_quality",
    "service_quality",
    "atmosphere",
    "value_score",
)

TABLE_COLUMNS = (
    "shop_name",
    "neighborhood",
    "overall_rating",
    "coffee_quality",
    "service_quality",
    "atmosphere",
    "value_score",
    "avg_price",
    "wait_time_minutes",
    "review_count",
    "wifi_pct",
    "mobile_pct",
)


@dataclass(frozen=True)
class ShopFilters:
    search: str = ""
    neighborhoods: tuple[str, ...] = ()
    min_overall_rating: float = 1.0
    wifi_required: bool = False
    mobile_required: bool = False


def load_reviews() -> pd.DataFrame:
    return pd.read_csv(CSV_PATH)


def _as_bool(series: pd.Series) -> pd.Series:
    if series.dtype == bool:
        return series
    return series.astype(str).str.strip().str.lower().eq("true")


def aggregate_shops(reviews: pd.DataFrame) -> pd.DataFrame:
    df = reviews.copy()
    df["_wifi"] = _as_bool(df["has_wifi"])
    df["_mobile"] = _as_bool(df["mobile_ordering"])

    shops = (
        df.groupby("shop_name", as_index=False)
        .agg(
            neighborhood=("neighborhood", "first"),
            overall_rating=("overall_rating", "mean"),
            coffee_quality=("coffee_quality", "mean"),
            service_quality=("service_quality", "mean"),
            atmosphere=("atmosphere", "mean"),
            value_score=("value_score", "mean"),
            avg_price=("avg_price", "mean"),
            wait_time_minutes=("wait_time_minutes", "mean"),
            review_count=("shop_name", "size"),
            wifi_pct=("_wifi", lambda s: float(s.mean()) * 100.0),
            mobile_pct=("_mobile", lambda s: float(s.mean()) * 100.0),
        )
        .sort_values("shop_name")
        .reset_index(drop=True)
    )
    return shops


def apply_filters(shops: pd.DataFrame, filters: ShopFilters) -> pd.DataFrame:
    result = shops

    if filters.neighborhoods:
        result = result[result["neighborhood"].isin(filters.neighborhoods)]

    if filters.search.strip():
        needle = filters.search.strip()
        result = result[
            result["shop_name"].str.contains(needle, case=False, na=False)
        ]

    result = result[result["overall_rating"] >= filters.min_overall_rating]

    if filters.wifi_required:
        result = result[result["wifi_pct"] >= 50.0]

    if filters.mobile_required:
        result = result[result["mobile_pct"] >= 50.0]

    return result.reset_index(drop=True)


def compare_ratings_frame(
    shop_a: pd.Series, shop_b: pd.Series, metric_labels: tuple[str, ...]
) -> pd.DataFrame:
    return pd.DataFrame(
        {
            shop_a["shop_name"]: [shop_a[col] for col in RATING_COLUMNS],
            shop_b["shop_name"]: [shop_b[col] for col in RATING_COLUMNS],
        },
        index=list(metric_labels),
    )
