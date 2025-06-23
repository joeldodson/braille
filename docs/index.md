# Welcome to Braille Codes

As I was trying to learn the braille codes to use the Hable One, I could not find easy to reference tables published on a simple website.
So here they are, under the tables menu.

I also want easy to access references for various Braille input devices I might use.
I'm starting with [Hable One](https://iamhable.com), also on the menu.

I toyed with structuring these reference pages into multiple pages with menus and sub-menus with each page focused on a narrow topic.
For example, I had the grade one letters on a page and punctuation on a separate page.
I had the Hable One split into three pages, common commands, iOS, and Android.

That was making the sphinx and pydata-sphinx-theme more complicated to configure with less accessible output,
and URLs were longer than what I wanted to get to some basic information.

I decided to significantly simplify these pages by, at least for now, June 2025, keeping a very flat structure.

Each page now has more information though still related under a broad topic, e.g., Hable One.
I'm very careful though to optimize accessibility using semantic HTML as much as possible.
Each page has at its beginning a note on how one might want to navigate the page
(hint, lots of headings, tables including captions, and lists).

``` {toctree}
:maxdepth: 3
:hidden: true
:caption: Table of Contents

tables
hableone
about
```
