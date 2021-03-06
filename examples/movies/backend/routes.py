#!/usr/bin/env python
# encoding: utf-8


from tbone.resources.routers import Router
from resources import *

# create a resource router for this app
_movies_router = Router(name='api/movies')
_movies_router.register(MovieResource, 'movie')

routes = []

routes += _movies_router.urls()



