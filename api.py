from fastapi import FastAPI
from pydantic import BaseModel
from pii_utils import mask_pii
from predict import predict_category

app = FastAPI()

class EmailRequest(BaseModel):
    input_email_body: str

@app.post("/classify")
def classify_email(request: EmailRequest):
    original_text = request.input_email_body
    masked_text, pii_entities = mask_pii(original_text)
    category = predict_category(masked_text)

    return {
        "input_email_body": original_text,
        "list_of_masked_entities": pii_entities,
        "masked_email": masked_text,
        "category_of_the_email": category
    }

@app.get("/")
def root():
    return {"message": "Email Classification API is running. Use POST /classify"}
