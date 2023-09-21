import time
import getpass

# internal packages
from email_collector import EmailCollector


def main():
    collector = EmailCollector("imap.gmail.com", 993, input("Enter your email address: "), getpass.getpass("Enter your password: "))
    response = input("Type 1, to scan your email once, or 2 to scan your email every 5 minutes: ")
    if response == "1":
        collector.scan_email()
    else:
        print("Scanning email every 5 minutes, type Ctrl+C to stop")
        while True:
            collector.scan_email()
            print("finished scan, waiting for 5 minutes, type Ctrl+C to stop")
            time.sleep(300)


if __name__ == '__main__':
    main()
