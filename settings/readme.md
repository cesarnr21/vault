# Settings for all systems
* [Settings for all systems](#settings-for-all-systems)
  * [Linux Configurations](#linux-configurations)
      * [Mounting Google drive on Linux](#mounting-google-drive-on-linux)
  * [VSCode Shortcuts](#vscode-shortcuts)
  * [Vim configuration](#vim-configuration)
  * [Mac Configurations](#mac-configurations)
    * [Some apps to use light mode or dark mode](#some-apps-to-use-light-mode-or-dark-mode)
  * [Terminal](#terminal)

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


## VSCode Shortcuts

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
- **`F2`**  while cursor is on a variable and cursors name to change all instances
- **`ESC`** to close any of these
- **`CTRL` + `L`** select entire line
- **`SHIFT` + `UP/DOWN`** to multi select lines
- **`SHIFT` + `LEFT/RIGHT`** to select to right/left
- **`CTRL` + `J`** toogle terminal
- **`CTRL` + `B`** toogle sidebard/files
- **`F5`** debugging mode
- **`CTRL` + `,`** for settings
- **`CTRL` + `ALT` + `UP/DOWN`** for multi cursor,
- Switch between tab groups: **`CTRL` + `group #`**
- Move between tabs: **`CTRL` + `ALT` +`LEFT/RIGHT`**

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

## Vim configuration
Edits file in `~/.vimrc`
```vim
syntax on

" use spaces instead of tabs
set expandtab

" set 1 tab to 4 spaces
set shiftwidth=4
set tabstop=4

" show line number
set number
set numberwidth=2

" add command to save file with priviliges
command W :execute ':silent w !sudo tee % > /dev/null' | :edit!
```


## Mac Configurations

### Some apps to use light mode or dark mode
**Stack Exchange: <https://apple.stackexchange.com/questions/338044/can-i-turn-to-dark-mode-only-for-specific-apps-in-macos-mojave/347101#347101>**

Use the command below in terminal:
```sh
$ defaults write [ Bundle-Identifier ] NSRequiresAquaSystemAppearance -bool yes
```
To find an applications bundle ID, use the command below
```sh
$ osascript -e 'id of app "i[ app name ]"'
```

To undo try:
```sh
$ defaults delete [ Bundle-Identifier ] NSRequiresAquaSystemAppearance
```

but MacOS will sometimes use `.bash_profile` instead, so add this below to source `.bashrc`:
```sh
if [ -f $HOME/.bashrc ]; then
        source $HOME/.bashrc
fi
```



## Terminal
Add colored git branch

set setting in `.bashrc`

```sh
function parse_git() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# macos specific
export PS1="\[\033[36;1m\]\u@\h:\[\033[33;1m\]\w\[\033[31m\]\$(parse_git) \[\033[m\]\$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

# better on linux
# .............[user:hostname].....[directoory]......[git]....................[$]
export PS1="\[\033[01;32m\]\u@\h:\[\033[34m\]\w\[\033[31m\]\$(parse_git) \[\033[m\]\$ "
```
