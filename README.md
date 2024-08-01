# cophora: makes you look cool while doing nothing
If you are working on your laptop at a café and someone walking by behind you peeks at your computer, they are sure to think you are an amazing engineer who uses a lot of software for large and complex analyses, if only you are using `cophora`!

### What is cophora?
`cophora` makes it look as if numerous software tools are being installed, but in reality, nothing is installed.

## Installation

### Prerequisites
Make sure you have installed `git` and `python` on your system.

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
----------------------------------------------------------------------------------------------------------------------------
edgninsi       3.28.04        biocophora     |########################################################################| 100%
gecpf          2.58.29        cophora-forge  |########################################################################| 100%
jufncsh        1.41.65        nonToxic       |########################################################################| 100%
lhjaf          0.0.56         cophora-forge  |########################################################################| 100%
ndypueia       0.20.61        nonToxic       |########################################################################| 100%
nqspjk         3.49.58        cophora-forge  |########################################################################| 100%
tmjh           2.29.48        nonToxic       |########################################################################| 100%
vwtjxcb        2.0.33         nonToxic       |########################################################################| 100%
wchqmkok       2.4.43         nonToxic       |########################################################################| 100%
ypjfc          3.2.36         cophora-forge  |########################################################################| 100%
```

## Specify how many tools to install
To specify the number of tools, use `-l` or `--line` (this option is default). The default value is 10, so if no value is specified, it looks as if 10 tools are installed.

## Specify how many seconds to install
Use `-s` or `--second`. The default value is 10.
