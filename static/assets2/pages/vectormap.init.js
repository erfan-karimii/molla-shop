/**
 * Theme: Unikit - Responsive Bootstrap 5 Admin Dashboard
 * Author: Mannatthemes
 * SVG Map Js
 */
// new svgMap({
//   targetElementID: 'svg-map-1',
//   data: svgMapDataGPD,
//   colorMin: '#dbe5f4',
//   colorMax: '#0b51b7'
// });

// new svgMap({
//   targetElementID: 'svg-map-2',
//   data: svgMapDataPopulation,
//   colorMin: '#dbe5f4',
//   colorMax: '#0b51b7'
// });

// new svgMap({
//   targetElementID: 'svg-map-3',
//   countryNames: svgMapCountryNamesDE,
//   data: svgMapDataPersonHeight,
//   colorMin: '#dbe5f4',
//   colorMax: '#0b51b7'
// });


var map = new jsVectorMap({
  map: 'world',
  selector: '#map_1',
  zoomOnScroll: false,
  zoomButtons: false,
  selectedMarkers: [0, 2],
  markersSelectable: true,
  markers:[
    { name: "فلسطین", coords: [31.9474,35.2272] },
    { name: "روسیه", coords: [61.524,105.3188] },
    { name: "کانادا", coords: [56.1304,-106.3468] },
    { name: "گرین لند", coords: [71.7069,-42.6043] },
  ],
  markerStyle:{
    initial: { fill: "#5c5cff" },
    selected: { fill: "#ff5da0" }
  },
  labels: {
    markers: {
      render: marker => marker.name
    }
  }
});

var map_2 = new jsVectorMap({
  map: 'world',
  selector: '#map_2',
  zoomOnScroll: false,
  zoomButtons: false,
  markers: [
    { name: "گرین لند", coords: [72, -42] },
    { name: "کانادا", coords: [56.1304, -106.3468] },
    { name: "برزیل", coords: [-14.2350, -51.9253] },
    { name: "مصر", coords: [26.8206, 30.8025] },
    { name: "روسیه", coords: [61, 105] },
    { name: "چین", coords: [35.8617, 104.1954] },
    { name: "ایالات متحده", coords: [37.0902, -95.7129] },
    { name: "نروز", coords: [60.472024, 8.468946] },
    { name: "اوکراین", coords: [48.379433, 31.16558] },
  ],
  lines: [
    { from: "کانادا", to: "مصر" },
    { from: "روسیه", to: "مصر" },
    { from: "گرین لند", to: "مصر" },
    { from: "برزیل", to: "مصر" },
    { from: "ایالات متحده", to: "مصر" },
    { from: "چین", to: "مصر" },
    { from: "نروژ", to: "مصر" },
    { from: "اوکراین", to: "مصر" },
  ],
  labels: {
    markers: {
      render: marker => marker.name
    },
  },
  lineStyle: {
    animation: true,
    strokeDasharray: "6 3 6",
  },
});


var map_3 = new jsVectorMap({
  selector: "#map_3",
  map: "russia",
});