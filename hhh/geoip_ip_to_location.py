import sys
import pygeoip
import json


def main():
    #     geoip_country()
    geoip_city()
    print 'done'


def geoip_city():
    path = '/Users/user14/Documents/cindy/geoip-api-python-master/tests/data/GeoLiteCity.dat'
    csv = 'dataset/ip_only.csv'

    data = []

    f = open(csv, 'r')
    for i in open(csv):
        data.append(f.readline())
    o = open('dataset/ip1.txt', 'w')

    for i in data:
        gic = pygeoip.GeoIP(path)
        k = json.dumps(gic.record_by_addr(i))
        j = i.split('\r')[0]

        o.write(j + '@' + k + '\n')


if __name__ == '__main__':
    main()