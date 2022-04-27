from urllib import response
from api.models.data_point import DataPoint
from api.models.perceptron_state import PerceptronState
import api.perceptron as perceptron
import api.constants as CONSTANT
import api.validation.validate as validate
import os

#Reads a file and returns an array of Datapoints 
def read_default_training_data() -> list:
    #Precondition: Default training file is in valid format. 
    training_set = []
    default_training_file = open(CONSTANT.DEFAULT_PATH_TRAINING_FILE)
    for lines in default_training_file:
        color_value = lines.split()
        training_point = DataPoint(color_value[0], color_value[1], color_value[2], color_value[3])
        training_set.append(training_point.to_dict())
    default_training_file.close()
    return training_set

def read_provided_training_data(file_stream) -> list:
    pass
