#***********************************************
#DESCRIPTION:Downloads Lotto Results CSV file - Splunk will then ingest the data
#FILENAME:dc_get_lotto_csv.py
#USAGE:python3 <script name>
#DATE: 08/01/2021
#VERSION:0.1
#OWNER:Deepak Chohan
#*********************************************** 

#import modules  
import os, sys
import urllib.request
from pathlib import Path
import shutil 


#Lottery generating function
def get_lotto_results_csv ():

    #Paths for copying csv files to lookups folder
    src_path = '/opt/splunk/etc/apps/DC_APP_uk_lottery_generator/bin/scripts/'
    trg_path = '/opt/splunk/etc/apps/DC_APP_uk_lottery_generator/lookups/'


    # URL and call to download csv file
    url = 'https://www.national-lottery.co.uk/results/lotto/draw-history/csv'
    csv = urllib.request.urlopen(url).read() # returns type 'bytes' 
    with open('lotto-draw-history.csv', 'wb') as fx: # bytes, hence mode 'wb' 
        fx.write(csv)
        print ("Csv file downloaded")
         


#This is to move csv files to lookup folder 
    for src_file in Path(src_path).glob('*.csv'):
        shutil.copy(src_file, trg_path)
        print ("Csv files moved")


#This calls main code
get_lotto_results_csv()

#End of code
