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
        return "Error: Input failure @: " + "invalid model: " + str(valid_model) + " or invalid color: " + str(valid_color)



def perceptron_stats_result(request: dict, result_type: str) -> dict:
    #Reads in a perceptron state
    state_dict = request['perceptron_state']
    state = PerceptronState(state_dict['red'], state_dict['green'], state_dict['blue'], state_dict['bias'], state_dict['learning_rate'])
    dataset = None 


    confusion_matrix = {"PredictedBright_ActuallyDim": 0, "PredictedDim_ActuallyDim":0, "ActuallyDim":0, "PredictedBright_ActuallyBright": 0, "PredictedDim_ActuallyBright": 0, "ActualBright":0,
    "PredictedBright_Total":0, "TestCases_Total": 0}


    statistic_result = {"Accuracy":0, "BrightPrecision":0, "DimPrecision":0, 'BrightRecall':0, "DimRecall":0 }

    if(result_type == CONSTANT.CUSTOM_FILE):
        dataset = dataController.read_default_training_data() #Set the data as default 
    else:
        dataset = dataController.read_default_training_data() #Set the data as custom

    #Run an evaluation on all items
    for data_point_item in dataset:
        print(str(data_point_item)) 
        data_point = DataPoint(float(data_point_item["red"]), float(data_point_item["green"]), float(data_point_item["blue"]), float(data_point_item["expectedTruthValue"])) 
        perceptron.feed_forward(data_point, state)
        #Update statistics matrix
        if(data_point_item["expectedTruthValue"] == 1): #expected value = 1


            if(data_point_item["predictedTruthValue"] == 1):
                #Expected=1;Predicted = 1
                confusion_matrix["PredictedBright_ActuallyBright"] += 1 #Correct Prediction
            else: 
                #expected value = 0 Expected dim 
                confusion_matrix["PredictedDim_ActuallyBright"] += 1 #Wrong prediction 
        else: 
            if(data_point_item["predictedTruthValue"] == 1):
                #Expected=0;Predicted = 1
                confusion_matrix["PredictedBright_ActuallyDim"] += 1 #Correct Prediction
            else: 
                # Expected=0;Predicted=0
                confusion_matrix["PredictedDim_ActuallyDim"] += 1 #Wrong prediction 

        confusion_matrix["TestCases_Total"] += 1

    confusion_matrix["ActuallyDim"] = confusion_matrix["PredictedBright_ActuallyDim"] + confusion_matrix["PredictedDim_ActuallyDim"]
    confusion_matrix["ActualBright"] = confusion_matrix["PredictedBright_ActuallyBright"] + confusion_matrix["PredictedDim_ActuallyBright"]

    return {"confusion_matrix": confusion_matrix, "statistics_dataset": statistic_result}













   
    



    print(result)
    return {"training_array": str(result)}

