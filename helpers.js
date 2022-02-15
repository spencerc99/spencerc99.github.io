function showSnackbar(text) {
  // Get the snackbar DIV
  var x = document.getElementById("snackbar");

  // Add the "show" class to DIV
  x.className = "show";
  x.innerHTML = text; 

  // After 3 seconds, remove the show class from DIV
  setTimeout(function () {
    x.className = x.className.replace("show", "");
  }, 2000);
}


function showLinkCopiedSnackbar() {
  showSnackbar('Link copied to clipboard!')
}

function copyLink(text) {
  navigator.clipboard.writeText(text);
  showLinkCopiedSnackbar();
  return undefined;
}

function scrollUp(elementId) {
  document.querySelector(`#${elementId}`)?.scrollIntoView({behavior: "smooth"});
}
