import urllib3
import bs4


class gettwcitylist(object):
    """docstring for get tw city list."""
    def __init__(self, language):
        http = urllib3.PoolManager()
        if language == 'zh':
            url = 'http://www.cwb.gov.tw/V7/forecast/f_index.htm'
        else:
            url = 'http://www.cwb.gov.tw/V7e/forecast/f_index.htm'
        response = http.request('GET', url)
        html = response.data
        self.soup = bs4.BeautifulSoup(html, 'html.parser')

    def twcity(self):
        citylist = []
        city = self.soup.findAll('tr')
        for value in city:
            if value.get('id') is not None:
                citylist.append(value.get('id').rstrip('List'))
        return citylist

    def getcityurl(self, city):
        city = self.soup.find('tr', id=city)
        url = city.findAll('td')[0].a.get('href')
        url = 'http://www.cwb.gov.tw' + url
        return url


def main():
    c = gettwcitylist('zh')
    citylist = c.twcity()
    for value in citylist:
        print(value)


if __name__ == '__main__':
    main()
