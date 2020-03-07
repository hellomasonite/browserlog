# Browserlog

```
pip install browserlog
```

```
from browserlog.providers import BrowserlogProvider

# ...
PROVIDERS = [
    # ..

    # Third Party Providers
    BrowserlogProvider,
    #..
]
```

```
craft browserlog:install
```

```
Get('/logs', 'Browserlog/BrowserlogController@index')
```

