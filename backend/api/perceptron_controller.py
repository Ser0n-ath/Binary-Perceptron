from api.models.data_point import DataPoint
from api.models.perceptron_state import PerceptronState
import api.perceptron
import api.constants as CONSTANT


def init_state(): #Returns the standard perceptron. 
    state = PerceptronState(CONSTANT.PRETRAINED_RED, CONSTANT.PRETRAINED_GREEN, CONSTANT.PRETRAINED_BLUE, CONSTANT.PRETRAINED_BIAS, CONSTANT.DEFAULT_LEARNING_RATE).to_dict()
    return {"perceptron_state": state, "prediction": {"Red": -1, "Green": -1, "Blue": -1}}
