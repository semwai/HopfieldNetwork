import numpy as np

class Hopfield_network: 
    w = np.zeros(0)
    
    def train(self, neu, training_data):
        self.w = np.zeros([neu, neu])
        for data in training_data:
            self.w += np.outer(data, data)
        for diag in range(neu):
            self.w[diag][diag] = 0
    
    def retrieve_pattern(self, data, steps = 2):
        res = np.array(data)
        for _ in range(steps):
            for i in range(len(res)):
                raw_v = np.dot(self.w[i], res)
                if raw_v > 0:
                    res[i] = 1
                else:
                    res[i] = -1
                
        return res

class Hopfield_converter: 

    def to_hop():
        pass 

    def from_hop(): 
        pass