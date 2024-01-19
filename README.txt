Steps to run the projects:

1.) install django and django-rest-framework : pip install django djangorestframework

2.) Run the server: python manage.py runserver

3.) click on the model links to perform CRUD operations on DRF UI;

4.) To perform query operation open shell: python manage.py shell: 
	from volobotapp.models import Section, Student
	List all sections -> Section.objects.values('studentSection').distinct()	
	List all students within a section -> Section.objects.filter(studentSection='B').values()
	