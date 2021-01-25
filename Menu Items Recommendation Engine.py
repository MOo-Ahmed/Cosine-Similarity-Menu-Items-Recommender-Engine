import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer



# loading the data
df = pd.read_csv('menu_items.csv')

# Count the number of items
#df.shape

# Create list of important columns for the recommender
#columns = ['price', 'section', 'description', 'item']
columns = ['price', 'section', 'description']


# Check for any missing values
#df[columns].isnull().values.any()

#Create a function to combine the values of the important columns into a single string
def get_important_features(data):
    important_features = []
    for i in range (0,data.shape[0]):
        important_features.append(str(data['price'][i]) + ' ' + str(data['section'][i]) + ' ' + str(data['description'][i]))
    return important_features 

# Create column to hold the combined strings
df['important_features'] = get_important_features(df)


# Convert the text to matrix of token counts
cm = CountVectorizer().fit_transform(df['important_features'])


#Get the cosine similarity matrix from the count matrix
cs = cosine_similarity(cm)
#print(cs)


#Get the shape of the cosine similarity matrix
cs.shape

#Get the title of the item that the user likes
title = 'thai tea'

#Find the item id of the most matching item to compare the rest with
item_id = df[df.item == title]['item_id'].values[0]

#Create a list of enumerations for the similarity score [(item_id, similarity score) , (..) , (...)]
scores = list(enumerate(cs[item_id]))

#sort the list -- reverse detertmines if sorted descendingly or not
sorted_scores = sorted(scores, key = lambda x : x[1], reverse = True)

#Don't take the first element because it's the same
sorted_scores = sorted_scores[1:]

#print the sotred scores
#print(sorted_scores)

#Create a loop to print the first 7 similar items
j = 0
print('The 7 most recommended menu items to ', title , ' are \n' )
for item in sorted_scores :
    item_title = df[df.item_id == item[0]]['item'].values[0]
    print(j+1, item_title)
    j = j + 1
    if j > 6 :
        break
