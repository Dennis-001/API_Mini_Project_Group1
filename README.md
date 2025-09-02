Individual Mini-Project for 089521
Packages installation, since I am coding/programming with a phone, python, django,virtual environment and git packages had to be installed.
The virtual environment was created.
Django project was Created followed by the relevant application, in the virtual environment.
HTML templates were designed, with the time-limit they were designed to show knowledge in HTML, CSS and implementation of both.
Views and models were programmed and coded into the django project folder
Views contains ModelViewSet and ViewSets for each respective function.
Models contains products table and cart/checkout table. For now no relationships have been set.
The models were migrated and screenshot uploaded to show a successful migration of the database.
Serializers have been set for each model and initialized in each ViewSet where it is required.
The urls have been programmed but not tested(2/09/2025). Each viewset has been registered and url patterns set(For Example, router.register(r'cart',CartView)
urlpatterns=[
 path(' ',include(router.urls))
])
ERROR(bug) fixing.
Project will be fully tested after the exam is over.
