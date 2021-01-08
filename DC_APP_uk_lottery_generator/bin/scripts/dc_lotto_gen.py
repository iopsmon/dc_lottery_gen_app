#***********************************************
#DESCRIPTION:Generates random numbers for lottery
#FILENAME:dc_lotto_gen.py
#USAGE:python <script name>
#DATE: 06/01/2021
#VERSION:0.7
#OWNER:Deepak Chohan
#*********************************************** 

#import modules  
import datetime # date 
import random  #random number generator
import os, sys


#Lottery generating function
def lottery_gen ():

#File variables
    my_text_file = ("/opt/splunk/etc/apps/DC_APP_uk_lottery_generator/bin/scripts/lottery_gen.txt")
    my_log_file = ("/opt/splunk/etc/apps/DC_APP_uk_lottery_generator/bin/scripts/lottery_gen.log")
    add_log_file = open(my_text_file, "w")

#Date Time 
    #Date variable  
    ct = datetime.datetime.now() 

#Create log file 
    #f = open("lottery_gen.txt", "w")
       
#lotto range - print results 6 numbers 
    #lotto = [random.randrange(1, 59, 1) for i in range(6)]
    lotto = random.sample(range (1, 59, 1),6)
    #print ("************************************************************")
    #print (ct,"Lotto Numbers= " + str(lotto))
    #print ("************************************************************")
    #Write data with date and results
    add_log_file.write(str(ct) + " lotto_numbers=" + str(lotto) + '\n')

#euro millions range  5 numbers and 2 lucky stars
    eurom = random.sample(range (1, 50, 1),5)
    luckys = random.sample(range (1, 12, 1),2) 
    #print (ct,"Euro Millions Numbers & Lucky Stars= " + str(eurom) + str (luckys))
    #print ("************************************************************")
    #Write data with date and results
    add_log_file.write(str(ct) + " euro_millions=" + str(eurom) + str (luckys) + '\n')

#set for life range 5 numbers and 1 life ball 
    setfl = random.sample(range (1, 47, 1),5) 
    lb = random.sample(range (1, 10, 1),1) 
    #print (ct,"Set For Life - Life Ball= " + str(setfl) + str (lb))
    #print ("************************************************************")
    #Write data with date and results
    add_log_file.write(str(ct) + " set_for_life=" + str(setfl) + str (lb) +'\n')

#Thunderball range 5 numbers and 1 thunderball  
    tbnumbers = random.sample(range (1, 39, 1),5)  
    tb = random.sample (range(1, 14, 1), 1) 
    #print (ct,"Thunderball= " + str(tbnumbers) + str (tb))
    #print ("************************************************************")
     #Write data with date and results
    add_log_file.write(str(ct) + " thunderball=" + str(tbnumbers) + str(tb) + '\n')
    add_log_file.close()

    #read file - just for testing 
    #f = open("lottery_gen.log", "r")
    #print(f.read()) 
    #f.close()


    #This renames the file 
    os.rename(my_text_file, my_log_file)

#This calls the main fucnction

lottery_gen()

#End of code
