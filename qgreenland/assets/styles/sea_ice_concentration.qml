<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" minScale="1e+08" maxScale="0" version="3.10.7-A Coruña" hasScaleBasedVisibilityFlag="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property key="WMSBackgroundLayer" value="false"/>
    <property key="WMSPublishDataSourceUrl" value="false"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="identify/format" value="Value"/>
  </customproperties>
  <pipe>
    <rasterrenderer opacity="1" type="singlebandpseudocolor" band="1" classificationMax="25" alphaBand="-1" classificationMin="0">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader classificationMode="1" colorRampType="DISCRETE" clip="0">
          <colorramp type="gradient" name="[source]">
            <prop k="color1" v="215,25,28,255"/>
            <prop k="color2" v="43,131,186,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.25;253,174,97,255:0.5;255,255,191,255:0.75;171,221,164,255"/>
          </colorramp>
          <item label="Unused" color="#093c70" alpha="0" value="14.99"/>
          <item label="15-20%" color="#137AE3" alpha="255" value="20"/>
          <item label="20-25%" color="#1684eb" alpha="255" value="25"/>
          <item label="25-30%" color="#178CF2" alpha="255" value="30"/>
          <item label="30-35%" color="#1994F9" alpha="255" value="35"/>
          <item label="35-40%" color="#1A9BFC" alpha="255" value="40"/>
          <item label="40-45%" color="#23A3FC" alpha="255" value="45"/>
          <item label="45-50%" color="#31ABFC" alpha="255" value="50"/>
          <item label="50-55%" color="#45B4FC" alpha="255" value="55"/>
          <item label="55-60%" color="#57BCFC" alpha="255" value="60"/>
          <item label="60-65%" color="#6AC4FC" alpha="255" value="65"/>
          <item label="65-70%" color="#7DCCFD" alpha="255" value="70"/>
          <item label="70-75%" color="#94D5FD" alpha="255" value="75"/>
          <item label="75-80%" color="#A8DCFD" alpha="255" value="80"/>
          <item label="80-85%" color="#BCE4FE" alpha="255" value="85"/>
          <item label="85-90%" color="#D0ECFE" alpha="255" value="90"/>
          <item label="90-95%" color="#E4F4FE" alpha="255" value="95"/>
          <item label="95-100%" color="#F7FCFF" alpha="255" value="100"/>

          <item label="Unused" color="#000000" alpha="0" value="254"/>
          <item label="Missing" color="#e9cb00" alpha="255" value="255"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeOn="0" colorizeBlue="128" colorizeGreen="128" saturation="0" colorizeRed="255" colorizeStrength="100" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
