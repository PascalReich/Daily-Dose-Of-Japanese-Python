#Libraries
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

#Get Kanjis Meanings
def GetKanjiMeanings(kanjis):
    allMeanings = []
    for kanji in tqdm(kanjis):   
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

#Get Readings
def GetKanjiReadings(kanjis):
    allReadings = []
    for kanji in tqdm(kanjis):      
        kanjiURL = f"https://japonesbasico.com/kanji/{kanji}"
        kanjiRequest = requests.get(kanjiURL)
        #kanjiRequest.raise_for_status()

        soup = BeautifulSoup(kanjiRequest.text, "html.parser")

        #headingObjects = soup.find_all("h3")
        paragraph = soup.select("p")
        
        readings = paragraph[0].text

        end = readings.find("Lecturas japonesas")

        chineseReadings = ""
        japaneseReadings = ""
        
        e = 0
        for i in readings:
            if e > len("Lecturas chinas") and e < end:
                chineseReadings += i
            e += 1

        e = 0
        for i in readings:
            if e >= end + len("Lecturas japonesas: "):
                japaneseReadings += i
            e += 1

        allReadings.append([chineseReadings, japaneseReadings])

    return allReadings

#Get words with the kanjis
def GetKanjiExpamples(kanjis):
    allExamples = []
    for kanji in tqdm(kanjis):
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
    for kanji in tqdm(kanjis):

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
    for kanji in tqdm(kanjis):
        
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