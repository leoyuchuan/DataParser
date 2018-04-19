# DataParser

## Introduction
This repository contains a DataParser.py script for parsing a tab delimited file and store it into sqlite3 database.

## Language / Technology Used
Python2.7, Pandas

## Database Used
SQLite3

## Python Libraries Used
pandas, sqlite3, sys

## How to use
1. For help:

   ``$ python DataParser.py -h``

2. For parsing:

   ``$ python DataParser.py[ <input_path> <output_path> <table_name>]``

   Example:
      * ``$ python DataParser.py``

      * ``$ python DataParser.py http://www.zurionlinestore.com/sites/all/modules/zurionlinestore/files/google/googlebase.txt result.db googlebase``

3. To install required libraries:
   
   ``$ pip install pandas``

   Other libraries should come with python2.7.

## Sample Result
A sample result is provided in the folder SampleResult.
The table name is "googlebase" and is stored in res.db file.

It can be viewed using "DB Browser for SQLite" from http://sqlitebrowser.org/.
