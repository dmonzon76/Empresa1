// New clients (last 12 months)
new Chart(document.getElementById('chartNewClients'), {
    type: 'line',
    data: {
        labels: window.crmData.labels_12,
        datasets: [{
            label: 'New Clients',
            data: window.crmData.values_12,
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

// Active vs inactive clients
new Chart(document.getElementById('chartActiveInactive'), {
    type: 'doughnut',
    data: {
        labels: ['Active', 'Inactive'],
        datasets: [{
            data: [window.crmData.active, window.crmData.inactive],
            backgroundColor: ['#16a34a', '#dc2626'],
            borderColor: ['#15803d', '#b91c1c'],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

// Clients by category
new Chart(document.getElementById('chartCategory'), {
    type: 'bar',
    data: {
        labels: window.crmData.labels_category,
        datasets: [{
            label: 'Clients',
            data: window.crmData.values_category,
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
