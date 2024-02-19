import json
import tkinter as tk
from PIL import Image, ImageTk



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, InfoPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            self.geometry("800x600")

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#6d81a3")
        self.controller = controller

        self.controller.title("Pieniondzex")
        self.controller.state("zoomed")
        self.controller.iconphoto(False, tk.PhotoImage(file="money.png"))


        head_label = tk.Label(self,
                              text="PIENIONDZEX",
                              font=("All Star Resort", 30, "bold"),
                              bg="#6d81a3")
        label1 = tk.Label(self, text="KALKULATOR WYDANYCH PIENIONSZKOW",
                          font=("Allstar", 20, "bold"),
                          bg= "#6d81a3",
                          fg="white")

        head_label.pack(side="top", fill="x", pady=100)
        label1.pack(pady=50)

        button1 = tk.Button(self, text="Zaczynamy!",
                            command=lambda: controller.show_frame("PageOne"), font=("All Star Resort", 18), bg="#E3CF57")
        info_button = tk.Button(self, text="Troche o Apce",
                            command=lambda: controller.show_frame("InfoPage"), font=("All Star Resort", 18), bg="#E3CF57")

        # exit_button = tk.Button(self,
        #                         text="Wyjdź",
        #                         font=("All Star Resort", 18),
        #                         bg="#E3CF57",
        #                         command=wyjdz)

        button1.pack()
        info_button.pack(pady= 30)
        # exit_button.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#6d81a3")
        self.controller = controller

        with open("Dane_do_Apki.json") as dane:
            dane1 = json.load(dane)

        zdjecie1 = Image.open("emotka.jpg")
        test = ImageTk.PhotoImage(zdjecie1)

        def click_jedzenie():
            try:
                dane1["jedzenie"].append(float(entry_jedzenie.get()))
            except ValueError:
                # zdjecie1 = Image.open("emotka.jpg")
                # test = ImageTk.PhotoImage(zdjecie1)
                errorpage = tk.Tk()
                errorpage.geometry("300x100")
                errorpage.title("Niepoprawne dane")
                lbl = tk.Label(errorpage,
                               text="TO NIE JEST LICZBA!",
                               font=("Arial", 18, "bold"),
                               fg="Black")
                # lbl1 = tk.Label(errorpage,
                #                 image=test,
                #                 height=60,
                #                 width=80)
                # lbl1.image = test
                lbl.pack()
                # lbl1.pack()
                errorpage.mainloop()
            with open("Dane_do_Apki.json", "w") as dane:
                json.dump(dane1, dane)
            entry_jedzenie.delete(0,tk.END)

        def click_zakupy():
            try:
                dane1["zakupy"].append(float(entry_zakupy.get()))
            except ValueError:
                # zdjecie1 = Image.open("emotka.jpg")
                # test = ImageTk.PhotoImage(zdjecie1)
                errorpage = tk.Tk()
                errorpage.geometry("300x100")
                errorpage.title("Niepoprawne dane")
                lbl = tk.Label(errorpage,
                               text="TO NIE JEST LICZBA!",
                               font=("Arial", 18, "bold"),
                               fg="Black")
                # lbl1 = tk.Label(errorpage,
                #                 image=test,
                #                 height=60,
                #                 width=80)
                # lbl1.image = test
                lbl.pack()
                # lbl1.pack()
                errorpage.mainloop()
            with open("Dane_do_Apki.json", "w") as dane:
                json.dump(dane1, dane)
            entry_zakupy.delete(0, tk.END)



        def click_alkohol():
            try:
                dane1["alkohol"].append(float(entry_alkohol.get()))
            except ValueError:
                # zdjecie1 = Image.open("emotka.jpg")
                # test = ImageTk.PhotoImage(zdjecie1)
                errorpage = tk.Tk()
                errorpage.geometry("300x100")
                errorpage.title("Niepoprawne dane")
                lbl = tk.Label(errorpage,
                               text="TO NIE JEST LICZBA!",
                               font=("Arial", 18, "bold"),
                               fg="Black")
                # lbl1 = tk.Label(errorpage,
                #                 image=test,
                #                 height=60,
                #                 width=80)
                # lbl1.image = test
                lbl.pack()
                # lbl1.pack()
                errorpage.mainloop()
            with open("Dane_do_Apki.json", "w") as dane:
                json.dump(dane1, dane)
            entry_alkohol.delete(0, tk.END)


        def click_inne():
            try:
                dane1["inne"].append(float(entry_inne.get()))
            except ValueError:
                # zdjecie1 = Image.open("emotka.jpg")
                # test = ImageTk.PhotoImage(zdjecie1)
                errorpage = tk.Tk()
                errorpage.geometry("300x100")
                errorpage.title("Niepoprawne dane")
                lbl = tk.Label(errorpage,
                               text="TO NIE JEST LICZBA!",
                               font=("Arial", 18, "bold"),
                               fg="Black")
                # lbl1 = tk.Label(errorpage,
                #                 image=test,
                #                 height=60,
                #                 width=80)
                # lbl1.image = test
                lbl.pack()
                # lbl1.pack()
                errorpage.mainloop()
            with open("Dane_do_Apki.json", "w") as dane:
                json.dump(dane1, dane)
            entry_inne.delete(0, tk.END)


        instrukcja = tk.Label(self,
                              bg="#6d81a3",
                              text="W ODPOWIEDNIE MIEJSCE WPISZ NA CO POSZŁY TWOJE PIENIONSZKI",
                              font=("Arial", 22, "bold"),
                              fg="White")
        cala_suma_napis = tk.Label(self,
                             bg="#6d81a3",
                             text="CAŁA SUMA",
                             font=("Allstar", 20, "bold"),
                             fg="Black"
                             )
        sumy = tk.Label(self,
                        text="SUMY",
                        bg="#6d81a3",
                        font=("Allstar", 20, "bold"),
                        fg="Black")
        jedzenie = tk.Label(self,
                            text="JEDZENIE",
                            font=("Allstar", 17, "bold"),
                            bg="#6d81a3",
                            fg="White")
        zakupy_spozywcze = tk.Label(self,
                            text="ZAKUPY SPOZYWCZE",
                            font=("Allstar", 17, "bold"),
                            bg="#6d81a3",
                            fg="White")

        alkohol = tk.Label(self,
                            text="ALKOHOL",
                            font=("Allstar", 17, "bold"),
                            bg="#6d81a3",
                            fg="White")
        inne_rzeczy = tk.Label(self,
                            text="INNE RZECZY",
                            font=("Allstar", 17, "bold"),
                            bg="#6d81a3",
                            fg="White")


        entry_jedzenie = tk.Entry(self,
                                  borderwidth=4,
                                  width=40)
        entry_zakupy = tk.Entry(self,
                                borderwidth=4,
                                width=40)
        entry_alkohol = tk.Entry(self,
                                 borderwidth=4,
                                 width=40)
        entry_inne = tk.Entry(self,
                              borderwidth=4,
                              width=40)

        btn_jedzenie = tk.Button(self,
                                 bg="#E3CF57",
                                 font=("All Star Resort", 10),
                                 text=">>",
                                 command=click_jedzenie)
        btn_zakupy = tk.Button(self,
                              bg="#E3CF57",
                              font=("All Star Resort", 10),
                              text=">>",
                              command=click_zakupy)
        btn_alkohol = tk.Button(self,
                                 bg="#E3CF57",
                                 font=("All Star Resort", 10),
                                 text=">>",
                                command=click_alkohol)
        btn_inne = tk.Button(self,
                                 bg="#E3CF57",
                                 font=("All Star Resort", 10),
                                 text=">>",
                                command=click_inne)

        back_button = tk.Button(self,
                                text="Wróć",
                                font=("All Star Resort", 18), bg="#E3CF57",
                                width=15,
                                command=lambda: controller.show_frame("StartPage"))


        # SUMY
        suma_jedzenie_zmienna = 0
        suma_zakupy_zmienna = 0
        suma_alkohol_zmienna = 0
        suma_inne_zmienna = 0
        for i in dane1["jedzenie"]:
            suma_jedzenie_zmienna += i
        for j in dane1["zakupy"]:
            suma_zakupy_zmienna += j
        for k in dane1["alkohol"]:
            suma_alkohol_zmienna += k
        for l in dane1["inne"]:
            suma_inne_zmienna += l
        suma_cala_zmienna = suma_jedzenie_zmienna + suma_zakupy_zmienna + suma_alkohol_zmienna + suma_inne_zmienna

        suma_jedzenie = tk.Label(self,
                                 text=suma_jedzenie_zmienna,
                                 width=15,
                                 height=1,
                                 relief="solid")
        suma_zakupy = tk.Label(self,
                               text=suma_zakupy_zmienna,
                               width=15,
                               height=1,
                               relief="solid")
        suma_alkohol = tk.Label(self,
                                text=suma_alkohol_zmienna,
                                width=15,
                                height=1,
                                relief="solid")
        suma_inne = tk.Label(self,
                             text=suma_inne_zmienna,
                             width=15,
                             height=1,
                             relief="solid")
        cala_suma = tk.Label(self,
                             text=suma_cala_zmienna,
                             width=17,
                             height=2,
                             relief="raised",
                             bg="#E3CF57")




        instrukcja.pack()

        cala_suma_napis.pack()
        cala_suma_napis.place(x=1485, y=115)

        sumy.pack()
        sumy.place(x=615, y=115)

        suma_jedzenie.pack()
        suma_jedzenie.place(x=600, y=150)

        suma_zakupy.pack()
        suma_zakupy.place(x=600, y=300)

        suma_alkohol.pack()
        suma_alkohol.place(x=600, y=450)

        suma_inne.pack()
        suma_inne.place(x=600, y=600)

        cala_suma.pack()
        cala_suma.place(x=1500, y=150)

        jedzenie.pack()
        jedzenie.place(x=160, y=120)

        entry_jedzenie.pack()
        entry_jedzenie.place(x=100, y= 150)

        btn_jedzenie.pack()
        btn_jedzenie.place(x=360, y= 150)

        zakupy_spozywcze.pack()
        zakupy_spozywcze.place(x=106, y=270)

        entry_zakupy.pack()
        entry_zakupy.place(x=100, y=300)

        btn_zakupy.pack()
        btn_zakupy.place(x=360, y=300)

        alkohol.pack()
        alkohol.place(x=170, y=420)

        entry_alkohol.pack()
        entry_alkohol.place(x=100, y=450)

        btn_alkohol.pack()
        btn_alkohol.place(x=360, y=450)

        inne_rzeczy.pack()
        inne_rzeczy.place(x=150, y=570)

        entry_inne.pack()
        entry_inne.place(x=100, y=600)

        btn_inne.pack()
        btn_inne.place(x=360, y=600)

        back_button.pack()
        back_button.place(x=830, y=900)



