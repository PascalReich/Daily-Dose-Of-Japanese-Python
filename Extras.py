import tkinter
import datetime

def Font(font, fontSize, fontWeight, fontSlant):
		font_ = f"{font} {fontSize} {fontWeight} {fontSlant}"
		return font_
		
def destroy(widget, type = "place"):
	if type == "place":
		widget.place_forget()
	elif type == "pack":
		widget.pack_forget()
	elif type == "grid":
		widget.grid_forget()

# Calculate the days between two dates
def DaysBetween(d1, d2):
	d1 = datetime.datetime.strptime(d1, "%Y/%m/%d")
	d2 = datetime.datetime.strptime(d2, "%Y/%m/%d")
	return abs((d2 - d1).days)

def CreateBox(screenSize, width, height, num):
	box = []

	xCap = screenSize[0] // width // 2
	yCap = (num // xCap) + 1


	e = 0
	for y in range(yCap):
		for x in range(xCap):
			box.append((x, y))
			
			e += 1
			if e >= num: break
		if e >= num: break

	# print(box)
	# print(f"X: {xCap}--Y: {yCap}")
	# print(f"Actual: {len(box)}--Ideal: {num}")

	return box

listStr = lambda x: ", ".join(map(str, x))

class EntryWithPlaceholder(tkinter.Entry):
	def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
		super().__init__(master)

		self.placeholder = placeholder
		self.placeholder_color = color
		self.default_fg_color = self['fg']
		self.focIn = False

		self.bind("<FocusIn>", self.foc_in)
		self.bind("<FocusOut>", self.foc_out)

		self.put_placeholder()

		vcmd = (self.master.register(self.callback))
		self["validate"] = "all"
		self["validatecommand"] = (vcmd, "%P")

	def put_placeholder(self):
		self.insert(0, self.placeholder)
		self['fg'] = self.placeholder_color

	def foc_in(self, *args):
		self.focIn = True
		if self['fg'] == self.placeholder_color:
			self.delete('0', 'end')
			self['fg'] = self.default_fg_color

	def foc_out(self, *args):
		self.focIn = False

		if not self.get():
			self.put_placeholder()

	def callback(self, P):
		if str.isdigit(P) or P == "":
			return True
		else:
			return False

class VerticalScrolledFrame(tkinter.Frame):
	"""A pure Tkinter scrollable frame that actually works!

	* Use the 'interior' attribute to place widgets inside the scrollable frame
	* Construct and pack/place/grid normally
	* This frame only allows vertical scrolling
	"""
	def __init__(self, parent, *args, **kw): #Arguemnts
		tkinter.Frame.__init__(self, parent, *args, **kw) #Arguments            

		parent.update() #Update the parent for get the correct size

		# create a self.canvas object and a vertical scrollbar for scrolling it
		self.vscrollbar = tkinter.Scrollbar(self, orient=tkinter.VERTICAL)
		self.vscrollbar.pack(fill=tkinter.Y, side=tkinter.RIGHT, expand=tkinter.FALSE)
		self.canvas = tkinter.Canvas(self, bd=0, highlightthickness=0, yscrollcommand=self.vscrollbar.set, height=parent.winfo_height(), width=parent.winfo_width())
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))
		
		self.canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.TRUE)
		self.vscrollbar.config(command=self.canvas.yview)

		# reset the view
		self.canvas.xview_moveto(0)
		self.canvas.yview_moveto(0)

		# create a frame inside the self.canvas which will be scrolled with it
		self.interior = interior = tkinter.Frame(self.canvas)
		interior_id = self.canvas.create_window(0, 0, window=interior,
										   anchor=tkinter.NW)
		
		# track changes to the self.canvas and frame width and sync them,
		# also updating the scrollbar
		def _configure_interior(event):
			# update the scrollbars to match the size of the inner frame
			size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
			self.canvas.config(scrollregion="0 0 %s %s" % size)
			
			if interior.winfo_reqwidth() != self.canvas.winfo_width():
				# update the self.canvas's width to fit the inner frame
				self.canvas.config(width=interior.winfo_reqwidth())

		interior.bind('<Configure>', _configure_interior)

		def _configure_canvas(event):
			if interior.winfo_reqwidth() != self.canvas.winfo_width():
				# update the inner frame's width to fill the self.canvas
				self.canvas.itemconfigure(interior_id, width=self.canvas.winfo_width())
		self.canvas.bind('<Configure>', _configure_canvas)

class HorizontalScrolledFrame(tkinter.Frame):
	"""A pure Tkinter scrollable frame that actually works!

	* Use the 'interior' attribute to place widgets inside the scrollable frame
	* Construct and pack/place/grid normally
	* This frame only allows vertical scrolling
	"""
	def __init__(self, parent, *args, **kw):
		tkinter.Frame.__init__(self, parent, *args, **kw)            

		parent.update()
		# create a self.canvas object and a vertical scrollbar for scrolling it
		self.vscrollbar = tkinter.Scrollbar(self, orient=tkinter.HORIZONTAL)
		self.vscrollbar.pack(fill=tkinter.Y, side=tkinter.RIGHT, expand=tkinter.FALSE)
		self.canvas = tkinter.self.canvas(self, bd=0, highlightthickness=0, xscrollcommand=self.vscrollbar.set, height=parent.winfo_height(), width=parent.winfo_width())
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))
		
		self.canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.TRUE)
		self.vscrollbar.config(command=self.canvas.xview)

		# reset the view
		self.canvas.xview_moveto(0)
		self.canvas.yview_moveto(0)

		# create a frame inside the self.canvas which will be scrolled with it
		self.interior = interior = tkinter.Frame(self.canvas)
		interior_id = self.canvas.create_window(0, 0, window=interior,
										   anchor=tkinter.NW)
		
		self.self.canvas = self.canvas

		# track changes to the self.canvas and frame width and sync them,
		# also updating the scrollbar
		def _configure_interior(event):
			# update the scrollbars to match the size of the inner frame
			size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
			self.canvas.config(scrollregion="0 0 %s %s" % size)
			if interior.winfo_reqwidth() != self.canvas.winfo_width():
				# update the self.canvas's width to fit the inner frame
				self.canvas.config(width=interior.winfo_reqwidth())

		interior.bind('<Configure>', _configure_interior)

		def _configure_canvas(event):
			if interior.winfo_reqwidth() != self.canvas.winfo_width():
				# update the inner frame's width to fill the self.canvas
				self.canvas.itemconfigure(interior_id, width=self.canvas.winfo_width())
		self.canvas.bind('<Configure>', _configure_canvas)

		def mousescroll(event):
			"""mouse wheel scroll callback"""
			# Divide the event.delta by some value to effect the scrolling speed
			self.canvas.view_scroll(int(-(event.delta/120)), "units")
		self.canvas.bind_all("<MouseWheel>", mousescroll)
