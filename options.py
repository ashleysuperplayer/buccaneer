import os
import butils

class OptionsHandler:
    def __init__(self):
        self.options = self.initOptions()

    def initOptions(self):
        self.options = {}
        with open('/home/slater/store/coding/buccaneer/options.cfg') as optionLines:
            for line in optionLines:
                lineComponents = validateOption(line)
                self.options[lineComponents[0]] = lineComponents[1]
                print(self.options[lineComponents[0]])


def validateOption(optionLine):
    return splitOption(butils.removeWhitespace(butils.removeComments(optionLine)))

def splitOption(string):
    return string.split("=")

wagwan = OptionsHandler()
wagwan.initOptions()