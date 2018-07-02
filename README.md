# QGIS2Mapea4 (V0.1) <img src="icon.png" height="42" width="42">

Para más información puede consultarse la entrada en [SIGdeletras.com](http://www.sigdeletras.com/2017/blog/plugin-de-qgis-para-descarga-de-datos-catastrales-inspire/)

## Instalar plugin

**Disponible para 3.0.***

El complemento puede ser instalado desde el menú <b>Complementos>Administrar e instalar complementos</b> de QGIS. Para localizar de forma rápida el complemento puede introducirse el término <i>"catastro"</i> en la herramienta de búsqueda.

## Uso

Tras su instalación el plugin puede ser ejecutado desde la barra de herramientas o bien desde el menú <b>Complementos>Descarga Catrastro Inspire</b> o bien <b>Spanish Inspire Catastral Downloader</b> si tenemos instalado QGIS en otro idioma.

<img src="help/ui.PNG" width="50%">

Una vez ejecutado el complemento se debe <b>obligatoriamente</b>:
<ul>
<li>Seleccionar la provincia</li>
<li>Seleccionar el municipio</li>
<li>Indicar la ruta local de descarga</li>
<li>Indicar el conjunto de capas a descargar: Parcelas Catastrales, Edificios y/o Direcciones</li>
</ul>

El programa descarca los GML correspondientes y lso convierte a formato GeoJSON en la ubicación indicada y dentro de una carpeta con el códifo INE del municipio seleccionado. Si se desea añadir las capas GeoJSON descargardas al proyecto QGIS activo se debe marcar la casilla correspondiente. Si se desea pueden cargarse a posteriori tanto los GeoJSON como los GML originales, aunque en la versión QGIS 3.* no se visualizan correctamente los GML catastrales tal y como son suministrados.

## 2DO

- Posibilidad de applicar simbología a las capas

## Changelog
- 22.06.2018 V1.1: 
