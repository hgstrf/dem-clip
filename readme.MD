# dem-clip

📍 A lightweight Python tool to clip Digital Elevation Models (DEMs) using a shapefile or GeoJSON polygon.

## Features
- Clip elevation GeoTIFFs using an AOI polygon
- Outputs clipped raster with retained metadata

## Installation

1. Clone the repo or download the files:
```bash
git clone https://github.com/yourusername/dem-clip.git
cd dem-clip
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Make sure you have:
- A `.tif` DEM file (e.g., `input.tif`)
- A `.geojson` or `.shp` file for the area of interest (AOI)

Then run:
```bash
python clip_dem.py --input examples/input.tif --aoi examples/aoi.geojson --output clipped.tif
```

## Folder Structure
```
dem-clip/
├── clip_dem.py
├── requirements.txt
├── README.md
├── LICENSE
└── examples/
    ├── input.tif      # Your DEM file
    └── aoi.geojson    # Your AOI file
```

## License
MIT License
