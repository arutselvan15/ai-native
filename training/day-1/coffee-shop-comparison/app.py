"""Local web app: pandas loads CSV; browser handles filters and compare (no Streamlit)."""

from __future__ import annotations

import json

from flask import Flask, render_template

import data

app = Flask(__name__)


@app.route("/")
def index():
    reviews = data.load_reviews()
    shops = data.aggregate_shops(reviews)
    neighborhoods = sorted(shops["neighborhood"].unique().tolist())
    payload = shops.to_dict(orient="records")
    return render_template(
        "index.html",
        shops_json=json.dumps(payload),
        neighborhoods=json.dumps(neighborhoods),
        review_count=len(reviews),
        shop_count=len(shops),
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8501, debug=False)
