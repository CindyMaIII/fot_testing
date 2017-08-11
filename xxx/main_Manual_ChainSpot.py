# -*- coding: UTF-8 -*-

import sys
import json
# import codecs
# import urllib
# import cgi
# import re
from pyes import ES
# import time
import random



def onlyReadFile(_path):
    with open(_path) as data_file:
        data = json.load(data_file)
    return data


def insertElasticsearch(_index, _type, data):
    # conn = ES('127.0.0.1:9200', timeout=3.5)
    # conn = ES('192.168.30.63:9200', timeout=3.5)
    # conn = ES('140.92.13.186:9200', timeout=3.5)
    conn = ES('localhost:9200', timeout=3.5)
    conn.index(data, _index, _type)


def toElasticsearch(readfile, newreplacestring):
    print 'replacestring：', newreplacestring
    for r_time in readfile.keys():
        for element in readfile[r_time]:
            newElement = dict()
            # newElement.clear()


            # print element['LogTime']
            newElement = element
            filesize = random.sample([105, 103, 100, 98, 95], 1)[0]
            newElement['filesize'] = filesize
            newElement['replacestring'] = newreplacestring
            newElement['LogTime'] = element['LogTime'].replace("2016-04-01", newreplacestring)
            newElement['@LogTime'] = element['@LogTime'].replace("2016-04-01", newreplacestring)

            # print json.dumps(newElement),'\n'


            insertElasticsearch('mic_demo', 'chainspot', newElement)
            # break

    print '_____________'

    readfile = dict()


'''  異常順序改變 '''


def onlyReadFile_Logtime(readfile, replacestring):
    logtimeListRandom = list()
    logtimeListreg = list()
    datasetList = list()
    for r_time in readfile.keys():
        for element in readfile[r_time]:
            # newtime = element['LogTime'].replace(replacestring, "2016-04-01")
            newtime = element['LogTime'].replace("2016-04-01", replacestring)
            newtime = element['@LogTime'].replace("2016-04-01", replacestring)
            logtimeListreg.append(newtime)
            datasetList.append(element)
    logtimeListRandom = random.sample(logtimeListreg, len(logtimeListreg))
    return datasetList, logtimeListRandom


def toElasticsearchRamdom(dataset, replacestring, randomLogtime):
    # allresult = list()
    for i in range(len(dataset)):
        element = dataset[i]
        filesize = random.sample([110, 120, 130, 100, 80, 90, 70], 1)[0]
        element['filesize'] = filesize
        element['replacestring'] = replacestring
        element['LogTime'] = randomLogtime[i]
        element['@LogTime'] = randomLogtime[i]
        # allresult.append(element)
        insertElasticsearch('mic_demo', 'chainspot', element)
        # return allresult


'''  合併異場資料 '''


def onlyReadAnotherFile(readfile_forURI):
    URI_List = list()
    flag = 0
    for r_time in readfile_forURI.keys():
        for element in readfile_forURI[r_time]:
            URI = element['URI']
            URI_List.append(URI)
            flag = flag + 1
            if flag == 30:
                break
        # if flag == 30:
        #     break
    return URI_List


def mergeData(rawDatasetList, URI_List, randomLogtime):
    # mergeData(rawDatasetList, URI_List, randomLogtime)
    print 'rawDatasetList:', len(rawDatasetList)
    print 'URI_List:', len(URI_List)
    print 'randomLogtime', len(randomLogtime)
    for i in range(len(rawDatasetList)):
        element_new = rawDatasetList[i]
        element_new['URI'] = URI_List[i]
        element_new['LogTime'] = randomLogtime[i]
        element_new['@LogTime'] = randomLogtime[i]
        filesize = random.sample([100, 101, 102], 1)[0]
        element_new['filesize'] = filesize
        insertElasticsearch('mic_demo', 'chainspot', element_new)

    print len(rawDatasetList)

    for element in rawDatasetList:
        # print '_____element=====>', element
        insertElasticsearch('mic_demo', 'chainspot', element)


def outputFile(data, _outputPath):
    with open(_outputPath, 'w') as outfile:
        json.dump(data, _outputPath, indent=2)


def tempFunction(_path):
    with open(_path) as data_file:
        data = json.load(data_file)
    for element in data:
        print element
        insertElasticsearch('mic_demo', 'chainspot', element)


def checkData(readfile):
    s = set()
    for r_time in readfile.keys():
        for element in readfile[r_time]:
            e = element['LogTime'].split(' ')[0]
            s.add(e)
    print s


if __name__ == "__main__":
    print '___( \start/ )___( \start/ )___( \start/ )___( \start/ )___'
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # insertElasticsearch('chu_chu_test','aaaa',m)
    # _path_source = 'dataset/mic.mv.txt'
    _path_source = 'dataset/mic.mv.6.19.txt'
    # _path_source_anomaly = 'dataset/inter.result.txt'
    # checkData(readfile)

    # for i in range(1,21):
    # 	replacestring = "2016-04-0"+str(i)
    # 	readfile = onlyReadFile(_path_source)
    # 	toElasticsearch(readfile,replacestring)
    # 	sys.exc_clear()


    for i in range(11,21):
    # for i in range(18,21):
    	replacestring = "2016-04-"+str(i)
      	readfile = onlyReadFile(_path_source)
    	print replacestring
    	toElasticsearch(readfile,replacestring)

    # for i in range(21,27):
    # 	replacestring = "2016-04-"+str(i)
    #  	readfile = onlyReadFile(_path_source)
    # 	print replacestring
    # 	datasetList,randomLogtime = onlyReadFile_Logtime(readfile,replacestring)
    # 	toElasticsearchRamdom(datasetList,replacestring,randomLogtime)


    # for i in range(27, 31):
    #     _path_source_anomaly = 'dataset/inter.result.txt'
    #     readfile_forURI = onlyReadFile(_path_source_anomaly)
    #     URI_List = onlyReadAnotherFile(readfile_forURI)
    #     replacestring = "2016-04-" + str(i)
    #     readfile = onlyReadFile(_path_source)
    #     print replacestring
    #     rawDatasetList, randomLogtime = onlyReadFile_Logtime(readfile, replacestring)
    #     # print len(rawDatasetList), len(URI_List), len(randomLogtime)
    #     mergeData(rawDatasetList, URI_List, randomLogtime)
    #     toElasticsearchRamdom(rawDatasetList, replacestring, randomLogtime)

    # _tempPath = 'dataset/temp.1.txt'
    # tempFunction(_tempPath)
    print '______finish______'



# 140.92.13.186

# 1QAZ2wsx3EDC
# 2017-6_web
## 2017-chain
# http://192.168.6.90:9200/_plugin/head
# http://140.92.13.186:9200/_plugin/head
