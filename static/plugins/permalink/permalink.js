// source: https://github.com/remy/permalink
(function () {
  "use strict";
  var className = "anchor";
  var idcache = {};
  var count = 0;

  function injectStyles() {
    // TODO: get rid of this and just do it in main.scss
    // for some reason this is not working right now where :hover .anchor span:before styles
    // are not being applied even though document.querySelectorAll finds them
    // Maybe something to do with the fact we are injecting these elements in after and CSS does some smart pre-selection?
    // TODO: this doesn't play nicely on mobile, ideally on mobile it appears after the header text content.
    var css = [
      "h1:hover .anchor span:before,",
      "h2:hover .anchor span:before,",
      "h3:hover .anchor span:before,",
      "h4:hover .anchor span:before,",
      "h5:hover .anchor span:before,",
      "h6:hover .anchor span:before {",
      'content: "\\1F517";',
      "position: absolute;",
      "left: 0px;",
      "top: -3px;",
      "}",
    ]
      .join("")
      .replace(/\.anchor/g, "." + className);

    var style = document.createElement("style");
    style.innerHTML = css;
    document.head.appendChild(style);
  }

  function permalink() {
    // Kept in sync with .postContent class to only put links on headers in the post content.
    var postContent = document.querySelector('.postContent')

    var anchor = document.createElement("a");
    anchor.className = className;
    anchor.innerHTML = "<span></span>";

    // TODO: maybe enable this for all block text elements (basically just p) in order to link to any place
    [].forEach.call(postContent.querySelectorAll("h1,h2,h3,h4,h5,h6"), function (el) {
      if (!el.id) {
        // let's make one
        var id = (el.textContent || el.innerText)
          .replace(/&.*?;/g, "")
          .replace(/\s+/g, "-")
          .replace(/[^\w\-]/g, "")
          .toLowerCase();
        if (idcache[id]) {
          id = id + "-" + count;
        }
        el.id = id;
        idcache[id] = 1;
      }

      var clone = anchor.cloneNode(true);
      clone.href = "#" + el.id;
      clone.onclick = function () {
        // copy URL to clipboard
        // navigator.clipboard doesn't have 100% browser support so let fall through otherwise.
        navigator.clipboard.writeText(clone.href);
      };
      el.insertBefore(clone, el.firstChild);
      count = count + 1;
    });
  }

  if (document.querySelector && Function.prototype.bind) {
    injectStyles();
    permalink();
    if (window.location.hash && window.scrollY === 0) {
      // touching the location will cause the window to scroll
      window.location = window.location;
    }
  }
})();
