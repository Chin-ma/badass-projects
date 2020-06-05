'''this programs copies text from ur command line or clipboard,
searches it on google and opens the top links in ur browser
'''
import requests, webbrowser, pyperclip, sys
from bs4 import BeautifulSoup

if len(sys.argv)>1:
    string = sys.argv[1:]
    string = '+'.join(string)

else:
    string = pyperclip.paste()
    string = string.split(' ')
    string = '+'.join(string)
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
website = f'http://google.com/search?hl=en&q={string}'
req_web = requests.get(website, headers=headers).text
parser = BeautifulSoup(req_web, 'html.parser')
gotolinks = [link.a['href'] for link in parser.find_all('div', class_='r')]
print(gotolinks)
for link in gotolinks:
    webbrowser.open(link)
