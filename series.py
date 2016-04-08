'''
Data structure for 1-dimensional data
'''

import collections
import index as klindex
reload(klindex)

#TODO: make index method
#TODO: head method
#TODO: not sure about how index should work
class Series(object):
    ''' based on dictionary '''
    
    def __init__(self, data=None, index=None, name=None):
        #data - can be:
        #   dictionary (no index)
        #   list - index as list
        self.name = name
        self.data = collections.OrderedDict()
        if(data is None): 
            data = []
        if(index is None):
            index = [i for i in xrange(len(data))]
        for index_position, index_value in enumerate(index):
            self.data[index_value] = data[index_position]
        self.index = klindex.Index(index)
        self.type = None
    
    
    def __str__(self):
        s = '%s\n' %('\n'.join(['%s\t%s' %(k,v) for k,v in self.data.iteritems()]))
        if(self.name is not None):
            s+= 'Name: %s,' %(self.name)
        s+= 'dtype: %s' %(self.type)
        return(s)
    
    __repr__ = __str__
    
    def apply(self, fx):
        data = [fx(v) for v in self.data.values()]
        return(Series(data, index=self.index))
        
    def __getitem__(self, index_value):
        return(self.data[index_value])
    
    def __eq__(self, b):
        return(self.apply(lambda x: x==b))
    
    def __ne__(self, b):
        return(self.apply(lambda x: x!=b))
    
    def __lt__(self, b):
        return(self.apply(lambda x: x< b))
    
    def __le__(self, b):
        return(self.apply(lambda x: x<=b))
        
    def __gt__(self, b):
        return(self.apply(lambda x: x> b))
    
    def __ge__(self, b):
        return(self.apply(lambda x: x>=b))
    
    #TODO: use slice
    def head(self, n=5):
        pass

    #TODO: make slice
    def slice():
        pass

            

