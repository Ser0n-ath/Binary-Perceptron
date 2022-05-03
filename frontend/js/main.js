var colorPicker = new iro.ColorPicker("#picker", {
	width: 220,
	color: "#f00",
});


//---------------------------Selection DOM elements-----------------------------//
const colorDisplay = document.getElementById('colorDisplay');
const predictionResult = document.getElementById('server-prediction-result');
const serverStatus = document.getElementById('server-status');
//-----------------------------------------------------------------//

//---------------------------Network Result DOM elements-----------------------//

//Test case values
const testingDataCount = document.getElementById('testing-data-count');
const trainingDataCount = document.getElementById('training-data-count');

//Confusion matrix values
const actuallyBrightPredictedBright = document.getElementById('PredictedBright_ActuallyBright');
const actuallyBrightPredictedDim = document.getElementById('PredictedDim_ActuallyBright');
const actuallyBrightTotal = document.getElementById('ActuallyBright_Total');

const actuallyDimPredictedBright = document.getElementById('PredictedBright_ActuallyDim');
const actuallyDimPredictedDim = document.getElementById('PredictedDim_ActuallyDim');
const actuallyDimTotal = document.getElementById('ActuallyDim_Total');

const predictedBrightTotal = document.getElementById('PB_Total');
const predictedDimTotal = document.getElementById('PD_Total');
const totalTestData = document.getElementById('Total_Dataset_count');

//Perceptron State Values
const perceptronStateRed = document.getElementById('red-state');
const perceptronStateBlue = document.getElementById('blue-state');
const perceptronStateGreen = document.getElementById('green-state');
const perceptronStateBias = document.getElementById('bias-state');
const perceptronStateLearningRate = document.getElementById('learningrate-state');


//Statistics State Values
const perceptronAccuracy = document.getElementById('accuracy');
const perceptronBrightPrecision = document.getElementById('bright_precision');
const perceptronDimPrecision = document.getElementById('dim_precision');
const perceptronBrightRecall = document.getElementById('bright_recall');
const perceptronDimRecall = document.getElementById('dim_recall');




//------------------------Edit Perceptron DOM elements ------------------------//
//-> Train Model Btn
const selectTrainingFileBtn = document.getElementById('select-training-file-btn');
const runTrainingFileBtn = document.getElementById('run-training-file-btn');

//->Batch Test Models
const selectBatchTestFileBtn = document.getElementById('select-batch-test-file-btn');
const runBatchTestFileBtn = document.getElementById('run-batch-test-file');

//-> Custom Perceptron WeightSelections Boxs & Buttons
const newRedValueBox = document.getElementById('new-red-value');
const newBlueValueBox = document.getElementById('new-blue-value');
const newGreenValueBox = document.getElementById('new-green-value');
const newBiasValueBox = document.getElementById('new-bias-value');
const newLearningRateBox = document.getElementById('new-learning-rate-value');
const setValues = document.getElementById('enter-new-perceptron-state-btn');

const resetAll = document.getElementById('reset-perceptron-filedataset-btn');


//->

//----------------------- Application States -----------------------------------//

var succesful_ping = false

var client_perceptron_state = {
	"red": 0,
	"green": 0,
	"blue": 0,
	"bias": 0,
	"learning_rate": 0
}

var perceptron_confusion_matrix = {
	"AD_PB": 0,
	"AD_PD": 0,
	"AB_PB": 0,
	"AB_PD": 0,
	"AD_Total": 0,
	"AB_Total": 0,
	"PB_Total": 0,
	"PD_Total": 0,
  "Total_Tests": 0
}


var perceptron_confusion_matrix_statistics = {
	"Accuracy": 0,
	"BP": 0,
	"DP": 0,
	"BR": 0,
	"DR": 0
}

var dataset_size = {
	"testing_data": 0,
	"training_data": 0
}

//-------------------DOM writers-----------------------//
/*Rewrites all the dom values to the current result*/
function dom_rewrite_network_results() {
	//Update Testing Data/Training Data values
	testingDataCount.innerHTML = perceptron_confusion_matrix["Total_Tests"]
	trainingDataCount.innerHTML = dataset_size.training_data


	 actuallyBrightPredictedBright.innerHTML = perceptron_confusion_matrix["AB_PB"]
	 actuallyBrightPredictedDim.innerHTML = perceptron_confusion_matrix["AB_PD"]
	 actuallyBrightTotal.innerHTML = perceptron_confusion_matrix["AB_Total"]
	 actuallyDimPredictedBright.innerHTML = perceptron_confusion_matrix["AD_PB"]
	 actuallyDimPredictedDim.innerHTML = perceptron_confusion_matrix["AD_PD"]
   	 actuallyDimTotal.innerHTML = perceptron_confusion_matrix["AD_Total"]
	 predictedBrightTotal.innerHTML = perceptron_confusion_matrix["PB_Total"]
	 predictedDimTotal.innerHTML = perceptron_confusion_matrix["PD_Total"]
	 totalTestData.innerHTML = perceptron_confusion_matrix["Total_Tests"]


	//Perceptron State Values
	 perceptronStateRed.innerHTML = client_perceptron_state["red"]
	 perceptronStateBlue.innerHTML = client_perceptron_state["blue"]
	 perceptronStateGreen.innerHTML = client_perceptron_state["green"]
	 perceptronStateBias.innerHTML = client_perceptron_state["bias"]
	 perceptronStateLearningRate.innerHTML = client_perceptron_state["learning_rate"]


	//Statistics State Values
	 perceptronAccuracy.innerHTML = perceptron_confusion_matrix_statistics["Accuracy"]
	 perceptronBrightPrecision.innerHTML = perceptron_confusion_matrix_statistics["BP"]
	 perceptronDimPrecision.innerHTML = perceptron_confusion_matrix_statistics["DP"]
	 perceptronBrightRecall.innerHTML = perceptron_confusion_matrix_statistics["BR"]
	 perceptronDimRecall.innerHTML = perceptron_confusion_matrix_statistics["DR"]
}


