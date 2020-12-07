from qgreenland.tasks.layers.arctic_vegetation import ArcticVegetation
from qgreenland.tasks.layers.background_image import BackgroundImage
from qgreenland.tasks.layers.basal_thermal_state import BasalThermalState
from qgreenland.tasks.layers.bedmachine import BedMachineDataset
from qgreenland.tasks.layers.delimited_text_vector import DelimitedTextVector
from qgreenland.tasks.layers.glacier_terminus import GlacierTerminus
from qgreenland.tasks.layers.gzipped_vector_parts import GzippedVectorParts
from qgreenland.tasks.layers.ice_thickness_change import IceThicknessChange
from qgreenland.tasks.layers.local_vector import LocalVector
from qgreenland.tasks.layers.local_zipped_vector import LocalZippedVector
from qgreenland.tasks.layers.netcdf_raster import NetCdfRaster
from qgreenland.tasks.layers.ogr_remote_vector import OgrRemoteVector
from qgreenland.tasks.layers.online_vector import OnlineVector
from qgreenland.tasks.layers.rarred_vector import RarredVector
from qgreenland.tasks.layers.raster import Raster
from qgreenland.tasks.layers.raster_calc import RasterCalc
from qgreenland.tasks.layers.velocity_mosaic import VelocityMosaic
from qgreenland.tasks.layers.zipped_netcdf import ZippedNetCdf
from qgreenland.tasks.layers.zipped_vector import ZippedVector

# TODO: Automatically generate this list from some Python metadata?
INGEST_TASKS = {
    'arctic_vegetation': ArcticVegetation,
    'background_image': BackgroundImage,
    'basal_thermal_state': BasalThermalState,
    'bedmachine': BedMachineDataset,
    'delimited_text_points_vector': DelimitedTextVector,
    'glacier_terminus': GlacierTerminus,
    'gzipped_vector_parts': GzippedVectorParts,
    'ice_thickness_change': IceThicknessChange,
    'local_vector': LocalVector,
    'local_zipped_vector': LocalZippedVector,
    'netcdf_raster': NetCdfRaster,
    'ogr_remote_vector': OgrRemoteVector,
    'online_vector': OnlineVector,
    'rarred_vector': RarredVector,
    'raster': Raster,
    'raster_calc': RasterCalc,
    'velocity_mosaic': VelocityMosaic,
    'zipped_netcdf': ZippedNetCdf,
    'zipped_vector': ZippedVector,
}
