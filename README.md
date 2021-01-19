# Music Player

ME102 is so boring, I just write this project on the class.

## Introduction

Local music player software based on **pygame** and **tkinter**

## How to Encapsulate

### Install Library

In the Windows Command Prompt, type the following command to install packages:

```
pip install -r install_requir
```

### Pack Python Script

Use the following template to create the executable:

```
pyinstaller -F [.py] -w -i [.ico]
```

Since in this project, the command to create the executable:

```
pyinstaller -F Music.py -w -i 01.ico
```

Then it is available to get .exe file which can be directly executed in folder *disk*.(The image files are also required upload in this folder. Otherwise script will report error)

![Music.exe](/Music.exe)

## Sample Output

![Sample Music Player](/Music-example.gif)
