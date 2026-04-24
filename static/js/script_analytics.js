Chart.defaults.font.family = "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif";
Chart.defaults.color = '#666';

let abcChart, xyzChart, seasonalityChart;
let currentPeriod = 365;

// =====================
// ЗАГРУЗКА ДАННЫХ
// =====================
async function loadAnalyticsData() {
    showLoading();

    try {
        const [abcRes, xyzRes, seasonRes, topRes] = await Promise.all([
            fetch('/analytics/abc'),
            fetch('/analytics/xyz'),
            fetch('/analytics/seasonality'),
            fetch('/analytics/top-products')
        ]);

        const abcData = (await abcRes.json()).data || [];
        const xyzData = (await xyzRes.json()).data || [];
        const seasonData = (await seasonRes.json()).data || [];
        const topProducts = (await topRes.json()).data || [];

        createABCChart(abcData);
        createXYZChart(xyzData);
        createSeasonalityChart(seasonData);
        populateTopProductsTable(topProducts);

        updateLastUpdateTime();
        hideLoading();

    } catch (error) {
        console.error('Ошибка загрузки:', error);
        showError('Ошибка загрузки данных');
        hideLoading();
    }
}

// =====================
// ABC (PARETO)
// =====================
function createABCChart(data) {
    if (!document.getElementById('abcAnalysisChart')) return;

    if (abcChart) abcChart.destroy();

    const ctx = document.getElementById('abcAnalysisChart').getContext('2d');

    const colors = data.map(item => {
        if (item.category === "A") return "rgba(52,152,219,0.7)";
        if (item.category === "B") return "rgba(46,204,113,0.7)";
        return "rgba(241,196,15,0.7)";
    });

    abcChart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: data.map(i => i.product_code),
            datasets: [
                {
                    label: "Выручка",
                    data: data.map(i => i.revenue),
                    backgroundColor: colors,
                    yAxisID: "y"
                },
                {
                    label: "Накопленная доля (%)",
                    data: data.map(i => (i.cumulative * 100)),
                    type: "line",
                    yAxisID: "y1",
                    tension: 0.3
                }
            ]
        },
        options: {
            responsive: true,
            interaction: { mode: "index", intersect: false },
            scales: {
                y: { position: "left", title: { display: true, text: "Выручка" }},
                y1: {
                    position: "right",
                    min: 0,
                    max: 100,
                    grid: { drawOnChartArea: false },
                    title: { display: true, text: "%" }
                }
            }
        }
    });
}

// =====================
// XYZ
// =====================
function createXYZChart(data) {
    if (!document.getElementById('xyzAnalysisChart')) return;
    if (xyzChart) xyzChart.destroy();

    const ctx = document.getElementById('xyzAnalysisChart').getContext('2d');

    const counts = { X: 0, Y: 0, Z: 0 };

    data.forEach(i => {
        counts[i.xyz_category] += 1;
    });

    xyzChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['X', 'Y', 'Z'],
            datasets: [{
                label: 'Количество товаров',
                data: [counts.X, counts.Y, counts.Z],
                backgroundColor: [
                    'rgba(52,152,219,0.6)',
                    'rgba(46,204,113,0.6)',
                    'rgba(231,76,60,0.6)'
                ]
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

// =====================
// СЕЗОННОСТЬ
// =====================
function createSeasonalityChart(data) {
    if (!document.getElementById('seasonalityChart')) return;
    if (seasonalityChart) seasonalityChart.destroy();

    const ctx = document.getElementById('seasonalityChart').getContext('2d');

    seasonalityChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map(i => i.month),
            datasets: [{
                label: 'Выручка',
                data: data.map(i => i.revenue),
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

// =====================
// ТАБЛИЦА
// =====================
function populateTopProductsTable(products) {
    const tableBody = document.getElementById('topProductsTable');
    if (!tableBody) return;

    if (!products.length) {
        tableBody.innerHTML = `<tr><td colspan="6">Нет данных</td></tr>`;
        return;
    }

    tableBody.innerHTML = products.map((p, i) => `
        <tr>
            <td>${i + 1}</td>
            <td>${p.product_code}</td>
            <td>${formatCurrency(p.revenue)}</td>
            <td>${formatCurrency(p.revenue)}</td>
            <td>-</td>
            <td>-</td>
        </tr>
    `).join('');
}

// =====================
// УТИЛИТЫ
// =====================
function formatCurrency(value) {
    return new Intl.NumberFormat('ru-RU').format(Math.round(value));
}

function showLoading() {
    document.getElementById('refreshBtn').disabled = true;
}

function hideLoading() {
    document.getElementById('refreshBtn').disabled = false;
}

function showError(msg) {
    alert(msg);
}

function updateLastUpdateTime() {
    const time = new Date().toLocaleTimeString('ru-RU');
    document.getElementById('lastUpdate').textContent = time;
}

// =====================
// СОБЫТИЯ
// =====================
document.addEventListener('DOMContentLoaded', () => {
    loadAnalyticsData();
});

document.getElementById('refreshBtn').addEventListener('click', loadAnalyticsData);