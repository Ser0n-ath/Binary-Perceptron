from api.models.data_point import DataPoint
from api.models.perceptron_state import PerceptronState

def feed_forward(color: DataPoint, state: PerceptronState) -> int:
    weighted_sum = state.red_weight * color.red + state.blue_weight * color.blue + state.green_weight * color.green
    if(weighted_sum < state.bias):
        color.predictedTruthValue = -1
        return -1
    color.predictedTruthValue = 1
    return 1

def learning_supervisor(predicted_outcome: int, correct_outcome: int) -> bool:
    return predicted_outcome == correct_outcome

def update(color: DataPoint, state: PerceptronState) -> PerceptronState:
    error = color.expectedTruthValue - color.predictedTruthValue
    state.red_weight = state.red_weight + error * state.learning_rate * color.red
    state.blue_weight = state.blue_weight + error * state.learning_rate * color.blue
    state.green_weight = state.green_weight + error * state.learning_rate * color.green
    state.bias = state.bias + error * state.learning_rate * 1
    return state

def perceptron_train(init_state: PerceptronState, colors: list) -> PerceptronState: #returns final perceptron state after training.
    for color in colors:
        predicted_outcome = feed_forward(color, init_state)
        if(learning_supervisor(predicted_outcome, color.expectedTruthValue)):
            continue
        else:
            update(color, init_state)
    return init_state
