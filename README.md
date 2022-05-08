## Shortster
- A url shortening service that provides you with a unique code to access your long website links making sharing links easier than ever.

### System Requirements
- python 3.x
- django
- django restframework
- postgresql database
- pipenv

#### Setup
- clone the repo url
- create a `.venv` folder in the root of the project
- initialize a virtualenvironment `pipenv -p python3`
- install dependencies `pipenv install`
- create a database e.g. `shortster`
- add a `.env` file to the project root and populate the following env variables with corresponding values.

```
DEBUG=True

DATABASE_URL='database_URi' e.g postgresql://user:password@localhost:5432/database_name

SECRET_KEY='something super secret'

ALLOWED_HOSTS=.localhost,*.*.com

```

- run database migrations `python manage.py migrate`
- create a superuser to access the dashboard `python manage.py createsuperuser`
- run the development server `python manage.py runserver`
- visit the admin dashboard on `http://localhost:8000/admin/`

#### Use the API
- you will need to first login via the admin dashboard (assumed authentication)

#### view your shortened urls
- visit `http://localhost:8000/api/
![Screen Shot 2022-05-08 at 13 57 33](https://user-images.githubusercontent.com/18280598/167294952-070f31a7-ec2a-4cc6-8891-c23ba599f810.png)


#### Test redirection
- open one of the created items url e.g. `"url": "http://localhost:8000/api/a916fj/"`

# creating shortened urls
- send a post request to `http://localhost:8000/api/new/url/`

```
sample data

 {
     "website":"https://google.com",
     "short_code":"12ta"
 }

```

#### check stats of your website
- visits any if your shortened links stats page e.g. `http://localhost:8000/api/a916fj/stats/`
![Screen Shot 2022-05-08 at 13 57 17](https://user-images.githubusercontent.com/18280598/167294967-2f9c0321-157d-45fe-86b4-cfa6bc789565.png)
