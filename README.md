# Smart Restock Engine

### Запуск через Docker Compose

```bash
docker compose up --build -d
```

--build нужен, если

## 📤 Импорт из dump

### PostgreSQL

```bash
cat dumps/postgres_dump.sql | docker exec -i smart_restock_postgres psql -U postgres -d smart_restock
```

---

### ClickHouse

#### 1. Создание таблиц

```bash
cat dumps/sales.sql | docker exec -i smart_restock_clickhouse clickhouse-client
cat dumps/orders.sql | docker exec -i smart_restock_clickhouse clickhouse-client
cat dumps/stock_levels.sql | docker exec -i smart_restock_clickhouse clickhouse-client
```

---

#### 2. Загрузка данных

```powershell
type dumps/sales.csv | docker exec -i smart_restock_clickhouse clickhouse-client --query="INSERT INTO sales FORMAT CSVWithNames"
type dumps/orders.csv | docker exec -i smart_restock_clickhouse clickhouse-client --query="INSERT INTO orders_history FORMAT CSVWithNames"
type dumps/stock_levels.csv | docker exec -i smart_restock_clickhouse clickhouse-client --query="INSERT INTO stock_levels FORMAT CSVWithNames"
```

### Отключение

```bash
docker compose down
```

### Запуск (если нет изменений)

```bash
docker compose up -d
```