//Send a get request to the server
window.onload = function() {
	fetch_inital_perceptron();
}


//Add a catch response when it fails to connect?
function fetch_inital_perceptron() {
	fetch("http://127.0.0.1:5000/v1/api/")
		.then(response => response.json())
		.then(data => {
			data = data["perceptron_state"]
			client_perceptron_state["red"] = data["red_weight"]
			client_perceptron_state["green"] = data["green_weight"]
			client_perceptron_state["blue"] = data["blue_weight"]
			client_perceptron_state["bias"] = data["bias"]
			client_perceptron_state["learning_rate"] = data["learning_rate"]
			fetch_inital_network_result()
		})
}

function fetch_inital_network_result() {
	payload = {
		perceptron_state: client_perceptron_state
	}
	fetch("http://127.0.0.1:5000/v1/api/get-perceptron-status", {
			method: "post",
			headers: {
				'Accept': 'application/json',
				'Content-Type': 'application/json'
			},
			//make sure to serialize your JSON body
			body: JSON.stringify(payload)
		})
		.then(response => response.json()).then(data => {
			//Update DOM elements 
			//dom_rewrite_network_results()

			console.log(data)
			//Update Statistic States
			perceptron_confusion_matrix_statistics["Accuracy"] = data["statistics_dataset"]["Accuracy"]
			perceptron_confusion_matrix_statistics["BP"] = data["statistics_dataset"]["BrightPrecision"]
			perceptron_confusion_matrix_statistics["DP"] = data["statistics_dataset"]["DimPrecision"]
			perceptron_confusion_matrix_statistics["BR"] = data["statistics_dataset"]["BrightRecall"]
			perceptron_confusion_matrix_statistics["DR"] = data["statistics_dataset"]["DimRecall"]

			//Update ConfusionMatrix State
			perceptron_confusion_matrix["AD_PB"] = data["confusion_matrix"]["PredictedBright_ActuallyDim"]
			perceptron_confusion_matrix["AD_PD"] = data["confusion_matrix"]["PredictedDim_ActuallyDim"]
			perceptron_confusion_matrix["AB_PB"] = data["confusion_matrix"]["PredictedBright_ActuallyBright"]
			perceptron_confusion_matrix["AB_PD"] = data["confusion_matrix"]["PredictedDim_ActuallyBright"]

			perceptron_confusion_matrix["AD_Total"] = data["confusion_matrix"]["ActuallyDim"]
			perceptron_confusion_matrix["AB_Total"] = data["confusion_matrix"]["ActualBright"]
			perceptron_confusion_matrix["PB_Total"] = data["confusion_matrix"]["PredictedBright_Total"]
			perceptron_confusion_matrix["PD_Total"] = data["confusion_matrix"]["PredictedDim_Total"]
      perceptron_confusion_matrix["Total_Tests"] = data["confusion_matrix"]["TestCases_Total"]

      dom_rewrite_network_results()
		})
}


//--------------------Edit Perceptron---------------------//

//Read Training Data.txt -> Verify if valid format and send to server
//->Response is a new perceptron_state, and an updated training_data_count


//Read Batch Data.txt -> Verify if valid format and send to server
//->Response is binary file type which should be converted to .txt on client side and downloaded.

//Custom Weights, Read the changed weights and apply to perceptron model. Reevaluate NN result with default training/testing file

//Reset -> Refreshes the page -> [reset the perceptron to inital server provided state]

function display_server_results(prediction) {
	console.log(prediction)

	if (prediction == -1) {
		predictionResult.innerHTML = "Dim";
	} else if (prediction == 1) {
		predictionResult.innerHTML = "Bright";
	} else {
		predictionResult.innerHTML = "Loading..";
	}

}



function read_values(){
	//Read input
	var red_input = newRedValueBox.value.trim()
	var blue_input = newBlueValueBox.value.trim()  
	var green_input = newGreenValueBox.value.trim()   
	var bias_input = newBiasValueBox.value.trim()  
	var learning_rate_input = newLearningRateBox.value.trim()   

	console.log("Clicked!")
	console.log(red_input, blue_input, green_input, bias_input, learning_rate_input)
	console.log(!(red_input), blue_input, green_input, bias_input, learning_rate_input)
}

setValues.addEventListener("click", read_values)


//Fetch function
function evaluateColor(color) {
	payload = {
		color: {
			"red": color['r'],
			"green": color['g'],
			"blue": color['b']
		},
		perceptron_state: client_perceptron_state
	}
	fetch("http://127.0.0.1:5000/v1/api/evaluate-color", {
			method: "post",
			headers: {
				'Accept': 'application/json',
				'Content-Type': 'application/json'
			},
			//make sure to serialize your JSON body
			body: JSON.stringify(payload)
		})
		.then(response => response.json()).then(data => {
			display_server_results(data['prediction'])
		})
}


colorPicker.on('color:change', function(color) {
	colorDisplay.style.backgroundColor = color.hexString
	evaluateColor(color.rgb)
});