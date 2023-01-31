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


### Mac Connfigurations
```sh
$ brew install --cask blender coteditor

```

set setting in `.bashrc`

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

# for git autocomplete
# need to install macos command line tools
[ -f /Library/Developer/CommandLineTools/usr/share/git-core/git-completion.bash ] \
    && . /Library/Developer/CommandLineTools/usr/share/git-core/git-completion.bash
```
but MacOS will sometimes use `.bash_profile` instead, so add this below to source `.bashrc`:
```
if [ -f $HOME/.bashrc ]; then
        source $HOME/.bashrc
fi
```
