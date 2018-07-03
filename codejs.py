codejs1 = """M.proxy(proxy);

mapajs = M.map({
    container: "map",
    controls:"""
codejs2 =""",
    // zoom: 7,
    bbox : bb,
    wmcfiles: basemaps
  });
  
"""

pointSyle = """
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

"""

polygonStyle = """
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

"""

lineStyle  = """
// Define estilo line

let estiloLayer = new M.style.Line({
    fill: {
       color: fillColor,
       width: 2
    }
});

"""

codejs3="""
// Crea capa

var layerQGIS2Mapea4 = new M.layer.GeoJSON(
  {name: layerName, 
  source: geo

});

layerQGIS2Mapea4.setStyle(estiloLayer);
mapajs.addLayers(layerQGIS2Mapea4);


"""