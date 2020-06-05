import webbrowser, requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
website = 'https://google.com/search?q=coronavirus+cases+in+india'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
web_info = requests.get(website, headers=headers).text
web_scraper = BeautifulSoup(web_info, 'html.parser')
total_cases_india = web_scraper.find('div', jsname='fUyIqc').text
increased_cases = web_scraper.find('div', class_='h5Hgwe').span.text
notification = ToastNotifier()
notification.show_toast(f'LATEST CORONAVIRUS UPDATES:', f'''coronavirus cases in india today: {total_cases_india}
coronavirus cases increased from yesterday: {increased_cases}''')

