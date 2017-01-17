from Class.getweather import getmorning_weather


def main():
    w = getmorning_weather('zh')
    where, degree = w.gettemperature('TaipeiCityList')
    print("%s is %s" % (where, degree))
    where, rainfall = w.getrainfall('TaipeiCityList')
    print("%s is %s" % (where, rainfall))
    where, weather = w.getweather('TaipeiCityList')
    print("%s is %s" % (where, weather))
    url = w.getcityurl('TaipeiCityList')
    print(url)


if __name__ == '__main__':
    main()
