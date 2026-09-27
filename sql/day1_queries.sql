-- Day 1: Data Exploration

-- View first 10 records
SELECT * FROM workspace.default.bigmart_sales
LIMIT 10;

-- Total records
SELECT COUNT(*) AS total_records
FROM workspace.default.bigmart_sales;

-- View schema
DESCRIBE workspace.default.bigmart_sales;

-- Missing Item_Weight values
SELECT COUNT(*) AS missing_weight
FROM workspace.default.bigmart_sales
WHERE Item_Weight IS NULL;

-- Count by Item_Fat_Content
SELECT Item_Fat_Content,
       COUNT(*) AS total
FROM workspace.default.bigmart_sales
GROUP BY Item_Fat_Content;

