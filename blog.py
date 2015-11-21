import falcon
import json

from db import *

class blogSource:
    def on_get(self, req, resp):
        for post in Post.objects:
            resp.body = json.dumps(post.to_json())

app = falcon.API()
app.add_route('/blog', blogSource())
       

