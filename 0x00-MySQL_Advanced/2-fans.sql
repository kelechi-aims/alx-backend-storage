-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Requirements:
-- Import the table dump: metal_bands.sql.zip
-- Column names must be: origin and nb_fans
-- Your script can be executed on any database

-- Rank country origins of bands by the number of non-unique fans
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
