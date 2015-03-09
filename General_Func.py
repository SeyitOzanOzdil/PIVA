import numpy as np
import string

def convertUserStringToInput(str):

        while "  " in str:
            str = str.replace("  "," ")       #bosluklar tek'e indirildi

        strSpaceOut = str.split(" ")          #bosluklara gore split edildi

        #TODO: numbers only control for lineEdits

        for i in range(len(strSpaceOut)):     #split edilen array item'larinin bas veya sonunda virgul varsa o virguller silindi
            if "," in strSpaceOut[i][0]: 
                strSpaceOut[i] = strSpaceOut[i][1:]
            if "," in strSpaceOut[i][len(strSpaceOut[i])-1]:
                strSpaceOut[i] = strSpaceOut[i][:len(strSpaceOut[i])-1]


        splitted = []
        for item in strSpaceOut:              #string dizisi virgullere gore split edildi
            temp = item.split(",")
            for t in temp:
                #splitted.append(t.translate(all, nodigs))
                splitted.append(t)           #TODO: burasini check et

        
        resultArr = []
        for item in splitted:                 #stringler int ya da floata donusturuldu
            try:
                num = int(item)
            except ValueError:
                num = float(item)
            resultArr.append(num)

        return resultArr

def getTailInfoAndCalculationRes(isLower, lower_yArray):
    if isLower == True:
        yArrayStr = ConvertArrayToStrOutput(lower_yArray)
        tail = "Alt sinir"
                    
    else:
        upper_yArray = []
        for item in lower_yArray:
            upper_yArray.append(1-float(item))

        yArrayStr = ConvertArrayToStrOutput(upper_yArray)
        tail = "Ust sinir"

    return tail, yArrayStr 

def ConvertArrayToStrOutput(array):
        
    strRes = ""
    for item in array:
        if array.index(item) < len(array)-1:
            strRes += str(item) + ", "
        else:
            strRes += str(item)

    return strRes
