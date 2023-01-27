# Visual Studio Code Configurations
Use `ctrl + shift + p` to open the command palette, then select `preferences: open user settings json`

```json
{
    "telemetry.telemetryLevel": "error",
    "security.workspace.trust.untrustedFiles": "open",
    "extensions.ignoreRecommendations": true,
    "editor.renderWhitespace": "all",
    "files.associations": {
        "*.py": "python"
    },
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
                },
            ]
        }
    },
    "editor.fontSize": 18
}

```