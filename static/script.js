document.addEventListener("DOMContentLoaded", function () {
  const inputElement = document.getElementById("autocomplete");
  if (inputElement) {
    inputElement.value = "";
  }
});

const autocompleteInput = new autocomplete.GeocoderAutocomplete(
  document.getElementById("autocomplete"),
  Geo_API,
  {
    type: "city",
    limit: 3,
    skipDetails: true,
    skipIcons: true,
    placeholder: "Enter a city name ",
  }
);

autocompleteInput.on("select", (location) => {
  // Populate the hidden fields with the selected location data
  document.getElementById("selectedCityName").value =
    location.properties.city +
    ", " +
    location.properties.state +
    ", " +
    location.properties.country;
  document.getElementById("selectedCityLat").value = location.properties.lat;
  document.getElementById("selectedCityLon").value = location.properties.lon;
});

document
  .getElementById("locationForm")
  .addEventListener("submit", function (e) {
    if (!document.getElementById("selectedCityName").value) {
      e.preventDefault(); // Prevent form submission
      alert("Please select a valid city name.");
    }
  });


// About this project 


// Contact

const form = document.getElementById("form");
const result = document.getElementById("result");

form.addEventListener("submit", function (e) {
  const formData = new FormData(form);
  e.preventDefault();
  var object = {};
  formData.forEach((value, key) => {
    object[key] = value;
  });
  var json = JSON.stringify(object);
  result.innerHTML = "Please wait...";

  fetch("https://api.web3forms.com/submit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: json,
  })
    .then(async (response) => {
      let json = await response.json();
      if (response.status == 200) {
        result.innerHTML = json.message;
        result.classList.remove("text-gray-500");
        result.classList.add("text-green-500");
      } else {
        console.log(response);
        result.innerHTML = json.message;
        result.classList.remove("text-gray-500");
        result.classList.add("text-red-500");
      }
    })
    .catch((error) => {
      console.log(error);
      result.innerHTML = "Something went wrong!";
    })
    .then(function () {
      form.reset();
      setTimeout(() => {
        result.style.display = "none";
      }, 5000);
    });
});