class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#6d81a3")
        self.controller = controller

        zdjecie = Image.open(r"C:\Users\kunik\Apka\Kalkulator_wydatk-w\deszcz_pieniedzy.jpg")
        test = ImageTk.PhotoImage(zdjecie)

        empty_label = tk.Label(self,
                                height=4,
                                bg="#6d81a3")
        empty_label.pack()
        opis = tk.Label(self,
                        text="Apka ma nam pomóc w zliczaniu wydanych pieniążków,",
                        bg="#6d81a3",
                        fg="White",
                        font=("All Star Resort", 20, "bold"))
        opis2 = tk.Label(self,
                         text="ale głównie jest po to by uświadomić nas o tym,",
                         bg="#6d81a3",
                         fg="White",
                         font=("All Star Resort", 20, "bold"))
        opis3 = tk.Label(self,
                         text="na co ląduja nasze pieniążki :)",
                         bg="#6d81a3",
                         fg="White",
                         font=("All Star Resort", 20, "bold"))
        photo_opis = tk.Label(self,
                              text="A tak bedą wyglądać osoby korzystające z apki:",
                              bg="#6d81a3",
                              fg="Black",
                              font=("All Star Resort", 20, "bold"))
        empty_label2 = tk.Label(self,
                               height=2,
                               bg="#6d81a3")
        photo = tk.Label(self,
                         image=test,
                         height=400,
                         width=400)
        photo.image = test
        back_button = tk.Button(self,
                                text="Wróć",
                                font=("All Star Resort", 18),
                                bg="#E3CF57",
                                width=15,
                                command=lambda: controller.show_frame("StartPage"))

        opis.pack(pady=20)
        opis2.pack(pady=20)
        opis3.pack(pady=20)
        empty_label2.pack()
        photo_opis.pack(pady=20)
        photo.pack(pady=40)
        back_button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()