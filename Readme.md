# Labplot documentation

This repository contains the documentation for labplot. Read this guide for additional help in contributing to the documentation. This documentation is written using reStructuredText and build with [sphinx](https://www.sphinx-doc.org/en/master/#get-started). Check out their website to get familiar with it. The benefit of this sort of documentation is that multiple people can work simultaneous on the text. The text will be compiled into the final documentation afterwards.

If you have any problems, have a look into [FAQ.md](FAQ.md).

## Setup
This section will describe the installation process of all applications required to work with this documentation. This description contains information for Linux, Windows and MacOs. If you encounter a section for not your OS, just skip it to the next one.

### GIT
Git is a version control program used to track all changes to the documentation. To be able to contribute to this documentation and downloading the repository (Folder with the documentation) you need it.

To have an easier overview a graphical user interface can be used:

- Windows: [Gittyup](https://murmele.github.io/Gittyup/)
- Linux: [Gittyup](https://flathub.org/apps/com.github.Murmele.Gittyup)
- MacOs: **TODO**

### VSCodium
VSCodium is an extensible texteditor which is able to build the documentation and showing a preview of the changes.

The application can be downloaded from:
- Windows: https://vscodium.com/
- Linux: https://flathub.org/apps/com.vscodium.codium
- MacOS: **TODO**

### VSCodium reStructuredText Plugin

For easier writing the documentation the `reStructuredText` Plugin of VSCodium can be used. To install this Plugin start the application search for the Plugin and just install it.

![VSCodiumreStructuredTextPluginInstallation](resources/VSCodeRestructuredTextPlugin.png)

### Sphinx
- Ubuntu: `sudo apt install python3-sphinx python3-sphinx-rtd-theme python3-sphinxcontrib.youtube`
- Fedora / RHEL: 
    - `sudo dnf install python3-sphinx python3-sphinx_rtd_theme`
    - `sudo dnf install python3-pip`
    - `pip install sphinxcontrib-youtube`

### Clone (Download) the Documentation

In order to contribute to the documentation wether you are an active KDE member or external you have to download the documentation:
#### KDE member
No need to fork the repository use in the next step the following ssh link: git@invent.kde.org:marmsoler/labplotdocumentation.git

#### External
1) Register on https://invent.kde.org
2) Fork the project (Making a copy of the documentation)
![ForkProject](resources/ForkProject.png)

Use Gittyup to clone (creating a local copy of the repository):
- Open Gittyup
- `File -> Clone Repository`
- Enter the documentation url determined above
- Follow the instructions of the dialog.

## Building the documentation

Editing can be done in VSCodium. There is also a live preview available with the above installed `restructuredText` plugin. So you don't need to compile the complete documentation all the time.
To update the html documentation execute the following script:

- Windows: Execute the script `make.bat`
- Linux / MacOs: Execute the makefile with the command `make html`

The main html file is in `build/html/index.html`. Open it in your browser and you will see the compiled documentation.
