# DataParser

## Introduction
This repository contains a DataParser.py script for parsing a tab delimited file and store it into sqlite3 database.

## Language / Technology Used
Python, Pandas

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

