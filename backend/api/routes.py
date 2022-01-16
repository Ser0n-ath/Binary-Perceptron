from http import server
from flask import Blueprint, request, jsonify
import api.perceptron_controller as controller



api = Blueprint('api', __name__, url_prefix='/v1/api')

@api.route('/') #Use pretrained perceptron model
def main():
    return "Specify a valid route you would like to take."


@api.route('/entry') #Done.
def entry():
    result = controller.init_state()
    return result

@api.route('/custom-state')  #Custom perceptron model
def get_custom_state():
    return 'Loaded custom state & update confusion matrix'

@api.route('/current-state')  #Current perceptron model ? 
def get_current_state():
    return 'evaluation'

@api.route('/rand-state')   #Random perceptron model
def get_rand_state():
    return 'evaluation'


@api.route('/get-confusion-matrix') #Gets Confusion Matrix of current perceptron state with current training/testing data
def get_confusion_matrix():
    return 'Loaded Confusion matrix'


@api.route('/evaluate-color' , methods=['POST']) #Evaluate a user selected color
def evaluate():
    #Precondition: Perceptron Model and 
    if(request.is_json == False):
        return "Invalid Request Header"
    client_request = request.get_json() #This is of type dictionary. 
    server_response = controller.eval_color(client_request)
    return server_response



@api.route('/custom-train') #Custom dataset with a prefixed learning rate and inital bias.
def custom_data_set():
    return 'evaluation'