from fastapi import Body
from app.Model.model import UserSchema, UserLoginSchema
from app.infrastructure.auth_handler import signJWT
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from huggingface_hub import HfApi
import warnings


from app.Config.config import API_TOKEN 
class UserController:
    def __init__(self, api_token=API_TOKEN):
        self.api_token = api_token
        self.api = HfApi()
        self.api.token = self.api_token
        self.models = self.api.list_models()
        warnings.filterwarnings('ignore')

        self.users = []

    def create_user(self, user: UserSchema = Body(...)):
        self.users.append(user)
        return {"status_code": 200, "Message": "Sign Up successfully"}

    def user_login(self, user: UserLoginSchema = Body(...)):
        email, is_valid = self.check_user(user)
        if is_valid:
            
            v = signJWT(email)
            var = v['access_token']
            return {"status_code": 200, "access_token": var, "Message": "Log In successfully"}
        return {"error": "Wrong login details!"}

    def current_user(self, email: str):
        return {"Status_Code": 200, "Message": "Current User detail", "email": email}

    def model_result(self, text: str):
        h = self.fun(text)
        return {"Status_Code": 200, "result": h[0]}

    def check_user(self, data: UserLoginSchema):
        for user in self.users:
            if user.email == data.email and user.password == data.password:
                return user.email, True
        return None, False

    def fun(self, t):
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

        inputs = tokenizer("Provide information on this [" + str(t) + "]", return_tensors="pt")
        outputs = model.generate(**inputs)
        v = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        return v
