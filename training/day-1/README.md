# Day 1 — independent project

**Focus:** Coffee-shop comparison lab (AI-assisted coding warm-up)

Each training day is its own mini-project: agent rules, planning docs, and implementation live under this folder.

| Resource | Location |
| --- | --- |
| Agent instructions | [`AGENTS.md`](./AGENTS.md) |
| Plan / design / verify | [`docs/`](./docs/README.md) |
| Hands-on lab | [`coffee-shop-comparison/README.md`](./coffee-shop-comparison/README.md) |

## Quick start

1. Read [`coffee-shop-comparison/README.md`](./coffee-shop-comparison/README.md) for lab goals.
2. Follow [`AGENTS.md`](./AGENTS.md): plan and design in `docs/` before code changes.
3. Run the app:

```bash
cd coffee-shop-comparison
./serve.sh
# open http://127.0.0.1:8080/index.html
```

## Layout

```text
day-1/
├── AGENTS.md
├── README.md
├── docs/
│   ├── README.md
│   ├── _templates/
│   └── coffee-shop-comparison/
│       ├── plan.md
│       ├── design.md
│       └── verify.md
└── coffee-shop-comparison/
    ├── README.md
    ├── index.html
    ├── serve.sh
    └── coffee_shop_reviews.csv
```
