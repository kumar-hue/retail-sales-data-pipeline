-- ===========================================
-- Day 4 - Exploratory Data Analysis (EDA)
-- Project: BigMart Sales Data Pipeline
-- ===========================================

-- 1. Total number of item types

SELECT COUNT(DISTINCT Item_Type) AS Total_Item_Types
FROM workspace.default.bigmart_sales_cleaned;


-- 2. List all item types

SELECT DISTINCT Item_Type
FROM workspace.default.bigmart_sales_cleaned
ORDER BY Item_Type;


-- 3. Number of products in each item type

SELECT
    Item_Type,
    COUNT(*) AS Total_Products
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Item_Type
ORDER BY Total_Products DESC;


-- 4. Which outlet type has the most products?

SELECT
    Outlet_Type,
    COUNT(*) AS Total_Products
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Outlet_Type
ORDER BY Total_Products DESC;


-- 5. Average sales by item type

SELECT
    Item_Type,
    ROUND(AVG(Item_Outlet_Sales), 2) AS Avg_Sales
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Item_Type
ORDER BY Avg_Sales DESC;


-- 6. Average MRP by item type

SELECT
    Item_Type,
    ROUND(AVG(Item_MRP), 2) AS Avg_MRP
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Item_Type
ORDER BY Avg_MRP DESC;


-- 7. Total sales by fat content

SELECT
    Item_Fat_Content,
    ROUND(SUM(Item_Outlet_Sales), 2) AS Total_Sales
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Item_Fat_Content
ORDER BY Total_Sales DESC;


-- 8. Total sales by outlet size

SELECT
    Outlet_Size,
    ROUND(SUM(Item_Outlet_Sales), 2) AS Total_Sales
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Outlet_Size
ORDER BY Total_Sales DESC;


-- 9. Total sales by outlet location

SELECT
    Outlet_Location_Type,
    ROUND(SUM(Item_Outlet_Sales), 2) AS Total_Sales
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Outlet_Location_Type
ORDER BY Total_Sales DESC;


-- 10. Top 10 highest selling products

SELECT
    Item_Identifier,
    Item_Type,
    Item_Outlet_Sales
FROM workspace.default.bigmart_sales_cleaned
ORDER BY Item_Outlet_Sales DESC
LIMIT 10;


-- 11. Top 10 lowest selling products

SELECT
    Item_Identifier,
    Item_Type,
    Item_Outlet_Sales
FROM workspace.default.bigmart_sales_cleaned
ORDER BY Item_Outlet_Sales ASC
LIMIT 10;


-- 12. Sales statistics

SELECT
    ROUND(AVG(Item_Outlet_Sales), 2) AS Average_Sales,
    MIN(Item_Outlet_Sales) AS Minimum_Sales,
    MAX(Item_Outlet_Sales) AS Maximum_Sales
FROM workspace.default.bigmart_sales_cleaned;