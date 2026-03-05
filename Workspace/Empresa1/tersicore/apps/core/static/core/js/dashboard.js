/* ============================================================
   DASHBOARD JS – Tersicore ERP
   ============================================================ */

/* ------------------------------------------------------------
            KPI Animation
   ------------------------------------------------------------ */
function animateKPI(element, finalValue, duration = 1200) {
    let start = 0;
    const increment = finalValue / (duration / 16);

    const counter = setInterval(() => {
        start += increment;
        if (start >= finalValue) {
            start = finalValue;
            clearInterval(counter);
        }
        element.textContent = Math.floor(start);
    }, 16);
}

/* ------------------------------------------------------------
   Chart: Customers by category
   ------------------------------------------------------------ */
function renderCustomersByCategory(labels, data) {
    const ctx = document.getElementById("chartCustomersByCategory");
    if (!ctx) return;

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Customers",
                data: data,
                backgroundColor: "#0d6efd",
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: {
                y: { beginAtZero: true, ticks: { stepSize: 1 } }
            }
        }
    });
}

/* ------------------------------------------------------------
   Chart: Inventory Movements (Monthly)
   ------------------------------------------------------------ */
function renderInventoryMonthlyChart(data) {
    const ctx = document.getElementById("inventoryMonthlyChart");
    if (!ctx) return;

    const labels = Object.keys(data);
    const entradas = labels.map(m => data[m].IN);
    const salidas = labels.map(m => data[m].OUT);

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Incoming",
                    data: entradas,
                    backgroundColor: "rgba(75, 192, 192, 0.6)"
                },
                {
                    label: "Outgoing ",
                    data: salidas,
                    backgroundColor: "rgba(255, 99, 132, 0.6)"
                }
            ]
        },
        options: {
            responsive: true,
            scales: { y: { beginAtZero: true } }
        }
    });
}

/* ------------------------------------------------------------
   Dashboard Initialization
   ------------------------------------------------------------ */
document.addEventListener("DOMContentLoaded", () => {

    /* 1. Animate static KPIs (customers, products) */
    document.querySelectorAll("[data-kpi]").forEach(el => {
        const value = parseInt(el.getAttribute("data-kpi"));
        animateKPI(el, value);
    });

    /* 2. Customer chart by category */
    if (window.dashboardData) {
        renderCustomersByCategory(
            window.dashboardData.categories_labels,
            window.dashboardData.categories_counts
        );
    }

    /* 3. KPIs of Sales */
    fetch("/sales/api/kpis/")
        .then(res => res.json())
        .then(data => {
            document.getElementById("kpi_sales_today").innerText = data.sales_today;
            document.getElementById("kpi_sales_month").innerText = data.sales_month;
            document.getElementById("kpi_sales_count").innerText = data.count_orders;
            document.getElementById("kpi_ticket_avg").innerText = data.ticket_avg.toFixed(2);
        })
        .catch(err => console.error("Error cargando KPIs de ventas:", err));

    /* 4. KPIs of Inventory */
    fetch("/inventory/api/kpis/")
        .then(res => res.json())
        .then(data => {
            document.getElementById("inv_low_stock").innerText = data.low_stock;
            document.getElementById("inv_total_products").innerText = data.total_products;
            document.getElementById("inv_total_stock").innerText = data.total_stock;
        })
        .catch(err => console.error("Error cargando KPIs de inventario:", err));

    /* 5. List of products with low stock */
    fetch("/inventory/api/low-stock/")
        .then(res => res.json())
        .then(items => {
            const list = document.getElementById("low_stock_list");
            if (!list) return;

            list.innerHTML = "";
            items.forEach(i => {
                const li = document.createElement("li");
                li.classList.add("list-group-item");
                li.innerHTML = `<strong>${i.product}</strong> — ${i.quantity} (mín: ${i.min_stock})`;
                list.appendChild(li);
            });
        })
        .catch(err => console.error("Error cargando lista de stock bajo:", err));

    /* 6. Monthly Inventory Chart */
    fetch("/inventory/api/chart/monthly/")
        .then(res => res.json())
        .then(data => renderInventoryMonthlyChart(data))
        .catch(err => console.error("Error cargando gráfico de inventario:", err));
});