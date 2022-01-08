from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/v1/api')

@api.route('/init-state') #Use pretrained perceptron model
def get_init_state():
    return 'Loaded perceptron start state'

@api.route('/custom-state')  #Custom perceptron model
def get_custom_state():
    return 'Loaded custom state & update confusion matrix'

@api.route('/current-state')  #Current perceptron model
def get_current_state():
    return 'evaluation'

@api.route('/rand-state')   #Random perceptron model
def get_rand_state():
    return 'evaluation'


@api.route('/get-confusion-matrix') #Gets Confusion Matrix of current perceptron state with current training/testing data
def get_confusion_matrix():
    return 'Loaded Confusion matrix'


@api.route('/evaluate-color') #Evaluate a user selected color
def evaluate():
    return 'evaluation'

@api.route('/custom-train') #Custom dataset with a prefixed learning rate and inital bias.
def custom_data_set():
    return 'evaluation'