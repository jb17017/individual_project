from langdetect import detect
import pandas as pd
import numpy as np
import re

#####################
# WILL NOT RUN JUST PROOF I USED THE PROGRAM
# WILL NOT RUN BECAUSE OF SPECIFIC NAMES FOR READING IN DATA SETS
# WERE SPECIFIC TO MY MACHINE
#####################

df = pd.read_csv('dota2_ascii_only.csv')

count = 0

array = df.to_numpy()

#This array stores all messages in oone match before concatenation
temp_match_conv = []

#This array stores all match conversations, with all messages concatenated into one element
match_conv = []

print("-----Loaded csv file-----")

#Initialise
j = array[0][0]

#Collects each match conversation and stores it as one string
for i in range(0,len(array)):
    if (array[i][0] == j):
        temp_match_conv.append(array[i][3])
    #Add to a complete array, reset temp_match_conv and add current, reset j
    if (array[i][0] != j):
        match_conv.append((". ".join(temp_match_conv) + ". "))
        temp_match_conv = []
        temp_match_conv.append(array[i][3])
        j = array[i][0]

match_conv.append((". ".join(temp_match_conv) + "."))

#This array stores a binary value for each match, 0 indicating that the conversation is not in english, and 1 for english
english_classifier = np.zeros(len(match_conv))

print("----- checking the text now, this may take some time... -----")


for k in range(0,len(match_conv)):

    letter_check = " ".join(re.findall("[a-zA-Z]+",match_conv[k]))

    if (len(letter_check) > 10):
        #Ignore URLs often links to a social media account that means people can be identified, and we do not want that
        url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.search(url_regex,match_conv[k])
        if (url == None):
            # Langdetect does not work with @ symbols
            res = bool(re.search(r"@", match_conv[k]))
            if (res == False):
                #use langdetect
                if (detect(match_conv[k]) == "en"):
                    #All messages from this match should be added to an match_conv
                    english_classifier[k] = 1

    count = count + 1
    if(count%100 == 0):
        print(count)

final_list = []

m = 0

# Combine all messages that got a 1 for their match being passed by langdetect
for l in range(0,len(array)):
    if(array[l][0] != m and m < (len(english_classifier)-1)):

        m = m + 1
    if(english_classifier[m] == 1 and m < len(english_classifier)):

        final_list.append(array[l])

back_to_np = np.array(final_list)

print(back_to_np)

print("-----exporting to a csv file-----")

export = pd.DataFrame(data = back_to_np,columns=["match","time","player_num","text"])

export.to_csv('dota2_english_chat_messages.csv',index = False)
