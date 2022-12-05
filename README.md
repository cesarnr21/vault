# Vault
Just random stuff that I might need later

> disclaimer: some images, 3D models, and other content in this repo are downloaded from the interent and are not owned by me.


-----------------------------------------------------


## Utilities
### Utility to Create a Markdown tables of content:
#### Issues
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


### add a mac section with these.
```sh
brew install --cask blender coteditor

```

settings are for `.bash_profile`. should they be changed to `.bashrc`

```sh
export PS1="\[\033[36;1m\]\u@\h:\[\033[33;1m\]\w\[\033[m\]\$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

cd ~/projects/
eval "$(/opt/homebrew/bin/brew shellenv)"

alias drive="cd ~/Google\ Drive/My\ Drive/"

code () {
    open $1 -a "Visual Studio Code"
}

chrome () {
    open $1 -a "Google Chrome"
}

subl () {
    open $1 -a "Sublime Text (4107)"
}
```


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

### Bulk email Sender
> note: research if this is the best way to send emails through server

This handy script will let you send bulk emails to anyone. The script uses the Smtplib with an email format module that can log in and send emails to a list of addresses.

It’s a handy script for those who want to send bulk emails programmatically.
```py
# Bulk Email Sender
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders, message
from email.mime.multipart import MIMEMultipart
import smtplib


# send email 
def send_email(email_list, subject, body):


mail_ID = 'SENDER_EMAIL'
    mail_pass = 'SENDER_EMAIL_PASSWORD'
    subject = 'EMAIL_SUBJECT'
    msg = MIMEMultipart()
    msg['From'] = mail_ID
    msg['To'] = ", ".join(email_list)
    msg['Subject'] = subject
    body = 'EMAIL_BODY'
    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(mail_ID,mail_pass)
    server.sendmail(mail_ID, email_list,text)
    server.quit()


send_email(['email1', 'email2'], 'EMAIL_SUBJECT', 'EMAIL_BODY')
```

### Read and Create PDFs

Have a lot of PDFs and want to extract text from them then try this new automation script which uses the PyMuPDF module with a few lines of code.

Not only Extraction you can also create and modify any PDF using this script. It's a complete handy script for Programmers who need to programmatically read and create PDF files.

```py
# Read and Create PDF
# pip install PyMuPDF
# pip install fpdf2
# Read PDF file
import fitz

def read_pdf(file_name):
    pdf = fitz.open(file_name)
    text = ""
    for p in pdf:
        text += p.getText()
    return text

# Write PDF file
import fpdf

def write_pdf():
    PDF_w = fpdf.FPDF()
    PDF_w.add_page()
    PDF_w.set_font("Arial", size=12)

    # Single cell
    PDF_w.cell(txt="Hello Medium World", )
    
    # Multi Cell
    PDF_w.multi_cell(0, 5, "Hello Medium World")
    PDF_w.output("my_test.pdf")
```

### Compress Files

```py
# Compress Files
import zlib
import os

def Compress(file):
    with open(file, 'rb') as f:
        data = f.read()

    compressed = zlib.compress(data)

    with open(file, 'wb') as f:
        f.write(compressed)


def Decompress(file):
    with open(file, 'rb') as f:
        data = f.read()

    decompressed = zlib.decompress(data)

    with open(file, 'wb') as f:
        f.write(decompressed)


Compress("Data.pdf")
Decompress("Data.pdf")
```

### Spelling and Grammar Corrector
> note: this mostly only work with .txt files so they need to be tested

```py

# Grammer Corrector
# Method 1
# pip install grammar-check
from grammar_check import LanguageTool

def grammar_check(text):
    lt = LanguageTool('en-US')
    matches = lt.check(text)
    return matches


# Method 2
# pip install gingerit
import gingerit

def ginger_check(text):
    gi = gingerit.GingerIt()
    return gi.parse(text)
```
and this 

```py
# Spelling Corrector
# pip install pyspellchecker
from spellchecker import SpellChecker

tool = SpellChecker()
word = input("Enter a word: ")
word = word.lower()

if word in tool:
    print("The word is correct.")
else:
    correction = tool.correction(word)
    print(f"The word is incorrect. Did you mean {correction}?")
```



