def cInterest(principal, time, rate):
    ci = principal*(((1+ rate/100))**time - 1)
    return ci