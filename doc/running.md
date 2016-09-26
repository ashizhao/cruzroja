# Basic git flow

Clone repository

	git clone git@cruzroja.ucsd.edu:aed

will create a directory 'aed'.

	cd aed
	
will move you into the directory. Use

	git pull
	
to bring in the latest changes into your copy of the repository.

CREATE A BRANCH FOR YOURSELF BEFORE MAKING ANY CHANGES using:

	git checkout -b YOURBRANCH

You will not be able to push changes to the master branch so you need
to create your own!

Before making changes and pushing changes back to the repository make
sure your are on your branch by checking

	git branch

If you're not in it change branches using

	git checkout YOURBRANCH

After making changes locally and testing the code add them to the list
of changes to be commited:

	git add **whatever files you changed**

Try

	git status

to see which files have been modified. Then commit all changes with

	git commit -a

When you're ready push changes back to the repository with

	git push

When you're changes are good enough contact the admin to merge your
changes into the master branch.


# Running on cruzroja.ucsd.edu

You will need to ssh to the ties account using:

	ssh -L8000:localhost:8000 ties@cruzroja.ucsd.edu
	
There is a local copy of the AED application on the directory 'aed'.
Go to the directory:

	cd aed

Switch to your branch:

	git checkout YOURBRANCH

pull any changes from the repo:

	git pull

and start the application with:

	python manage.py runserver	

Go back to your local machine and browse to 

http://localhost:8000/craed

When you're interrupt the process with ^C and logout. 
Only one person can run the server at a time.
Make changes on your local copy of the repository.
Use the repository at ties@cruzroja only to run your changes.