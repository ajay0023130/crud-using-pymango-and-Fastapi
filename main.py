from fastapi import FastAPI
from routes.home import home_root
from routes.blog import blog_root

app = FastAPI()

app.include_router(home_root)
app.include_router(blog_root)


