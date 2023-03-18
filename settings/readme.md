# Settings for all systems

## Linux Configurations

To keep computer running while locked and with the screen turned off:
```sh
$ sudo vim /etc/systemd/logind.conf

# change
HandleLidSwitch=no 
# or this also works
HandleLidSwitch=lock

LidSwitchIgnoreInhibited=no

# then restart
$ sudo service systemd-logind restart
```

#### Mounting Google drive on Linux

- [on github](https://github.com/astrada/google*drive*ocamlfuse)

- [more instructions](https://linuxhint.com/mount_google_drive_linux_mint/)

- [compere these](https://ostechnix.com/how*to*mount*google*drive*locally*as*virtual*file*system*in*linux/)


## Visual Studio Code Configurations
Use `CTRL + SHIFT + p` to open the command palette, then select `preferences: open user settings json`

```json
{
    "telemetry.telemetryLevel": "error",
    "security.workspace.trust.untrustedFiles": "open",
    "extensions.ignoreRecommendations": true,
    "python.pythonPath": "/opt/homebrew/bin/python3",
    "jupyter.jupyterServerType": "local",
    "jupyter.useDefaultConfigForJupyter": false,
    "editor.renderWhitespace": "all",
    "files.associations": {
        "*.py": "python"
    },
    "python.defaultInterpreterPath": "/opt/homebrew/bin/python3",
    "terminal.integrated.defaultProfile.osx": "bash",
    "debug.console.fontSize": 16,
    "terminal.integrated.fontSize": 16,
    "terminal.integrated.enableMultiLinePasteWarning": false,
    "javascript.suggest.autoImports": false,
    "python.analysis.autoImportCompletions": false,
    "markdown.preview.fontSize": 16,
    "editor.tokenColorCustomizations": {
        "[Default Dark+]": {
            "textMateRules": [
                {
                    "scope": ["markup.fenced_code.block.markdown", "meta.embedded.block.shellscript"],
                    "settings": {
                        "foreground": "#86c900",
                    }
                },
                {
                    "scope": ["meta.embedded.block.python"],
                    "settings": {
                        "foreground": "#61a5cc",
                    }
                },
                {
                    "scope": "markup.inline.raw.string.markdown",
                    "settings": {
                        "foreground": "#86c900",
                    }
                }
            ]
        }
    },
    "editor.fontSize": 18
}
```
> these below are not needed 

**Change color of keywrods:**
place under: **`editor.tokenColorCustomizations -> Default Dark -> textMateRules`**
```json
{
    "scope": "keyword",
    "settings": {
            "foreground": "#4400ff",
    }
}
```
keywords examples:
```py
# inside comment highlighting:
# TODO: more words below
"""
- FIXME
- XXX
- BUG
- HACK
- NOTE
"""
```

### VSCode Shortcuts

Open Keybinds on mac to make sure some keys match what's use. if `cmd` and `CTRL` keys are swappe, vscode swaps them as well messing up everything

**more shorcuts: <https://www.sitepoint.com/visual-studio-code-keyboard-shortcuts/>**

- **`CTRL` + `G`** to go to line
- **`CTRL` + `/`** to comment/uncoment line
- **`CTRL` + `UP/DOWN`** to stay in the same orientation
- **`SHIFT` + `ALT` + `UP/DOWN`** to place cursors in multiple lines
- **`CTRL` + `P`** to seach for files in projects
- **`CTRL` + `SHIFT` + `P`** to open command palette
- **`CTRL` + `H`** find and replace
    - **`CTRL` + `Enter`** to replace all
- **`ESC`** to close any of these
- **`CTRL` + `L`** select entire line
- **`SHIFT` + `UP/DOWN`** to multi select lines
- **`SHIFT` + `LEFT/RIGHT`** to select to right/left
- **`CTRL` + `J`** toogle terminal
- **`CTRL` + `B`** toogle sidebard/files
- **`F5`** debugging mode
- **`CTRL` + `,`** for settings

to set as defaults go: **`Preferences/Settings -> Keyboard Shortcuts -> Open Keyboard Shortcuts (JSON)`**
```json
// Place your key bindings in this file to override the defaults
[
    {
        "key": "cmd+g",
        "command": "workbench.action.gotoLine"
    },
    {
        "key": "ctrl+g",
        "command": "-workbench.action.gotoLine"
    },
    {
        "key": "shift+cmd+h",
        "command": "workbench.action.replaceInFiles"
    },
    {
        "key": "shift+cmd+h",
        "command": "-workbench.action.replaceInFiles"
    },
    {
        "key": "cmd+h",
        "command": "editor.action.startFindReplaceAction",
        "when": "editorFocus || editorIsOpen"
    },
    {
        "key": "alt+cmd+f",
        "command": "-editor.action.startFindReplaceAction",
        "when": "editorFocus || editorIsOpen"
    },
    {
        "key": "ctrl+j",
        "command": "-editor.action.joinLines",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "cmd+j",
        "command": "workbench.action.terminal.toggleTerminal",
        "when": "terminal.active"
    },
    {
        "key": "ctrl+`",
        "command": "-workbench.action.terminal.toggleTerminal",
        "when": "terminal.active"
    }
]
```

## vim configuration
Edits file in `~/.vimrc`
```vim
syntax on

" edits by cesar

" use spaces instead of tabs
set expandtab

" set 1 tab to 4 spaces
set SHIFTwidth=4
set tabstop=4
```


## Mac Connfigurations
```sh
$ brew install --cask blender coteditor

# to view markdown files. more info: https://github.com/sbarex/QLMarkdown
brew install --cask qlmarkdown
```



### Some apps to use light mode or dark mode
**Stack Exchange: <https://apple.stackexchange.com/questions/338044/can-i-turn-to-dark-mode-only-for-specific-apps-in-macos-mojave/347101#347101>**

Use the command below in terminal:
```sh
$ defaults write <Bundle-Identifier> NSRequiresAquaSystemAppearance -bool yes
```
To find an applications bundle ID, use the command below
```sh
$ osascript -e 'id of app "<App-Name>"'
```

To undo try:
```sh
$ defaults delete <Bundle-Identifier> NSRequiresAquaSystemAppearance
```

### Terminal Customization

Change the terminal from zsh to bash: `terminal -> preferences -> Shell opens with:` and select `/bin/bash`
[stack exchange](https://apple.stackexchange.com/questions/156216/how-to-have-full-directory-path-always-shown-in-mac-terminal/156222)


set setting in `.bashrc`

```sh
function parse_git() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

export PS1="\[\033[36;1m\]\u@\h:\[\033[33;1m\]\w\[\033[31m\]\$(parse_git) \[\033[m\]\$ "
# export CLICOLOR=1
#export LSCOLORS=ExFxBxDxCxegedabagacad

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

# for git autocomplete
# need to install macos command line tools
[ -f /Library/Developer/CommandLineTools/usr/share/git-core/git-completion.bash ] \
    && . /Library/Developer/CommandLineTools/usr/share/git-core/git-completion.bash

# added by cesar
# after installing MacPorts 
export PATH=$PATH:/opt/local/bin

cat ~/.login_message

cd ~/local/
```
but MacOS will sometimes use `.bash_profile` instead, so add this below to source `.bashrc`:
```sh
if [ -f $HOME/.bashrc ]; then
        source $HOME/.bashrc
fi
```


## Linux Configuration
### Themes Directory

Themes for Gnome Shell
If you want to use a theme, move the folder to the `/usr/share/themes` directory
**Juno**
Source: https://www.pling.com/p/1280977/

**Ant-themes**
Try these our later
source: https://www.opendesktop.org/p/1099856/


### Sublime Text

To make sublime the default text editor go to `/etc/gnome/default.list` and replaces all instances of `gedit` with `sublime_text`. It is all possible to just use the command: 
```sh
sudo sed -i 's/gedit/sublime_text/g' /etc/gnome/defaults.list
```

#### Sublime Text Themes

To use a sublime Theme, copy it to the following directory

This website allows you to generate a Sublime Text 3 Theme
[tmTheme Editor] [https://tmtheme-editor.herokuapp.com/#!/editor/theme/Monokai]
Almost there but you must get use to doing that

after installing a theme move it to:
```bash
home/cesar/.config/sublime-text-3/Packages
or
~/.config/sublime-text-3/Packages
```
Figure out how to edit sublime Text Themes

### For later
[sublime] [https://forum.sublimetext.com/t/two-easy-markdown-questions/4127/5]
[stack] [https://stackoverflow.com/questions/55559850/is-it-possible-to-have-multicolored-headings-in-markdown-syntax-in-at-least-one/55560276]

## Preferences
these are your current settings:
```sh
{
    "added_words":
    [
        "Villanova",
        "microcontrollers"
    ],
    "font_size": 13,
    "theme": "Adaptive.sublime-theme",
    "update_check": false,
    "word_wrap": true,
    "open_files_in_new_window": true,
    "draw_white_space": "all"
}
```

## Terminal
Add colored git branch
try these:
```sh
### Better Prompt
function color_my_prompt {
    local user_and_host="[\033[01;32m]\u@\h"
    local cur_location="[\033[01;34m]\w"
    local git_branch_color="[\033[31m]"
    #local git_branch="`ruby -e "print (%x{git branch 2> /dev/null}.grep(/^*/).first || '').gsub(/^* (.+)$/, '(\1) ')"`"
    local git_branch='git branch 2> /dev/null | grep -e ^* | sed -E  s/^\\\\\*\ \(.+\)$/\(\\\\\1\)\ /'
    local prompt_tail="[\033[35m]$"
    local last_color="[\033[00m]"
    export PS1="$user_and_host $cur_location $git_branch_color$git_branch$prompt_tail$__last_color "
}
color_my_prompt
```

edit the file `~/.bashrc` and add the current settings:
```sh
# the line below is for the terminal user@hostname:directory Customazation
export PS1="\[$(tput bold)\]\[\033[38;5;40m\]\u@\H\[$(tput bold)\]\[\033[38;5;92m\]:\w\[$(tput sgr0)\]\[\033[38;5;92m\]\\$\[$(tput sgr0)\] \[$(tput sgr0)\]"

#aliases for to have certain commands
# always open terminal in this directory
cd ~/local

# for using ccat instead of cat
alias cat='/usr/local/bin/ccat -G Comment="faint" -G String="teal" -G Punctuation="yellow" -G Type="red"'

# use open instead of xdg-open
alias open=xdg-open

# edit the colors of many things here
LS_COLORS='rs=0:di=01;34:fi=00;96:*.pdf=00;35:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;33:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:';

export LS_COLORS # leave this to make the changes permanent
```

[Color Chart for bash](https://misc.flogisoft.com/bash/tip_colors_and_formatting)

**To customize ls colors in Terminal**
[Tutorial and Charts](https://linuxhint.com/ls_colors_bash/)

Use the following website [http://bashrcgenerator.com/] to create a terminal command to change the color of the terminal
To make the change permament, edit the .bashrc file in the home folder. Simply add the value of PS1 at the end of the file.
One theme you really like
**For main laptop**
```bash
export PS1="\[$(tput bold)\]\[\033[38;5;40m\]\u@\H\[$(tput bold)\]\[\033[38;5;92m\]:\w\[$(tput sgr0)\]\[\033[38;5;92m\]\\$\[$(tput sgr0)\] \[$(tput sgr0)\]"
```

**For other systems**
```bash
export PS1="\[$(tput bold)\]\[\033[38;5;55m\]\u@\H:\[$(tput bold)\]\[\033[38;5;36m\]\w\\$\[$(tput sgr0)\]"

```

### Using ccat command instead of cat command

[https://ubunlog.com/en/ccat-color-salida-cat/#Instalacion_de_Ccat_en_Ubuntu]
* go to the `~/.bashrc` file and add the line `alias cat='/usr/local/bin/ccat'` to always use ccat instead of cat
* for help use `ccat -help`
* to change colors, add the color code with the allias at `~/.bashrc` file. for example
    - Here `alias cat='/usr/local/bin/ccat -G Comment="faint" -G String="teal" -G Punctuation="yellow" -G Type="red"''`, the last part of the code will always print comments with the faint color. to make more changes just add more

