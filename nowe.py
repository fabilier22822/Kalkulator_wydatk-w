import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Frame Navigation")
        self.geometry("800x600")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for F in (StartPage, SecondPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="This is the Start Page")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Go to Second Page",
                           command=lambda: controller.show_frame(SecondPage))
        button.pack()


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="This is the Second Page")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Go to Start Page",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
