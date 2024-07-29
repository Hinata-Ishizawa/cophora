# cophora

If you are working on your laptop at a café and someone walking by behind you peeks at your computer, they are sure to think you are an amazing engineer who uses a lot of software for large, complex analyses. If only you are using `cophora`!

## Installation

### Prerequisites
- Make sure you have installed `git` and `python` on your system.
- The python library `pandas` is installed.

### Install `laborder4`
```
git clone git@github.com:Hinata-Ishizawa/laborder4.git
```

## Usage
Move to installed directory and run:

```
python laborder4.py
```

When using `laborder4` **for the first time**, you are asked your name: 

```
Input your name:
```

and the path to 消耗品価格表.xlsx and 発注履歴.xlsx. Input the **absolute path**.

```
Input path to '消耗品価格表.xlsx':

Input path to '発注履歴.xlsx':

```

`laborder4` writes these to output/config.ini and refer this file.

`laborder4` searches goods information in 消耗品価格表.xlsx, writes an email message for ordering, and summarizes order information in order_info.xlsx.
