from  tkinter import *
class Application(Frame):
	def _init_(self,master=None):
		Frame._init_(self,master)
		self.pack()
		self.createWidgets()

def createWidgets(self):
	self.helloLabel = Label(self,text='Hello,world!')
	self.helloLabel.pack()
	self.quitButton = Button(self,text='Quit',command=self.quit)
	self.quitButton.pack()