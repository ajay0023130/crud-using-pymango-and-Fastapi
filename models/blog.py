from pydantic import BaseModel

class BlogModel(BaseModel):
    title : str
    sub_title : str
    content :str
    author : str
   


class UpdateBlogModel(BaseModel):
    title : str = None
    sub_title : str = None
    content :str = None
    author : str = None
   