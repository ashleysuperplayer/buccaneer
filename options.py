import os
import butils

class OptionsHandler:
    def __init__(self):
        # defaults
        self.options = {'CJWPopupConfirmation': 0,
                        'DefaultHeight':        500,
                        'DefaultWidth':         500}

        # replace defaults with values from cfg, if they exist
        self.options.update(self.initOptions())

    def initOptions(self):
        options = {}
        with open('options.cfg', 'r') as optionLines:
            # each line in the cfg is a KVP separated by an '='
            for line in optionLines:
                lineComponents = validateOption(line)
                options[lineComponents[0]] = lineComponents[1]
        return options

def validateOption(optionLine):
    # TODO: options with integral value?
    # TODO: arbitrary options are possible to be set; problem?
    return splitOption(butils.removeWhitespace(butils.removeComments(optionLine)))

def splitOption(string):
    return string.split("=")

# optionsHandler = OptionsHandler() testing
# optionsHandler.initOptions()
# optionsHandler.checkKeys()
