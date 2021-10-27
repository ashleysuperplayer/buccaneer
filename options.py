
import os
import butils

class OptionsHandler:
    def __init__(self):
        self.options = initOptions()

    def initOptions():
        self.options = {}
        with open('options.cfg') as optionLines:
            for line in optionLines:
                lineComponents = validateOption(line)
                self.options[lineComponents[0]] = lineComponents[1]

    def validateOption(optionLine):
        return splitOption(butils.noWhitespace(butils.noComments(optionLine)))

    def splitOption(string):
        return string.split("=")