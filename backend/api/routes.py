from http import server
from flask import Blueprint, request, jsonify
import api.perceptron_controller as controller


api = Blueprint('api', __name__, url_prefix='/v1/api')



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


@api.route('/get-perceptron-status', methods=['GET', 'POST'])
def get_perceptron_status():
    #Reads  
    return


    

@api.route('/evaluate-color' , methods=['POST']) #Evaluate a user selected color
def evaluate():
    if(request.is_json == False):
        return "Invalid Request Header"
    client_request = request.get_json()  
    server_response = controller.eval_color(client_request)
    return server_response