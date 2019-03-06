from datetime import datetime
import dateutil.parser
import pprint
from sys import argv

class ICSParser():
    def __init__(self, filename = None):
        self.filename = filename
        self.event = []
        if(filename != None):
            self.event = self.parse_ics()
        
    def parse_ics(self, filename = None):
        if filename == None:
            filename = self.filename
        event = []
        with open(filename, "r") as file:
            for line in file:
                line = line.strip().split(":", 1)
                if line[0] in ["URL", "DTSTART", "DTEND", "SUMMARY", "DESCRIPTION", "LOCATION"]:
                    if(len(line)==2):
                        event += [[line[0].lower(), line[1]]]
        return event
        
    def to_dict(self):
        event_dict = {}
        for E in self.event:
            if E[0] == "dtstart" or E[0] == "dtend":
                E[1] = dateutil.parser.parse(E[1])
            event_dict[E[0]] = E[1]
        return event_dict


# if __name__ == '__main__':
#     parser = ICSParser(argv[1])
#     pprint.pprint(parser.to_dict())
