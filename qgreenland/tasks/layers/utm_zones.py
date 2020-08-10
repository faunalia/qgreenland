"""Exactly like a zipped shapefile, but supports feature filtering."""

from qgreenland.tasks.common.fetch import FetchDataFiles
from qgreenland.tasks.common.misc import Unzip
from qgreenland.tasks.common.shapefile import (FilterShapefileFeatures,
                                               ReprojectShapefile,
                                               SubsetShapefile)
from qgreenland.util.luigi import LayerPipeline


class UtmZones(LayerPipeline):
    """Rename files to their final location."""

    def requires(self):
        fetch_data = FetchDataFiles(
            source_cfg=self.cfg['source'],
            output_name=self.cfg['id']
        )  # ->
        unzip = Unzip(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )  # ->
        filter_shapefile = FilterShapefileFeatures(
            requires_task=unzip,
            layer_id=self.layer_id,
            # The UTM Zones file includes a Zone 0 which overlaps all the other
            # zones. It looked bad so I removed it. Should we solve this some
            # other way?
            filter_func=lambda df: df['ZONE'] != 0,
        )  # ->
        reproject_shapefile = ReprojectShapefile(
            requires_task=filter_shapefile,
            layer_id=self.layer_id
        )  # ->
        return SubsetShapefile(
            requires_task=reproject_shapefile,
            layer_id=self.layer_id
        )
