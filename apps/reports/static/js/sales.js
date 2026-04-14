// Sales by day (last 30 days)
new Chart(document.getElementById('chartSalesByDay'), {
    type: 'line',
    data: {
        labels: window.salesData.labels_day,
        datasets: [{
            label: 'Sales',
            data: window.salesData.values_day,
            borderColor: '#0ea5e9',
            backgroundColor: 'rgba(14,165,233,0.2)',
            tension: 0.3,
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

// Sales by category
new Chart(document.getElementById('chartSalesByCategory'), {
    type: 'bar',
    data: {
        labels: window.salesData.labels_category,
        datasets: [{
            label: 'Sales',
            data: window.salesData.values_category,
            backgroundColor: '#6366f1',
            borderColor: '#4f46e5',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

// Top 10 products
new Chart(document.getElementById('chartTopProducts'), {
    type: 'bar',
    data: {
        labels: window.salesData.labels_top,
        datasets: [{
            label: 'Total',
            data: window.salesData.values_top,
            backgroundColor: '#16a34a',
            borderColor: '#15803d',
            borderWidth: 1
        }]
    },
    options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false
    }
});
