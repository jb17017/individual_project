import pandas as pd
import numpy as np

#####################
# WILL NOT RUN JUST PROOF I USED THE PROGRAM
# WILL NOT RUN BECAUSE OF SPECIFIC NAMES FOR READING IN DATA SETS
# WERE SPECIFIC TO MY MACHINE
#####################

print("-----Loading from csv files-----")

df = pd.read_csv('dota2_training_set.csv',header=None, names=['lmatch', 'player_num','gmatch','text','OFF'])
df2 = pd.read_csv('dota2_test_set.csv',header=None, names=['lmatch', 'player_num','gmatch','text','OFF'])


first_dataset_gmatch = df.gmatch.values
second_dataset_gmatch = df2.gmatch.values
first_dataset = df.to_numpy()
second_dataset = df2.to_numpy()

combined_dataset = []

# Add first data set
for i in range(0,len(first_dataset)):
    combined_dataset.append(first_dataset[i])

# Search second, check no clashes if not add entry
for j in range(0,len(second_dataset)):

        if (second_dataset[j][2] not in first_dataset_gmatch):

            combined_dataset.append(second_dataset[j])
        else:
            print("CLASH! Match:")
            print(second_dataset[j][2])

back_to_np = np.array(combined_dataset)

print("-----exporting to a csv file-----")

export = pd.DataFrame(data = back_to_np,columns=["lmatch","player_num","gmatch","text","OFF"])

export.to_csv('dota2_can_be_deleted.csv')
