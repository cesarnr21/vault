
if [ "$(uname)" == "Darwin" ]; then
    echo "running MacOS configuration"
    brew update
    brew upgrade
    brew install --cask blender coteditor

elif [ "$(uname)" == "Linux" ]; then
    echo "running Ubuntu Linux configuration"
    # for apt packages
    sudo apt-get update
    sudo apt-get upgrade

    #install the following programs
    sudo apt-get install openssh-server git nodejs python3-pip

    snap install blender

    # other programs

    # chrome
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -P ~/Downloads
    sudo apt install ~/Downloads/google-chrome-stable_current_amd64.deb

    # balena etcher
    # sublime text
    # spotify
    # gnu-radio

    # python programs
    python3 -m pip install --upgrade pip
    python3 -m pip install matplotlib numpy pandas scipy tensorflow Flask


    # for snap packages
    sudo snap refresh


    sudo apt-get autoclean
    sudo apt-get clean
    sudo apt-get autoremove

fi
