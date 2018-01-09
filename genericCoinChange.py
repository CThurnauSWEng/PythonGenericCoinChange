def genericCoinChange(legend,amt):
    '''
    This function determines how many of each type of "generic" coin would be required
    to make up the given amt
    '''

    # initialize the output object
    countLegend = {  "triangle"   : 0,
                    "square"      : 0,
                    "rectangle"   : 0}

    loopCounter = 0

    dmResult = {}

    while (amt > 0 and loopCounter < 5):

        loopCounter += 1        
        key = getNextMax(legend,amt)
        dmResult = divmod(amt,legend[key])
        countLegend[key] = dmResult[0]
        amt = dmResult[1]
    
    return countLegend

def getNextMax(legend,amt):
    max = 0
    maxkey = ""
    for key in legend:
        if legend[key] > max:
            if legend[key] <= amt:
                max = legend[key]
                maxkey = key
    return maxkey

legend = {  "triangle"    : 1,
            "square"      : 7,
            "rectangle"   : 15}

amt = 100
print "Values of denominations: ",legend, "amt: ",amt
print "Numbers of each type of coins:"
print genericCoinChange(legend,amt)

print "*******************************"
legend = {  "triangle"    : 1,
            "square"      : 4,
            "rectangle"   : 10}

amt = 47
print "Values of denominations: ",legend, "amt: ",amt
print "Numbers of each type of coins:"
print genericCoinChange(legend,amt)
