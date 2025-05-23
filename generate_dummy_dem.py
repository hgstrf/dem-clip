import numpy as np
import rasterio
from rasterio.transform import from_origin
import os

output_path = os.path.join("examples", "input.tif")
data = np.linspace(100, 500, 10000).reshape((100, 100)).astype("float32")

# Define transform: upper-left corner (x=10, y=10), pixel size = 0.01
transform = from_origin(10, 10, 0.01, 0.01)

with rasterio.open(
    output_path,
    "w",
    driver="GTiff",
    height=data.shape[0],
    width=data.shape[1],
    count=1,
    dtype="float32",
    crs="EPSG:4326",
    transform=transform,
) as dst:
    dst.write(data, 1)

print(f"Dummy DEM written to {output_path}")