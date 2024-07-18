from fastapi import FastAPI
from app.routes.user_routes import create_user_router  # # reference from __init__.py at project root folder
from app.exception_handlers import list_of_exceptions_handlers
import time
import datetime as dtm
"""
main_01.py are with codes tested until chapters Typing and Response Model
main_02.py are with codes tested until chapter Expanded Field Information, nested Classes
main_03.py
    are with codes tested for Expanded Field Information, re-organizing using Inheritance, and
    tested heavily on passing tester1 or UserX (unpacked Dict in Dict, or Dict into Dict)
main_04.py
    finally understand why create an instance first before passing to FullUserProfile,
    # Method 1 by Max, is the BETTER one as it allows flexibility to choose variable inputs
main_05.py complete testing of Return Bodies \
    #   what is return from schemas class FullUserProfile(User, EducationInfo), and class CreateUserResponse(BaseModel):
    #       are schemas (without commas for different variables)
    #   3 endpoints:
    #           GET /user/me  Test Endpoint  <also provide a Number of users currently:  XXX>
    #           GET /user/{user_id}  Get User Info By Id
    #           POST /user  Add User
    #       take note server shutdown restart at times when modifying codes
    #       which leads to past entries of dummy data reset
main_06.py
    A thorough experimentation on the schema class and dict class
main_07.py
    Simple demo of throwing query, and limit the number of users that can be displayed per page/time,
    while at the same time showed the total number of users in the system.
main_08.py <Put and Delete>
    modify create_new_update_user() to reuse for making POST, aka update user details
    added find_user_to_delete() and delete_user()
main_09.py  <Async Functions> async what and how. Added async and await for def
main_10.py  
    user_routes_10.py
    user_services_10.py
    user_schemas_10.py
        <Directory Structure> creating folders to make package
        <API Routers Continued, 
        Environment Variables, 
        HTTP Status Codes, 
        Exceptions, Logging, Logging Formatter>
            this edition captures all above lessons
main_11.py <Custom Exception Handlers> and <Headers and Dependencies>
    Response under FastAPI
    Depends plus the use of Annotated, Dict
        on single function (endpoint), and 
        at common endpoint --> APIRouter
    created dependencies.py to contain depended functions
"""
"""
main_12.py  --- chapter 2 yeah!


"""


def create_application() -> FastAPI:
    print("Start time inside create_application :", dtm.datetime.fromtimestamp(time.time()))

    user_router = create_user_router()

    myapp = FastAPI()  # # create instance, <class 'fastapi.applications.FastAPI'>
    myapp.include_router(user_router)
    list_of_exceptions_handlers(myapp)
    return myapp


app = create_application()
print("Time after app = create_application  :", dtm.datetime.fromtimestamp(time.time()))
