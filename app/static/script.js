// Auto completed address Suggestions
const autocompleteInput = new autocomplete.GeocoderAutocomplete(
  document.getElementById("autocomplete"),
  Geo_API,
  {
    type: 'city', 
    limit: 3,
    skipIcons: true
  }
);

autocompleteInput.on("select", (location) => {
  // Populate the hidden fields with the selected location data
  document.getElementById('selectedCityName').value = location.properties.city +", " + location.properties.state+", " + location.properties.country  ;
  document.getElementById('selectedCityLat').value = location.properties.lat;
  document.getElementById('selectedCityLon').value = location.properties.lon;
});

autocompleteInput.on("suggestions", (suggestions) => {
  // process suggestions here
});
