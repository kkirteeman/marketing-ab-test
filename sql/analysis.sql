-- Query 1: Dataset overview
SELECT
    COUNT(*) AS total_users,
    SUM(converted) AS total_conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 4) AS overall_conversion_rate
FROM experiment_data;

-- Query 2: Users by experiment group
SELECT
    test_group,
    COUNT(*) AS users
FROM experiment_data
GROUP BY test_group
ORDER BY test_group;

-- Query 3: Conversion performance by group
SELECT
    test_group,
    COUNT(*) AS users,
    SUM(converted) AS conversions,
    COUNT(*) - SUM(converted) AS non_conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 4) AS conversion_rate_percentage
FROM experiment_data
GROUP BY test_group
ORDER BY conversion_rate_percentage DESC;

-- Query 4: Average ad exposure by group
SELECT
    test_group,
    ROUND(AVG(total_ads), 2) AS average_total_ads,
    MIN(total_ads) AS minimum_total_ads,
    MAX(total_ads) AS maximum_total_ads
FROM experiment_data
GROUP BY test_group
ORDER BY test_group;

-- Query 5: Conversion rate by day
SELECT
    most_ads_day,
    test_group,
    COUNT(*) AS users,
    SUM(converted) AS conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 4) AS conversion_rate
FROM experiment_data
GROUP BY most_ads_day, test_group
ORDER BY CASE most_ads_day
    WHEN 'Monday' THEN 1 WHEN 'Tuesday' THEN 2 WHEN 'Wednesday' THEN 3
    WHEN 'Thursday' THEN 4 WHEN 'Friday' THEN 5 WHEN 'Saturday' THEN 6
    WHEN 'Sunday' THEN 7 END, test_group;

-- Query 6: Conversion rate by hour
SELECT
    most_ads_hour,
    test_group,
    COUNT(*) AS users,
    SUM(converted) AS conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 4) AS conversion_rate
FROM experiment_data
GROUP BY most_ads_hour, test_group
ORDER BY most_ads_hour, test_group;

-- Query 7: Converted vs non-converted exposure
SELECT
    converted,
    COUNT(*) AS users,
    ROUND(AVG(total_ads), 2) AS average_total_ads
FROM experiment_data
GROUP BY converted
ORDER BY converted;
