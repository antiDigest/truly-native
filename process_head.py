from bs4 import BeautifulSoup as bs
import os
import sys
import logging
import string
import glob
import cssutils as cu
import json

ferr = open("errors_in_scraping.log", "w")


def parse_page(in_file):
    page = open(in_file, 'r')
    soup = bs(page)
    print("#"*20)
    # print(soup.head.find_all('link'))

    for link in soup.head.find_all('link'):
        print str(link.get('href').encode('ascii', 'ignore'))
        
    print("#"*20)
    return None


def parse_head(soup):
    """ parameters:
            - soup: beautifulSoup4 parsed html page
        out:
            - textdata: a list of parsed text output by looping over html paragraph tags
        note:
            - could soup.get_text() instead but the output is more noisy """
    linkdata = ['']

    for parser in soup.find_all('head'):
        for link in parse.find_all('a'):
            try:
                linkdata.append(str(link.get('href').encode('ascii', 'ignore')))
            except Exception:
                continue

    return filter(None, linkdata)


def parse_body(soup):
    """ parameters:
            - soup: beautifulSoup4 parsed html page
        out:
            - title: parsed title """

    linkdata = ['']

    for parser in soup.find_all('body'):
        for link in parse.find_all('a'):
            try:
                linkdata.append(str(link.get('href').encode('ascii', 'ignore')))
            except Exception:
                continue

    return filter(None, linkdata)


def parse_footer(soup):
    """ parameters:
            - soup: beautifulSoup4 parsed html page
        out:
            - linkdata: a list of parsed links by looping over html link tags
        note:
            - some bad links in here, this could use more processing """

    linkdata = ['']


    # print(soup.head)
    # for parser in soup.get('footer'):
    #     return parser
    #     for link in parse.find_all('a'):
    #         try:
    #             linkdata.append(str(link.get('href').encode('ascii', 'ignore')))
    #         except Exception:
    #             continue

    return filter(None, linkdata)


def main(argv):
    json_array, last_bucket = [], str(0)

    fIn = glob.glob('new/*raw*')

    for idx, filename in enumerate(fIn):

        filenameDetails = filename.split("/")
        urlId = filenameDetails[-1].split('_')[0]
        bucket = filenameDetails[-2]

        doc = parse_page(filename)
        break

        json_array.append(doc)


if __name__ == "__main__":
    main(sys.argv)
