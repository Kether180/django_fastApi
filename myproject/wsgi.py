import os

from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the Django WSGI application
django_app = get_wsgi_application()

# Create a new FastAPI app
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/market")
async def market():
    return {"message": "Market Place"}



# Mount the Django app on the "/django" path
app.mount("/django", WSGIMiddleware(django_app))

application = get_wsgi_application() ## necessary for FastAPI to work - created object 

