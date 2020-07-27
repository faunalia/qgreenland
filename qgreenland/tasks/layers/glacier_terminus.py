from qgreenland.tasks.common.fetch import FetchCmrGranule
from qgreenland.tasks.common.shapefile import ReprojectShapefile
from qgreenland.util.luigi import LayerPipeline


class GlacierTerminus(LayerPipeline):
    """Dataproduct NSIDC-0642.

    https://nsidc.org/data/NSIDC-0642
    """

    def requires(self):
        fetch_data = FetchCmrGranule(source_cfg=self.cfg['source'],
                                     output_name=self.cfg['id'])
        return ReprojectShapefile(
            requires_task=fetch_data,
            layer_id=self.layer_id
        )