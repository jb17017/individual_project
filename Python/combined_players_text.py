import pandas as pd
import numpy as np
import re

#####################
# WILL NOT RUN JUST PROOF I USED THE PROGRAM
# WILL NOT RUN BECAUSE OF SPECIFIC NAMES FOR READING IN DATA SETS
# WERE SPECIFIC TO MY MACHINE
#####################

df = pd.read_csv('dota2_training_set.csv')

array = df.to_numpy()

temp_player_text = []

player_text = []

temp_condensed = []

condensed = []

temp_label = []

new_label = []

#Initialise
j = array[0][1]
m = array[0][0]

#Loops through each message
for i in range(0,len(array)):
    # If player number and match index the same
    if (array[i][1] == j and array[i][0] == m):

        #For first value
        if (i == 0):
            temp_condensed = [array[i][0],array[i][1],array[i][2]]
        #Add to temporary message list
        temp_player_text.append(array[i][3])
        temp_label.append(array[i][4])

    # If there is a change in player num or match index from previous save
    if (array[i][1] != j or array[i][0] != m):

        #Combine player messages
        condensed.append(temp_condensed)
        player_text.append((" ".join(temp_player_text)))

        # If only 1 label and sentence give this label
        if (len(temp_label) == 1):
            new_label.append(temp_label[0])
        else:
            # Loop through all temp labels looking for OFF label, if one then output new label as OFF
            for k in range(0,len(temp_label)):
                print(temp_label[k])
                label_check = bool(re.search('OFF', temp_label[k]))
                if (label_check == True):
                    break
            if (label_check == True):
                new_label.append("OFF")
            # Otherwise all NOT and therefore re-annotate to decide label, if anything is changed
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
        m = array[i][0]

#print(temp_match_conv)
condensed.append(temp_condensed)
player_text.append((" ".join(temp_player_text)))

# Does it for last entry in data set
if (len(temp_label) == 1):
    new_label.append(temp_label[0])
else:

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


final_array = []

# Combine all info back together
for m in range(0,len(player_text)):
    final_array.append([condensed[m][0],condensed[m][1],condensed[m][2],player_text[m],new_label[m]])

back_to_np = np.array(final_array)

print("-----exporting to a csv file-----")
export = pd.DataFrame(data = back_to_np,columns=["lmatch","player_num","gmatch","text","OFF"])

export.to_csv('dota2_training_combined_messages_set.csv',index = False)
