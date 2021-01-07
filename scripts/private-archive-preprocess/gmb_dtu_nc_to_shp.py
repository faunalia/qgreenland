import datetime as dt
import os

import fiona
from fiona.crs import from_epsg
from netCDF4 import Dataset

DATASET_ARCHIVE_LOCATION = '/share/appdata/qgreenland-private-archive/esa_cci_gravimetric_mass_balance_dtu/'
DATA_PATH = os.path.join(DATASET_ARCHIVE_LOCATION, 'greenland_gravimetric_mass_balance_rl06_dtuspace_v2_0-170820/CCI_GMB_GIS.nc')
OUTPUT_SHAPEFILE_PATH = os.path.join(DATASET_ARCHIVE_LOCATION, 'QGREENLAND_SHAPEFILES')

os.makedirs(OUTPUT_SHAPEFILE_PATH, exist_ok=True)

# Write out a simple README.
with open(os.path.join(OUTPUT_SHAPEFILE_PATH, 'README.txt'), 'w') as f:
    f.write(
        f'Shapefiles generated from gmb_dtu_nc_to_shp.py on {dt.date.today():%Y-%m-%d}\n'
    )

ds = Dataset(DATA_PATH, 'r')
lats = ds.variables['latitude'][:]
lons = ds.variables['longitude'][:]
times = ds.variables['t'][:]
datas = ds.variables['GMB_trend'][:]
epoch_start = dt.datetime(2003, 1, 1)

def _pop_schema(lat, lon, data):
    return {
        'geometry': {
            'type': 'Point',
            'coordinates': (lon, lat)
        },
        'properties': {
            'GMB_trend': data
        }
    }

shp_schema = {
    'geometry': 'Point',
    'properties': {
        'GMB_trend': 'float'
    }
}

crs = from_epsg(4326)

for time_idx, time in enumerate(times):
    date = epoch_start + dt.timedelta(days=float(time))
    with fiona.open(
            os.path.join(OUTPUT_SHAPEFILE_PATH, f'points_{date:%Y_%m_%d_%H_%M_%S}.shp'),
            'w',
            crs=crs,
            driver='ESRI Shapefile',
            schema=shp_schema) as f:
        for lat, lon, data in zip(lats, lons, datas[:, time_idx]):
            f.write(_pop_schema(float(lat), float(lon), float(data)))