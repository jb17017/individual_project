import pandas as pd
import numpy as np
import random
import re

df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\dota_2_english_chat_messages.csv')
#df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\test.csv')

all_data = df.to_numpy()

#This all_data stores all messages in oone match before concatenation
temp_match_conv = []

player_num_temp = []
#This all_data stores all match conversations, with all messages concatenated into one element
match_conv = []
player_num = []

print("-----Loaded csv file-----")

#Initialise
j = all_data[0][0]

#Collects each match conversation and stores it as one string
#for i in range(0,limit):
for i in range(0,len(all_data)):
    if (all_data[i][0] == j):
        temp_match_conv.append(all_data[i][3])
        player_num_temp.append(all_data[i][2])
    #Add to a complete all_data, reset temp_match_conv and add current, reset j
    if (all_data[i][0] != j):
        match_conv.append(temp_match_conv)
        player_num.append(player_num_temp)
        temp_match_conv = []
        player_num_temp = []
        temp_match_conv.append(all_data[i][3])
        player_num_temp.append(all_data[i][2])
        j = all_data[i][0]

#print(temp_match_conv)
match_conv.append(temp_match_conv)
player_num.append(player_num_temp)

#print(match_conv[0][0])

count = 0

LIMIT = 500
#LIMIT = 1000
#LIMIT = 5

off_array_temp = []

off_array = []

#So there are no repeats
random_index_list = []

print("YOU MUST DECIDE WETHER THIS IS OFFENSIVE (TYPE 1) OR NOT OFFENSIVE (TYPE 0):\n")

match_index = random.randint(0,(len(match_conv)-1))
random_index_list.append(match_index)

while count < LIMIT:

    for text_index in range(0,len(match_conv[match_index])):
        off_array_temp.append(count+1)
        off_array_temp.append(player_num[match_index][text_index])
        off_array_temp.append(match_index);
        off_array_temp.append(match_conv[match_index][text_index])
        off_val = input("%s (1 or 0?): " %match_conv[match_index][text_index])
        print("\n")
        while (off_val == ""):
            off_val = input("%s (1 or 0?): " %match_conv[match_index][text_index])
            print("\n")
        off_string = ''
        while (off_val != "0" and off_val != "1"):
            off_val = input("%s (1 or 0?): " %match_conv[match_index][text_index])
            print("\n")
        off_val = int(off_val)
        if (off_val == 0):
            off_string = 'NOT'
        elif(off_val == 1):
            off_string = 'OFF'

        off_array_temp.append(off_string)
        off_array.append(off_array_temp)
        off_array_temp = []
    match_index = random.randint(0,(len(match_conv)-1))

    while(match_index in random_index_list):
        match_index = random.randint(0,(len(match_conv)-1))

    random_index_list.append(match_index)
    count = count + 1
    print(count)

#print(off_array)

back_to_np = np.array(off_array)

print("-----exporting to a csv file-----")
export = pd.DataFrame(data = back_to_np,columns=["lmatch","player num","gmatch","text","OFF"])
# #print(export)
#export.to_csv('test_outcome.csv',index = False)
export.to_csv('dota2_classified_dataset.csv',index = False)
