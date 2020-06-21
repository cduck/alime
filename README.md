<a href="https://cduck.github.io/alime/demo.html">
<img alt="Demo animation" src="https://raw.githubusercontent.com/cduck/alime/master/docs/demo.gif" height="98">
</a>

# Alime: Animated anti-bot email obfuscation for your website

- Stops email scraping bots that don't understand CSS transforms and page layout
- Works without JavaScript (JavaScript is only used to make a clickable mailto: link)

[Demo page](https://cduck.github.io/alime/demo.html)


## Usage

- Install the tool from PyPI:
    ```bash
    python3 -m pip install alime
    ```
- Run alime with your email:
    ```bash
    python3 -m alime 'my.email@example.com'
    ```
    alime-example.html, alime.css, and alime.js are created in the current directory.
- Copy alime.css and alime.js (optional for mailto: hyperlink support) to your website.
- Copy the marked contents of alime-example.html into your webpage HTML source.

More options are available by using alime from Python code:
```python
import alime
help(alime.Alime)

gen = alime.Alime('my.email@example.com')
gen.generated_html, gen.generated_css, gen.generated_js
gen.save()
```
