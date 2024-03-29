from fractions import Fraction
import numpy as np
from gym_exchange import Config
import random;random.seed(Config.seed)


class Twap():
    def __init__(self):
        self.initialize() # return self.num_list
        self.step_index = 0
    def initialize(self):
        # step_integer = Config.num2liquidate // Config.max_horizon
        # arr = np.full(Config.max_horizon, step_integer)
        # selected_indices = random.sample(range(len(arr)), Config.num2liquidate - Config.max_horizon * step_integer)
        # arr[selected_indices] += 1
        # assert arr.sum() == Config.num2liquidate
        arr = np.full(Config.max_horizon, 0) #$ masked for testing
        self.num_list = arr

    @property
    def done(self):
        if self.step_index < Config.max_horizon: return False
        else: return True
        
    def step(self) -> int:
        """Return the simple actions: numbers to sell/buy"""
        self.action = self.num_list[self.step_index]
        self.step_index +=1
        return self.action, self.done
    
class ResidualPolicy_Factory():
    '''factory methods/ or interface methods
    TWAP is one implemention of ResidualPolicy'''
    @staticmethod
    def produce(name):
        if name == "Twap":
            return Twap()
        else: raise NotImplementedError
    
if __name__ == '__main__':
    action_list = []
    twap = Twap()
    done = False
    while True:
        action, done = twap.step()
        action_list.append(action)
        if done: break
    print(sum(action_list) == Config.num2liquidate)


