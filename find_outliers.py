"""
Author: Thinh Mai
Date: 11/4/2019
Purpose: Find outliers 

"""
#load modules
import numpy as np

def findOL(arryMatx):
    #create 2 empty arrays for calculating the deviation and reshaping the array for final output
    result_array  = np.array([])
    dev_array = np.array([])

    #checking the shape of the input array, then will use this to reshape the calc array and return appropriate results
    shape_n = (np.shape(arryMatx))

    #create an array from users' input
    a = (np.array(arryMatx))
    for var in a:
        for num in var:
            #calculate the deviation
            dev = (np.abs(num-np.median(var)))
            dev_array = np.append(dev_array,dev)
    #reshape array to have as same shape as the input array
    new_array = (np.reshape(dev_array,shape_n))
    
    for new_num in new_array:
        #find the maximum deviation
        new_value = np.argmax(new_num)
        result_array = np.append(result_array,new_value)
        #convert float type to integer type in the result array
    return (result_array.astype(int))








