# SiL for Squiddrone

SiL System for the Squiddrone project, to implement and test Squiddrone drone collision algorithms on a desktop computer.
Based on Python and PyQt.

# Setup
## Setup PyQt for Linux
```console
sudo apt-get install qttools5-dev-tools
sudo apt-get install qttools5-dev
```

## Open Qt Designer on Linux
```console
/usr/lib/x86_64-linux-gnu/qt5/bin/designer
```

## Convert .ui file into .py file
```console
pyuic5 -x gui.ui -o gui.py
```

# Run SiL
Install all required packages, mentioned in requirements.txt and run main.py.