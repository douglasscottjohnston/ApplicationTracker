# Application Tracker
Uses imaplib to search your inbox using queries in query_strings.txt, and moves them to the "Applications" folder

## How to Use
Currently, Gmail is the only supported email inbox\
To use the application tracker, you must create an application specific password for your Gmail account\
see https://support.google.com/accounts/answer/185833 for more information.\
Once you've created the application specific password, you must use that to log into the program\
\
For better accuracy you can add your own imap search queries to query_strings.txt

## Requirements
Python 3.7.16\
Conda 23.1.0

## Future Improvements
- Add a text classification model to classify application emails for better accuracy
- Differentiate application accepted and application declined emails
- Add support for multiple/different email systems