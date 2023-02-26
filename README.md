
## Integrate FastAPI with Django & Python3


- To integrate FastAPI with Django, you can use the ASGI interface provided by Uvicorn. You can add the following code to the wsgi.py file in your Django project:

- check wsgi.py is installed.


## This will define a FastAPI application that includes a single endpoint at the root URL, and a mounted Django application at the/django URL.


## Django and FastAPI. 


## Django has its own server that can be started using 


- python3 manage.py runserver 

## FastAPI uses the uvicorn server to run the application


- uvicorn main:app --reload then  uvicorn myproject.wsgi:app 

- Django's built-in development server is designed to be simple and easy to use during development, but it's not recommended for production use. 

- On the other hand, FastAPI is a modern, fast, web framework designed to handle high-performance production traffic.

- It's designed to be used with ASGI servers like Uvicorn, which provide better performance and scalability than Django's development server, depending on your use case, you may choose to use one or the other, or even both in some cases.



### Views : create some views and configure some URLs in your Django project. You can start by creating a new app using the following command:

- python manage.py startapp myapp
- then edit your views.py in myapp folder and also the urls.py in your project.
- run your views in your project by running python manage.py .