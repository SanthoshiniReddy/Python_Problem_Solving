def formString(str):
    length = len(str)
    if length <3:
        return("string too short")
    
    if length % 2 == 0:
            
        middle_char = string[length // 2 - 1 : length // 2 + 1]
    else:
        middle_char = str[length // 2]
    
    formed_string = str[0] + middle_char + str[-1]
    return formed_string
string = "dinesh"
formString(string)