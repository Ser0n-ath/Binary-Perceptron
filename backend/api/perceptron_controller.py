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


def train_perceptron(request: dict) -> dict:
    state_dict = request['perceptron_state']
    state = PerceptronState(state_dict['red'], state_dict['green'], state_dict['blue'], state_dict['bias'], state_dict['learning_rate'])
    pass

    #Get perceptron state 

def perceptron_stats_result(request: dict, result_type: str) -> dict:
    #Reads in a perceptron state
    state_dict = request['perceptron_state']
    state = PerceptronState(state_dict['red'], state_dict['green'], state_dict['blue'], state_dict['bias'], state_dict['learning_rate'])
    dataset = None 
    confusion_matrix = {"PredictedBright_ActuallyDim": 0, "PredictedDim_ActuallyDim":0, "ActuallyDim":0, "PredictedBright_ActuallyBright": 0, 
    "PredictedDim_ActuallyBright": 0, "ActualBright":0, "PredictedBright_Total":0, "PredictedDim_Total":0, "TestCases_Total": 0}

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
        if(data_point.expectedTruthValue == 1): 
            if(data_point.predictedTruthValue == 1):
                confusion_matrix["PredictedBright_ActuallyBright"] += 1 
            else: 
                confusion_matrix["PredictedDim_ActuallyBright"] += 1 
        else: 
            if(data_point.predictedTruthValue == 1):
                confusion_matrix["PredictedBright_ActuallyDim"] += 1 
            else: 
                confusion_matrix["PredictedDim_ActuallyDim"] += 1 

        confusion_matrix["TestCases_Total"] += 1

    confusion_matrix["ActuallyDim"] = confusion_matrix["PredictedBright_ActuallyDim"] + confusion_matrix["PredictedDim_ActuallyDim"]
    confusion_matrix["ActualBright"] = confusion_matrix["PredictedBright_ActuallyBright"] + confusion_matrix["PredictedDim_ActuallyBright"]
    confusion_matrix["PredictedDim_Total"] = confusion_matrix["PredictedDim_ActuallyDim"] + confusion_matrix["PredictedDim_ActuallyBright"]
    confusion_matrix["PredictedBright_Total"] = confusion_matrix["PredictedBright_ActuallyBright"] + confusion_matrix["PredictedBright_ActuallyDim"]
    statistic_result = generate_statistics(statistic_result,confusion_matrix)
    return {"confusion_matrix": confusion_matrix, "statistics_dataset": statistic_result}



def generate_statistics(statistics: dict, confusion_matrix: dict) -> dict:
    statistics["Accuracy"] = round((confusion_matrix["PredictedBright_ActuallyBright"] + confusion_matrix["PredictedDim_ActuallyDim"]) / confusion_matrix["TestCases_Total"],2) * 100.0
    #Precisions = True Positive / Total Predicted Positive
    statistics["BrightPrecision"] = round(confusion_matrix["PredictedBright_ActuallyBright"] / confusion_matrix["PredictedBright_Total"],3) * 100.0
    statistics["DimPrecision"] =  round(confusion_matrix["PredictedDim_ActuallyDim"] / confusion_matrix["PredictedDim_Total"],3) * 100.0
    #Recall True Positive / Total Actual Positive
    statistics["BrightRecall"] = round(confusion_matrix["PredictedBright_ActuallyBright"] / confusion_matrix["ActualBright"],3) * 100.0
    statistics["DimRecall"] =  round(confusion_matrix["PredictedDim_ActuallyDim"] / confusion_matrix["ActuallyDim"],3) * 100.0
    return statistics












   
    



    print(result)
    return {"training_array": str(result)}

