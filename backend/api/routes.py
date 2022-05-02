import flask
from http import server
from flask import Blueprint, request, jsonify
import api.perceptron_controller as controller
import api.constants as CONSTANT

api = Blueprint('api', __name__, url_prefix='/v1/api')


#-------------------------------------------------------------#


#Returns True if the server is online
@api.route('/heart_beat', methods = ['GET'])  #Done
def heart_beat():
    return str(True)

@api.route('/', methods=['GET']) 
def main():
    #Returns the following
    #->Perceptron State
    #-----------Perceptron Results--------#
    #->Number of Testing Data used
    #->Number of Training Data used
    #->Perceptron Confusion Matrix
    #->Statistics

    result = controller.init_state()
    return result

#Evaluate a selected users color
@api.route('/evaluate-color' , methods=['POST']) 
def evaluate():
    if(request.is_json == False):
        return "Invalid Request Header"
    client_request = request.get_json()  
    server_response = controller.eval_color(client_request)
    return server_response

#-------------------------------------------------------#

@api.route('/get-perceptron-status', methods=['GET', 'POST'])
def get_perceptron_status():
    # -> Get # Testing Data, Training Data
    # -> Get Perceptron Confusion Matrix on Test Dataset (Requires Testing Data + Perceptron State) => Matrix + statistics
    # -> Get NN State[Not required]




    #If its a get request provide the status of the premade model with premade training set.
    if(request.is_json == False):
        return "Invalid Request Header. Payload not json format."
    #Do checks on json input
    client_request = request.get_json()


    response = controller.perceptron_stats_result(client_request, CONSTANT.DEFAULT_FILE)
    return response