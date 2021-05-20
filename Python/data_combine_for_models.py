import pandas as pd
import numpy as np

#####################
# WILL NOT RUN JUST PROOF I USED THE PROGRAM
# WILL NOT RUN BECAUSE OF SPECIFIC NAMES FOR READING IN DATA SETS
# WERE SPECIFIC TO MY MACHINE
#####################

print("-----Loading from csv files-----")
df = pd.read_csv('dota2_training_set.csv',names=['index','local match','message','label'])
df2 = pd.read_csv('dota2_training_combined_messages_set.csv',names=['index','local match','message','label'])
df3 = pd.read_csv('olid-training-v1.0.tsv',delimiter='\t',header=None,names=['index','tweet','subtask-a','subtask-b','subtask-c'])

#Drop columns so all are the same number of columns
df.drop('index',axis=1,inplace=True)
df.drop('local match',axis=1,inplace=True)
df2.drop('index',axis=1,inplace=True)
df2.drop('local match',axis=1,inplace=True)
df3.drop('index',axis=1,inplace=True)
df3.drop('subtask-b',axis=1,inplace=True)
df3.drop('subtask-c',axis=1,inplace=True)


dota_message = df.message.values
dota_play_comb_message = df2.message.values
array_dota_train = df.to_numpy()
array_dota_player_train = df2.to_numpy()
array_olid_train = df3.to_numpy()

array_dota_combined = []
array_dota_olid_combined = []

# Append array with OLID
for k in range(0,len(array_olid_train)):
    array_dota_olid_combined.append(array_olid_train[k])

# Add dota to the OLID array
for i in range(0,len(array_dota_train)):
    array_dota_combined.append(array_dota_train[i])
    array_dota_olid_combined.append(array_dota_train[i])

# Add combined messages to Dota 2 data set
for j in range(0,len(array_dota_player_train)):

        if (array_dota_player_train[j][0] not in dota_message):

            array_dota_combined.append(array_dota_player_train[j])


np_array_dota_olid = np.array(array_dota_olid_combined)
np_array_dota_combined = np.array(array_dota_combined)

print("-----exporting to a csv file-----")
export1 = pd.DataFrame(data = np_array_dota_olid)

export1.to_csv('dota2_olid_combined_training_set.csv',index = True)

export2 = pd.DataFrame(data = np_array_dota_combined)

export2.to_csv('dota2_combined_player_and_none_combined_training_set.csv',index = True)
