# ========================== 03 ==========================
class AlmgrenChriss():
    def __init__(self):
        pass
    
    def u(self,t):
        return 0#TODO
    def q(self,t):
        return 0#TODO
    def S(self,t):
        return 0#TODO
    def S_tilde(self,t):
        return 0#TODO
    
    @property
    def book_value_at_initial_time(self):
        return self.q(0) * self.S(0)
    @property
    def running_revenue(self):
        '''self.time'''
        if t != T: return self.u(t) * self.S_tilde(t)
        else: return self.q(T) * self.S_tilde(T)
    @property  
    def revenue(self):
        revenue = 0
        for t in self.time_list:
            revenue += self.running_revenue
        return revenue
    @property  
    def total_execution_cost(self):
        return self.book_value_at_initial_time - self.revenue
    
    
if __name__ == "__main__":
    pass