#!/bin/sh
# update all packages

# for apt packages
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoclean
sudo apt-get clean
sudo apt-get autoremove

# for snap packages
sudo snap refresh
