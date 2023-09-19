import argparse
import re
import urllib.request
import csv
import sys
import datetime
import io

def downloadFile(url):
    # read the URL

    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response


def processFile(file_content):

    reader = csv.reader(io.StringIO(file_content))
    for count, line in enumerate(reader):
        print(count, line)



def main(url):
    print(f"Running main with URL = {url}...")
    url_data = downloadFile(url)
    processFile(url_data)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
