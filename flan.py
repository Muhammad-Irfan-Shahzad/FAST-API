from huggingface_hub import HfApi, HfFolder

TOKEN = 'hf111111111111111111111111111111111'

api = HfApi()
api.token = TOKEN

models = api.list_models()
# print(models)

import warnings
warnings.filterwarnings('ignore') 

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
def fun(t):
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

    inputs = tokenizer("Provide information on this [" +str(t)+ "]", return_tensors="pt")
    outputs = model.generate(**inputs)
    v = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return v
