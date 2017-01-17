import urllib3
import bs4


class getmorning_weather(object):
    """docstring for getweather."""
    def __init__(self, language):
        http = urllib3.PoolManager()
        if language == 'zh':
            url = 'http://www.cwb.gov.tw/V7/forecast/f_index.htm'
        else:
            url = 'http://www.cwb.gov.tw/V7e/forecast/f_index.htm'
        response = http.request('GET', url)
        html = response.data
        self.soup = bs4.BeautifulSoup(html, 'html.parser')

    def gettemperature(self, city):
        city = self.soup.find('tr', id=city)
        where = city.findAll('td')[0].string
        degree = city.findAll('td')[1].string
        return where, degree

    def getrainfall(self, city):
        city = self.soup.find('tr', id=city)
        where = city.findAll('td')[0].string
        rainfall = city.findAll('td')[2].string
        return where, rainfall

    def getweather(self, city):
        city = self.soup.find('tr', id=city)
        where = city.findAll('td')[0].string
        weather = city.findAll('td')[3].a.div.img.get('alt')
        return where, weather


class gettonight_weather(object):
    """docstring for getweather."""
    def __init__(self, language):
        http = urllib3.PoolManager()
        if language == 'zh':
            url = 'http://www.cwb.gov.tw/V7/forecast/f_index2.htm'
        else:
            url = 'http://www.cwb.gov.tw/V7e/forecast/f_index2.htm'
        response = http.request('GET', url)
        html = response.data
        self.soup = bs4.BeautifulSoup(html, 'html.parser')

    def gettemperature(self, city):
        city = self.soup.find('tr', id=city)
        where = city.findAll('td')[0].string
        degree = city.findAll('td')[1].string
        return where, degree

    def getrainfall(self, city):
        city = self.soup.find('tr', id=city)
        where = city.findAll('td')[0].string
        rainfall = city.findAll('td')[2].string
        return where, rainfall

    def getweather(self, city):
        city = self.soup.find('tr', id=city)
        where = city.findAll('td')[0].string
        weather = city.findAll('td')[3].a.div.img.get('alt')
        return where, weather


class gettomorrow_weather(object):
    """docstring for getweather."""
    def __init__(self, language):
        http = urllib3.PoolManager()
        if language == 'zh':
            url = 'http://www.cwb.gov.tw/V7/forecast/f_index3.htm'
        else:
            url = 'http://www.cwb.gov.tw/V7e/forecast/f_index3.htm'
        response = http.request('GET', url)
        html = response.data
        self.soup = bs4.BeautifulSoup(html, 'html.parser')

    def gettemperature(self, city):
        city = self.soup.find('tr', id=city)
        where = city.findAll('td')[0].string
        degree = city.findAll('td')[1].string
        return where, degree

    def getrainfall(self, city):
        city = self.soup.find('tr', id=city)
        where = city.findAll('td')[0].string
        rainfall = city.findAll('td')[2].string
        return where, rainfall

    def getweather(self, city):
        city = self.soup.find('tr', id=city)
        where = city.findAll('td')[0].string
        weather = city.findAll('td')[3].a.div.img.get('alt')
        return where, weather


def main():
    w = getmorning_weather('zh')
    where, degree = w.gettemperature('TaipeiCityList')
    print("%s is %s" % (where, degree))
    where, rainfall = w.getrainfall('TaipeiCityList')
    print("%s is %s" % (where, rainfall))
    where, weather = w.getweather('TaipeiCityList')
    print("%s is %s" % (where, weather))
    w = gettonight_weather('zh')
    where, degree = w.gettemperature('TaipeiCityList')
    print("%s is %s" % (where, degree))
    where, rainfall = w.getrainfall('TaipeiCityList')
    print("%s is %s" % (where, rainfall))
    where, weather = w.getweather('TaipeiCityList')
    print("%s is %s" % (where, weather))
    w = gettomorrow_weather('zh')
    where, degree = w.gettemperature('TaipeiCityList')
    print("%s is %s" % (where, degree))
    where, rainfall = w.getrainfall('TaipeiCityList')
    print("%s is %s" % (where, rainfall))
    where, weather = w.getweather('TaipeiCityList')
    print("%s is %s" % (where, weather))


if __name__ == '__main__':
    main()
