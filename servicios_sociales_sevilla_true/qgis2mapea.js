var proxy = true
var layerName = 'Servicios Sociales (Datos Abiertos Sevilla)'
var fillColor = '#3dc439'
var strokeColor = 'blue'
var bb = [233470.824576,4135243.407779,240069.982919,4145294.270417]
var basemaps = ['cdau', 'cdau_satelite', 'cdau_hibrido']

//M.proxy('true');
M.proxy(proxy );

mapajs = M.map({
    container: "map",
    controls:['layerswitcher', 'layerswitcher', 'scale', 'scale', 'mouse', 'mouse', 'Scaleline', 'Scaleline', 'panzoombar', 'panzoombar', 'location', 'location'],
    // center: {
      // x: 350373,
      // y: 4190372
    // },
    // zoom: 7,
    bbox : bb,
    wmcfiles: basemaps
  });


mapajs.setProjection ("EPSG:25830*d");

mapajs.addPlugin(new M.plugin.Searchstreet({"locality": "41091"}));

// Define estilo punto

let estiloLayer = new M.style.Point({
  radius: 5, 
  fill: {  
    color: fillColor
    //opacity: 0.5
   },
   stroke: {
    color: '#FFFFFF',
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


