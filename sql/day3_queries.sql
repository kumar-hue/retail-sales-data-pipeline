CREATE OR REPLACE TABLE workspace.default.bigmart_sales_cleaned AS

SELECT
    Item_Identifier,
    Item_Weight,

    CASE
        WHEN Item_Fat_Content IN ('LF','low fat') THEN 'Low Fat'
        WHEN Item_Fat_Content='reg' THEN 'Regular'
        ELSE Item_Fat_Content
    END AS Item_Fat_Content,

    Item_Visibility,
    Item_Type,
    Item_MRP,
    Outlet_Identifier,
    Outlet_Establishment_Year,
    Outlet_Size,
    Outlet_Location_Type,
    Outlet_Type,
    Item_Outlet_Sales

FROM workspace.default.bigmart_sales;


Update table for Item_Weight and Outlet_Size( Handling null values)

select avg(Item_weight) AS Average_Weight from workspace.default.bigmart_sales_cleaned;
update workspace.default.bigmart_sales_cleaned 
SET Item_Weight = (
    select avg(Item_Weight) from workspace.default.bigmart_sales_cleaned
)
    where Item_Weight is null;

Checkimg Duplicates

SELECT *,
       COUNT(*) AS duplicate_count
FROM workspace.default.bigmart_sales_cleaned
GROUP BY
    Item_Identifier,
    Item_Weight,
    Item_Fat_Content,
    Item_Visibility,
    Item_Type,
    Item_MRP,
    Outlet_Identifier,
    Outlet_Establishment_Year,
    Outlet_Size,
    Outlet_Location_Type,
    Outlet_Type,
    Item_Outlet_Sales
HAVING COUNT(*) > 1;

