import koalas as kl

def main():
    
    #no args
    kl.DataFrame()

    #one row of data, no other args
    data = [[1,2]]
    kl.DataFrame(data)

    #one row of data, index, no columns
    index = ['a']
    kl.DataFrame(data, index)

    #one row of data, index, columns
    index = ['a']
    columns = ['z', 'y']
    kl.DataFrame(data, index, columns)

    index = ['a']
    columns = ['z']
    kl.DataFrame(data, index, columns)



if __name__=='__main__':
    main()
