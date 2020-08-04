# django timezone
It is django based timezone project.

# Instructions 

1) ### Installations
  Make sure to have python version 3 install on you pc or laptop. 
  If not install it from [here](https://www.python.org) <br>
  **Clone repository** <br>
  `ps://github.com/surajkarale15/shopping.git`<br>
  `cd shopping`
  
2) ### Installing dependencies 
  It will install all required dependies in the project.<br>
  `pip install -r requirements.txt`
  
3) Add 'category,type,product' to your 'INSTALLED_APPS' setting.
	INSTALLED_APPS={
		...
		'category',
		'type',
		'product',
		...
	}
	
	Add the following to your projects 'urls.py' file, substituting 'api/v1/'
	for whatever you want the service base url to be.
	urlpatterns = [
    ...
    url('category/',include('category.urls')),
    url('type/',include('type.urls')),
    url('product/',include('product.urls')),
    
	...
	]
	
4) ### Migrations 
  To run migrations. <br>
  `python manage.py makemigrations`<br>
  `python manage.py migrate`

5) ### Running locally
  To run at localhost. It will run on port 8000 by default.<br>
  `python manage.py runserver` 
 
 

  
