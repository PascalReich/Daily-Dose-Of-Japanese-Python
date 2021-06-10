#Libraries
import PREFS #Library to store information
from bs4 import BeautifulSoup #Library to read xml file
import time
from tqdm import tqdm

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

	def FindWordsWithKanjis(self, kanjis): # Find words with some specific kanji
		startTime = time.time()

		result = dict( (i, {}) for i in kanjis)

		e = 0
		for i in self.jmdictPrefs.ReadPrefs().items():
			if e > 16 * len(kanjis): break

			for kanji in kanjis:
				if kanji in i[0]:
					result[kanji][i[0]] = i[1]

					e += 1

		print(f"\n\n------------- {time.time() - startTime} seconds for {len(kanjis)} finding examples, average for each kanji {(time.time() - startTime) / len(kanjis)} -------------\n\n")
		return result

	def GetKanjiInformation(self, kanji, indivualWords = False):
		kanjiData = self.kanjidicPrefs.ReadPrefs()[kanji]
		if indivualWords:
			kanjiExamples = self.FindWordsWith(kanji)
			kanjiData["Examples"] = kanjiExamples

		result = kanjiData

		return result

def GetKanjisInformation(kanjis, indivualWords = False):
	startTime = time.time()
	kanji = KanjisEn()
	if not indivualWords: examples = kanji.FindWordsWithKanjis(kanjis)
	result = {}

	for i in tqdm(kanjis):
		result[i] = kanji.GetKanjiInformation(i, indivualWords=indivualWords)
		result[i]["Examples"] = examples[i]

	print(f"\n\n------------- {time.time() - startTime} seconds for {len(kanjis)} finding all info, average for each kanji {(time.time() - startTime) / len(kanjis)} -------------\n\n")
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

#kanji = KanjisEn()
#result = GetKanjisInformation("劾弾痕憂鬱")
# readings = GetKanjisReadings(result)

#print(result)