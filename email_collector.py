import imaplib
from imaplib import IMAP4
import re

uid_pattern = re.compile(r'\d+ \(UID (?P<uid>\d+)\)')
query_string_file_path = "./query_strings.txt"

class EmailCollector:
    def __init__(self, imap_url, port, email_address, password):
        self.__imap_url = imap_url
        self.__port = port
        self.__email_address = email_address
        self.__password = password
        self.__imap_url = imap_url
        self.__login()
        self.__folder = "Applications"
        self.create_applications_folder()

    def create_applications_folder(self):
        self.__imap_connection.create(self.__folder)

    def __move_email(self, email_id):
        resp, data = self.__imap_connection.fetch(email_id, '(UID)')
        email_uid = self.__parse_uid(
            data[0].decode())  # have to decode the data because it's returned as a byte like object
        self.__imap_connection.uid('COPY', email_uid, self.__folder)

    @staticmethod
    def __parse_uid(data):
        match = uid_pattern.match(data)
        return match.group('uid')

    def scan_email(self):
        """Scans the email inbox and moves all application emails found to the Applications mailbox"""
        self.__imap_connection.select('INBOX')
        for email_id in self.__find_application_email_ids():
            self.__move_email(email_id)

    def __find_application_email_ids(self):
        """Search using all queries in query_strings.txt and return an array of email_ids"""
        with open(query_string_file_path, 'r') as file:  # reads in query_strings.txt into an array of query strings
            query_strings = file.read().split('\n')
        email_ids = []
        for query in query_strings:
            try:
                email_ids.extend(self.__imap_connection.search(None, query)[1][0].split())
            except IMAP4.error:
                self.__login()
                email_ids.extend(self.__imap_connection.search(None, query)[1][0].split())
        return email_ids

    def __login(self):
        self.__imap_connection = imaplib.IMAP4_SSL(self.__imap_url, self.__port)
        self.__imap_connection.login(self.__email_address, self.__password)