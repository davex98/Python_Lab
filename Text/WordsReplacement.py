def replaceWordsFromText(replaceMap, text: str):
    data = text.split()
    newText = []
    for c in data:
        if c in replaceMap.keys():
          c = replaceMap.get(c)
        newText.append(c)
    return newText

if __name__ == '__main__':
    replaceMap = {"and": "AAA",
                 "are": "BBB",
                 "of" : "CCC",
                 "as" : "DDD",
                 "the": "EEE",
                 "or" : "FFF"}
    text = replaceWordsFromText(replaceMap, open("graphics").read())
    print(text)