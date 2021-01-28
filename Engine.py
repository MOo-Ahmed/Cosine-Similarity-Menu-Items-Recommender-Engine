import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class RecommendationEngine :
    dataset_filename = 'Datasets/menu_items.csv'
    recommendation_name = 'menu item'
    
    def __init__(self, item_name, n, recommendation_name):
        self.item_name = item_name
        self.n = n
        self.recommendation_name = recommendation_name

    def set_Dataset_Filename(self, file):
        self.dataset_filename = file

    def get_Important_Columns(self, recommendation_name):
        if recommendation_name == 'menu item' :
            return [ 'name', 'section']
    
    #Create a function to combine the values of the important columns into a single string
    def getConcatenatedString(self, data, i):
        columns = self.get_Important_Columns(self.recommendation_name)
        output = ''
        for j in range (0,len(columns)):
            output = output + str(data[columns[j]][i]) + ' '
        return output 
 
    #Create a function to combine the values of the important columns into a single string
    def get_important_features(self, data):
        important_features = []
        for i in range (0,data.shape[0]):
            important_features.append(self.getConcatenatedString(data, i))
        return important_features 
        
    def run (self):
        
        # loading the data
        df = pd.read_csv(self.dataset_filename)

        # Count the number of items
        #df.shape

        # Create list of important columns for the recommender
        columns = self.get_Important_Columns(self.recommendation_name) 

        # Check for any missing values
        #df[columns].isnull().values.any()

        # Create column to hold the combined strings
        df['important_features'] = self.get_important_features(df)

        # Convert the text to matrix of token counts
        cm = CountVectorizer().fit_transform(df['important_features'])
        
        #Get the cosine similarity matrix from the count matrix
        cs = cosine_similarity(cm)
        #print(cs)

        #Get the shape of the cosine similarity matrix
        cs.shape

        #Find the item id of the most matching item to compare the rest with
        item_id = df[df.name == self.item_name]['id'].values[0]

        #Create a list of enumerations for the similarity score [(item_id, similarity score) , (..) , (...)]
        scores = list(enumerate(cs[item_id]))

        #sort the list -- reverse detertmines if sorted descendingly or not
        sorted_scores = sorted(scores, key = lambda x : x[1], reverse = True)

        #Don't take the first element because it's the same
        sorted_scores = sorted_scores[2:]

        #print the sotred scores
        #print(sorted_scores)

        #Create a loop to print the first n similar items
        j = 0
        print('The ' , self.n , '  most recommended items to ', self.item_name , ' are \n' )
        for item in sorted_scores :
            item_title = df[df.id == item[0]]['name'].values[0]
            item_id = df[df.id == item[0]]['id'].values[0]
            print(j+1, '-\t', item_id , '\t' , item_title)
            j = j + 1
            if j > (self.n - 1) :
                break
