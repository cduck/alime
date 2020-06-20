/* This file was automatically generated (https://github.com/cduck/alime) */

function alime_load() {
  let elems = document.getElementsByClassName("alime");
  for (var i=0; i < elems.length; i++) {
    elems[i].href = "#click-to-unscramble";
    elems[i].onclick = alime_click_handler(elems[i]);
  }
}

function alime_click_handler(elem) {
  function alime_clicked(e) {
    // Immediately complete animation
    elem.classList.add("alimeclicked");

    // Unscramble
    let whole_str = Array.prototype.map.call(elem.children,
      function(val, i) {
        return [val.getBoundingClientRect().x, val];
      }).sort(function(a, b) {
        return a[0]-b[0];
      }).map(function(pair) {
        if (pair[1].classList.contains("sr-only")) {
          return "";
        }
        pair[1].style.display = "none";
        return pair[1].innerText || " ";
      }).join("");

    // Add plain clickable link
    let link_text = (
      whole_str.substring(1, whole_str.indexOf(":"))
      + "to"
      + whole_str.substring(whole_str.indexOf(":"), whole_str.indexOf("<"))
    ).trim().replace(" ", "");

    let print_text = whole_str.substring(whole_str.indexOf("<"), -1).trim();

    elem.classList.remove("alime");
    elem.classList.remove("alimeclicked");
    elem.classList.add("alimestatic");
    let static_elem = document.createElement("a");
    static_elem.innerText = print_text;
    static_elem.href = link_text;
    elem.href = link_text;
    elem.appendChild(static_elem);

    elem.onclick = null;
  }
  return alime_clicked;
}

alime_load();
