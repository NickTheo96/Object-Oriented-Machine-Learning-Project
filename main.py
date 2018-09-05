import pandas as pd # Load the Pandas libraries with alias 'pd'
import numpy as np
import matplotlib.pyplot as plt
from Class_Data_Exploration import Data_Exploration
from Class_Data_Loader import data_matrix
from collections import Counter#used to count size of each classification for an attribute


def main():
    matrix = Data_Exploration()#create the object matrix that has variables test and train matrix
    matrix.sale_price_against_attribute_scatter_plot('1stFlrSF')#create a scatterplot of sale price against first floor square foot
    #matrix.sale_price_against_attribute_scatter_plot('2ndFlrSF')
    #matrix.sale_price_against_attribute_scatter_plot('BsmtFinSF1')
    #matrix.sale_price_against_attribute_scatter_plot('BsmtFinSF2')
    #matrix.sale_price_against_attribute_scatter_plot('TotalBsmtSF')
    #matrix.sale_price_against_attribute_scatter_plot('MSSubClass')

    print(Counter(matrix._train["ExterQual"]))#prints the number of each classification for ExterQual

    # print(train.head())#prints the first 5 columns of train
    # np.savetxt('Test/First_Floor_Sq_Foot.out', train['1stFlrSF'].values, delimiter=',')  # creates a file so that the data is easier to look at
    #np.savetxt('Test/ExterQual.out', matrix._train['ExterQual'].values, delimiter=',',fmt="%s")  # creates a file so that the data is easier to look at

    #sale_price_against_attribute_scatter_plot('1stFlrSF')  # function that takes in a column name of train as an attribute and creates a scatter plot of
    # the sale price against the attribute




    ##################################################################################################################################################################
    #This attribute is already ordered as excellent, good, average, fair, poor can be converted to 5,4,3,2,1 easily




    list_exterior_quality = matrix._train['ExterQual'].values
    list_colour_corresponding_to_exterior_quality = [0] * len(matrix._train)
    list_of_colours = ['r', 'b', 'g', 'y', 'm']
    list_of_attributes = ['Excellent', 'Good', 'Average', 'Fair', 'Poor']

    for i in range(0, len(matrix._train)):
        if list_exterior_quality[i] == 'Ex':
            list_exterior_quality[i] = 5
            list_colour_corresponding_to_exterior_quality[i] = "r"
        elif list_exterior_quality[i] == 'Gd':
            list_exterior_quality[i] = 4
            list_colour_corresponding_to_exterior_quality[i] = "b"
        elif list_exterior_quality[i] == 'TA':
            list_exterior_quality[i] = 3
            list_colour_corresponding_to_exterior_quality[i] = "g"
        elif list_exterior_quality[i] == 'Fa':
            list_exterior_quality[i] = 2
            list_colour_corresponding_to_exterior_quality[i] = "y"
        elif list_exterior_quality[i] == 'Po':
            list_exterior_quality[i] = 1
            list_colour_corresponding_to_exterior_quality[i] = "m"
        else:
            print("Error")
            break

    plt.scatter(matrix._train['1stFlrSF'].values, matrix._train['SalePrice'].values, color=list_colour_corresponding_to_exterior_quality)
    plt.xlabel('1stFlrSF')
    plt.ylabel('SalePrice')
    for i in range(0, len(list_of_attributes)):# plot empty lists with the desired size and label to creat the legend (not possible any other way)
        plt.scatter([], [], c=list_of_colours[i], alpha=1, label=list_of_attributes[i])

    plt.legend(loc=0, scatterpoints=1, frameon=False, labelspacing=0, title='RoofStyle: ', prop={'size': 9})
    plt.show()


    ###################################################################################################################################################################################################







    ########################################################################################################################################################################################################################
    # This attribute is not ordered so it is not as simple to conver to 6,5,4,3,2,1


    list_Roof_Style = matrix._train['RoofStyle'].values#define a column of all the roof types
    list_colour_corresponding_to_roof_style = [0] * len(matrix._train)#used when later converting the strings to int
    list_of_colours = ['r', 'b', 'g', 'y', 'm','c']#colours used to visualise the data
    list_of_attributes = ['Flat', 'Gable', 'Gambrel', 'Hip', 'Mansard', 'Shed']#the ith colour corresponds to the ith type of roof

    for i in range(0, len(matrix._train)):
        if list_Roof_Style[i] == 'Flat':
            list_Roof_Style[i] = 6 #this converts the style to an int however as I do not know the order of which roof style is more desireable than the other,
            #cant simply just rank them alphabetically
            list_colour_corresponding_to_roof_style[i] = "r" #this is the loop that defines the coorect colour for each roof style
        elif list_Roof_Style[i] == 'Gable':
            list_Roof_Style[i] = 5
            list_colour_corresponding_to_roof_style[i] = "b"
        elif list_Roof_Style[i] == 'Gambrel':
            list_Roof_Style[i] = 4
            list_colour_corresponding_to_roof_style[i] = "g"
        elif list_Roof_Style[i] == 'Hip':
            list_Roof_Style[i] = 3
            list_colour_corresponding_to_roof_style[i] = "y"
        elif list_Roof_Style[i] == 'Mansard':
            list_Roof_Style[i] = 2
            list_colour_corresponding_to_roof_style[i] = "m"
        elif list_Roof_Style[i] == 'Shed':
            list_Roof_Style[i] = 1
            list_colour_corresponding_to_roof_style[i] = "c"
        else:
            print("Error")#break if theres an error
            break

    plt.scatter(matrix._train['1stFlrSF'].values, matrix._train['SalePrice'].values, color=list_colour_corresponding_to_roof_style)#creates the scatter plot
    #where colour contributes to the roof style
    plt.xlabel('1stFlrSF')
    plt.ylabel('SalePrice')

    for i in range(0, len(list_of_attributes)):# plot empty lists with the desired size and label to creat the legend (not possible any other way)
        plt.scatter([], [], c=list_of_colours[i], alpha=1, label=list_of_attributes[i])

    plt.legend(loc=0, scatterpoints=1, frameon=False, labelspacing=0, title='RoofStyle: ', prop={'size': 9})
    plt.show()

    ##################################################################################################################################################################



    print(Counter(matrix._train["RoofStyle"]))  # prints the number of each classification for ExterQual

if __name__ == "__main__":
    main()
