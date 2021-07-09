# Blind SQLi conditional responses by triggering SQL errors ![Python](https://img.shields.io/badge/Python-yellow?logo=python)
This script is an exercise for [this ](https://portswigger.net/web-security/sql-injection/blind#inducing-conditional-responses-by-triggering-sql-errors) lab.
Very often, an unhandled error thrown by the database will cause some difference in the application's response (such as an error message), allowing us to infer the truth of the injected condition.

In this situation, it is often possible to induce the application to return conditional responses by triggering SQL errors conditionally, depending on an injected condition. This involves modifying the query so that it will cause a database error if the condition is true, but not if the condition is false. 

## Run script
The script accepts 2 parameters, a mandatory URL parameter and an mandatory Tracking id file parameter. 
### Usage
Without a password file:

       python main.py URL TrackingID