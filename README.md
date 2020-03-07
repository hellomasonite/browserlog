<h1 align="center">Browserlog</h1>

<div align="center">
  <strong>Log Viewer for Masonite Framework</strong>
</div>

<div align="center">
  <h3>
    <a href="https://www.hellomasonite.com/">
      Read our Blog
    </a>
    <span> | </span>
    <a href="https://twitter.com/HelloMasonite">
      Follow us on Twitter
    </a>
  </h3>
</div>

## Table of Contents
- [Preview](#preview)
- [Installation](#installation)
- [Support](#support)

## Preview

<img src='preview.png'>

## Installation

```sh
# Using pip
$ pip install browserlog

# Using Pipenv
$ pipenv install browserlog

# Using Poetry
$ poetry add browserlog
```

Add `BrowserlogProvider` to your providers list in `config/providers.py`:

```python
from browserlog.providers import BrowserlogProvider

PROVIDERS = [

    # Third Party Providers
    BrowserlogProvider,
]
```

This will add a new `browserlog:install` command to craft. Then run in your terminal:

```bash
craft browserlog:install
```

Go to http://myapp/logs.

## Support

`Browserlog` appreciates help from a wide range of different backgrounds. Small improvements or fixes are always appreciated and issues labeled as easy may be a good starting point. If you are considering larger contributions outside the traditional coding work, please contact us through hellomasonite@gmail.com .