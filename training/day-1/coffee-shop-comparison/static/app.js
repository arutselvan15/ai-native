const RATING_KEYS = [
  "overall_rating",
  "coffee_quality",
  "service_quality",
  "atmosphere",
  "value_score",
];
const RATING_LABELS = ["Overall", "Coffee", "Service", "Atmosphere", "Value"];

let compareChart;
let ratingChart;
let scatterChart;

function filterShops(shops, state) {
  return shops.filter((s) => {
    if (state.search && !s.shop_name.toLowerCase().includes(state.search.toLowerCase())) {
      return false;
    }
    if (state.neighborhoods.size && !state.neighborhoods.has(s.neighborhood)) {
      return false;
    }
    if (s.overall_rating < state.minRating) {
      return false;
    }
    if (state.wifiRequired && s.wifi_pct < 50) {
      return false;
    }
    if (state.mobileRequired && s.mobile_pct < 50) {
      return false;
    }
    return true;
  });
}

function readFilterState() {
  const search = document.getElementById("search").value.trim();
  const neighborhoods = new Set(
    [...document.querySelectorAll(".nb-checkbox:checked")].map((el) => el.value),
  );
  const minRating = Number(document.getElementById("min-rating").value);
  return {
    search,
    neighborhoods,
    minRating,
    wifiRequired: document.getElementById("wifi-required").checked,
    mobileRequired: document.getElementById("mobile-required").checked,
  };
}

function fmt(n, d = 2) {
  return Number(n).toFixed(d);
}

