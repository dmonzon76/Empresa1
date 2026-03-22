console.log("Dashboard JS loaded");

// Animación de KPIs
document.querySelectorAll(".kpi-value[data-kpi]").forEach(el => {
    const target = parseInt(el.dataset.kpi);

    if (isNaN(target)) {
        el.textContent = "0";
        return;
    }

    let value = 0;
    const increment = Math.ceil(target / 40); // velocidad suave

    const interval = setInterval(() => {
        value += increment;
        if (value >= target) {
            value = target;
            clearInterval(interval);
        }
        el.textContent = value;
    }, 20);
});
document.querySelectorAll(".kpi-value[data-kpi]").forEach(el => {
    const target = parseInt(el.dataset.kpi);

    if (isNaN(target)) {
        el.textContent = "0";
        return;
    }

    let value = 0;
    const increment = Math.ceil(target / 40);

    const interval = setInterval(() => {
        value += increment;
        if (value >= target) {
            value = target;
            clearInterval(interval);
        }
        el.textContent = value;
    }, 20);
});
