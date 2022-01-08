class PerceptronState:
    def __init__(self, red_weight: float, blue_weight: float, green_weight: float, bias: float, learning_rate: float):
        self.red_weight = red_weight
        self.blue_weight = blue_weight
        self.green_weight = green_weight
        self.bias = bias
        self.learning_rate = learning_rate
    
    def to_dict(self) -> dict:
        return{
            'red_weight': self.red_weight,
            'blue_weight': self.blue_weight,
            'green_weight': self.green_weight,
            'bias': self.bias,
            'learning_rate': self.learning_rate,
        }
