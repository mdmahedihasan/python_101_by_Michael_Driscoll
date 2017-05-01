import tkinter as tk


class App():
    def __init__(self, parent):
        """constructor"""
        frame = tk.Frame(parent)
        frame.pack()

        btn22 = tk.Button(frame, text="22", command=lambda : self.printNum(22))
        btn22.pack(side=tk.LEFT)
        btn44 = tk.Button(frame, text="44", command=lambda : self.printNum(44))
        btn44.pack(side=tk.LEFT)

        quitBtn = tk.Button(frame, text="quit", fg="red", command=frame.quit)
        quitBtn.pack(side=tk.LEFT)

    def printNum(self, num):
        print("you passed the %s button" % num)


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()