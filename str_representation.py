def formString(str):
    length = len(str)
    if length <3:
        return("string too short")
    middle = length // 2
    if length % 2==0:
        middle -=1
    finaltext = str[0] +str[middle] + str[-1]
    return finaltext
string = "Shine" 
formString(string)