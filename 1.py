def hello(arg):
    '''
    >>>hello('Vasya')
    Heelo, Vasya!
    '''
    return "Heelo, {}!".format(arg)
    
def histogram(num_list):
    '''
    Procedure that takes a list of integers and prints a histogram to the screen.
    >>> histogram([4, 9, 7])   
    ****
    *********
    *******  
    '''
    import time
    for num in num_list:
        time.sleep(1.5)
        print('*' * num)
        
        
histogram([4, 9, 7])