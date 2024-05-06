def DecodeBlog(doc) -> dict:
    return {
        "id" : str(doc["_id"]),
        "title": doc["title"],
        "sub_title": doc["sub_title"],
        "author": doc["author"],
        "content": doc["content"],
        

    }

def DecodeBlogs(docs) -> list:
    return [DecodeBlog(doc) for doc in docs] 