function switchTab(tabId) {
  removeActive();
  hideAll();
  $("#" + tabId).removeClass("is-hidden");
  
  // Highlight the active tab
  $("#" + tabId.replace('-content', '')).addClass("is-active");
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
