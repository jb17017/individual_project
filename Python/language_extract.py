from langdetect import detect
from textblob import TextBlob
from googletrans import Translator
import pandas as pd
import numpy as np
import time

#---------TO DO-----------
#REDUCE AMOUNT OF DATA THAT COMES INTO DF - chunk data
#REDUCE HTTP REQUESTS - add a delay - 600 requests per minute limit

string_check = False
english_check = True
limit = 100000
#df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\dota_2_ascii_only.csv')
df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\test.csv')
count = 0
#Drops the slot column
df.drop('slot',axis=1,inplace=True)
array = df.to_numpy()
#limit = len(array)
second_array = []
#translator = Translator()
#print(second_array)
#print(array[5][3])
print("-----Loaded csv file-----")

print("----- checking the text now, this may take some time... -----")
for i in range(0,len(array)):
    #Uses google services to detect a language
    if (english_check == True):
        if (len(array[i][2]) > 2):
            lang = TextBlob(array[i][2])
            #Sends a http request to google: 600 per minute LIMIT
            if (lang.detect_language() == "en"):
                second_array.append(array[i])
            #Must sleep so request limit is not reached, so you do not get IP banned by google -- 0.15 = 400 per minute
            time.sleep(0.15)
        #If 2 or less characters then apply ascii check
        elif (type(array[i][2]) == str):
            if (array[i][2].isascii()):
                second_array.append(array[i])
    #Checks if it is ascii values, got rid of 600,000 foreign language records
    elif (string_check == True):
        if (type(array[i][2]) == str):
            if (array[i][2].isascii()):
                second_array.append(array[i])
    count = count + 1
    if(count%100 == 0):
        print(count)
back_to_np = np.array(second_array)
print(second_array)
print("-----exporting to a csv file-----")
export = pd.DataFrame(data = back_to_np,columns=["match","time","text"])
print(export)
#export.to_csv('dota2_english_chat_messages.csv',index = False)
export.to_csv('test_complete.csv',index = False)
#print(back_to_np)
#print(array)
#print(second_array)
