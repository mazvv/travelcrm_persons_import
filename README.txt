TravelCRM Persons Import
===============================

Getting Started
---------------

This application is extension for TravelCRM that allows to import existing
clients into TravelCRM

To install application:

- cd <directory containing this file>
- $VENV/bin/python setup.py develop


To add this app in yor TravelCRM instance add in your ini file into pyramid.includes
this row
- travelcrm_persons_import

After that you need to register travelcrm_persons_import into TravelCRM.
Go to System -> Resources Types and add new resource type with data:

public name: Persons Import
name: persons_import
resource: travelcrm_persons_import.resources.persons_import.PersonsImportResource

Add this app in any menu you want with url /persons_import/action and action dialog_open


CSV File
--------
Please use csv file with delimiter ';' and quotechar '"'.
For foreign passport end date use dates in format 'YYYY-MM-DD'

Import runs as background task and after complete you will get notification.
