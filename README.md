# uenv
Tiny simple .env reader.

## Usage
```py
import uenv
```

## Why
Ever writing a Jupyter notebook and you want to use a token, where do you set it?

- write directly to the Jupyter, then it is like write secret to code. Some may git add the .ipynb file and push to GitHub
- set shell ENVIRONMENT variable, then it would need to restart the notebook every time
- read from some random file, then you may need to delete before go production.

`.env` file is a popular way to handle it, put the env key=value inside it and load with some library, e.g https://github.com/theskumar/python-dotenv

## Why uenv?
μenv, like utorrent.
Mu .env reader, because [`dotenv` name on PYPI is already taken](https://pypi.org/project/dotenv/), and https://github.com/theskumar/python-dotenv is a bit more full-features or more than too simple.

## Install

```
pip install git+https://github.com/hvnsweeting/uenv
```

Or

#### TODO

```
pip install uenv
```

or open uenv.py then copy 5 lines of code.
