# README Boilerplate

I created this project while researching a number of solutions of trying to connect Django with ReactJS. This project uses the Django Rest Framework (DRF) and Webpack modules which made it possible for ReactJS and Django to exchange data via API.

In the next iteration I will probably include Redux to manage states more efficiently.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation

I recommend to use Python virtualenv to set up your virtual environment with the required Python packages. In any case, these are the Python modules needed:

```sh
pip install django
pip install django-webpack-loader
pip install djangorestframework
```

Alternatively you can install the python packages from requirements.txt:
```sh
pip install -r requirements.txt
```

You also need to install a couple of NPM modules:
```sh
npm install --save-dev jquery react react-dom webpack webpack-bundle-tracker babel-loader babel-core babel-preset-es2015 babel-preset-react
```

I kept this simple, so all data will be stored on sqllite database. You can adapt your database of choice accordingly.

## Usage

This project is made up of the following components:
- x1 Django project called `reactdrf` which can be accessed through http://localhost:8000.
- x1 Django application called `api` which can be accessed through http://localhost:8000/api/. This is created as a DRF API with very basic routes, namely POST and GET.
- x1 ReactJS Class based component called `BookList` which is loaded from assets/js/index.js and compiled inside assets/bundles (refer to webpack.config.js)

In order to run this project you need to first compile the frontend through webpack as follows:
```sh
./node_modules/.bin/webpack --config webpack.config.js
```

Once frontend is compiled, the Django server can be run as follows:
```sh
python manage.py runserver
```

Feel free to remove any sections that aren't applicable to your project.

## Credits
As I have explained in the introduction, I have made extensive research to come up with the best way to integrate Django with ReactJS. I would like to credit in particular the following developers who inspired me:
- [Jonathan Cox](http://geezhawk.github.io/using-react-with-django-rest-framework)
- [Owaise Lone](http://owaislone.org/blog/webpack-plus-reactjs-and-django/)
