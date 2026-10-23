from pydantic import BaseModel,HttpUrl

class Website_Check_Request(BaseModel):

   url:HttpUrl

class Website_Check_Response(BaseModel):

   id:int
   url:str
   is_reachable:bool
   status_code:int|None=None
   response_time:float|None=None
   error:str|None=None