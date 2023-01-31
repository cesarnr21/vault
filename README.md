# Vault
Just random stuff that I might need later

> disclaimer: some images, 3D models, and other content in this repo are downloaded from the interent and are not owned by me.


## Table of Contents
* [Utilities](#utilities)
    * [Create Table of Contents for Markdown](#create-table-of-contents-for-markdown)
        * [Issues](#issues)
    * [TO DO:](#to-do:)
    * [Downloading utility](#downloading-utility)
    * [add a mac section with these.](#add-a-mac-section-with-these.)
    * [Update all Git projects](#update-all-git-projects)
    * [Send utiltity](#send-utiltity)
    * [Utility to format](#utility-to-format)
    * [Bulk email Sender](#bulk-email-sender)
    * [Read and Create PDFs](#read-and-create-pdfs)
    * [Compress Files](#compress-files)
    * [Spelling and Grammar Corrector](#spelling-and-grammar-corrector)

------------------------------------------------------------


## Utilities
### Create Table of Contents for Markdown
#### Issues
- [ ] Don't remove top header, just change to example: **`Title Header - Vault`**
- [ ] scrip currenctly picks up all `#` occurences, some unwanted cases can be comments in fenced code blocks
    Some solutions:
    - replace `if '#' in lines:` with `if lines[0] == '#' in lines:`
    - what about headers that are created using `----` abd `====`

- [ ] Adding color to background requires using html which doesn't play nice with markdown, would probably have to write separate code for html
    ```html
    <div style="white-space:pre">
    <p style="background-color:#EFEBEC;">
    * [Utilities](#utilities)
        * [TO DO:](#to-do:)
        * [Downloading utility](#downloading-utility)
        * [add a mac section with these.](#add-a-mac-section-with-these.)
        * [Update all Git projects](#update-all-git-projects)
        * [Send utiltity](#send-utiltity)
        * [Utility to format](#utility-to-format)
        * [Bulk email Sender](#bulk-email-sender)
        * [Read and Create PDFs](#read-and-create-pdfs)
        * [Compress Files](#compress-files)
        * [Spelling and Grammar Corrector](#spelling-and-grammar-corrector)

    </div>

    <p>Some Markdown text with <span style="color:blue">some <em>blue</em> text</span>.</p>
    ```

- [ ] Add `--update` option to simply update the table


### TO DO:
- [ ] `drive.sh`: check if it is ubuntu and then install google drive
- [ ] add error handling to all
- [ ] improve `arduino_utilities.h`
- [ ] add utility to safe stuff to google drive, google sheets
- [ ] scheduler utility
- [ ] utility to parse a markdown file and insert a table of contents somewhere 
- [ ] format code utility


### Downloading utility
download stuff from:
- twitter
  - repo: <https://github.com/inteoryx/twitter-video-dl>
- tiktok
- instagram
- youtube

for ig and titkok: <https://github.com/PabloEscobar1337/tiktok-and-instagram-content-downloader/tree/main/lib>



### Update all Git projects
use this to update all git projects in folder `projects`


### Send utiltity
Use to send stuff through ssh

- maybe use a python file to help with managing the ip addresses and mac addresses

```sh
# get argument

```


### Utility to format
change and format different programming languages


## Markdown and HTML Table Generator from Excel
A python script that will take a table from excel and create a copy in either markdown or html. most likely will use html since markdown can be a little limited

