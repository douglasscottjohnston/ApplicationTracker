from email_collector import EmailCollector
import getpass


def main():
    collector = EmailCollector("imap.gmail.com", 993, input("Enter your email address: "), getpass.getpass("Enter your password: "))
    collector.scan_email()


if __name__ == '__main__':
    main()
