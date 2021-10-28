import os
import butils

dummyOptions = ('CJWPopupConfirmation', 'DefaultHeight', 'DefaultWidth')

class OptionsHandler:
    def __init__(self):
        self.options = self.initOptions()

    def initOptions(self):
        self.options = {}
        with open('options.cfg') as optionLines:
            for line in optionLines:
                lineComponents = validateOption(line)
                self.options[lineComponents[0]] = lineComponents[1]
                print(self.options[lineComponents[0]])

    def checkKeys(self):
        for dummyOption in dummyOptions:
            if not dummyOption in self.options.keys():
                print(dummyOption)
                self.options[dummyOption] = 0

def validateOption(optionLine):
    return splitOption(butils.removeWhitespace(butils.removeComments(optionLine)))

def splitOption(string):
    return string.split("=")

# optionsHandler = OptionsHandler() testing
# optionsHandler.initOptions()
# optionsHandler.checkKeys()