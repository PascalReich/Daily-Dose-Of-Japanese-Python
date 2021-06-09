#Libraries
import PREFS
from bs4 import BeautifulSoup

class KanjisEs(object):
	"""docstring for KanjisEs"""
	def __init__(self):
		super(KanjisEs, self).__init__()

		hispadicData = lambda: self.ReadHispadicData()
		kanjidicData = lambda: self.ReadKanjiDicData()

		self.hispadicPrefs = PREFS.PREFS(hispadicData, filename="Prefs/hispadicPrefs", interpret=True)
		self.kanjidicPrefs = PREFS.PREFS(kanjidicData, filename="Prefs/kanjidicPrefsEs", interpret=True)

	def ReadHispadicData(self): #Read hispadic.utf8 file and return it as dictionary
		result = {}

		file = open("Data/hispadic.utf8", "r")
		lines = file.readlines()

		for line in lines:
			line = line.strip()
			#Ignore comments
			if line[0] == "#": continue
			###

			if line[-1] != "/": line += "/"
			
			# print(line)
			line1 = line.split("/")


			if line1[-1].strip() == "\n": line1.pop(-1)
			if line1[-1].strip() == "": line1.pop(-1)
			
			if "[" in line1[0] and "]" in line1[0]:
				line1[0] = line1[0].split("[")
				result[line1[0][0].strip()] = {line1[0][1].strip()[:-1]: line1[1:]}
			else:
				result[line1[0].strip()] = {line1[0].strip(): line1[1:]}


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

			meanings = [a.get_text(strip=True) for a in i.find_all("meaning", m_lang="es")]
			if meanings == []:
				meanings = [a.get_text(strip=True) for a in i.find_all("meaning")]
				meanings.append("No encontrado en español")

			grade = self.TryEmpty(lambda: i.find("grade").get_text(strip=True))

			jlpt = self.TryEmpty(lambda: i.find("jlpt").get_text(strip=True))
			
			result[kanjiName] = {"On": on, "Kun": kun, "Meanings": meanings, "Strokes": strokes, "Grade": grade, "JLPT": jlpt}


		return result

	def FindWordsWith(self, kanji): # Find words with some specific kanji
		result = {}
		e = 0
		for i in self.hispadicPrefs.ReadPrefs().items():
			if e > 16: break
			
			if kanji in i[0]:
				result[i[0]] = i[1]

				e += 1

		return result

	def GetKanjiInformation(self, kanji):
		result = {}

		kanjiData = self.kanjidicPrefs.ReadPrefs()[kanji]
		kanjiExamples = self.FindWordsWith(kanji)

		kanjiData["Examples"] = kanjiExamples

		result = kanjiData

		return result

def GetKanjisInformation(kanjis):
	kanji = KanjisEs()
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

# kanji = KanjisEs()
# result = GetKanjisInformation("劾")
# readings = GetKanjisReadings(result)

# print(readings)