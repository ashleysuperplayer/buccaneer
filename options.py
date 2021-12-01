import os
import butils

class OptionsHandler:
    def __init__(self):

        # the default options
        self.options: dict[str, str] = {"CJWPopupConfirmation": "0",
                                        "DefaultHeight":      "500",
                                        "DefaultWidth":       "500"}

        # replace defaults with values from cfg, if they exist
        self.options.update(self.initOptions())

    def initOptions(self) -> dict[str, str]:
        """Read the options from the 'options.cfg' file."""
        options: dict[str, str] = {}
        if os.path.exists("options.cfg"):
            with open("options.cfg", "r") as optionLines:
                for line in optionLines:
                    lineComponents: list[str] = validateOption(line) # clean and split line; returns like ["option", "value"]
                    options[lineComponents[0]] = lineComponents[1]
        return options

def validateOption(optionLine: str) -> list[str]:
    """Takes a raw string from a configuration file and converts it to a [str, str] KVP"""
    # TODO: options with integral value?
    # TODO: arbitrary options are possible to be set; problem?

    # "  ab  = cd ## ef" |-> ["  ab  ", " cd "]
    optionparts = butils.removeComments(optionLine).split("=")

    # ["  ab  ", " cd "] |-> ["ab", "cd"]
    optionparts = [butils.removeWhitespace(optionpart) for optionpart in optionparts]
    return optionparts

def splitOption(s: str) -> list[str]:
    return s.split("=")

#TESTING
def testOptions() -> None:
    optionsHandler = OptionsHandler()
    optionsHandler.initOptions()
    #optionsHandler.checkKeys()
