# Day 1 — independent project

**Focus:** Coffee-shop comparison lab (AI-assisted coding warm-up)

Each training day is its own mini-project: agent rules, planning docs, and implementation live under this folder.

| Resource | Location |
| --- | --- |
| Agent instructions | [`AGENTS.md`](./AGENTS.md) |
| Plan / design / verify | [`docs/`](../../docs/README.md) (repository root) |
| Hands-on lab | [`coffee-shop-comparison/README.md`](./coffee-shop-comparison/README.md) |

## Quick start

1. Read [`coffee-shop-comparison/README.md`](./coffee-shop-comparison/README.md) for lab goals.
2. Follow [`AGENTS.md`](./AGENTS.md): plan and design in repository-root `docs/` before code changes.
3. From the **repository root**, create `.venv`, `pip install -r requirements.txt`, then run the app:

```bash
cd training/day-1/coffee-shop-comparison
./run.sh
# open http://127.0.0.1:8501/
```

## Layout

```text
day-1/
├── AGENTS.md
├── README.md
├── docs/README.md          # redirect → repository-root docs/
└── coffee-shop-comparison/
    ├── README.md
    ├── app.py
    ├── data.py
    ├── run.sh
    └── coffee_shop_reviews.csv

docs/                         # repository root (plan, design, verify)
├── README.md
├── _templates/
└── coffee-shop-comparison/
```
