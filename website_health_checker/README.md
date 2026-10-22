# Website Health Checker

A begeinner friendly API built with FastApi that checks website avalibility and measures response time.

## Features

-Checks wheather a  website respnds to an HTTP request.
-Retrive the HTTP status code 
-Measures Response Time
-Handels requests and timeouts
-Explore and tests endpoints using Swagger UI

## Tech Stack

-Python
-FastAPI
-Pydantic
-HTTPX
-Time

## Example Request

Send a Post request to `/check-website` with the JSON body":

```json
   
   {
    "url":"https://example.com"
   }
   ```

   The API returns information such as HTTP status code, reachability,response time and any other error details.

## Current Limitations 
   -Check history is not stored in database 
   -The API is an educational project and requires additional security protections before public use.

## Author 
Built this as a part of my journey into python backend development
