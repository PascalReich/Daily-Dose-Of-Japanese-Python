#Libraries
import requests
from bs4 import BeautifulSoup

#Check if there are japanese characters
def CheckJapChar(string):
    # -*- coding:utf-8 -*-
    ranges = [
      {"from": ord(u"\u3300"), "to": ord(u"\u33ff")},         # compatibility ideographs
      {"from": ord(u"\ufe30"), "to": ord(u"\ufe4f")},         # compatibility ideographs
      {"from": ord(u"\uf900"), "to": ord(u"\ufaff")},         # compatibility ideographs
      {"from": ord(u"\U0002F800"), "to": ord(u"\U0002fa1f")}, # compatibility ideographs
      {'from': ord(u'\u3040'), 'to': ord(u'\u309f')},         # Japanese Hiragana
      {"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},         # Japanese Katakana
      {"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},         # cjk radicals supplement
      {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},
      {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},
      {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},
      {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},
      {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},
      {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}  # included as of Unicode 8.0
    ]

    def is_cjk(char):
      return any([range["from"] <= ord(char) <= range["to"] for range in ranges])

    def cjk_substrings(string):
      i = 0
      while i<len(string):
        if is_cjk(string[i]):
          start = i
          while is_cjk(string[i]): i += 1
          yield string[start:i]
        i += 1

    #string = string.decode("utf-8")
    for sub in cjk_substrings(string):
      string = string.replace(sub, "(" + sub + ")")
    return string

#Get Readings
def GetKanjiReadings(kanjis):
    allReadings = []
    for kanji in kanjis:      
        kanjiURL = f"https://jisho.org/search/{kanji} kanji"
        kanjiRequest = requests.get(kanjiURL)
        #kanjiRequest.raise_for_status()

        soup = BeautifulSoup(kanjiRequest.text, "html.parser")
        #headingObjects = soup.find_all("h3")
        #paragraph = soup.find("dl", {"class": "dictionary_entry on_yomi"})
        #paragraph = soup.find("div", {"id": "page_container"})
        #paragraph = soup.find("div", {"id": "main_results"})
        #paragraph = soup.find("div", {"id": "result_area"})
        paragraph = soup.find_all(class_ = "kanji-details__main-readings-list")


        #paragraph = paragraph.prettify()

        #text = soup.find_all(text=True)
        
        chineseReadings = ""
        japaneseReadings = ""

        e = 0
        print(paragraph)#.get_text())

        allReadings.append([chineseReadings, japaneseReadings])
        
    #print(allReadings)
    return allReadings

#Get Kanjis Meanings
def GetKanjiMeanings(kanjis):
    allMeanings = []
    for kanji in kanjis:   
        kanjiURL = f"https://japonesbasico.com/kanji/{kanji}"
        kanjiRequest = requests.get(kanjiURL)
        ##kanjiRequest.raise_for_status()

        soup = BeautifulSoup(kanjiRequest.text, "html.parser")

        headingObjects = soup.find_all("h3")
        paragraph = soup.select("p")
        
        meanings = []
        
        e = 0
        for i in headingObjects:
            meanings.append(i.text)
            e += 1

        allMeanings.append(meanings)
    return allMeanings

#Get words with the kanjis
def GetKanjiExpamples(kanjis):
    allExamples = []
    for kanji in kanjis:
        kanjiURL = f"https://japonesbasico.com/kanji/{kanji}"
        kanjiRequest = requests.get(kanjiURL)
        #kanjiRequest.raise_for_status()

        soup = BeautifulSoup(kanjiRequest.text, "html.parser")

        #headingObjects = soup.find_all("h3")
        paragraph = soup.select("p")

        examples = []

        word = ""
        words = []

        meaning = ""
        meanings = []
        
        e = 0
        for i in paragraph:
            if e > 2:
                examples.append(paragraph[e].text)
            e += 1
        
        e = 0
        wordsCount = 0
        for example in examples:
            #print(example)
            E = 0
            done = False
            word = ""
            for letter in example:
                if letter != " " and done == False and wordsCount < 15:
                    word += letter
                elif letter == " ":
                    done = True

                E += 1
            words.append(word)
            wordsCount += 1
            e += 1

        allExamples.append(words)
    return allExamples

def GetKanjiExampleReadings(kanjis):
    allExampleReadings = []
    for kanji in kanjis:

        kanjiURL = f"https://japonesbasico.com/kanji/{kanji}"
        kanjiRequest = requests.get(kanjiURL)
        #kanjiRequest.raise_for_status()

        soup = BeautifulSoup(kanjiRequest.text, "html.parser")

        #headingObjects = soup.find_all("h3")
        paragraph = soup.select("p")

        examples = []

        reading = ""
        readings = []
        
        e = 0
        for i in paragraph:
            if e > 2:
                examples.append(paragraph[e].text)
            e += 1
        
        e = 0
        wordsCount = 0
        for example in examples:
            #print(example)
            E = 0
            done = True
            reading = ""
            for letter in example:
                if letter == "(":
                    done = False
                elif done == False and wordsCount < 15:
                    if letter != ")":
                        reading += letter
                    else:
                        done = True
                        break

                E += 1
            readings.append(reading)
            wordsCount += 1
            e += 1

        allExampleReadings.append(readings)
    return allExampleReadings

##Get example words meaning with the notes (the parentesis after the reading) of the kanji
def GetKanjiExampleMeaning(kanjis, ):
    allExampleMeanings = []
    kanjiCount = 0
    for kanji in kanjis:
        
        kanjiURL = f"https://japonesbasico.com/kanji/{kanji}"
        kanjiRequest = requests.get(kanjiURL)
        #kanjiRequest.raise_for_status()

        soup = BeautifulSoup(kanjiRequest.text, "html.parser")

        #headingObjects = soup.find_all("h3")
        paragraph = soup.select("p")

        examples = []

        meaning = ""
        meanings = []
        
        e = 0
        for i in paragraph:
            if e > 2:
                examples.append(paragraph[e].text)
            e += 1
        
        wordsCount = 0
        for example in examples:
            #print(example)
            a = 0
            e = 0
            meaning = ""
            for letter in example:
                if a > 0:
                    if wordsCount < 15:
                        meaning += letter
                    else:
                        break
                if letter == ")":
                    a += 1
                e += 1

            meanings.append(meaning)
            wordsCount += 1

        allExampleMeanings.append(meanings)
    return allExampleMeanings