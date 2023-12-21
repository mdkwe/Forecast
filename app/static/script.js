function switchTab(tabId) {
  removeActive();
  hideAll();
  $("#" + tabId).removeClass("is-hidden");

  // Highlight the active tab
  $("#" + tabId.replace("-content", "")).addClass("is-active");
}

function removeActive() {
  $("li").each(function () {
    $(this).removeClass("is-active");
  });
}

function hideAll() {
  $("#weather-tab-content").addClass("is-hidden");
  $("#settings-tab-content").addClass("is-hidden");
}

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
  document.getElementById('selectedCityName').value = location.properties.formatted;
  document.getElementById('selectedCityLat').value = location.properties.lat;
  document.getElementById('selectedCityLon').value = location.properties.lon;
});

autocompleteInput.on("suggestions", (suggestions) => {
  // process suggestions here
});
