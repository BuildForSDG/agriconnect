[![N|Solid](http://www.undp.org/content/dam/undp/sdg/sdg-header-en.png)](https://docs.google.com/presentation/d/1YioOEE9Mke9xQr1m_pV0T9XPZu1xbXiqnFFs_XCfD9o/edit#slide=id.g747becbb5f_5_36)

# AGRICONNECT

## About

This is a project for team 162,we are creating a solution that will give local farmers access to advanced farming
 practices. This involves offering expert advice and platform for discussions.
 
 ## Why
 
 This project is born out of farmers lacking necessary information to engage in better informed farming activities.
 
 ## Usage
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
	
	# Create super user
	python manage.py createsuperuser

	# Load initial default data (if present) in the fixtures directory
	python manage.py loaddata fixture

	# runserver
	python manage.py runserver
 
 Running Tests
 -------------
 
 The tests are ran with the help of py.test;
 
    pytest
    
 ## Authors
 
 The following are the authors of this awesome solution;
 
 1. [Virginiah Periah](https://github.com/virginiah894)
 2. [Harison Mwangi](https://github.com/Harison-Mwangi)
 3. [Sherline Kinyanjui](https://github.com/sherlinekinyanjui)
 4. [Cyrus Mushier](https://github.com/cymushier) | 
 [![LinkedIn](https://cdnjs.cloudflare.com/ajax/libs/webicons/2.0.0/webicons/webicon-linkedin-s.png)](https://www.linkedin.com/in/mushierc/) | 
 [![Twitter](https://cdnjs.cloudflare.com/ajax/libs/webicons/2.0.0/webicons/webicon-twitter-s.png)](https://twitter.com/cymushier)
    
 ## Contributing
 
 To contribute to the project, kindly go through the `CONTRIBUTING.md` guidelines for more information.
 
 ### Contributing Basics
 
 1. All development work should be from a branch targeting the `dev` branch as the main development target.
 2. All test across the project MUST be running for the work to be accepted.
 3. Maintain tests coverage of at least 85% with your feature contributions.
 
 
[linkedinlogo]: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAADZklEQVR4Xu2bXUgUURTH/3f8QlvNPhQrCazITMooDfEhyAc1EykiKqFe8z3SLGujfFCJnsJ66iGMsIdA1m/MF9OU0sKiXaOUiCx1K3OdTVd3JmYgapcd52MV5uPO486Z3fv/3XPOPefuHQLhqm7JAMfUgufywRCb+JlZLw5eMFwPCKlATYmTiOL9/AAYJsGsmkPq4rhZRJBcgsttzSB8qaXE/xPrIKhq8Zje7SVnl2MJrrTyFp19UTYFQD2AhgDNATQJ0lXAwgTCWgYzk22oL8rA4bT1EOKoZ+w7KjpccE7PGQapZgCC+Ofn8xAfExkgdnZhCbn3+g0DQTOA1nM5KN6ZFHKmHa4plDa+NIQXaAbgtRciNioipEjW54ftRqe5AbD2QsRZGYDjbDZK0pNDznKzcxLHHg6Z2wMykmwYKM9DQlASnJlfFJPgqJs1NwBBnQChrnAX8rdtEMV2f3SjstNlGPG0Hab7AWFsiPA1xcvGOKluC7iv1L5gx0ac2bsZ2VvWYmtiLOKjI7HE8fjx24d3U3Po+uDG/aHPmGJ9K5JjNNcBSgX9HaWcfdS1djSe3IdTezbJCvMu+nGxw4WGwU+ytnIGugFwqWsUtQXpcuMNuC8k3PreMVXPBBvrBsD4Ty/S1sWpEsPxPHLu9mN44peq5/431g0ArQrC7TsMD8DP8UipfQq3V1tSNDwAwXNON71C05uvmpzIFABu943jQrvT+AAejUzg1rNxvJ30iGKyUuJReWg7TmSmLCuu7f00jj54YWwAgviyx69DinhSth/Hd0tDGPnmQdadXmMDONDQJ7mcHUxNxGB5nqTAL7PzSK3vMTaAGHsHfH4upIiYSAbz14skBXoWlpBws8vYAIJ7h2A1y5XSi34e0fZ26wLgeYC5Gth8KaWhm2UwHA8QxMo9LwWEAtB6PkCuvdW6HyA1U2p/j4aAQgI0BGgIaDwiozYm1dqrqQPoKkCXQVoH0EKIVoJBf8QoLAO0H5VVm9XV2tNVIIhAuABXvBlS6mJ6t9NcCutdmNLxUQBaewGlhPVuRz2AeoDGblDvrq10fDQEaAhYPgSqWlkwUHc2RWmA6d5OfHHS4QCYEt2PdXUG2Gzhl6cxgwgml4hghTfIeVIHcPkAs2Z1YOvlWzkWYLpBmErUHBn9A//QJWCgfoEmAAAAAElFTkSuQmCC
