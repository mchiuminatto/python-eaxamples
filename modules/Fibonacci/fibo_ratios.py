
ret_ratios = [0, 23.1, 38.6, 50, 61.8, 76.4, 100]
exp_ratios = [127.1, 161.8, 2]


def fibo_retrace(level):
    """
    fibonacci ratiio by level
    
    returns a fibinacci retracement level 
    :param level: retracement level
    :return: expansion level 
    """
    if level > ret_ratios.count():
        return -1
    elif level < 0:
        return -1
    else:
        return ret_ratios[level]


def fibo_expansion(level):
    """
    fibinacci expansion ratio by level
    
    ertunrs the fibinacci expansion rations depending on level
    :param level: expansioin level
    :return: expansion ratio 
    """

    if level > exp_ratios.count():
        return -1
    elif level < 0:
        return -1
    else:
        return exp_ratios[level]


def calc_fibo_ratio(n):
    """
    calculate fibinacci golden ratio
    
    :param n:number of iterations 
    :return: fibinacci ratio for the number of iterations
    """
    ratio = 0
    a, b = 0, 1
    for i in range(0, n+1):
        a, b = b, a + b
        ratio = a/b
    print(ratio)
    return ratio


# this adds the ability for the module to be called as a script or to be imported
# calling a module like this can be useful to run test suits
if __name__ == "__main__":
    import sys
    calc_fibo_ratio(int(sys.argv[1]))
