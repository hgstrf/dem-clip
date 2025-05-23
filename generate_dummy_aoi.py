import json
import rasterio
from shapely.geometry import box, mapping
import geopandas as gpd

with rasterio.open("examples/input.tif") as src:
    bounds = src.bounds
    crs = src.crs

minx = bounds.left + 0.3 * (bounds.right - bounds.left)
maxx = bounds.left + 0.7 * (bounds.right - bounds.left)
miny = bounds.bottom + 0.3 * (bounds.top - bounds.bottom)
maxy = bounds.bottom + 0.7 * (bounds.top - bounds.bottom)
aoi_geom = box(minx, miny, maxx, maxy)

aoi_gdf = gpd.GeoDataFrame([{"geometry": aoi_geom}], crs=crs)
aoi_gdf.to_file("examples/aoi.geojson", driver="GeoJSON")

print("Dummy AOI saved to examples/aoi.geojson")