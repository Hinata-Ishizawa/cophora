# cophora

If you are working on your laptop at a café and someone walking by behind you peeks at your computer, they are sure to think you are an amazing engineer who uses a lot of software for large, complex analyses. If only you are using `cophora`!

### What is cophora?
`Cophora` makes it appear as if numerous software tools are being installed, but in reality, nothing is installed.

## Installation

### Prerequisites
- Make sure you have installed `git` and `python` on your system.

### Install `cophora`
```
git clone git@github.com:Hinata-Ishizawa/cophora.git
```

## Simple usage
Move to installed directory and run:

```sh
python cophora
```
and you get output like:
```
#
# Name         Version        Channel
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bhdayml        3.3.27         cophora-forge  |##################################################################################################################################|
bjnaml         3.45.50        cophora-forge  |##################################################################################################################################|
brkazjs        2.4.23         cophora-forge  |##################################################################################################################################|
buttq          0.3.11         cophora-forge  |##################################################################################################################################|
drrqitpd       0.59.53        nonToxic       |##################################################################################################################################|
idyu           0.47.45        biocophora     |##################################################################################################################################|
jftu           2.06.19        cophora-forge  |##################################################################################################################################|
kuntdc         3.3.14         cophora-forge  |##################################################################################################################################|
oqiwijd        3.0.28         biocophora     |##################################################################################################################################|
swzywfq        3.2.15         biocophora     |##################################################################################################################################|
```

## Specify how many tools to install
To specify the number of tools, use `-l` or `--line` (this option is default). The default value is 10, so if no value is specified, it looks as if 10 tools are installed.

## Specify how many seconds to install
Use `-s` or `--second`. The default value is 10.
