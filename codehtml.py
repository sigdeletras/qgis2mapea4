# -*- coding: utf-8 -*-

indexCode1 = """
 <!DOCTYPE html>
 <html lang="es">
 <head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
   <meta http-equiv="X-UA-Compatible" content="IE=edge" />
   <meta name="mapea" content="yes">
   <title>"""
## Inserta título del visor
indexCode2 =    """</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<link href="https://mapea4-sigc.juntadeandalucia.es/assets/css/mapea.ol.min.css" rel="stylesheet" />
<link href="https://mapea4-sigc.juntadeandalucia.es/plugins/geosearch/geosearch.min.css" rel="stylesheet" /> 
<link rel="stylesheet" href="https://mapea4-sigc.juntadeandalucia.es/plugins/searchstreet/searchstreet.min.css"> 
  <style>
  html,
  body,
  #map {
    padding: 0;
    margin: 0;
    width: 100%;
    height: 100%;
  }

  </style>
</head>
<body>
  <div id="map">
  </div>
  """

## Inserta geojson para descarga
indexCode3 = """

  <script src="https://mapea4-sigc.juntadeandalucia.es/js/mapea.ol.min.js"></script>
  <script src="https://mapea4-sigc.juntadeandalucia.es/js/configuration.js"></script>
  <script src="https://mapea4-sigc.juntadeandalucia.es/plugins/geosearch/geosearch.ol.min.js"></script>
  <script src="https://mapea4-sigc.juntadeandalucia.es/plugins/searchstreet/searchstreet.ol.min.js"></script> 

  <script  src="""
## Inserta geojs
indexCode4 = """></script>
  <script  src="qgis2mapea.js"></script>
  </body>
</html>
"""