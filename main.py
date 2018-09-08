
import pandas as pd # Load the Pandas libraries with alias 'pd'
import numpy as np
import matplotlib.pyplot as plt
from Class_Data_Exploration import Data_Exploration
from Class_Data_Loader import data_matrix
from collections import Counter#used to count size of each classification for an attribute
import fancyimpute as fi
import sklearn


def main():
    matrix = Data_Exploration(pd.read_csv("Data_In/test.csv"), pd.read_csv("Data_In/train.csv"))#load in the data, the other variables within the object will then be initialised later on using other functions
    matrix.dim_data()#method that updates the dimension of the train and test data which is the 4th and 5th variable in object matrix
    matrix.first_column_drop()#drops the first column of both test_X and train_X
    matrix.dim_data()#called again so that the dimension can be updated so the function that initialised train.Y with the correct values works properly
    matrix.move_classification_to_train_y()#moves the final column of train_X to train_Y


    matrix.dim_data()  # called again to verify everything worked correctly with the following print statement
    matrix.sale_price_against_attribute_scatter_plot('1stFlrSF')#creates the plot of sale price against house

    matrix.dim_data()
    matrix.split_attributes()#splits the attributes into a string dataset and a float + int dataset so that one hot encoding can be used
    matrix.one_hot_encoding()#method to convert all the string attributes into one hot encoded
    matrix._train_X_string.to_csv('Data_Out/_train_X_string.csv', index=False)
    matrix._test_X_string.to_csv('Data_Out/_test_X_string.csv', index=False)

    #print(matrix._train_X_string.head())#print one_hot encoded to ensure it actually works

    matrix.normalise_data()#normalises train_X_int_float, test_X_int_float, train_Y
    matrix.fill_missing_values()#fills in the missing values of train_X_int_float
    matrix.normalise_data()  # normalises train_X_int_float, test_X_int_float, train_Y

    matrix.combine_string_int_float()#combines the two objexts for both test_X and train_X
    matrix.export_CSV()#exports the train_X, train_Y and test_X to a csv file


    ################################################################################################################################################################
    # simple linear model


    regr = sklearn.linear_model.LinearRegression()# Create linear regression object
    regr.fit(matrix._train_X, matrix._train_Y)# Train the model using the training sets
    Pred_Y_list = regr.predict(matrix._test_X)# Make predictions using the testing set
    Pred_Y = pd.DataFrame(data=Pred_Y_list, columns={'SalePrice'})#

    a = pd.concat([matrix._id, Pred_Y], axis=1)
    a.to_csv('Data_Out/predict_Y_up.csv', index=False)

    # The coefficients
    # print('Coefficients: \n', regr.coef_)


if __name__ == "__main__":
    main()
