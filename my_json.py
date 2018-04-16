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
        self.fancy_phrase = " ".join([d_keys[randint(0, len(d_keys)-1)],
                                d_keys[randint(0, len(d_keys)-1)],
                                d_keys[randint(0, len(d_keys)-1)],
                                d_keys[randint(0, len(d_keys)-1)]])

    def makeSimpler(self):
        import re
        pattern = re.compile(r'\b(' + '|'.join(self.d.keys()) + r')\b')
        self.result = pattern.sub(lambda x: self.d[x.group()], self.fancy_phrase)

def main():
    myMenu = SimplerMenu()
    myMenu.loadDictFromJSON()
    myMenu.getRandomFancyPhrase()
    myMenu.makeSimpler()
    print("{} --> {}".format(myMenu.fancy_phrase, myMenu.result))

    myMenu.loadDictFromJSON("sample_response.json")
    label = myMenu.d['responses'][0]['textAnnotations'][0]['description']
            #"OCTOBER 11, 2008\nPenQ\nPeggy e Michael\nCO GADI\nMENU\nPassed Hors d'Oeuvres\nPAN-SEARED CRAB CAKES\nSERVED WITH A CAJUN REMOULADE\nROASTED BEEF WELLINGTONS\nSERVED WITH A RED WINE DEMI GLAZE\nSEARED AHI TUNA WONTONS\nWITH A WASABI DRIZZLE\nSMOKED DUCK BREAST\nWITH A COGNAC INFUSED APRICOT CHUTNEY\nSalad\nHOUSE SALAD SERVED WITH RANCH DRESSING\nEntrée\nCHAR GRILLED FILET MIGNON WITH MAYTAG BLUE CHEESE\nINFUSED MASHED POTATO, SAUTEED ASPARAGUS\nAND A CABERNET DEMI GLAZE\nDessert\nWEDDING CAKE\nDESSERT BAR\n",
    print(label)

    import spacy
    nlp = spacy.load('en')
    doc = nlp(label.lower())
    for token in doc:
        if (token.pos_ != 'ADJ'):
            print(token.text, end=' ')
            #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            #      token.shape_, token.is_alpha, token.is_stop)

if __name__=="__main__":
    main()