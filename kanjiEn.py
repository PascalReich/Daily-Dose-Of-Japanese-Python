#Libraries
import PREFS #Library to store information
from bs4 import BeautifulSoup #Library to read xml file

class KanjisEn(object):
	"""docstring for KanjisEs"""
	def __init__(self):
		super(KanjisEn, self).__init__()

		jmdictPrefs = lambda: self.ReadJMdictData()
		kanjidicData = lambda: self.ReadKanjiDicData()

		self.jmdictPrefs = PREFS.PREFS(jmdictPrefs, filename="Prefs/jmdictPrefs", interpret=True)
		self.kanjidicPrefs = PREFS.PREFS(kanjidicData, filename="Prefs/kanjidicPrefsEn", interpret=True)

	def ReadJMdictData(self): #Reading JMdict_e.xml and filtering the information that i need
		with open("Data/JMdict_e.xml", "r") as f:
		    data = f.read() #Reading

		Data = BeautifulSoup(data, "xml")

		kanjis = Data.find_all("entry") #Getting all entries which are where the words are stored

		result = {}

		for i in kanjis:
			word = self.TryEmpty(lambda: i.find("keb").get_text(strip=True)) #Finding the word
			if word == None or not isinstance(word, str): continue #If the word is null ignore this iteration

			readings = self.TryEmpty(lambda: i.find("reb").get_text(strip=True))# Getting the word reading [self.TryEmpty(lambda: a.get_text(strip=True)) for a in i.find_all("reb")]
			meanings = [self.TryEmpty(lambda: a.get_text(strip=True)) for a in i.find_all("gloss")] #Getting the meanings
			extra = [self.TryEmpty(lambda: a.get_text(strip=True)) for a in i.find_all("xref")] 
			if extra != [] or len(extra) != 0:
				extra[0] = "(" + extra[0]
				extra[-1] = extra[-1] + ")"
			else:
				extra = []

			# print(f"-----{word}-----")
			result[word] = {readings: meanings + extra}


		return result

	def TryEmpty(self, func): # Return the value if it's possible and empty if except
		try:
			result = func()
		except AttributeError:
			result = None

		return result

	def ReadKanjiDicData(self):
		with open("Data/kanjidic2.xml", "r") as f:
		    data = f.read()

		Data = BeautifulSoup(data, "xml")

		kanjis = Data.find_all("character")

		result = {}

		for i in kanjis:
			kanjiName = self.TryEmpty(lambda: i.find("literal").get_text(strip=True))

			on = [a.get_text(strip=True) for a in i.find_all("reading", r_type="ja_on")]

			kun = [a.get_text(strip=True) for a in i.find_all("reading", r_type="ja_kun")]
			
			strokes = self.TryEmpty(lambda: i.find("stroke_count").get_text(strip=True))

			meanings = [a.get_text(strip=True) for a in i.find_all("meaning", m_lang=False)]

			grade = self.TryEmpty(lambda: i.find("grade").get_text(strip=True))

			jlpt = self.TryEmpty(lambda: i.find("jlpt").get_text(strip=True))
			
			result[kanjiName] = {"On": on, "Kun": kun, "Meanings": meanings, "Strokes": strokes, "Grade": grade, "JLPT": jlpt}


		return result

	def FindWordsWith(self, kanji): # Find words with some specific kanji
		result = {}
		e = 0
		for i in self.jmdictPrefs.ReadPrefs().items():
			if e > 16: break

			if kanji in i[0]:
				result[i[0]] = i[1]

				e += 1

		return result

	def GetKanjiInformation(self, kanji):
		kanjiData = self.kanjidicPrefs.ReadPrefs()[kanji]
		kanjiExamples = self.FindWordsWith(kanji)

		kanjiData["Examples"] = kanjiExamples

		result = kanjiData

		return result

def GetKanjisInformation(kanjis):
	kanji = KanjisEn()
	result = {}

	for i in kanjis:
		result[i] = kanji.GetKanjiInformation(i)

	return result


def GetKanjisMeanings(data):
	return [data[i]["Meanings"] for i in list(data)]

def GetKanjisReadings(data):
	return [(data[i]["On"], data[i]["Kun"]) for i in list(data)]

def GetExampleWords(data):
	examples = [data[i]["Examples"] for i in list(data)]	
	result = []

	for kanji in examples:
		result.append(list(kanji))

	# result = [j for i in result for j in i]
	return result

def GetExampleReadings(data):
	examples = [data[i]["Examples"] for i in list(data)]
	result = []

	e = 0
	for kanji in examples:
		result.append([])
		for word in kanji.items():
			for i in word[1].items():
				result[e].append(i[0])
		e += 1

	return result

def GetExampleMeanings(data):
	examples = [data[i]["Examples"] for i in list(data)]
	result = []

	e = 0
	for kanji in examples:
		result.append([])
		for word in kanji.items():
			for i in word[1].items():
				result[e].append(i[1])
		e += 1
	return result		

# kanji = KanjisEn()
# result = GetKanjisInformation("劾")
# readings = GetKanjisReadings(result)

# print(readings)