# MY HOOD
### 11th Jan. 2022
## Author 
[Maryann Mwikali](https://github.com/Maryan23)
# Description 

##  Live Link
https://jiraninext.herokuapp.com/

## Screenshots
<img src="static/images/Screenshot from 2021-12-14 14-07-22.png">
<img src="static/images/Screenshot from 2021-12-14 14-07-30.png">
<img src="static/images/Screenshot from 2021-12-14 14-08-05.png">

## User Story 
1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the health department and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.


## Setup and Installation 

##### Clone the repository: 
 ```bash
git@github.com:Maryan23/MyHood.git
```
##### Navigate into the folder and install requirements 
 ```bash
cd Laurels
 - pip install -r requirements.txt
```
##### Install and activate Virtual 
 ```bash
- python3 -m venv virtual
- source virtual/bin/activate
```
##### Install Dependencies 
 ```bash
 pip install -r requirements.txt
```
##### Setup Database 
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations photos
 ```
 Now Migrate
 ```bash
 python manage.py migrate
```
##### Run the application 
 ```bash
 python manage.py runserver
```
##### Running the application 
 ```bash
 python manage.py server
```
##### Testing the application 
 ```bash
 python manage.py test
```
Open the application on your browser `127.0.0.1:8000`.
## Technology used 
* [Python3.8](https://www.python.org/)
* [Django==3.2.9](https://docs.djangoproject.com/en/2.2/)
* [Heroku](https://heroku.com)
## Known Bugs 
* There are no known bugs
## Support and Contact Information
Incase of any contributions fork the repo and make any substantial changes.
Incase of any ideas,suggestions or complaints feel free to connect with me on mwikali119@gmail.com 

## License
MIT
Copyright (c) 2021 **MyHood**