function renderTable(filtered) {
  const tbody = document.querySelector("#shops-table tbody");
  tbody.replaceChildren();
  for (const s of filtered) {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${s.shop_name}</td>
      <td>${s.neighborhood}</td>
      <td>${fmt(s.overall_rating)}</td>
      <td>${fmt(s.coffee_quality)}</td>
      <td>${fmt(s.service_quality)}</td>
      <td>${fmt(s.atmosphere)}</td>
      <td>${fmt(s.value_score)}</td>
      <td>${fmt(s.avg_price)}</td>
      <td>${fmt(s.wait_time_minutes, 1)}</td>
      <td>${s.review_count}</td>
      <td>${fmt(s.wifi_pct, 0)}%</td>
      <td>${fmt(s.mobile_pct, 0)}%</td>`;
    tbody.appendChild(tr);
  }
}

function syncSelect(selectEl, names, current) {
  const prev = current || selectEl.value;
  selectEl.replaceChildren();
  for (const name of names) {
    const opt = document.createElement("option");
    opt.value = name;
    opt.textContent = name;
    selectEl.appendChild(opt);
  }
  if (names.includes(prev)) {
    selectEl.value = prev;
  } else if (names.length) {
    selectEl.value = names[0];
  }
}

function resolveCompare(filtered, pickA, pickB) {
  const names = filtered.map((s) => s.shop_name);
  if (names.length < 2) {
    return { a: names[0] || "", b: "", names };
  }
  let a = names.includes(pickA) ? pickA : names[0];
  let b = names.includes(pickB) ? pickB : names[1];
  if (b === a) {
    b = names.find((n) => n !== a) || names[0];
  }
  return { a, b, names };
}

function shopByName(filtered, name) {
  return filtered.find((s) => s.shop_name === name);
}

function renderCompare(filtered) {
  const selA = document.getElementById("shop-a");
  const selB = document.getElementById("shop-b");
  const { a, b, names } = resolveCompare(filtered, selA.value, selB.value);
  syncSelect(selA, names, a);
  syncSelect(selB, names, b);

  const panel = document.getElementById("compare-panel");
  const hint = document.getElementById("compare-hint");
  const charts = document.getElementById("charts");

  if (names.length < 2) {
    panel.classList.add("hidden");
    charts.classList.add("hidden");
    hint.textContent = "Need at least two shops in the filtered list to compare.";
    hint.classList.remove("hidden");
    return;
  }

  hint.classList.add("hidden");
  panel.classList.remove("hidden");

  if (selA.value === selB.value) {
    charts.classList.add("hidden");
    hint.textContent = "Pick two different shops to compare.";
    hint.classList.remove("hidden");
    return;
  }

  charts.classList.remove("hidden");
  const rowA = shopByName(filtered, selA.value);
  const rowB = shopByName(filtered, selB.value);
  if (!rowA || !rowB) {
    return;
  }

  document.getElementById("metrics-a").innerHTML = metricCards(rowA, rowB.overall_rating);
  document.getElementById("metrics-b").innerHTML = metricCards(rowB);

  updateCharts(filtered, rowA, rowB);
}

function metricCards(shop, otherOverall) {
  const delta =
    otherOverall !== undefined
      ? ` <small>(${fmt(shop.overall_rating - otherOverall, 2)} vs B)</small>`
      : "";
  return `
    <div class="metric"><span>Overall</span><strong>${fmt(shop.overall_rating)}${delta}</strong></div>
    <div class="metric"><span>Avg price</span><strong>$${fmt(shop.avg_price)}</strong></div>
    <div class="metric"><span>Wait (min)</span><strong>${fmt(shop.wait_time_minutes, 1)}</strong></div>`;
}

function updateCharts(filtered, rowA, rowB) {
  const compareCtx = document.getElementById("compare-chart");
  compareChart?.destroy();
  compareChart = new Chart(compareCtx, {
    type: "bar",
    data: {
      labels: RATING_LABELS,
      datasets: [
        {
          label: rowA.shop_name,
          data: RATING_KEYS.map((k) => rowA[k]),
        },
        {
          label: rowB.shop_name,
          data: RATING_KEYS.map((k) => rowB[k]),
        },
      ],
    },
    options: { responsive: true, maintainAspectRatio: false },
  });

  const ratingCtx = document.getElementById("rating-chart");
  ratingChart?.destroy();
  ratingChart = new Chart(ratingCtx, {
    type: "bar",
    data: {
      labels: filtered.map((s) => s.shop_name),
      datasets: [{ label: "Overall rating", data: filtered.map((s) => s.overall_rating) }],
    },
    options: { responsive: true, maintainAspectRatio: false, indexAxis: "y" },
  });

  const scatterCtx = document.getElementById("scatter-chart");
  scatterChart?.destroy();
  scatterChart = new Chart(scatterCtx, {
    type: "scatter",
    data: {
      datasets: [
        {
          label: "Shops",
          data: filtered.map((s) => ({
            x: s.avg_price,
            y: s.wait_time_minutes,
            label: s.shop_name,
          })),
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      parsing: false,
      plugins: {
        tooltip: {
          callbacks: {
            label(ctx) {
              const p = ctx.raw;
              return `${p.label}: $${fmt(p.x)} / ${fmt(p.y, 1)} min`;
            },
          },
        },
      },
      scales: {
        x: { title: { display: true, text: "Avg price ($)" } },
        y: { title: { display: true, text: "Wait (min)" } },
      },
    },
  });
}

function renderEmpty(message) {
  document.querySelector("#shops-table tbody").replaceChildren();
  document.getElementById("empty-msg").textContent = message;
  document.getElementById("empty-msg").classList.remove("hidden");
  document.getElementById("compare-panel").classList.add("hidden");
  document.getElementById("charts").classList.add("hidden");
  document.getElementById("compare-hint").classList.add("hidden");
}

function render() {
  const filtered = filterShops(window.ALL_SHOPS, readFilterState());
  document.getElementById("filtered-count").textContent = String(filtered.length);
  const empty = document.getElementById("empty-msg");
  if (!filtered.length) {
    renderEmpty("No shops match these filters. Adjust or reset filters.");
    return;
  }
  empty.classList.add("hidden");
  renderTable(filtered);
  renderCompare(filtered);
}

function resetFilters() {
  document.getElementById("search").value = "";
  document.querySelectorAll(".nb-checkbox").forEach((el) => {
    el.checked = true;
  });
  document.getElementById("min-rating").value = "1";
  document.getElementById("wifi-required").checked = false;
  document.getElementById("mobile-required").checked = false;
  render();
}

function initApp() {
  document.getElementById("search").addEventListener("input", render);
  document.getElementById("min-rating").addEventListener("input", render);
  document.getElementById("wifi-required").addEventListener("change", render);
  document.getElementById("mobile-required").addEventListener("change", render);
  document.querySelectorAll(".nb-checkbox").forEach((el) => el.addEventListener("change", render));
  document.getElementById("shop-a").addEventListener("change", render);
  document.getElementById("shop-b").addEventListener("change", render);
  document.getElementById("reset-btn").addEventListener("click", resetFilters);
  render();
}

document.addEventListener("DOMContentLoaded", initApp);
