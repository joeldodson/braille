# Tables of Braille Codes

## Letters

The below table shows the brille codes for the letters 'a' through 'z'.
The code by itself will generate a lower case letter.
This is consistent with typing on a keyboard, press a key and get the lower case symbol.
For a capital letter, 'shift' is used on a keyboard.
The 'shift' key is known as a modifier.

## Capital Letters

For braille input, the cell button 6 is the modifier key.
It is mostly analogous to the 'shift' key on a keyboard.
The difference is on a keyboard you press and hold down the 'shift' key and press the desired letter to generate its capital.
For braille input, the modifier cell button(s) is pressed and released, then the cell buttons  are pressed for the desired letter.
To generate a capital letter, first press and release the 6 cell button then press the cell buttons for the desired letter.

If you want to type a word in all capitals, press the 6 key twice, then the word.
All letters will be capitalized until a non letter is typed.

There is also an option closer to caps-lock.
By pressing the 6 key three times,
everything you type until the end of line will be capitalized.
To exit capital mode, press keys 1, 8 or 2, 8 (as you'll see in the Hable One reference).

```{list-table} Braille codes for letters
:header-rows: 1
:stub-columns: 1

* - Letter
  - Cells

* - a                                                                                                                     
  - 1                                                                                                                   

* - b                                                                                                                     
  - 1, 2                                                                                                                

* - c                                                                                                                     
  - 1, 4                                                                                                                

* - d                                                                                                                     
  - 1, 4, 5                                                                                                             

* - e                                                                                                                     
  - 1, 5                                                                                                                

* - f                                                                                                                     
  - 1, 2, 4                                                                                                             

* - g                                                                                                                     
  - 1, 2, 4, 5                                                                                                          

* - h                                                                                                                     
  - 1, 2, 5                                                                                                             

* - i                                                                                                                     
  - 2, 4                                                                                                                

* - j                                                                                                                     
  - 2, 4, 5                                                                                                             

* - k                                                                                                                     
  - 1, 3                                                                                                                

* - l                                                                                                                     
  - 1, 2, 3                                                                                                             

* - m                                                                                                                     
  - 1, 3, 4                                                                                                             

* - n                                                                                                                     
  - 1, 3, 4, 5                                                                                                          

* - o                                                                                                                     
  - 1, 3, 5                                                                                                             

* - p                                                                                                                     
  - 1, 2, 3, 4                                                                                                          

* - q                                                                                                                     
  - 1, 2, 3, 4, 5                                                                                                       

* - r                                                                                                                     
  - 1, 2, 3, 5                                                                                                          

* - s                                                                                                                     
  - 2, 3, 4                                                                                                             

* - t                                                                                                                     
  - 2, 3, 4, 5                                                                                                          

* - u                                                                                                                     
  - 1, 3, 6                                                                                                             

* - v                                                                                                                     
  - 1, 2, 3, 6                                                                                                          

* - w                                                                                                                     
  - 2, 4, 5, 6                                                                                                          

* - x                                                                                                                     
  - 1, 3, 4, 6                                                                                                          

* - y                                                                                                                     
  - 1, 3, 4, 5, 6                                                                                                       

* - z                                                                                                                     
  - 1, 3, 5, 6                                                                                                          
```


## Digits (0 - 9)

The digits 0 through 9 are the same as the characters 'a' through 'j'.
A combination of modifier keys is used to generate a number much like the 6 key is used as a modifier key to generate a capital letter.

Quickly press and release the keys 3, 4, 5, 6 at the same time to start entering digits.
As long as you're entering valid digit codes, digits will be generated.
Once you enter a non digit code, something other than codes for 'a' through 'j',
you will be out of digit mode and back into letters and punctuation.

```{list-table} Braille codes for digits 0 through 9
:header-rows: 1
:stub-columns: 1

* - digit
  - Cells

* - 1                                                                                                                     
  - 1                                                                                                                   

* - 2                                                                                                                     
  - 1, 2                                                                                                                

* - 3                                                                                                                     
  - 1, 4                                                                                                                

* - 4                                                                                                                     
  - 1, 4, 5                                                                                                             

* - 5                                                                                                                     
  - 1, 5                                                                                                                

* - 6                                                                                                                     
  - 1, 2, 4                                                                                                             

* - 7                                                                                                                     
  - 1, 2, 4, 5                                                                                                          

* - 8                                                                                                                     
  - 1, 2, 5                                                                                                             

* - 9                                                                                                                     
  - 2, 4                                                                                                                

* - 0                                                                                                                     
  - 2, 4, 5                                                                                                             
```

## Punctuation

These values are taken from a manual from Hable One, though any mistakes are mine.  I have done some manipulation to get them into the appropriate markdown format.
The first table is a subset of symbols based on python.
The next table is the complete list from the Hable One manual.

### Punctuation subset 

The folowing table is the list of symbols found in Python's string.punctuation module.
You can find the list yourself by running (if you have a command line and Python installed):
``` bash
python -c "import string; print(string.punctuation)"
```
The table is not in the same order as the python string.
It's mostly alphabetical, taken from the Hable One list.
I made a few changes (e.g., grouping less and greater than, swapping the order of closing/opening symbols).

```{list-table} Braille codes for punctuation, subset
:header-rows: 1
:stub-columns: 1

* - symbol
  - Cells

* - Ampersand , &
  - 4, then, 1, 2, 3, 4, 6

* - Apostrophe , '
  - 3

* - Asterisk , *
  - 5, then, 3, 5

* - At sign       , @
  - 4, then, 1

* - Backslash      , \
  - 4, 5, 6, then, 1, 6

* - Caret , ^
  - 4, then, 2, 6

* - Colon       , :
  - 2, 5

* - Comma       , ,
  - 2

* - Curly bracket opening , {
  - 4, 5, 6, then, 1, 2, 6

* - Curly bracket closing , }
  - 4, 5, 6, then, 3, 4, 5

* - Dollar sign      , $
  - 4, then, 2, 3, 4

* - Equals sign      , =
  - 5, then, 2, 3, 5, 6

* - Exclamation mark      , !
  - 2, 3, 5

* - Full stop period     , .
  - 2, 5, 6

* - Less than sign       , <
  - 4, then, 1, 2, 6

* - Greater than sign       , >
  - 4, then, 3, 4, 5

* - Hashtag , #
  - 4, 5, 6, then, 1, 4, 5, 6

* - Hyphen      , -
  - 6, then, 3, 6

* - Parenthesis opening , (
  - 5, then, 1, 2, 6

* - Parenthesis closing , )
  - 5, then, 3, 4, 5

* - Percent      , %
  - 4, 6, then, 3, 5, 6

* - Plus sign      , +
  - 5, then, 2, 3, 5

* - Question mark      , ?
  - 2, 3, 7

* - Quotation Mark       , "
  - 6, then, 2, 3, 5, 6

* - Semicolon       , ;
  - 2, 3

* - Square bracket opening , [
  - 4, 6, then, 1, 2, 6

* - Square bracket closing , ]
  - 4, 6, then, 3, 4, 5

* - Tilde       , ~
  - 4, then, 3, 5

* - Underscore , _
  - 4, 6, then, 3, 6

* - Vertical Pipe      , | (coming soon)
  - 4, 5, 6, then, 1, 2, 5, 6
```

### Punctuation full list

```{list-table} Braille codes for punctuation, full list
:header-rows: 1
:stub-columns: 1

* - symbol
  - Cells

* - Ampersand , &
  - 4, then, 1, 2, 3, 4, 6

* - Apostrophe , '
  - 3

* - Asterisk , *
  - 5, then, 3, 5

* - At sign       , @
  - 4, then, 1

* - Backslash      , \
  - 4, 5, 6, then, 1, 6

* - Bullet , •
  - 4, 5, 6, then, 2, 5, 6

* - Caret , ^
  - 4, then, 2, 6

* - Cent sign      , ¢
  - 4, then, 1, 4

* - Colon       , :
  - 2, 5

* - Comma       , ,
  - 2

* - Copyright sign      , ©
  - 4, 5, then, 1, 4

* - Curly bracket closing , }
  - 4, 5, 6, then, 3, 4, 5

* - Curly bracket opening , {
  - 4, 5, 6, then, 1, 2, 6

* - Dagger , †
  - 4, then, 6, then, 1, 4, 5, 6

* - Degree sign      , °
  - 4, 5, then, 2, 4, 5

* - Ditto mark , 〃
  - 5, then, 2

* - Division sign      , ÷
  - 5, then, 3, 4

* - Dollar sign      , $
  - 4, then, 2, 3, 4

* - Double arrow right , »
  - 4, 5, 6, then, 3, 5, 6

* - Double dagger , ‡
  - 4, then, 6, then, 1, 2, 4, 5, 6

* - Double prime   ,  
  - 2, 3, 5, 6, then, 2, 3, 5, 6

* - Double quotation mark closing , ”
  - 4, 5, then, 3, 5, 6

* - Double quotation opening , “
  - 4, 5, then, 2, 3, 6

* - Equals sign      , =
  - 5, then, 2, 3, 5, 6

* - Euro sign , €
  - 4, then, 1, 5

* - Exclamation mark      , !
  - 2, 3, 5

* - Franc sign , ₣
  - 4, then, 1, 2, 4

* - Full stop period     , .
  - 2, 5, 6

* - Greater than sign       , >
  - 4, then, 3, 4, 5

* - Hashtag , #
  - 4, 5, 6, then, 1, 4, 5, 6

* - Hyphen      , -
  - 6, then, 3, 6

* - Left double arrows , «
  - 4, 5, 6, then, 2, 3, 6

* - Less than sign       , <
  - 4, then, 1, 2, 6

* - Long dash , —
  - 5, then, 6, then, 3, 6

* - Mat, h
  - 4

* - Minus sign ,  
  - 5, then, 3, 6

* - Multiplication dot     ,  
  - 5, then, 2, 5, 6

* - Multiplication sign      , ×
  - 5, then, 2, 3, 6

* - Naira sign , ₦
  - 4, then, 1, 3, 4, 5

* - Number mode ,  
  - 3, 4, 5, 6

* - Paragraph section sign , §
  - 4, 5, then, 1, 2, 3, 4

* - Parenthesis closing , )
  - 5, then, 3, 4, 5

* - Parenthesis opening , (
  - 5, then, 1, 2, 6

* - Percent      , %
  - 4, 6, then, 3, 5, 6

* - Plus sign      , +
  - 5, then, 2, 3, 5

* - Pound sign      , £
  - 4, then, 1, 2, 3

* - Prim, e
  - 2, 3, 5, 6

* - Question mark      , ?
  - 2, 3, 7

* - Quotation Mark       , "
  - 6, then, 2, 3, 5, 6

* - Registered sign       , ®
  - 4, 5, then, 1, 2, 3, 5

* - Section sign , §
  - 4, 5, then, 2, 3, 4

* - Semicolon       , ;
  - 2, 3

* - Single quotation mark closing , ’
  - 6, then, 3, 5, 6

* - Single quotation mark opening , ‘
  - 6, then, 2, 3, 6

* - Square bracket closing , ]
  - 4, 6, then, 3, 4, 5

* - Square bracket opening , [
  - 4, 6, then, 1, 2, 6

* - Tilde       , ~
  - 4, then, 3, 5

* - Trademark , ™
  - 4, 5, then, 2, 3, 4, 5

* - Underscore , _
  - 4, 6, then, 3, 6

* - Vertical Pipe      , |
  - 4, 5, 6, then, 1, 2, 5, 6

* - Yen sign      , ¥
  - 4, then, 1, 3, 4, 5, 6
```
