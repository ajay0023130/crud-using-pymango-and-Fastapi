from fastapi import APIRouter

home_root = APIRouter()


#create blog
@home_root.get("/")
def Home():
    
    return {
        "status":"ok",
        "message":"This is home page",
        
        
    }

