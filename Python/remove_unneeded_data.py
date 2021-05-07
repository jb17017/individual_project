import pandas as pd
import numpy as np

#df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\individual_project\Datasets\dota2_test_set.csv',names=['local match','player num','global match','in-game text message','label'])
df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\individual_project\Datasets\dota2_training_combined_messages_set.csv',names=['local match','player num','global match','in-game text message','label'])
#df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\individual_project\Datasets\dota2_training_set.csv',names=['local match','player num','global match','in-game text message','label'])
#df = pd.read_csv(r'C:\Users\bitst\Documents\Individual project\individual_project\Datasets\dota2_test_combined_messages_set.csv',names=['local match','player num','global match','in-game text message','label'])

df.drop('player num',axis=1,inplace=True)
df.drop('global match',axis=1,inplace=True)

array = df.to_numpy()

export = pd.DataFrame(data = array, columns=["local match","in-game text message","label"])

#export.to_csv(r'C:\Users\bitst\Documents\Individual project\individual_project\Datasets\dota2_test_set_removed.csv')
export.to_csv(r'C:\Users\bitst\Documents\Individual project\individual_project\Datasets\dota2_training_combined_set_removed.csv')
#export.to_csv(r'C:\Users\bitst\Documents\Individual project\individual_project\Datasets\dota2_training__set_removed.csv')
#export.to_csv(r'C:\Users\bitst\Documents\Individual project\individual_project\Datasets\dota2_test_combined_messages_set_removed.csv')
