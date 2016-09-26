# Running on cruzroja.ucsd.edu

You will need to ssh to the ties account using:

	ssh -L8000:localhost:8000 ties@cruzroja.ucsd.edu
	
There is a local copy of the AED application on the directory 'aed'. You can start the application with:

	cd aed
	python manage.py runserver
	
Go back to your local machine and browse to 

http://localhost:8000/craed

When you're interrupt the process with ^C and logout. Only one person can run the server at a time.
