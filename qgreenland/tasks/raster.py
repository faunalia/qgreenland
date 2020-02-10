import os
import shutil

import geopandas
import luigi
import rasterio as rio
from earthpy import spatial as eps
from osgeo import gdal
from shapely.geometry import Polygon

from qgreenland.constants import BBOX_POLYGON, PROJECT_CRS, TaskType
from qgreenland.util.luigi import LayerConfigMixin


class BuildRasterOverviews(LayerConfigMixin, luigi.Task):
    task_type = TaskType.WIP
    requires_task = luigi.Parameter()

    def requires(self):
        return self.requires_task

    def output(self):
        fn = os.path.basename(self.input().path)
        of = os.path.join(self.outdir, 'overviews', fn)
        return luigi.LocalTarget(of)

    def run(self):
        with self.output().temporary_path() as tmp_path:
            # Copy the existing file into place. Currently, this task creates
            # 'internal overviews', which changes the file itself.
            shutil.copy2(self.input().path, tmp_path)
            with rio.open(tmp_path, 'r+') as ds:
                ds.build_overviews([2, 4, 8, 16],
                                   rio.enums.Resampling.average)


class ReprojectRaster(LayerConfigMixin, luigi.Task):
    task_type = TaskType.WIP
    requires_task = luigi.Parameter()

    def requires(self):
        return self.requires_task

    def output(self):
        fn = os.path.basename(self.input().path)
        of = os.path.join(self.outdir, 'reproject', fn)
        return luigi.LocalTarget(of)

    def run(self):
        with self.output().temporary_path() as tmp_path:
            warp_kwargs = {
                'resampleAlg': 'bilinear'
            }
            if 'warp_kwargs' in self.layer_cfg:
                warp_kwargs.update(self.layer_cfg['warp_kwargs'])

            gdal.Warp(tmp_path, self.input().path, dstSRS=PROJECT_CRS,
                      **warp_kwargs)


class SubsetRaster(LayerConfigMixin, luigi.Task):
    task_type = TaskType.WIP
    requires_task = luigi.Parameter()

    def requires(self):
        return self.requires_task

    def output(self):
        fn = os.path.basename(self.input().path)
        of = os.path.join(self.outdir, 'subset', fn)
        return luigi.LocalTarget(of)

    def run(self):
        with rio.open(self.input().path, 'r') as ds:
            bb_poly = geopandas.GeoSeries([Polygon(BBOX_POLYGON)])
            img_out, meta_out = eps.crop_image(ds, bb_poly)

        with self.output().temporary_path() as tmp_path:
            with rio.open(tmp_path, 'w', **meta_out) as c_ds:
                c_ds.write(img_out)
