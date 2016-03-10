import series

Series = series.Series

class DataFrame(object):
    #list of rows (which are lists)
    
    #FIX:
    def __init__(self, data=None, index=None, columns=None):
        if(data is None):
            data = [[]]
        if(index is None):
            index = [i for i in xrange(len(data))]
        if(columns is None):
            columns = []
        
        data_at_idx = {idx: [] for idx in index}
        data_in_col = {column: [] for column in columns}
        
        rows_are_lists = False
        rows_are_dicts = False
        for index_pointer, row in enumerate(data):
            print(row)
            if(isinstance(row, (list, dict)) == False):
                raise ValueError('Data must be two dimensional')
            if(rows_are_lists and rows_are_dicts): 
                raise ValueError('Data contains both lists and dicts')
            
            if(type(row) is list):
                rows_are_lists = True
                data_at_idx[index_pointer] = row
                if(len(columns) < len(row)):
                    raise ValueError('Rows are longer than columns specify')
                for col_pointer, element in enumerate(row):
                    data_in_col[col_pointer].append(element)
            
            elif(type(row) is dict):
                rows_are_dicts = True
                
        self.data = data
        self.data_at_idx = data_at_idx
        self.data_in_col = data_in_col    
        self.index = index
        self.columns = columns
