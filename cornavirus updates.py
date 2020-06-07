import webbrowser, requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
class corona_info():
    website = 'https://google.com/search?q=coronavirus+cases+in+india'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
    web_info = requests.get(website, headers=headers).text
    web_scraper = BeautifulSoup(web_info, 'html.parser')
    def __init__(self):
        self.total_cases_india = corona_info.web_scraper.find('div', jsname='fUyIqc').text
        self.increased_cases = corona_info.web_scraper.find('div', class_='h5Hgwe').span.text
    def push_notification(self):
        notification = ToastNotifier()
        notification.show_toast(f'LATEST CORONAVIRUS UPDATES:', f'''coronavirus cases in india today: {self.total_cases_india}
coronavirus cases increased from yesterday: {self.increased_cases}''')

corona_today = corona_info()
corona_today.push_notification()


