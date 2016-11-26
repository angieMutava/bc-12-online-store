## ISOKO

Isoko is an online management store where registered users can add stores, add products to the stores and send public urls of specific stores to logged out users. It is a bootcamp project built as a fulfillment of [Andela Kenya's](https://andela.com/) Cohort XII application process.

It is uses Python as the development stack and Flask as the web development framework.

> Isoko is a Kinyarwanda name that means market. Isoko can also be translated into i-soko to loosely mean my-market.


### Contributors
* [@jackiemacharia](https://github.com/jackiemacharia)


### Project Requirements

###### Online Store Application
* As a user I should be able to signup / login
* As a user I should be able to create a store
* As a store owner, I should be able to add products
* Every store created on the platform should have a shareable public URL


### Installation and Setup:

1. Clone the directory:

          * Using HTTPS: git clone https://github.com/jackiemacharia/bc-12-online-store.git

          * Using an SSH Key: git clone git@github.com:jackiemacharia/bc-12-online-store.git

2. Navigate to the app directory ```cd bc-12-online-store```

3. Create and activate a ```virtual environment```. Instructions on how to install virtual environments are available [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

4. Install requirements: ```pip install -r requirements.txt```

5. Setup a [PostgreSQL](https://www.postgresql.org/) database locally and set it as the end point to your ```DATABASE_URL``` path. Eg. if the database name is isokodb, the path becomes ```DATABASE_URL="postgresql:///isokodb"```

6. Export ```DATABASE_URL``` and ```APP_SETTINGS``` paths.

          * Using virtualenv: run the following commands:
                  * export DATABASE_URL="postgresql:///isokodb"
                  * export APP_SETTINGS="config.ProductionConfig"

          * Using virtualenvwrapper: add the paths to postactivate and save:
                  * export DATABASE_URL="postgresql:///isokodb"
                  * export APP_SETTINGS="config.ProductionConfig"

7. Initialize your PostgreSQL database and migrate the tables ```python manage.py db init``` ```python manage.py db migrate``` ```python manage.py db upgrade```

8. Run the app: ```python manage.py runserver```


### Live Demo

View the live app [here](https://isoko.herokuapp.com/)

The following credentials are available for application demo:
        * Email: jackiemacharia@example.com
        * Password: admin2


### Store Public URL
[Here](https://isoko.herokuapp.com/overview/15) is a store url available to non-registered users.


### Dependencies

* Language: ```Python 2.7.6```
* Database: ```PostgreSQL```


### Resources

* [Flask](http://flask.pocoo.org/)
* [Python](https://docs.python.org/2.7/)
* [Bootstrap](https://getbootstrap.com/)
* [Unsplash](https://unsplash.com/)

### Still Pending

* Application testing and coverage
* Additional app features and UI tweaks
* Sign up email confirmation
* Customize public urls to include store names
