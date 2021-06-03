import kanjiGraphics #Import script

GRAPHICS = kanjiGraphics.Graphics(600, 600)
kanjiGraphics.MainPrefs.WritePrefs("compareDate", kanjiGraphics.datetime.date.today().strftime("%Y/%m/%d"))