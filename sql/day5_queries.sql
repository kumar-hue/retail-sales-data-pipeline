-- ===========================================
-- Day 5 - Advanced SQL Analysis
-- Project: BigMart Sales Data Pipeline
-- ===========================================


-- 1. Total Sales by Outlet Type

SELECT
    Outlet_Type,
    ROUND(SUM(Item_Outlet_Sales), 2) AS Total_Sales
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Outlet_Type
ORDER BY Total_Sales DESC;


-- 2. Average Sales by Outlet Type

SELECT
    Outlet_Type,
    ROUND(AVG(Item_Outlet_Sales), 2) AS Average_Sales
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Outlet_Type
ORDER BY Average_Sales DESC;


-- 3. Total Sales by Outlet Establishment Year

SELECT
    Outlet_Establishment_Year,
    ROUND(SUM(Item_Outlet_Sales), 2) AS Total_Sales
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Outlet_Establishment_Year
ORDER BY Total_Sales DESC;


-- 4. Average Sales by Outlet Size

SELECT
    Outlet_Size,
    ROUND(AVG(Item_Outlet_Sales), 2) AS Average_Sales
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Outlet_Size
ORDER BY Average_Sales DESC;


-- 5. Total Sales by Item Type and Fat Content

SELECT
    Item_Type,
    Item_Fat_Content,
    ROUND(SUM(Item_Outlet_Sales), 2) AS Total_Sales
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Item_Type, Item_Fat_Content
ORDER BY Item_Type, Total_Sales DESC;


-- 6. Top 10 Products by MRP

SELECT
    Item_Identifier,
    Item_Type,
    Item_MRP
FROM workspace.default.bigmart_sales_cleaned
ORDER BY Item_MRP DESC
LIMIT 10;


-- 7. Top 10 Products by Visibility

SELECT
    Item_Identifier,
    Item_Type,
    Item_Visibility
FROM workspace.default.bigmart_sales_cleaned
ORDER BY Item_Visibility DESC
LIMIT 10;


-- 8. Total Sales by Outlet Type and Location

SELECT
    Outlet_Type,
    Outlet_Location_Type,
    ROUND(SUM(Item_Outlet_Sales), 2) AS Total_Sales
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Outlet_Type, Outlet_Location_Type
ORDER BY Total_Sales DESC;


-- 9. Number of Products in Each Outlet

SELECT
    Outlet_Identifier,
    COUNT(*) AS Total_Products
FROM workspace.default.bigmart_sales_cleaned
GROUP BY Outlet_Identifier
ORDER BY Total_Products DESC;


-- 10. Overall Dataset Summary

SELECT
    COUNT(*) AS Total_Records,
    COUNT(DISTINCT Item_Type) AS Total_Item_Types,
    COUNT(DISTINCT Outlet_Identifier) AS Total_Outlets,
    ROUND(SUM(Item_Outlet_Sales), 2) AS Total_Sales,
    ROUND(AVG(Item_Outlet_Sales), 2) AS Average_Sales
FROM workspace.default.bigmart_sales_cleaned;