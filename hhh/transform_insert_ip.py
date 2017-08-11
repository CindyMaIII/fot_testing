import sys
import csv
import json
import random
import pandas as pd
import numpy as np

filetxt = "dataset/mic.mv.6.19_v1.txt"
filecvs = 'dataset/ip.txt'

with open(filetxt) as data_file:
    datatxt = json.load(data_file)

# @chu
ip = []
geo = []

f = open(filecvs, 'r')
for i in open(filecvs):
    data = f.readline()
    ip.append(data.split('@')[0])
    geo.append(data.split('@')[1])


for i in datatxt.keys():
    for k in range(len(datatxt[i])):
        e = random.SystemRandom().choice(range(len(ip)))
        datatxt[i][k]['SrcIP'] = ip[e]
        datatxt[i][k]['geoip'] = json.loads(geo[e])


with open('mic.mv.6.19.txt', 'w') as outfile:
    json.dump(datatxt, outfile)