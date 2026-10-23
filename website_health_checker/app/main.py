from fastapi import FastAPI
from app.schemas import Website_Check_Response,Website_Check_Request
from app.services import check_website

App=FastAPI()

counter=0

@App.get("/")

def home():

    return {

        "Application Running Sucesfully"
    }

@App.post("/Check_Website",
          response_model=Website_Check_Response)


def check(request:Website_Check_Request):

    global counter
    counter=counter+1

    res=check_website(str(request.url))

    return{
        "id":counter,
        **res
    }