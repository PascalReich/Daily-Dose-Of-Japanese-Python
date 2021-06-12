#!/usr/bin/env python3
import kanjiGraphics  # Import script

if __name__ == "__main__":
	GRAPHICS = kanjiGraphics.Graphics(600, 600)  # Initialazing the program
	kanjiGraphics.MainPrefs.WritePrefs("compareDate", kanjiGraphics.datetime.date.today().strftime("%Y/%m/%d"))
