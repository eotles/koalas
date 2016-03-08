'''
Data structure for 1-dimensional data
'''

class Series(object):
    ''' dictionary '''
    
    def __init__(self, data=None, index=None, name=None):
        self.name = name
        if(data is None): data = {}
        if(index is None and not isinstance(data, dict)): 
            data = {k: v for k,v in enumerate(v)}
            index = range(len(data))
            data = {
