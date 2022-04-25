from urllib import response
from api.models.data_point import DataPoint
from api.models.perceptron_state import PerceptronState
import api.perceptron as perceptron
import api.constants as CONSTANT
import api.validation.validate as validate
import api.data_controller as dataController

def init_state() -> dict: #Returns the standard perceptron. 
    state = PerceptronState(CONSTANT.PRETRAINED_RED, CONSTANT.PRETRAINED_GREEN, CONSTANT.PRETRAINED_BLUE, CONSTANT.PRETRAINED_BIAS, CONSTANT.DEFAULT_LEARNING_RATE).to_dict()
    return {"perceptron_state": state}

def eval_color(request: dict) -> dict:
    valid_model = validate.validate_perceptron_state(request) #Merge  & Implement
    valid_color = validate.validate_color_selection(request)

    valid_model = True
    valid_color = True

    #If valid input
    if(valid_model and valid_color):
        state_dict = request['perceptron_state']
        state = PerceptronState(state_dict['red'], state_dict['green'], state_dict['blue'], state_dict['bias'], state_dict['learning_rate'])
        color_dict = request['color']
        color = DataPoint(color_dict['red'], color_dict['green'], color_dict['blue'],-1)
        server_response =  perceptron.feed_forward(color,state)
        return {"prediction":server_response}
    else:
        return "Error: Input failure @: " + "valid mode: " + str(valid_model) + " or valid color: " + str(valid_color)

def confusion_matrix(request: dict) -> dict:
    valid_model = validate.validate_perceptron_state(request) #Merge  & Implement
    valid_training = validate.validate_training_data(request) 

    valid_model = True
    valid_color = True

    if(valid_model and valid_color):
        state_dict = request['perceptron_state']
        state = PerceptronState(state_dict['red'], state_dict['green'], state_dict['blue'], state_dict['bias'], state_dict['learning_rate'])
        testing_data = dataController.default_training_generate()
        return {"testing_data": state.to_dict}

