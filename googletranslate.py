import sys
import requests
import json

class NewTranslate:
    def __init__(self, sl, tl):
        self.sl=sl.lower()
        self.tl=tl.lower()
        json_data=json.load(open('lang.json', 'r'))
        if self.sl not in json_data:
            print '%s language not found' %sl
            sys.exit(1)
        elif self.tl not in json_data:
            print '%s language not found' %tl
            sys,exit(1)
        elif self.tl=='detect-language':
            print 'Translation language should not be auto'
            sys.exit(1)
        self.sl=json_data[self.sl]
        self.tl=json_data[self.tl]

    def translate(self, query):
        parameters={'sl':self.sl, 'tl':self.tl, 'ie':'UTF-8', 'q':query}
        q=requests.get('https://translate.google.com/m', params=parameters)
        html_data=str(q.text)
        return (html_data.split('class="t0">')[-1]).split('<')[0]
