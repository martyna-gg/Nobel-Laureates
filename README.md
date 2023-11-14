# Markdown Editor

Markdown text editor with usage of list operations, file handling, functions, scopes, if/else statements, while and for loops and processing user input.

## Requirements

Code was developed and tested using: 

Ubuntu 18.04.6 LTS 

Python 3.6.9

## Usage

The program starts with menu with three options: choosing a formatter, displaying options or saving the text and exit.

### Displaying options

There are nine text options: plain, bold, italic, header, link, inline-code, new-line, ordered-list, unordered-list and two special commands: !help and !done.
```
$ python3 Markdown_Editor.py
Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >!help
Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list
Special commands: !help !done
```

### Formatters

After choosing a specific formatter user inserts the text and the formatted text is added to the document. After that the document is displayed.
```
$ python3 Markdown_Editor.py
Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >plain
Text: >This is plain text.
This is plain text. 
Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >bold
Text: >This is bold text.
This is plain text. **This is bold text.** 
Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >italic
Text: >This is italic text.
This is plain text. **This is bold text.** *This is italic text.*
Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >new-line
This is plain text. **This is bold text.** *This is italic text.*

Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >
```
However, some of the formatters require additional parameters. If it happens, program asks for parameter before inserting the text.
```
Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >header
Level: >1
Text: >Level one header
This is plain text. **This is bold text.** *This is italic text.* 

# Level one header

Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >header
Level: >2
Text: >Level two header
This is plain text. **This is bold text.** *This is italic text.* 

# Level one header

## Level two header

Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >link
Label: >Link
URL: >www.link.link
This is plain text. **This is bold text.** *This is italic text.* 

# Level one header

## Level two header
[Link](www.link.link) 
Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >inline-code
Text: >print('Hello world!')
This is plain text. **This is bold text.** *This is italic text.* 

# Level one header

## Level two header
[Link](www.link.link) `print('Hello world!')` 
Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >ordered-list
Number of rows: >3
Row #1: >one
Row #2: >two
Row #3: >three
This is plain text. **This is bold text.** *This is italic text.* 

# Level one header

## Level two header
[Link](www.link.link) `print('Hello world!')` 

1. one
2. two
3. three

Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >unordered-list
Number of rows: >3
Row #1: >four
Row #2: >five
Row #3: >six
This is plain text. **This is bold text.** *This is italic text.* 

# Level one header

## Level two header
[Link](www.link.link) `print('Hello world!')` 

1. one
2. two
3. three

*four
*five
*six

Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >

```

### Saving the document

When the !done option is inserted the text document is saved in the current directory.

## Support

If you face any problem let me know by Issue.

