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

## Conventions, Please Read

As I note in the [about page](about.md), I'm very new to braille.
Developing this site is part of my learning.
Also, I'm learning braille to use a braille input device, not, at least initially, to read physical braille.
Keep that in mind as you're reading, my terminology blunders might be explained by that perspective.

I mention the above to address how codes are written in the various references.
For example, in the letters table for 'a', the cells field is simply the number 1.
This means press and release the 1 key in an editable area and you should have an 'a'.
Similarly, 'g', for example, the cells field has the string, 1, 2, 4, 5.
This means press and release the 1, 2, 4, and 5 keys simultaneously, and you should get a 'g'.

Considering 6 dots can represent only 64 characters, including space, braille uses sequences to represent larger character sets.
That is, to type an at sign '@', for example, you press and release the 4 key, then press and release the 1 key.
You should see the at sign in your text, e.g., typing an email address.

Recalling the preamble to this section, I'm describing this from a braille input device perspective.
I'm assuming an at sign would take two cells on a braille display, or paper,
the first cell with a single dot 4 and the second cell with single dot 1.
Maybe this is only true for grade 1 braille.

Some less common characters have even longer sequences.
In the table with symbols, there's a symbol called a double dagger.
For that, you press and release the 4 key, then the 6 key, then the keys 1, 2, 4, 5, 6.

To represent sequences, where keys are pressed and released to affect how the next set of keys is interpreted, I separate each set of keys by the word "then".
Thus, the at sign is "4, then, 1" and double dagger is "4, then, 6, then, 1, 2, 4, 5, 6"

It's important to understand the press and hold as you start digging into using something like the Hable One device.
With the Hable One, for example, you're not only typing braille characters, you're controlling a mobile device and the Hable One itself.
For this you'll need to press and hold until you get some response (haptic in the case of the Hable One).
In some cases, you need to hold down one key while pressing another.
For example, on the Hable One, to navigate around text a character at a time,
you hold down the 7 key and press and release the 4 key.

I use the word "hold" to indicate you need to hold down the key, or set of keys until you get some response.
For cases where you hold down a key then press and release another key to navigate,
I use, for example, "hold 7, then press 1".

Of course I'll make mistakes and probably forget a "hold" somewhere, for example.
Keeping these notes in mind will hopefully encourage you to experiment when something isn't working quite like the description.
Try holding until you get feedback if you pressed and released and didn't get the result you expected.

## Enjoy

Hopefully you find braille.codes useful and not too verbose.
Check out the [about page](about) if you're curious how braille.codes  is created and hosted, or if you'd like to provide feedback.

Cheers!!

``` {toctree}
:maxdepth: 3
:hidden: true
:caption: Table of Contents

tables
hableone
about
```
