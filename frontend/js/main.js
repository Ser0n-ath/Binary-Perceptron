//Element Valies
const colorDisplay = document.getElementById('colorDisplay')
const predictionResult = document.getElementById('server-prediction-result')


var colorPicker = new iro.ColorPicker("#picker", {
	width: 220,
	color: "#f00",
});

//Application States

var client_perceptron_state = {
  "red": 0.1187515928706572,
  "green": 0.11714939038223227,
  "blue": 0.11849347714207387,
  "bias": 59.20319004735466,
  "learning_rate": 0.0002
}

//DOM MANUPILATION

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