document.addEventListener("DOMContentLoaded", () => {
    loadKPI();
    loadForecast();
    loadRecommendations();
});


//KPI
async function loadKPI() {
    try {
        const res = await fetch('/dashboard/kpi');
        const json = await res.json();
        const kpi = json.data;

        // Обновляем карточки KPI
        const kpiCards = document.querySelectorAll(".kpi-card");

        if (kpiCards.length >= 4) {
            // 1. Риски
            kpiCards[0].querySelector(".kpi-value").innerText =
                // `${(kpi.at_risk_items || 0) + (kpi.critical_items || 0)} SKU`;
                `${kpi.risk_products || 0} SKU`

            // 2. точность прогноза
            kpiCards[1].querySelector(".kpi-value").innerText =
                kpi.forecast_accuracy.toFixed(4) ?? "-";

            // 3. упущенный доход
            kpiCards[2].querySelector(".kpi-value").innerText =
                kpi.lost_revenue ?? "-";

            // 4. время поставки
            kpiCards[3].querySelector(".kpi-value").innerText =
                kpi.avg_lead_time ?? "-";
        }

    } catch (err) {
        console.error("KPI load error:", err);
    }
}

//График главной страницы
let forecastChartInstance = null;

async function loadForecast() {
    try {
        const res = await fetch('/dashboard/forecast');
        const json = await res.json();
        const data = json.data;
        console.log(data);

        if (!data) return;

        const ctx = document.getElementById('forecastChart');
        if (!ctx) return;

        const labels = data.dates || ['Пн','Вт','Ср','Чт','Пт','Сб','Вс'];

        const sales = data.sales || [65, 59, 80, 81, 56, 55, 40];
        const stock = data.stock || [28, 48, 40, 19, 86, 27, 90];
        const forecast = data.forecast;

        if (forecastChartInstance) {
            forecastChartInstance.destroy();
        }

        forecastChartInstance = new Chart(ctx.getContext('2d'), {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Прогноз спроса',
                        data: forecast,
                        borderWidth: 2,
                        tension: 0.4
                    },
                    {
                        label: 'Спрос',
                        data: sales,
                        borderWidth: 2,
                        tension: 0.4
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'top' },
                    title: { display: true, text: 'Прогноз на период' }
                }
            }
        });

    } catch (err) {
        console.error("Forecast error:", err);
    }
}

//Рекомендации
async function loadRecommendations() {
    try {
        const res = await fetch('dashboard/recommended');
        const json = await res.json();
        const recommendations = json.data;

        const tbody = document.querySelector("tbody");
        if (!tbody) return;

        if (!recommendations || recommendations.length === 0) {
            tbody.innerHTML = `
                <tr>
                    <td colspan="10" style="text-align:center;">
                        Нет рекомендаций
                    </td>
                </tr>
            `;
            return;
        }

        tbody.innerHTML = recommendations.map(rec => {
            const qty = Number(rec.recommended_quantity || 0);

            return `
                <tr>
                    <td><strong>${rec.SKU}</strong></td>
                    <td>${rec.current_stock ?? 0}</td>
                    <td>${rec.orders_in_transit ?? 0}</td>
                    <td>${rec.demand_during_lead_time ?? 0}</td>
                    <td>${rec.expected_stockout_date || '-'}</td>
                    <td><strong>${qty}</strong></td>
                    <td>${rec.status || '-'}</td>
                    <td>${rec.priority || '-'}</td>
                    <td>${rec.reason || ''}</td>
                    <td>
                        ${qty > 0
                            ? `<button class="action-btn btn-order" onclick="createOrder('${rec.SKU}', ${qty})">Заказать</button>`
                            : `<button class="action-btn btn-skip" onclick="skipRecommendation('${rec.SKU}')">Пропустить</button>`
                        }
                    </td>
                </tr>
            `;
        }).join('');

    } catch (err) {
        console.error("Recommendations error:", err);
    }
}

//прочее
async function refreshData() {
    const btn = event.target.closest('button');
    const original = btn.innerHTML;

    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Обновление...';
    btn.disabled = true;

    try {
        await Promise.all([
            loadKPI(),
            loadForecast(),
            loadRecommendations()
        ]);
    } finally {
        btn.innerHTML = original;
        btn.disabled = false;
    }
}

function refreshRecommendations() {
    loadRecommendations();
}

//действия с orders
async function createOrder(sku, quantity) {
    if (!confirm(`Создать заказ ${sku} (${quantity} шт.)?`)) return;

    try {
        const res = await fetch('/create_order', { //не /api/
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ sku, quantity })
        });

        const data = await res.json();

        if (data.success) {
            alert("Заказ создан");
            loadRecommendations();
        } else {
            alert(data.error || "Ошибка создания заказа");
        }

    } catch (err) {
        console.error(err);
        alert("Ошибка сети");
    }
}

function skipRecommendation(sku) {
    alert(`Пропущено: ${sku}`);
}