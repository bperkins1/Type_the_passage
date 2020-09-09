from tkinter import *
from time import *
from textretriever import *
from calculations import *

class typetest:
	def __init__(self):
		#create all the widgets necessary for the typing test
		self.root = Tk()
		self.bg = 'light steel blue'
		self.root.configure(bg=self.bg)
		self.root.title("Typing Test")
		self.sample = find_sample()
		self.test = Label(self.root, text = self.sample, wraplength = 1100, bg=self.bg)
		self.test.config(font=("Times New Roman", 14))
		self.type = Text(self.root, state = DISABLED, height = 8, width = 50, wrap = WORD)
		self.start = Button(self.root, text="Begin", command = self.begin)
		self.finish = Button(self.root, text="Submit", command = self.submit, state = DISABLED)


	def display(self):
		#displays the widgets on screen
		self.root.geometry("1100x268+300+200")
		self.test.grid(row=0, column=0, padx=5)
		self.type.grid(row=1, column=0)
		self.start.grid(row=3, column=0,pady=5)
		self.finish.grid(row=4, column=0,pady=5)
		#3 line label causes ugliness

	def begin(self):
		#enable text entry and take time
		self.starttime = time()
		self.type.configure(state=NORMAL)
		self.start.configure(state=DISABLED)
		self.finish.configure(state=NORMAL)

		
	def submit(self):
		#disable further text entry,take time, and calculate info.
		self.endttime=time()
		self.finish.configure(state=DISABLED)
		self.type.configure(state=DISABLED)
		self.paragraph = self.type.get(1.0, END)
		time_to_type = self.endttime-self.starttime
		self.speed = calculate_wpm(self.paragraph, time_to_type)

		self.accuracy = accuracy(self.sample, self.paragraph)
		self.test_completed()

	def test_completed(self):
		#creates a new window displaying stats and option to start again.
		global new_root
		new_root = Tk()
		new_root.geometry("+310+250")
		new_root.title("Finish")
		color = "light cyan"
		new_root.configure(bg=color)
		speed = Label(new_root, text=f"You typed {self.speed} WPM", bg=color)
		accuracy = Label(new_root, text=f"You typed {self.accuracy}% of the words correctly", bg=color)
		new_button = Button(new_root, text="New test", command = self.repeat)
		quit_button = Button(new_root, text="Quit", command = self.quit)
		quit_button = Button(new_root, text="Quit", command = self.quit)
		go_to_book = Button(new_root, text="Read that book (opens web browser)", command = self.read_that_book)
		#Display the widgets
		speed.grid(row=0, column=0)
		accuracy.grid(row=1, column=0)
		new_button.grid(row=2, column=0, pady=3)
		quit_button.grid(row=3, column=0, pady=3)
		go_to_book.grid(row=4, column=0, pady=3, padx=5)
		
	def quit(self):
		#ends the program
		new_root.destroy()
		self.root.destroy()

	def repeat(self):
		#starts a new typetest
		typetest2 = typetest()
		typetest2.display()
		self.quit()
		
	def read_that_book(self):
		#opens the gutenberg URL of the book where the typing test came from
		if self.sample[0:18] == "To Sherlock Holmes":
			webbrowser.open("http://www.gutenberg.org/files/1661/1661-h/1661-h.htm")
		else:
			webbrowser.open(url)

