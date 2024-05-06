from fastapi import APIRouter
from models.blog import BlogModel,UpdateBlogModel
from config.config import blogs_collection
from serilizers.blog import DecodeBlog,DecodeBlogs
from bson import ObjectId

blog_root = APIRouter()

#create blog
@blog_root.post("/new/blog")
def NewBlog(doc:BlogModel):
    doc = dict(doc)
    res =blogs_collection.insert_one(doc)
    doc_id = str(res.inserted_id)
    return {
        "status":"ok",
        "message":"Data Sussesfully Inserted",
        "_id": doc_id
        
    }
    

#getting all blog
@blog_root.get('/all/blogs')
def AllBlogs():
    res = blogs_collection.find()
    decode_data = DecodeBlogs(res)

    return {
        'status':'ok',
        'data':decode_data
    }

#getting single blog
@blog_root.get('/blog/{_id}')
def SingleBlogs(_id:str):
    print("id",_id)
    res = blogs_collection.find_one({"_id": ObjectId(_id)})
    decode_data = DecodeBlog(res)

    return {
        'status':'ok',
        'data':decode_data
    }

#update data
@blog_root.patch("/update/{_id}")
def UpdateBlog(_id:str,doc:UpdateBlogModel):

    update_data = dict(doc.model_dump(exclude_unset =True))
    doc_id = ObjectId(_id)
    # Update the document in the database
    res = blogs_collection.update_one({"_id": doc_id}, {"$set": update_data})
   
    return {
        "status":"ok",
        "message":"Data Successfully Updated!",
           
    }

    
#delete single blog
@blog_root.delete('/blog/{_id}')
def DeleteBlog(_id:str):
    res = blogs_collection.find_one_and_delete({"_id": ObjectId(_id)})
    
    return {
        'status':'ok',
        'data':'Successfully Deleted !'
    }