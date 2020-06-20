HTML = '''\
<a href="#javascript-disabled" class="alime{extra_class}" \
style="width: {width}em">
    <span class="sr-only">(Click to send mail)</span>
    <!-- Automatically generated (https://github.com/cduck/alime) -->
    {chars}
</a>\
'''
HTML_BETWEEN_STATIC = '\n\n<br>\n\n'
CHAR = '<span><span>{char}</span></span>'

CSS = '''\
/* This file was automatically generated (https://github.com/cduck/alime) */
.alime, .alimestatic {{
  display: inline-block;
  white-space: nowrap;
  padding: 0;
  font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", \
"Courier New", monospace !important;
}}
.alime > *:nth-child(n+2) {{
  display: inline-block;
  padding: 0;
  margin: 0;
  width: 0.6em;
  height: 1em;
  text-align: center;
  position: relative;
  left: 0em;
  transform-origin: center center;
  transition-duration: 1s;
  transition-property: transform;
}}
.alime > * > * {{
  display: inline-block;
  padding: 0;
  margin: 0;
  width: 0.6em;
  height: 1em;
  text-align: center;
  transform-origin: center center;
  transition-duration: 1s;
  transition-property: transform;
}}
.alime:hover > *,
.alime:active > *,
.alime:focus > *,
.alime.alimeanim > * {{
  transform: rotate({pos_deg}deg);
}}
.alime.alimeclicked > * {{
  transform: rotate({pos_deg}deg);
  transition-duration: 0;
  transition-property: none;
}}
.alime:hover > * > *,
.alime:active > * > *,
.alime:focus > * > *,
.alime.alimeanim > * > * {{
  transform: rotate({neg_deg}deg);
}}
.alime.alimeclicked > * > * {{
  transform: rotate({neg_deg}deg);
  transition-duration: 0;
  transition-property: none;
}}
.alime > .sr-only, .alimestatic > .sr-only {{
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}}
{rep}\
'''
CSS_REP = '''\
.alime{extra_class} > :nth-child({i}) {{\
left: {left}em; \
transform-origin: {origin}em {yoff}em;\
{other}\
}}
'''

JAVASCRIPT_STATIC = '''\
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
'''

EXAMPLE_PAGE = '''\
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Alime Example Web Page</title>

<!-- Include the following line between <head></head> in your page -->
<link rel="stylesheet" type="text/css" href="alime.css">

</head>
<body>

<h2>Alime Example Web Page</h2>

<p>

<!-- Include the following lines in your page where you want your address -->
{html}
<!-- End include -->

</p>

<!-- Include the following line at the very end of <body></body> in your page \
(optional) -->
<script src='alime.js'></script>
</body>
</html>
'''
