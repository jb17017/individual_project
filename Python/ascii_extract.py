import pandas as pd
import numpy as np

#####################
# WILL NOT RUN JUST PROOF I USED THE PROGRAM
# WILL NOT RUN BECAUSE OF SPECIFIC NAMES FOR READING IN DATA SETS
# WERE SPECIFIC TO MY MACHINE
#####################

df = pd.read_csv('dota2_chat_messages.csv')

count = 0

array = df.to_numpy()

second_array = []

print("-----Loaded csv file-----")

print("----- checking the text now, this may take some time... -----")

#Simple ASCII check
for i in range(0,len(array)):
    #Checks if it is ascii values, got rid of 600,000 foreign language records
    if (type(array[i][3]) == str):
        if (array[i][3].isascii()):
            second_array.append(array[i])
    count = count + 1
    if(count%100 == 0):
        print(count)


back_to_np = np.array(second_array)

print("-----exporting to a csv file-----")

export = pd.DataFrame(data = back_to_np, columns=["match","time","player_num","text"])

export.to_csv('dota2_ascii_only.csv',index = False)
