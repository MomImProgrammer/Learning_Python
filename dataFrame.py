#pip install pandas and xlrd 
import pandas as pd
import os
import re

os.chdir('/Users/lena/Documents') #change working dir
xlsx = pd.ExcelFile('Example.xlsx') #create xlsx object
batchDataRaw = pd.read_excel(xlsx,'Content') #read data from Content sheet
batchDataNoEmpty = batchDataRaw.dropna(how='all') #remove empty rows
batchData = batchDataNoEmpty.drop(['dontNeed'], axis=1) #remove unnecessary columns

print(batchData)

dateTimePattern = re.compile(r'(\d\d\d\d-\d\d-\d\d) ((\d\d):(\d\d):(\d\d).(\d\d\d))')
for index, row in batchData.iterrows():
    mo = dateTimePattern.search(row['runDate'])
    row['runDate'] = mo.group(1)
    mo = dateTimePattern.search(row['captureDuration'])
    row['captureDuration'] = int(mo.group(3))*60+int(mo.group(4))+int(mo.group(5))/60

print(batchData)
