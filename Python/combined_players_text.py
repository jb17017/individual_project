import pandas as pd
import numpy as np
import time
import re

#---------TO DO-----------
#REDUCE AMOUNT OF DATA THAT COMES INTO DF - chunk data
#REDUCE HTTP REQUESTS - add a delay - 600 requests per minute limit

df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\dota2_training_set.csv')
#df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\test_classify.csv')

array = df.to_numpy()

temp_player_text = []

player_text = []

temp_condensed = []

condensed = []

temp_label = []

new_label = []

#Initialise
j = array[0][1]
#Collects each match conversation and stores it as one string
#for i in range(0,limit):
for i in range(0,len(array)):
    if (array[i][1] == j):

        if (i == 0):
            temp_condensed = [array[i][0],array[i][1],array[i][2]]
        temp_player_text.append(array[i][3])
        temp_label.append(array[i][4])
    #Add to a complete array, reset temp_match_conv and add current, reset j
    if (array[i][1] != j):

        condensed.append(temp_condensed)
        player_text.append((" ".join(temp_player_text)))

        if (len(temp_label) == 1):
            new_label.append(temp_label[0])
        else:
            found_off = False
            # if any(l == "OFF" for l in temp_label):
            #     new_label.append("OFF")
            for k in range(0,len(temp_label)):
                print(temp_label[k])
                label_check = bool(re.search('OFF', temp_label[k]))
                if (label_check == True):
                    break
            if (label_check == True):
                new_label.append("OFF")
            else:
                off_val = input("%s (1 or 0?): " %(" ".join(temp_player_text)))
                while (off_val != "0" and off_val != "1"):
                    off_val = input("%s (1 or 0?): " %(" ".join(temp_player_text)))
                off_val = int(off_val)
                if (off_val == 0):
                    new_label.append("NOT")
                elif(off_val == 1):
                    new_label.append("OFF")

        temp_player_text = []
        temp_label = []
        temp_condensed = [array[i][0],array[i][1],array[i][2]]
        #temp_condensed.append(temp_stor)
        temp_player_text.append(array[i][3])
        temp_label.append(array[i][4])
        j = array[i][1]

#print(temp_match_conv)
condensed.append(temp_condensed)
player_text.append((" ".join(temp_player_text)))

if (len(temp_label) == 1):
    new_label.append(temp_label[0])
else:
    found_off = False
    # if any(l == "OFF" for l in temp_label):
    #     new_label.append("OFF")
    for k in range(0,len(temp_label)):
        print(temp_label[k])
        label_check = bool(re.search('OFF', temp_label[k]))
        if (label_check == True):
            break
    if (label_check == True):
        new_label.append("OFF")
    else:
        off_val = input("%s (1 or 0?): " %(" ".join(temp_player_text)))
        while (off_val != "0" and off_val != "1"):
            off_val = input("%s (1 or 0?): " %(" ".join(temp_player_text)))
        off_val = int(off_val)
        if (off_val == 0):
            new_label.append("NOT")
        elif(off_val == 1):
            new_label.append("OFF")

#print(condensed)
#print(player_text)
#print(new_label)

print(len(condensed))
print(len(player_text))
print(len(new_label))


final_array = []
for m in range(0,len(player_text)):
    final_array.append([condensed[m][0],condensed[m][1],condensed[m][2],player_text[m],new_label[m]])

back_to_np = np.array(final_array)

print("-----exporting to a csv file-----")
export = pd.DataFrame(data = back_to_np,columns=["lmatch","player_num","gmatch","text","OFF"])
#print(export)
export.to_csv('dota2_training_combined_messages_set.csv',index = False)
#export.to_csv('test_combined.csv',index = False)
