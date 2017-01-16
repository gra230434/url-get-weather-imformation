import urllib3
import bs4


def gettemperature(city, language='zh'):
    http = urllib3.PoolManager()
    if language=='zh':
        url = 'http://www.cwb.gov.tw/V7/forecast/f_index.htm'
    else:
        url = 'http://www.cwb.gov.tw/V7e/forecast/f_index.htm'
    response = http.request('GET', url)
    html = response.data
    soup = bs4.BeautifulSoup(html, 'html.parser')
    where = soup.find('tr', id=city).findAll('td')[0].string
    degree = soup.find('tr', id=city).findAll('td')[1].string
    return where, degree


def gettemperatureTomorrow(city, language='zh'):
    http = urllib3.PoolManager()
    if language=='zh':
        url = 'http://www.cwb.gov.tw/V7/forecast/f_index.htm'
    else:
        url = 'http://www.cwb.gov.tw/V7e/forecast/f_index.htm'
    response = http.request('GET', url)
    html = response.data
    soup = bs4.BeautifulSoup(html, 'html.parser')
    where = soup.find('tr', id=city).findAll('td')[0].string
    degree = soup.find('tr', id=city).findAll('td')[1].string
    return where, degree


def getrainfall(city, language='zh'):
    http = urllib3.PoolManager()
    if language=='zh':
        url = 'http://www.cwb.gov.tw/V7/forecast/f_index.htm'
    else:
        url = 'http://www.cwb.gov.tw/V7e/forecast/f_index.htm'
    response = http.request('GET', url)
    html = response.data
    soup = bs4.BeautifulSoup(html, 'html.parser')
    where = soup.find('tr', id=city).findAll('td')[0].string
    rainfall = soup.find('tr', id=city).findAll('td')[2].string
    return where, rainfall


def getweather(city, language='zh'):
    http = urllib3.PoolManager()
    if language=='zh':
        url = 'http://www.cwb.gov.tw/V7/forecast/f_index.htm'
    else:
        url = 'http://www.cwb.gov.tw/V7e/forecast/f_index.htm'
    response = http.request('GET', url)
    html = response.data
    soup = bs4.BeautifulSoup(html, 'html.parser')
    where = soup.find('tr', id=city).findAll('td')[0].string
    weather = soup.find('tr', id=city).findAll('td')[3].a.div.img.get('alt')
    return where, weather


def main():
    where, degree = gettemperature('TaipeiCityList')
    print("%s is %s" % (where, degree))
    where, degree = gettemperatureTomorrow('TaipeiCityList', 'en')
    print("%s is %s" % (where, degree))
    where, rainfall = getrainfall('TaipeiCityList')
    print("%s is %s" % (where, rainfall))
    where, weather = getweather('TaipeiCityList', 'en')
    print("%s is %s" % (where, weather))


if __name__ == '__main__':
    main()
