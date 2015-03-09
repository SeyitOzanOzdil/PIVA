
import Utils

class DataSet(object):

    lines = []
    lineCount = 0
    features = []
    featureCount = 0
    dataSetDic = {}
    hasFeatureLine = True

    numericFeatures = list()
    nonNumericFeatures = list()


    def __init__(self, lines, hasFeatureLine):
        self.lines = lines
        self.hasFeatureLine = hasFeatureLine
        self.__SetProperties()
        self.dataSetDic = self.__CreateDictionary()
        self._SetNumericOrNonNumericFeatures()

    def __SetProperties(self):
        
        self.lineCount = len(self.lines)-1
        if not self.hasFeatureLine:
            self.lineCount = len(self.lines)

        # feature lari belirleyelim

        i=0
        while i<=self.lineCount:
            self.features = self.lines[i].split(",")
            self.featureCount = len(self.features)
            if self.featureCount == 0:
                i = i+1
            else:
                break
        if not self.hasFeatureLine:
            j=1
            for feature in self.features:
                feature = "FEATURE " + str(j)
                self.features[j-1] = feature
                j=j+1

    def GetValue(self, feature, index):
        
        #Kontroller
        if index > self.lineCount:
            return Utils.CONST_FAILURE
        if self.features.count(feature) <= 0:
            return Utils.CONST_FAILURE

        FeatIndex = self.features.index(feature)
        LineSplit = self.lines[index].split(",")

        value = LineSplit[FeatIndex]

        return value

    def __CreateDictionary(self):
        dict = {}
        column = 0

        for feature in self.features:
            hasValues = []
            startIndex = 1
            stopIndex = self.lineCount+1

            if not self.hasFeatureLine:
                startIndex = 0
                stopIndex = self.lineCount  
                         
            for i in range(startIndex, stopIndex):
                lineSplit = self.lines[i].split(",")
                
                hasValues.append(Data(lineSplit[column]))

            column = column+1

            dict[feature] = hasValues
            del hasValues

        return dict

    def _SetNumericOrNonNumericFeatures(self):

        self.numericFeatures = list()
        self.nonNumericFeatures = list()
                
        for feature in self.features:

            numeric = 0
            nonNumeric = 0
            values = self.dataSetDic[feature]

            for value in values:

                if value.isNumeric:
                    numeric = numeric + 1
                else:
                    nonNumeric = nonNumeric + 1
            if numeric > nonNumeric:
                self.numericFeatures.append(feature)
            else:
                self.nonNumericFeatures.append(feature)

    def GetNonNumericValues(self, nonNumericFeature):

        values = list()
        counts = list()

        valueList = self.dataSetDic[str(nonNumericFeature)]

        for value in valueList:

                if len(values) == 0:
                    values.append(value.value)
                    counts.append(1)
                else:
                    for currentValue in values:
                        if currentValue == value.value:
                           index = values.index(value.value)
                           count = counts[index]
                           count = count + 1
                           counts[index] = count
                           break
                        if currentValue == values[len(values)-1]:
                            values.append(value.value)
                            counts.append(1)

        return values, counts

    def GetNumericValues(self, numericFeature):

        values = list()
        counts = list()

        valueList = self.dataSetDic[str(numericFeature)]

        for value in valueList:
            values.append(value.value)
            counts.append(1)
            '''if len(values) == 0:
                values.append(value.value)
                counts.append(1)
            else:
                for currentValue in values:
                    if currentValue == value.value:
                       index = values.index(value.value)
                       count = counts[index]
                       count = count + 1
                       counts[index] = count
                       break
                    if currentValue == values[len(values)-1]:
                       values.append(value.value)
                       counts.append(1)'''
        return values, counts



class Data(object):

    isNumeric = False
    value = ""

    def __init__(self, data):

        newData = data.replace(".", "")
        newData = newData.replace(",", "")

        if newData.isdigit():
            self.isNumeric = True
            self.value = float(data)
        else:
            self.isNumeric = False
            self.value = str(data)
            