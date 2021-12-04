import csv
import os
import pandas as pd
allspis=[]
f = open('yiddishallwords.csv')
tab = csv.reader(f)
def allfinder(filename,myword,res):
    f1 = open(filename, 'r', encoding='utf8')
    wordlist=[]
    a = f1.read()
    a = a.split('\n')
    for smth in a:
        smth = smth.split('\t')
        if len(smth) > 6:
            word = smth[12].strip
        if word not in wordlist:
            wordlist.append(word)
    for word in wordlist:
        if word == myword + 'in':
            res['n'] += 1
        elif word == myword + 'ke':
            res['ke'] += 1
        elif word == myword + 'te':
            res['te'] += 1
        elif word == myword + 'inte':
            res['inte'] += 1
        elif word == myword + 'nice':
            res['nice'] += 1
        elif word == myword + 'ice':
            res['ice'] += 1
        elif word == myword + 'ine':
            res['ine'] += 1
        elif word == myword + 'ene':
            res['ene'] += 1
        elif word == myword + 'cn':
            res['cn'] += 1
        elif word == myword + 'she':
            res['she'] += 1
        elif word == myword + 'ixe':
            res['ixe'] += 1
        elif word == myword + 'es' or word == myword + 'is':
            res['esis'] += 1
        elif word == myword + 'ese':
            res['ese'] += 1
from os import listdir
for smth in tab:
    yidword = smth[1].split()[0].strip()
    translation = smth[0]
    resslov = {'word': yidword, 'meaning': translation, 'n': 0, 'ke': 0, 'te': 0, 'inte': 0, 'nice': 0, 'ice': 0, 'ine': 0,
           'ene': 0, 'cn': 0, 'she': 0, 'ixe': 0, 'esis': 0, 'ese': 0}
    allbooks = listdir(r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2016')
    for name in allbooks:
        filename=r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2016\\'+name
        allfinder(filename,yidword,resslov)
    allbooks = listdir(r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2015')
    for name in allbooks:
        filename=r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2015\\'+name
        allfinder(filename,yidword,resslov)
    allbooks = listdir(r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2014')
    for name in allbooks:
        filename=r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2014\\'+name
        allfinder(filename,yidword,resslov)
    allbooks = listdir(r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2013')
    for name in allbooks:
        filename=r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2013\\'+name
        allfinder(filename,yidword,resslov)
    allbooks = listdir(r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2012\texts')
    for name in allbooks:
        filename=r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2012\texts\\'+name
        allfinder(filename,yidword,resslov)
    allbooks = listdir(r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2012\tanakh')
    for name in allbooks:
        filename=r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2012\tanakh\\' + name
        allfinder(filename,yidword,resslov)
    allbooks = listdir(r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2012\shevazucker')
    for name in allbooks:
        filename = r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2012\shevazucker\\' + name
        allfinder(filename, yidword, resslov)
    allbooks = listdir(r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2012\bavebter')
    for name in allbooks:
        filename = r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\fiction\2012\bavebter\\' + name
        allfinder(filename, yidword, resslov)
    allbooks = listdir(r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\press\forverts')
    for name in allbooks:
        filename = r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\press\forverts\\' + name
        allfinder(filename, yidword, resslov)
    allbooks = listdir(r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\press\lebnsfragn')
    for name in allbooks:
        filename = r'C:\Users\User\PycharmProjects\pythonProjectformycourse\parsed_data\press\lebnsfragn\\' + name
        allfinder(filename, yidword, resslov)
    allspis.append(resslov)
df = pd.DataFrame(allspis)
df.to_csv("feminitivesfinprob.csv", index=False)
