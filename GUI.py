from Tkinter import *

from main import main
from generatore2 import Generatore


class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.generate = Button(self)
        self.generate["activebackground"] = "white"
        self.generate["highlightcolor"] = "yellow"
        self.generate["text"] = "Genera dei nuovi casi"
        self.generate["justify"] = "center"
        self.generate["command"] = Generatore
        self.choosegen = Checkbutton(self)
        self.choosegen["text"] = "Genera 50 casi random"
        self.choosegen["variable"] = C1
        self.choosegen["onvalue"] = 1
        self.choosegen["offvalue"] = 0
        self.choosegen.pack({"side": "right"})

        self.generate.pack({"side": "left"})

        self.QUIT = Button(self)
        self.QUIT["text"] = "Chiudi"
        self.QUIT["fg"] = "red"
        self.QUIT["bg"] = "blue"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "right"})

        self.resolve = Button(self)
        self.resolve["text"] = "Risolvi"
        self.resolve["command"] = main(open("input2.txt"))
        self.resolve.pack({"side": "right"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()