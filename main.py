import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT
from flan import fun

users = []

app = FastAPI()

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return user.email, True
    return None, False

# route handlers


@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(...)):
    users.append(user) 
    return {"status_code ": "200" ,
            "Message" : "Sign Up successfully"
           }

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    email, is_valid = check_user(user)
    if is_valid:
        v =signJWT(email)
        var =v['access_token']
        
        return {"status_code ": "200" ,"access_token" : var,
               "Message" : "Log In successfully"
           }
    return {
        "error": "Wrong login details!"
    }

@app.get("/user/current", tags=["user"], dependencies=[Depends(JWTBearer())])
def current_user(email: str = Depends(JWTBearer())):
    return { "Status_Code" :"200","Message" : "Current User detail","email": email }

# print(models)


@app.post("/user/model", tags=["user"], dependencies=[Depends(JWTBearer())])
def model_resut(text : str):
    
  
    h = fun(text)
    return { "Status_Code" :"200","result": h }
