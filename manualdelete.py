
# server imports
from server import app

from server.fb_queue import  delete_FBqueue


link=input("Input the URL to be deleted: ")
delete_FBqueue(link)