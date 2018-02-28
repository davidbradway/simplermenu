class SimplerMenu(object):
    """
    """

    def __init__(self):
        pass

    def loadDictFromJSON(self, filename = 'fancy.json'):
        import json

        with open(filename) as json_data:
            self.d = json.load(json_data)

    def getRandomFancyPhrase(self):
        from random import randint

        d_keys = [*self.d]
        self.fancy_phrase = " ".join([d_keys[randint(0, len(d_keys))],
                                d_keys[randint(0, len(d_keys))],
                                d_keys[randint(0, len(d_keys))],
                                d_keys[randint(0, len(d_keys))],
                                d_keys[randint(0, len(d_keys))]])

    def makeSimpler(self):
        import re
        pattern = re.compile(r'\b(' + '|'.join(self.d.keys()) + r')\b')
        self.result = pattern.sub(lambda x: self.d[x.group()], self.fancy_phrase)

if __name__=="__main__":
    myMenu = SimplerMenu()
    myMenu.loadDictFromJSON()
    myMenu.getRandomFancyPhrase()
    myMenu.makeSimpler()
    print("{} --> {}".format(myMenu.fancy_phrase, myMenu.result))
