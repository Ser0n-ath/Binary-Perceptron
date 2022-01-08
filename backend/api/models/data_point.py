class DataPoint:
    def __init__(self, red:int, blue:int, green:int, expectedTruthValue:int):
        self.red = red
        self.blue = blue
        self.green = green
        self.expectedTruthValue = expectedTruthValue
        self.predictedTruthValue = -1
    
    def to_dict(self) -> dict:
        return{
            'red': self.red,
            'blue': self.blue,
            'green': self.green,
            'expectedTruthValue': self.expectedTruthValue,
        }