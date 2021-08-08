# Project with ANPYMON
Project created with ANgular, PYthon y MONgoDB

## Steps for setup:
1. Install python, NodeJs, Angular, MongoDb
2. Install with pip: Django, django-cors-header, djongo, dnspython, pip install djangorestframework
3. Create django project: django-admin startproject NameOfProj
4. Init Django project server with: py manage.py runserver
5. Connect MongoDb Atlas with our Mongo Compass and create a database where our data will be saved

### A Django project may have apps that is each route for example of our web page

1. Create an app: py manage.py startapp EmployeeAPP
2. Add to settings.py in INSTALLED_APPS section:
    *   'rest_framework',
    *   'corsheaders'
    *   the new created app ins this case for ex: 'EmployeeApp.apps.EmployeeappConfig'
3.  Add in MIDDLEWARE section:
    *   'corsheaders.middleware.CorsMiddleware'
4.  Create a new section CORS_ORIGIN_ALLOW_ALL = True. This is not recommended for production, instead, we need to set a WHITELIST of domains that will have access to our API

### To set up mongo db
1. Connect our cluster from MongoDb atlas via 'Connect your application'
2. Set in django project settings:
```
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT':{
            'host':"dbStringFromMongoDbAtlasGettedInOptionConnectWithApplication",
            'name':"NameOfDatabase",
            'authMechanism':"SCRAM-SHA-1"#For atlas cloud connection
        }
    }
}
```

## Creating Models
1. In our app in models, create our models which represents our collections in MongoDB (like a table in sql)
2. We need to migrate our Models to MongoDb As collections, for that in console:
    * ```py manage.py makemigrations EmployeeApp```
    * ```py manage.py migrate EmployeeApp```
3. Create a serializers to convert complex types and models to native python data types and convert it into JSON OR XML valid formats

## Api´s
1. Create our api´s in views.py
2. Create urls.py in our app and set our routes
3. Include urls from our app to general django project in urls.py
4. Check if API works with postman in this case with the url /department
5. For upload media like profile photo:
    * Create a folder where media will be saved
    * Set the path in settings.py
    * Create the requesto for savefile form api in views.py