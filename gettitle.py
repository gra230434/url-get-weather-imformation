import urllib3
import bs4


def gettemperature(city):
    http = urllib3.PoolManager()
    url = 'http://www.cwb.gov.tw/V7/forecast/f_index.htm'
    response = http.request('GET', url)
    html = response.data
    soup = bs4.BeautifulSoup(html, 'html.parser')
    print(soup.find('tr', id=city).findAll('td')[0].string)
    print(soup.find('tr', id=city).findAll('td')[1].string)
    pass


def gettemperatureTomorrow(city):
    http = urllib3.PoolManager()
    url = 'http://www.cwb.gov.tw/V7/forecast/f_index3.htm'
    response = http.request('GET', url)
    html = response.data
    soup = bs4.BeautifulSoup(html, 'html.parser')
    print(soup.find('tr', id=city).findAll('td')[0].string)
    print(soup.find('tr', id=city).findAll('td')[1].string)
    pass


def main():
    gettemperature('TaipeiCityList')
    gettemperatureTomorrow('TaipeiCityList')


if __name__ == '__main__':
    main()
