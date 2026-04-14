// Stock by category
new Chart(document.getElementById('chartStockCategory'), {
    type: 'bar',
    data: {
        labels: window.inventoryData.labels_cat,
        datasets: [{
            label: 'Units',
            data: window.inventoryData.valores_cat,
            backgroundColor: '#0ea5e9'
        }]
    }
});

// Rotation by category
new Chart(document.getElementById('chartRotation'), {
    type: 'bar',
    data: {
        labels: window.inventoryData.labels_rot,
        datasets: [{
            label: 'Units OUT',
            data: window.inventoryData.valores_rot,
            backgroundColor: '#dc2626'
        }]
    }
});

// Monthly movements
new Chart(document.getElementById('chartMovements'), {
    type: 'line',
    data: {
        labels: window.inventoryData.labels_mov,
        datasets: [{
            label: 'Movements',
            data: window.inventoryData.valores_mov,
            borderColor: '#16a34a',
            tension: 0.3
        }]
    }
});
