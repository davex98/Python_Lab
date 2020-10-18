def removeWordsFromText(words, text: str):
    data = text.split()
    newText = []
    for c in data:
        if c not in words:
          newText.append(c)
    return newText

if __name__ == '__main__':
    blackList = ["and", "are", "of", "as", "the", "or"]
    text = removeWordsFromText(blackList, open("graphics").read())
    print(text)