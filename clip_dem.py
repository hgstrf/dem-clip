import argparse
import rasterio
import geopandas as gpd
from rasterio.mask import mask

def clip_raster(input_raster, aoi_file, output_raster):
    with rasterio.open(input_raster) as src:
        aoi = gpd.read_file(aoi_file)
        aoi = aoi.to_crs(src.crs)
        geometries = [feature["geometry"] for feature in aoi.__geo_interface__["features"]]
        out_image, out_transform = mask(src, geometries, crop=True)
        out_meta = src.meta.copy()
        out_meta.update({
            "driver": "GTiff",
            "height": out_image.shape[1],
            "width": out_image.shape[2],
            "transform": out_transform
        })
        with rasterio.open(output_raster, "w", **out_meta) as dest:
            dest.write(out_image)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clip a DEM using a shapefile or GeoJSON.")
    parser.add_argument("--input", required=True, help="Path to input GeoTIFF.")
    parser.add_argument("--aoi", required=True, help="Path to AOI shapefile or GeoJSON.")
    parser.add_argument("--output", required=True, help="Path to output clipped GeoTIFF.")
    args = parser.parse_args()
    clip_raster(args.input, args.aoi, args.output)
