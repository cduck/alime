
from collections import Counter, defaultdict
import html

import math

from . import templates


# Default configuration
PLACEHOLDER = '~'  # '~' is a placeholder for remaining characters
TEXT0 = 'scrambled: <~>'  # Text in HTML source
TEXT1 = 'Email: <scrambled ~>'  # Text shown in browser
TEXT2 = 'Email: placeholder@example.com <~>'  # Text shown when hover or click
CHAR_WIDTH = 0.6
ROT_DEGREES = 60


def counter_to_str(counter):
    return ''.join(counter.elements())

class Alime:
    def __init__(self, email='placeholder@example.com',
                 text0=TEXT0, text1=TEXT1, text2=TEXT2, placeholder=PLACEHOLDER,
                 char_width=CHAR_WIDTH, rot_degrees=ROT_DEGREES,
                 templates=templates):
        self.email = email
        self.text0 = text0
        self.text1 = text1
        self.text2 = text2
        self.placeholder = placeholder
        self.char_width = char_width
        self.rot_degrees = ROT_DEGREES
        self.templates = templates

        self._generate()

    def _generate(self):
        text2 = self.text2.replace('placeholder@example.com', self.email)

        # Count characters
        c0 = Counter(self.text0)
        c1 = Counter(self.text1)
        c2 = Counter(text2)
        c0[self.placeholder] = c1[self.placeholder] = c2[self.placeholder] = 0

        # Find the minimum set of characters to represent the three strings
        c_all = Counter()
        for char in sorted(set(c0) | set(c1) | set(c2)):
            c_all[char] = max(c0[char], c1[char], c2[char])

        # Determine output character order
        c_temp = Counter(c_all)
        c_rest = c_all - c0
        str_rest= ''.join(sorted(counter_to_str(c_rest)))
        char_order = self.text0.replace(self.placeholder, str_rest)
        char_order, len(char_order)

        # Calculate character positions for 1 and 2
        def calc_positions(text):
            char_search_index = defaultdict(int)
            unused_index = text.find(self.placeholder)
            positions = [None] * len(char_order)
            for i, char in enumerate(char_order):
                idx = text.find(char, char_search_index[char])
                if idx < 0:
                    positions[i] = unused_index
                else:
                    positions[i] = idx
                    char_search_index[char] = idx + 1
            return positions, unused_index
        positions1, unused_index1 = calc_positions(self.text1)
        positions2, unused_index2 = calc_positions(text2)

        # Calculate text width
        max_width = max(len(self.text0), len(self.text1), len(text2))
        em_width = round(max_width * self.char_width, 6)

        # Generate HTML
        self.generated_chars = ''.join(
            self.templates.CHAR.format(char=html.escape(char))
            for char in char_order
        )
        self.generated_html = self.templates.HTML.format(
            width=em_width,
            chars=self.generated_chars,
        )

        # Generate CSS
        def dist_to_yoff(dist):
            rot_rad = math.radians(self.rot_degrees)
            return dist / 2 / math.tan(rot_rad/2)
        self.css_rep=''.join(
            self.templates.CSS_REP.format(
                i=i+2,
                left=round((positions1[i]-i)*self.char_width, 6),
                origin=round((positions2[i]-positions1[i]+1)/2*self.char_width,
                             6),
                yoff=round(0.5+dist_to_yoff(
                                (positions2[i]-positions1[i])*self.char_width),
                           6),
                other=' display: none;' if (positions1[i] == unused_index1
                    and positions2[i] == unused_index2) else '',
            )
            for i in range(len(char_order))
        )
        self.generated_css = self.templates.CSS.format(
            pos_deg=self.rot_degrees,
            neg_deg=-self.rot_degrees,
            rep=self.css_rep,
        )

        # JavaScript
        self.generated_js = self.templates.JAVASCRIPT_STATIC

        # Generate example page
        self.generated_page = self.templates.EXAMPLE_PAGE.format(
            html=self.generated_html)

    def save(self, html_fname='alime-example.html', css_fname='alime.css',
             js_fname='alime.js'):
        self.save_page(html_fname)
        self.save_css(css_fname)
        self.save_js(js_fname)

    def save_page(self, fname='alime-example.html'):
        with open(fname, 'w') as f:
            f.write(self.generated_page)

    def save_css(self, fname='alime.css'):
        with open(fname, 'w') as f:
            f.write(self.generated_css)

    def save_js(self, fname='alime.js'):
        with open(fname, 'w') as f:
            f.write(self.generated_js)
