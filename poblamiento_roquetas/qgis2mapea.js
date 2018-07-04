var proxy = true
var layerName = 'Poblamiento Roquetas de Mar (DERA)'
var fillColor = '#b2df8a'
var strokeColor = 'blue'
var bb = [529958.989372,4061404.217715,539969.012344,4079038.022091]
var basemaps = ['cdau_satelite', 'cdau_satelite']

M.proxy(proxy);

mapajs = M.map({
    container: "map",
    controls:['layerswitcher', 'scale',  'mouse', 'Scaleline',  'panzoombar', 'location'],
    // zoom: 7,
    bbox : bb,
    wmcfiles: basemaps
  });
  
mapajs.setProjection ("EPSG:25830*d");

mapajs.addPlugin(new M.plugin.Searchstreet({"locality": "04079"}));

// Define estilo polygon

let estiloLayer = new M.style.Polygon({
  //radius: 5, 
   fill: {
      color: fillColor,
      opacity: 0.5,
    },
  stroke: {
    color: '#FF0000',
    width: 2
  }
});


// Crea capa

var layerQGIS2Mapea4 = new M.layer.GeoJSON(
  {name: layerName, 
  source: geo

});

layerQGIS2Mapea4.setStyle(estiloLayer);
mapajs.addLayers(layerQGIS2Mapea4);


