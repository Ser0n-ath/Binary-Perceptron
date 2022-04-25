from urllib import response
from api.models.data_point import DataPoint
from api.models.perceptron_state import PerceptronState
import api.perceptron as perceptron
import api.constants as CONSTANT
import api.validation.validate as validate

import os

def default_training_generate() -> list:
    #Note: Cache results in the future? 
    #Precondition: Default training data is in valid format.

    print(os.getcwd)
    training_set = []
    default_training_file = open('./api/dataset/training_data.txt')
    pass


