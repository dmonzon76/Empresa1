// Purchases last 12 months
new Chart(document.getElementById('chartPurchases12'), {
    type: 'line',
    data: {
        labels: window.purchasesData.labels_12,
        datasets: [{
            label: 'Purchases',
            data: window.purchasesData.valores_12,
            borderColor: '#0ea5e9',
            tension: 0.3
        }]
    }
});

// Purchases by supplier
new Chart(document.getElementById('chartPurchasesSupplier'), {
    type: 'bar',
    data: {
        labels: window.purchasesData.labels_prov,
        datasets: [{
            label: 'Total',
            data: window.purchasesData.valores_prov,
            backgroundColor: '#6366f1'
        }]
    }
});
