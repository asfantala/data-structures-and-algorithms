# Django REST Framework & Docker

### What are the key components of a Docker container, and how do they help streamline the development and deployment of applications?
- Docker Image: package that includes everything needed to run a piece of software
- Container: are isolated environments that encapsulate applications and their dependencies.
- Dockerfile:I t specifies the base image, dependencies, configurations, and commands to be executed during the image build process.
- Docker Engine: It provides an interface to interact with containers and orchestrates their execution.

### Describe the primary steps involved in building a library website using Django, including essential components like models, views, and templates.
1. Create a skeleton website and application. Use the django-admin tool to generate a project folder, the basic file templates, and manage.py, which serves as your project management script. Use manage.py to create one or more applications.
2. Create models to represent your application's data. Models are the heart of Django applications. They represent the data that your application will store and manipulate. You can create models using the models.Model class.
3. Use the Django admin site to populate your site's data. The Django admin site is a powerful tool that allows you to manage your application's data from the web. You can use the admin site to create, edit, and delete models.
4. Create views to retrieve specific data in response to different requests, and templates to render the data as HTML to be displayed in the browser. Views are the workhorses of Django applications. They are responsible for retrieving data from models and rendering it as HTML. Templates are used to render HTML content.
5. Create mappers to associate different URL patterns with specific views. Mappers are used to associate different URL patterns with specific views. This allows you to create a URL structure for your application.
6. Add user authorization and sessions to control site behavior and access. User authorization and sessions are essential for controlling access to your application. You can use Django's built-in user authentication system to add user authorization to your application.
7. Work with forms. Forms are used to collect data from users. You can use Django's built-in form system to create and validate forms.
8. Write test code for your app. It is important to write test code for your application to ensure that it works correctly. Django provides a powerful test framework that you can use to write tests for your application.
9. Use Django's security effectively. Django is a secure framework, but it is important to use it effectively. You should follow Django's security recommendations to help keep your application secure.
10. Deploy your application to production. Once your application is complete, you can deploy it to production. Django provides a number of deployment options, so you can choose the one that best suits your needs.
### Can you explain the primary differences between Django and Django REST framework?
- Django is a web framework for building web applications. Django REST framework is a toolkit for building RESTful APIs.
- Django REST framework provides a number of features that are specifically designed for building RESTful APIs, such as authentication, permissions, and documentation. Django does not include these features, but you can use third-party libraries to add them