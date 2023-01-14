-- Lists all bands with Glam rock as their main style
-- ranked by their longevity, Column names: band_name and lifespan (in years)
-- Use attributes formed and split for computing lifespan
-- Script should execute on any database

SELECT band_name, COALESCE(split, 2022) - formed as lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
