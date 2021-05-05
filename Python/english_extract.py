    from langdetect import detect
from textblob import TextBlob
import pandas as pd
import numpy as np
import time
import re

#---------TO DO-----------
#REDUCE AMOUNT OF DATA THAT COMES INTO DF - chunk data
#REDUCE HTTP REQUESTS - add a delay - 600 requests per minute limit

# m = re.search('[a-zA-Z]', "hello what have we here. a man with 0 ult percentage")
# print(m)
# word = []
# temp_word = ["hello","world"]
# word.append((". ".join(temp_word) + "."))
# print(word)
# res = bool(re.search(r"@", "PRHOOCKPUDGE."))
# print(res)
df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\dota_2_ascii_only.csv')
#df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\test.csv')
count = 0

limit = 1000

#Drops the slot column
#df.drop('slot',axis=1,inplace=True)

array = df.to_numpy()

#This array stores all messages in oone match before concatenation
temp_match_conv = []

#This array stores all match conversations, with all messages concatenated into one element
match_conv = []

print("-----Loaded csv file-----")

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

#print(len(match_conv))

#This array stores a binary value for each match, 0 indicating that the conversation is not in english, and 1 for english
english_classifier = np.zeros(len(match_conv))
#english_classifier = np.zeros(limit)

#print(len(english_classifier))

print("----- checking the text now, this may take some time... -----")

#for k in range(0,limit):
for k in range(0,len(match_conv)):
    #print(match_conv[k])
    letter_check = " ".join(re.findall("[a-zA-Z]+",match_conv[k]))
    #if (len(match_conv[k]) > 10):
    if (len(letter_check) > 10):
        #Ignore URLs often links to a social media account that means people can be identified, and we do not want that
        url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.search(url_regex,match_conv[k])
        if (url == None):
        #letter_check = re.search('[a-zA-Z]', match_conv[k])
        #if (letter_check != None):
            res = bool(re.search(r"@", match_conv[k]))
            if (res == False):
                #print(match_conv[k])
        #lang = TextBlob(match_conv[k])
        #Sends a http request to google: 600 per minute LIMIT
        #if (lang.detect_language() == "en"):
                if (detect(match_conv[k]) == "en"):
            #All messages from this match should be added to an match_conv
                    english_classifier[k] = 1

    #If 2 or less characters then apply ascii check
    # elif (type(match_conv[k]) == str):
    #     if (match_conv[k].isascii()):
    #         english_classifier[k] = 1
    count = count + 1
    if(count%100 == 0):
        print(count)
    #Must sleep so request limit is not reached, so you do not get IP banned by google -- 0.15 = 400 per minute
    #time.sleep(0.3)

#print(english_classifier)

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

# l = 0
# for m in range(0,len(match_conv)):
#     if(english_classifier[m] == 1):


#print(final_list)

back_to_np = np.array(final_list)

print("-----exporting to a csv file-----")
export = pd.DataFrame(data = back_to_np,columns=["match","time","player_num","text"])
#print(export)
export.to_csv('dota_2_english_chat_messages.csv',index = False)
#export.to_csv('test_complete.csv',index = False)
