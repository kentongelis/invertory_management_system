# Inventory Management System - Data Files

This directory contains generated inventory data for the Inventory Management System with Demand Forecasting.

## Generated Data Files

### 1. **products.csv / products.json**
Product master data including:
- `product_id`: Unique product identifier
- `sku`: Stock Keeping Unit code
- `name`: Product name
- `category`: Product category (Electronics, Office Supplies, Furniture, Software, Maintenance)
- `unit_price`: Selling price per unit
- `cost`: Cost per unit
- `description`: Product description
- `unit`: Unit of measurement
- `weight_kg`: Product weight
- `dimensions`: Product dimensions

**Total Products:** 28

### 2. **suppliers.csv / suppliers.json**
Supplier information:
- `id`: Supplier ID
- `name`: Supplier company name
- `email`: Contact email
- `phone`: Contact phone

**Total Suppliers:** 5

### 3. **product_suppliers.csv / product_suppliers.json**
Product-supplier relationships:
- `product_id`: Product identifier
- `supplier_id`: Supplier identifier
- `lead_time_days`: Days to deliver (3-14 days)
- `minimum_order_quantity`: Minimum order quantity
- `is_primary`: Whether this is the primary supplier

### 4. **sales.csv / sales.json**
Historical sales transactions (2 years of data):
- `transaction_id`: Unique transaction ID
- `date`: Sale date (YYYY-MM-DD)
- `product_id`: Product sold
- `quantity`: Quantity sold
- `unit_price`: Price per unit at time of sale
- `total_amount`: Total transaction amount
- `customer_id`: Customer identifier

**Total Sales Records:** ~17,000+ transactions

**Features:**
- Realistic daily/weekly patterns (more sales on weekdays)
- Seasonal variations (higher in Q4, lower in Q1)
- Product-specific demand patterns
- Slight upward trend over time

### 5. **inventory.csv / inventory.json**
Current inventory levels and reorder parameters:
- `product_id`: Product identifier
- `current_stock`: Current quantity in stock
- `reorder_point`: Stock level that triggers reorder
- `reorder_quantity`: Recommended reorder quantity
- `safety_stock`: Minimum safety stock level
- `status`: Stock status (Normal, Low, Critical, Overstock)
- `last_restocked`: Last restock date
- `warehouse_location`: Warehouse location code

### 6. **daily_demand.csv / daily_demand.json**
Daily demand summary (aggregated from sales):
- `date`: Date (YYYY-MM-DD)
- `product_id`: Product identifier
- `demand`: Total quantity demanded on that date

**Total Records:** ~10,700+ daily demand records

**Use Case:** This is the primary dataset for time-series forecasting models (Prophet, ARIMA, LSTM)

## Data Characteristics

### Time Period
- **Start Date:** November 2023
- **End Date:** Current date
- **Duration:** ~2 years of historical data

### Demand Patterns
- **Weekday vs Weekend:** Higher demand on weekdays
- **Seasonality:** 
  - Peak: November-December (holiday season)
  - Low: January-February
- **Trend:** Slight upward trend over time
- **Product Categories:**
  - Electronics & Office Supplies: Higher volume
  - Furniture: Lower volume, higher value
  - Software: Subscription-based patterns

## Regenerating Data

To regenerate the data with different parameters:

```bash
cd data
python3 generate_inventory_data.py
```

You can modify `generate_inventory_data.py` to:
- Change the number of products
- Adjust the time period (modify `days_back` parameter)
- Modify demand patterns
- Add more categories or suppliers

## Usage in Forecasting Models

### For Prophet/ARIMA:
Use `daily_demand.csv` - aggregate by product and date for time-series analysis.

### For LSTM:
Use `daily_demand.csv` with proper sequence preparation (sliding windows).

### For Reorder Point Optimization:
Use `inventory.csv` combined with forecasted demand from the models.

## Sample Queries for LLM Dashboard

The data supports natural language queries like:
- "What's our best-selling product this quarter?"
- "Which products are running low on stock?"
- "Show me products that need reordering"
- "What's the total revenue for Electronics category?"
- "Which supplier provides the most products?"

## Data Format

- **CSV files:** Comma-separated, UTF-8 encoded
- **JSON files:** Pretty-printed JSON format
- **Dates:** ISO format (YYYY-MM-DD)
- **Currency:** USD (floating point)

## Notes

- All data is randomly generated but follows realistic business patterns
- Sales data includes realistic variability and seasonality
- Inventory levels are calculated based on historical demand patterns
- Reorder points and quantities are algorithmically determined based on average demand

