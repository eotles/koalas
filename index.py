
class Index(object):
    def __init__(self, values):
        self.values = values
    
    def __iter__(self):
        self.cur = 0
        return(self)
    
    def next(self):
        if(self.cur >= len(self.values)):
            raise StopIteration
        else:
            cur_val = self.values[self.cur]
            self.cur += 1
            return(cur_val)
    
#TODO: LOC
#TODO: iLoc

