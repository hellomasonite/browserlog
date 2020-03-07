"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [

]

ROUTES += [ 
    Get('/logs', 'BrowserlogController@index'),
]
