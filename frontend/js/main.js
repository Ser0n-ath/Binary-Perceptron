const colorDisplay = document.getElementById('colorDisplay')
const predictionResult = document.getElementById('server-prediction-result')


var colorPicker = new iro.ColorPicker("#picker", {
	width: 220,
	color: "#f00",
});


var succesful_ping = false
var client_perceptron_state = {
  "red": 0,
  "green": 0,
  "blue": 0,
  "bias": 0,
  "learning_rate": 0
}

//Changes on the follow scenarios
//->Inital Connection to server or a reset request
//-> 

//AD = Actually Dim
//PB = Predicted Dim
//AB = Actually Bright
//PB = Predicted Bright


var perceptron_confusion_matrix = {
  "AD_PB": 0,
  "AD_PD": 0,
  "AB_PB": 0,
  "AB_PD": 0,
  "AD_Total": 0,
  "AB_Total": 0,
  "PB_Total": 0,
  "PD_Total": 0
}

var perceptron_confusion_matrix_statistics ={
  "Accuracy": 0,
  "BP": 0,
  "DP": 0,
  "BR": 0,
  "DR": 0
}


//----------------Perceptron Result Field Update --------------//

function update_input_stat(test_data_count, training_data_count){
  //Read the testing, training count, and reflect changes in HTMl
  return 0
}


function update_confusion_matrix(new_matrix_dictionary){
  //Reads the matrix dictionary, and reflect changes in HTML 
  return 0
}

function update_statistics_matrix(perceptron_confusion_matrix_res) {
  //Updates the statistics dictionary, and reflect changes in HTML 
  return 0
}

function update_perceptron_state(new_client_perceptron_state){
  //Updates the NN State fields in front-end

}

//--------------------Edit Perceptron---------------------//
 
//Read Training Data.txt -> Verify if valid format and send to server
//->Response is a new perceptron_state, and an updated training_data_count


//Read Batch Data.txt -> Verify if valid format and send to server
//->Response is binary file type which should be converted to .txt on client side and downloaded.

//Custom Weights, Read the changed weights and apply to perceptron model. Reevaluate NN result with default training/testing file

//Reset -> Refreshes the page -> [reset the perceptron to inital server provided state]







function display_server_results(prediction){
  console.log(prediction)

  if(prediction == -1){
    predictionResult.innerHTML = "Dim";
  }else if(prediction == 1){
    predictionResult.innerHTML = "Bright";
  }else{
    predictionResult.innerHTML = "Loading..";
  }

}


//Fetch function

function evaluateColor(color) {
  payload = {color: {"red": color['r'], "green": color['g'], "blue": color['b']}, perceptron_state: client_perceptron_state}
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