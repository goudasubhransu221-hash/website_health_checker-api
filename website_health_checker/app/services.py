import time
import httpx

def check_website(url:str)->dict:

    start=time.perf_counter()

    try:

        res=httpx.get(url,timeout=10.0)

        end=time.perf_counter()

        response_time=(end-start)*1000

        return {
            "url":str(res.url),
            "is_reachable":True,
            "status_code":res.status_code,
            "response_time":response_time,
            "error":None
        }

    except httpx.HTTPErroe as exception:

        return{
            "url":url,
            "is_reachable":False,
            "status_code":None,
            "response_time":None,
            "error":str(exception)
        }