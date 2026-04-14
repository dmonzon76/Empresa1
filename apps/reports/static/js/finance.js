// DATA FROM TEMPLATE (embedded via Django)
const income = parseFloat(document.getElementById("income_month").dataset.value);
const expenses = parseFloat(document.getElementById("expenses_month").dataset.value);
const operating = parseFloat(document.getElementById("operating_result").dataset.value);

// Labels for the charts
const labels = ["This Month"];

// INCOME VS EXPENSES
const ctx1 = document.getElementById('chartIncomeExpenses');
new Chart(ctx1, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            {
                label: 'Income',
                data: [income],
                borderColor: '#16a34a',
                tension: 0.3
            },
            {
                label: 'Expenses',
                data: [expenses],
                borderColor: '#dc2626',
                tension: 0.3
            }
        ]
    }
});

// CASHFLOW (Operating Result)
const ctx2 = document.getElementById('chartCashflow');
new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [
            {
                label: 'Cashflow',
                data: [operating],
                backgroundColor: '#0ea5e9'
            }
        ]
    }
});
