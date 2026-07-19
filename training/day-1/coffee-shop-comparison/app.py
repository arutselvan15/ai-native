"""Streamlit coffee shop comparison app (Gold tier)."""

from __future__ import annotations

import pandas as pd
import streamlit as st

import data

METRIC_LABELS = ("Overall", "Coffee", "Service", "Atmosphere", "Value")
DISPLAY_COLUMNS = list(data.TABLE_COLUMNS)


@st.cache_data(show_spinner=False)
def load_shop_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    reviews = data.load_reviews()
    shops = data.aggregate_shops(reviews)
    return reviews, shops


def _sidebar_filters(all_neighborhoods: list[str]) -> data.ShopFilters:
    st.sidebar.header("Filters")
    search = st.sidebar.text_input("Search shop name", key="filter_search")
    neighborhoods = st.sidebar.multiselect(
        "Neighborhood",
        options=all_neighborhoods,
        default=all_neighborhoods,
        key="filter_neighborhoods",
    )
    min_rating = st.sidebar.slider(
        "Minimum overall rating",
        min_value=1.0,
        max_value=5.0,
        value=1.0,
        step=0.1,
        key="filter_min_rating",
    )
    wifi_required = st.sidebar.checkbox("WiFi in ≥50% of reviews", key="filter_wifi")
    mobile_required = st.sidebar.checkbox(
        "Mobile ordering in ≥50% of reviews", key="filter_mobile"
    )

    if st.sidebar.button("Reset filters", key="filter_reset"):
        st.session_state["filter_search"] = ""
        st.session_state["filter_neighborhoods"] = all_neighborhoods
        st.session_state["filter_min_rating"] = 1.0
        st.session_state["filter_wifi"] = False
        st.session_state["filter_mobile"] = False
        st.rerun()

    return data.ShopFilters(
        search=search,
        neighborhoods=tuple(neighborhoods),
        min_overall_rating=min_rating,
        wifi_required=wifi_required,
        mobile_required=mobile_required,
    )


def _pick_shops(shop_names: list[str]) -> tuple[str | None, str | None]:
    if len(shop_names) < 2:
        return (shop_names[0] if shop_names else None, None)

    col_a, col_b = st.columns(2)
    with col_a:
        shop_a = st.selectbox("Shop A", shop_names, key="compare_shop_a")
    with col_b:
        default_b = shop_names[1] if shop_names[1] != shop_a else shop_names[0]
        shop_b = st.selectbox(
            "Shop B",
            shop_names,
            index=shop_names.index(default_b),
            key="compare_shop_b",
        )
    return shop_a, shop_b


def main() -> None:
    st.set_page_config(
        page_title="Coffee Shop Comparison",
        page_icon="☕",
        layout="wide",
    )
    st.markdown(
        """
        <style>
          div[data-testid="stMetricValue"] { font-size: 1.35rem; }
          h1 { margin-bottom: 0.1rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    reviews, shops = load_shop_data()
    all_neighborhoods = sorted(shops["neighborhood"].unique().tolist())

    st.title("Coffee Shop Comparison")
    st.caption(
        f"Loaded **{len(reviews):,}** reviews aggregated into **{len(shops)}** shops."
    )

    filters = _sidebar_filters(all_neighborhoods)
    filtered = data.apply_filters(shops, filters)

    st.subheader("All shops")
    if filtered.empty:
        st.warning("No shops match these filters. Adjust or reset filters in the sidebar.")
        return

    display = filtered[DISPLAY_COLUMNS].round(
        {"avg_price": 2, "wait_time_minutes": 1, "wifi_pct": 0, "mobile_pct": 0}
    )
    for col in ("overall_rating", "coffee_quality", "service_quality", "atmosphere", "value_score"):
        display[col] = display[col].round(2)
    st.dataframe(display, use_container_width=True, hide_index=True)

    shop_names = filtered["shop_name"].tolist()
    st.subheader("Compare")
    shop_a_name, shop_b_name = _pick_shops(shop_names)

    if shop_a_name and shop_b_name and shop_a_name != shop_b_name:
        row_a = filtered.loc[filtered["shop_name"] == shop_a_name].iloc[0]
        row_b = filtered.loc[filtered["shop_name"] == shop_b_name].iloc[0]
        delta = float(row_a["overall_rating"] - row_b["overall_rating"])

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"**{shop_a_name}**")
            st.metric("Overall rating", f"{row_a['overall_rating']:.2f}", f"{delta:+.2f} vs B")
            st.metric("Avg price ($)", f"{row_a['avg_price']:.2f}")
            st.metric("Wait (min)", f"{row_a['wait_time_minutes']:.1f}")
        with col_b:
            st.markdown(f"**{shop_b_name}**")
            st.metric("Overall rating", f"{row_b['overall_rating']:.2f}")
            st.metric("Avg price ($)", f"{row_b['avg_price']:.2f}")
            st.metric("Wait (min)", f"{row_b['wait_time_minutes']:.1f}")

        st.subheader("Visualizations")
        compare_df = data.compare_ratings_frame(row_a, row_b, METRIC_LABELS)
        st.markdown("**Rating comparison (Shop A vs Shop B)**")
        st.bar_chart(compare_df)

        rating_by_shop = filtered.set_index("shop_name")[["overall_rating"]]
        st.markdown("**Overall rating by shop (filtered)**")
        st.bar_chart(rating_by_shop)

        scatter_df = filtered[["avg_price", "wait_time_minutes"]].copy()
        scatter_df.index = filtered["shop_name"]
        st.markdown("**Price vs wait time (filtered shops)**")
        st.scatter_chart(scatter_df, x="avg_price", y="wait_time_minutes")
    elif shop_a_name and shop_b_name:
        st.info("Pick two different shops to compare.")
    else:
        st.info("Select at least two shops in the filtered list to compare.")


if __name__ == "__main__":
    main()
