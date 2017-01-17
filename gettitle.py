from Class.getweather import getweather


def main():
    w = getweather('zh')
    where, degree = w.gettemperature('TaipeiCityList')
    print("%s is %s" % (where, degree))
    where, degree = w.gettemperatureTomorrow('TaipeiCityList')
    print("%s is %s" % (where, degree))
    where, rainfall = w.getrainfall('TaipeiCityList')
    print("%s is %s" % (where, rainfall))
    where, weather = w.getweather('TaipeiCityList')
    print("%s is %s" % (where, weather))


if __name__ == '__main__':
    main()
