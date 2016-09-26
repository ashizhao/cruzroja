# Installation on a new server

The following instructions have been teste on ubuntu 16.04 server edition.

See https://docs.djangoproject.com/en/1.10/intro/install/ and https://docs.djangoproject.com/en/1.10/ref/contrib/gis/install/ for detailed installation on other platforms.

# Installing Postgis and libraries

From https://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS22UbuntuPGSQL95Apt:

    # add repository
    sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt xenial-pgdg main" >> /etc/apt/sources.list'
	# add keys
    wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -
	# update
	sudo apt-get update
	# install postgis
	sudo apt-get install postgresql-9.5-postgis-2.2 pgadmin3 postgresql-contrib-9.5
    # Install pgRouting 2.1 package 
    sudo apt-get install postgresql-9.5-pgrouting

## Enable Adminpack

   sudo -u postgres psql
   CREATE EXTENSION adminpack;
	
## Create database and enable postgis and pgrouting

	CREATE DATABASE cruzroja;
	\connect cruzroja;

	CREATE EXTENSION postgis;
	SELECT postgis_full_version();

    CREATE  EXTENSION pgrouting;
	SELECT * FROM pgr_version();
	
## Create user

	sudo su - postgres
	createuser -d -E -i -l -P -r -s cruzroja

## Install shp2pgsql-gui

	sudo apt-get install postgis

## Install psycopg2

	sudo apt-get install python3-psycopg2

# Installing Django

## Setting up python3 as default

	sudo update-alternatives --remove python /usr/bin/python2
	sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1

## Installing pip

	sudo apt-get install python3-pip
	
## Installing django

	sudo pip3 install django==1.10

## Installing django-braces

	sudo apt-get install python3-django-braces

## Clone repository

	git clone git@cruzroja.ucsd.edu:aed

You might have done that already if you're reading this inside a
cloned repo.

## Create your local settings file

A template is found in the doc/settings.py.

	cp doc/settings.template aed/settings.py
	
Edit aed/setting.py to reflect your local settings. Important settings
are 

- SECRET_KEY
- DATABASES: NAME, USER, and PASSWORD

