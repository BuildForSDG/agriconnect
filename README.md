[![N|Solid](http://www.undp.org/content/dam/undp/sdg/sdg-header-en.png)](https://docs.google.com/presentation/d/1YioOEE9Mke9xQr1m_pV0T9XPZu1xbXiqnFFs_XCfD9o/edit#slide=id.g747becbb5f_5_36)

# AGRICONNECT

This is a project for team 162,we are creating a solution that will give local farmers access to advanced farming
 practices. This involves offering expert advice and platform for discussions.
 
 ## Getting Started
 This is  `Python 3/ Django 3.0` project implementation. Necessary prerequisites are necessary to support the development
 , testing and deployment of the project.
 
 Python 3
 --------
 
 Install Python 3.0 from [Python download page](https://www.python.org/downloads/)
    
 Install Dependencies
 --------------------
 
 The project requirements have defined in the requirements.txt file.
 
    pip install -r requirements.txt
    
 Usage
 -----
 
 Simply run the development server in the project root;
 
    python manage.py runserver
    
 First Time Usage
 ----------------
 
 To run the application for the first time after cloning:

	# Make migrations
	python manage.py makemigrations

	# Apply migrations
	python manage.py migrate

	# Load initial default data (if present) in the fixtures directory
	python manage.py loaddata fixture

	# runserver
	python manage.py runserver
 
 Running Tests
 -------------
 
 The tests are ran with the help of py.test;
 
    pytest
    
 ## Contributing
 
 To contribute to the project, kindly go through the `CONTRIBUTING.md` guidelines for more information.
 
 ### Contributing Basics
 
 1. All development work should be from a branch targeting the `dev` branch as the main development target.
 2. All test across the project MUST be running for the work to be accepted.
 3. Maintain tests coverage of at least 85% with your feature contributions.
