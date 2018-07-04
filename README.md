# QGIS2Mapea4 (V0.1) <img src="icon.png" height="42" width="42">

***Complemento QGIS para crear visores de mapas web con datos geográficos de Andalucía (España) usando la librería Mapea4.*** 

***QGIS plugin to create web map with geographic data of Andalusia (Spain) using the Mapea4 javascript library***.

QGIS2Mapea4 tiene como objetivo facilitar a los usuarios de QGIS que trabajen con datos ubicados en Andalucía (España), la generación de visores web de mapas usando la librería Mapea4. La librería javascript Mapea4, basada en OpenLayers, es un desarrollo dentro del SIG Corporatico de la Junta de Andalucía. En la siguiente dirección https://github.com/sigcorporativo-ja/Mapea4 puede consultarse toda la información sobre la misma.

QGIS2Mapea4 aims to make it easier for QGIS users to make web maps with data located in Andalusia (Spain) using the Mapea4 library. The Mapea4 javascript library, based on OpenLayers, is a development within the Corporative GIS of the Regional Government of Andalucia. In the following link https://github.com/sigcorporativo-ja/Mapea4 you can consult all the information about it.

## Instalación plugin

El complemento puede ser instalado desde el menú <b>Complementos>Administrar e instalar complementos</b> de QGIS. Para localizar de forma rápida el complemento puede introducirse el término <i>"mapea"</i> en la herramienta de búsqueda.

Igualmente, puede descargarse el código en formato zip o realizar un *clone* de este repositorio e instalar el QGIS2Mpaea4 desde la herramienta de instalar mediante zip que incluye el Administrador de complementos de QGIS a partir de la versión 3.

## Usos y opciones

Ejecutando el complemento desde el el icono <img src="icon.png" height="25" width="25"> o desde el menú **Web>QGIS a Mapea4**, aparecerá un formulario con las distintas opciones del complemento.

- **Nombre de la capa**. Se podrá añadir el nombre de la capa que aparecerá en el visor.
- **Proxy**. Activa o desactiva el proxy de la API. 
	- *Desactivado*: Para archivos en local.
	- *Activado*: Para archivos en servidor.
- **Selección de capa vectorial**. Presenta un desplegable con las capas desplegables cargadas en el proyecto de QGIS. En el caso de tener elementos seleccionados permite crear el visor solo con ellos.
- **Ubicación de archivos**: Directorio local donde se creará la carpeta con los ficheros del visor.
- **Mapas base**: Permite seleccionar los mapas base del visor. En esta versión son los datos del proyecto de Callejero Digital de Andalucía Unificado (CDAU), ortoimagen y/o combinación de ambos.
- **Opciones del visor**. Permite añadir distintas opciones y herramientas al visor incluidas en Mapea4
- **Complementos**: Al API permite añadir un conjunto variado de [complementos](https://github.com/sigcorporativo-ja/Mapea4/wiki/Plugins). 

![Formulario](img/formulario.png)

En QGIS2Mapea4 se ha añadido el complemento de búsqueda de callejero. Una vez activado, se debe seleccionar alguno de los municipios de Andalucía.

## Consulta de atributos

Gracias a Mapea4, se puede de forma automática acceder a los atributos de la capa publicada simplemente haciendo clic en alguna de las geometrías.

![Formulario](img/info_popup.png)

## Añadir el visor a nuestra web.

La carpeta generada puede ser subida directamente a un hospedaje web. 

Accediendo a la URL dominio y completando con la ubicación de los ficheros tendremos la dirección del visor.  Por ejemplo [http://www.sigdeletras.com/qgis2mapea4/servicios_sociales_sevilla/](http://www.sigdeletras.com/qgis2mapea4/servicios_sociales_sevilla/)

Podemos también embeber el visor a una publicación de nuestra web o blog. Para ello se añadirá la dirección del visor dentro de una etiqueta <iframe> y los parámetros básicos para su configuración.

Ejemplo de códido iframe.

	<iframe width="525" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" 
	src="http://www.sigdeletras.com/qgis2mapea4/servicios_sociales_sevilla/"> </iframe> 


## 2DO

- Seleccionar varias capas vectoriales
- Ampliar los complementos de Mapea4 a instalar
- Aplicación de simbilogías para mapas temáticos (coropletas, categorizados, cluster)
- Botón de descarga de capa y panel de información sobre la capa

## Changelog
- 02.07.2018 V0.1: Primera versión
