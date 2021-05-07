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
df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\dota2_classified_dataset.csv')
#df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\test_classify.csv')
count = 0
#Drops the slot column
#df.drop('slot',axis=1,inplace=True)
array = df.to_numpy()
#limit = len(array)
second_array = []
#translator = Translator()
#print(second_array)
#print(array[5][3])
print("-----Loaded csv file-----")

#This array stores all messages in oone match before concatenation
temp_match_conv = []

#This array stores all match conversations, with all messages concatenated into one element
match_conv = []

#Initialise
j = array[0][0]

#Collects each match conversation and stores it as one string
#for i in range(0,limit):
for i in range(0,len(array)):
    if (array[i][0] == j):
        temp_match_conv.append(array[i][3])
    #Add to a complete array, reset temp_match_conv and add current, reset j
    if (array[i][0] != j):
        match_conv.append((". ".join(temp_match_conv) + ". "))
        temp_match_conv = []
        temp_match_conv.append(array[i][3])
        j = array[i][0]

#print(temp_match_conv)
match_conv.append((". ".join(temp_match_conv) + "."))

#This array stores a binary value for each match, 0 indicating that the conversation is not in english, and 1 for english
english_classifier = np.zeros(len(match_conv))

print("----- checking the text now, this may take some time... -----")

for k in range(0,len(match_conv)):
    if (len(match_conv[k]) > 2):
        lang = TextBlob(match_conv[k])
        #Sends a http request to google: 600 per minute LIMIT
        if (lang.detect_language() == "en"):
                #if (detect(match_conv[k]) == "en"):
            #All messages from this match should be added to an match_conv
                english_classifier[k] = 1

    #If 2 or less characters then apply ascii check
    elif (type(match_conv[k]) == str):
         if (match_conv[k].isascii()):
             english_classifier[k] = 1
    count = count + 1
    if(count%100 == 0):
        print(count)
    #Must sleep so request limit is not reached, so you do not get IP banned by google -- 0.15 = 400 per minute
    time.sleep(0.4)

final_list = []

m = 0
#print(len(english_classifier))
for l in range(0,len(array)):
    if(array[l][0] != m and m < (len(english_classifier)-1)):
    #if((array[l][0] != m) and (m < limit)):
        m = m + 1
    if(english_classifier[m] == 1 and m < len(english_classifier)):
    #if((english_classifier[m] == 1) and (m < limit)):
        #print(array[l])
        final_list.append(array[l])

back_to_np = np.array(final_list)

print("-----exporting to a csv file-----")
export = pd.DataFrame(data = back_to_np,columns=["lmatch","player num","gmatch","text","OFF"])
#print(export)
export.to_csv('dota2_english_classified.csv',index = False)
#export.to_csv('test_complete_class.csv',index = False)
#print(back_to_np)
#print(array)
#print(second_array)
