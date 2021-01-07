# Instructions

## Overview

When access to the Internet is available, online-only layers from various
sources can be added to QGreenland to compliment the data in the base package.

Online layers come in a variety of forms. Some of the most common are listed
below:

* Web Map Feature Service (WFS) provides access to vector data from Open
  Geospatial Consortium (OGC) compliant servers.
* Web Map Service/Web Map Tile Service (WMS/WMTS) provides access to rendered
  raster images from OGC compliant servers.
* Web Map Coverage Service (WCS) provides access to raw raster data from OGC
  compliant servers.
* ArcGIS Map Server provides access to rendered map data from ArcGIS map servers.
* ArcGIS Feature Server provides access to vector data from ArcGIS feature servers.

## Adding online-only layers

In order to add data from an online source, open the `Data Source Manager` in
QGIS (under the `Layer` dropdown) and select the appropriate layer type (e.g.,
'WMS/WMTS') from the list on the left.

Each layer type has different options associated with it. When creating a
connection to a new online source, click the 'New' button under the 'Server
Connections' section. This will open another popup that will let you name the
layer source, and provide a URL. Once these options are set, click 'OK', select
the new server from the dropdown list, and click 'Connect'. After a few moments,
a list of the server's available layers will appear as a list. Highlight the
layers that you wish to add, and then click 'Add'. The layer will appear in the
Table of Contents.

Additional details can be found in QGIS's documentation: TODO ADD LINK

# Optional Online Layers

## World Glacier Monitoring Service (Point)

The World Glacier Monitoring Service (WGMS) provides standardized observations
on changes in mass, volume, area and length of glaciers with time (Fluctuations
of Glaciers), as well as statistical information on the distribution of
perennial surface ice in space (World Glacier Inventory), and special
events. All data and information is freely available for scientific and
educational purposes. The use requires acknowledgement to the WGMS and/or the
original investigators and sponsoring agencies according to the available
meta-information.

### WFS Link
https://geoserver.geo.uzh.ch/wgms/wfs?request=GetCapabilities&version=1.1.0&layer=wgms:wgms_fog


## Danish Map Supply

The `Kortforsyningen` plugin for QGIS makes it easy to use webservices from the
Danish Map Supply (In Danish 'Kortforsyningen'). [See the QGIS plugin
page](https://plugins.qgis.org/plugins/Kortforsyningen/) for installation and
usage instructions.
