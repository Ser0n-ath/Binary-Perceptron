from backend.api.models.data_point import DataPoint
from backend.api.models.perceptron_state import PerceptronState


def feed_forward(color: DataPoint, state: PerceptronState) -> int:
    pass

def learning_supervisor(predicted_outcome: int, correct_outcome: int) -> bool:
    pass

def update(color: DataPoint, state: PerceptronState):
    pass
