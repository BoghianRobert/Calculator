from tkinter import *
# pentru combobox
from tkinter import ttk
import tkinter.messagebox


def raise_frame(frame):
    frame.tkraise()


root = Tk()
root.title("Calculator")
root.iconbitmap('calculator.ico')
root.geometry("500x300")

f1 = Frame(root, width=500, height=300, bg='grey')
f1.place(x=0, y=0)
f2 = Frame(root, width=500, height=300, bg='grey')
f2.place(x=0, y=0)



nume = Label(f1, text="Nume", fg='black', bg='grey')
parola = Label(f1, text="Parola", fg='black', bg='grey')
nume.place(x=180, y=108)
parola.place(x=180, y=134)



nume_entry = Entry(f1)
parola_entry = Entry(f1, show="*")
nume_entry.place(x=230, y=108)
parola_entry.place(x=230, y=134)


# buton verificare

def verificare():
    nume_introdus = nume_entry.get()
    if nume_introdus == "":
        tkinter.messagebox.showinfo("Mesaj", "Introduceti un nume de utilizator")
    else:
        parola_introdusa = parola_entry.get()
        if parola_introdusa == 'parola':
            nume_utilizator = nume_entry.get()
            name_tag = Text(f2, width=20, height=1, font='Helvetica 10 normal', bg='grey')
            name_tag.insert(END, nume_utilizator)
            name_tag.place(x=10, y=10)
            raise_frame(f2)
            parola_entry.delete(0, "end")
        else:
            tkinter.messagebox.showinfo("Mesaj", "Parola este gresita")
            parola_entry.delete(0, "end")


parola_entry.bind('<Return>', lambda event: verificare()) # legam functia verificare de entry-ul parolei

verifica = Button(f1, text='verifica', fg='black', bg='grey', command=verificare)
verifica.place(x=250, y=165)


# frame 2

number1_text = Label(f2, text="Primul Numar", bg='grey')
number2_text = Label(f2, text="Al Doilea Numar", bg='grey')
number1_text.place(x=200, y=10)
number2_text.place(x=200, y=50)

# Odata ce avem textul introdus vom introduce entry-urile corespunzatoare


def correct(inp):
    if inp.isdigit() or inp is "":
        return True
    else:
        return False


reg = f2.register(correct)

primul_numar = Entry(f2)
primul_numar.config(validate="key", validatecommand=(reg, '%P'))
aldoilea_numar = Entry(f2)
aldoilea_numar.config(validate="key", validatecommand=(reg, '%P'))

primul_numar.place(x=188, y=30)
aldoilea_numar.place(x=188, y=70)

# cele 4 operatii
grup = IntVar()
adunare = Radiobutton(f2, text="+", variable=grup, value=1, bg='grey')
scadere = Radiobutton(f2, text="-", variable=grup, value=2, bg='grey')
inmultire = Radiobutton(f2, text="*", variable=grup, value=3, bg='grey')
impartire = Radiobutton(f2, text="/", variable=grup, value=4, bg='grey')

adunare.place(x=190, y=90)
scadere.place(x=220, y=90)
inmultire.place(x=250, y=90)
impartire.place(x=280, y=90)

# rezultatul

rezultat = Label(f2, text="Rezultat", bg='grey')
rezultat.place(x=220, y=160)

rezultat_entry = Entry(f2)
rezultat_entry.place(x=190, y=180)

# butonul calculeaza


def operatie():
    try:
        numar1 = int(primul_numar.get())
        numar2 = int(aldoilea_numar.get())
        rezultat_entry.delete(0, "end")
        if grup.get() == 1:
            rez = numar1 + numar2
        elif grup.get() == 2:
            rez = numar1 - numar2
        elif grup.get() == 3:
            rez = numar1 * numar2
        elif grup.get() == 4:
            rez = round(numar1 / numar2 , 2)
        else:
            tkinter.messagebox.showinfo("Mesaj", "Alegeti o operatie")
        rezultat_entry.insert(0, rez)
    except ValueError:
        tkinter.messagebox.showinfo("Mesaj", "Introduceti ambele numere")


aldoilea_numar.bind('<Return>', lambda event: operatie())

button_calculeaza = Button(f2, text="Calculeaza", bg='grey', width=20, height=1, command=operatie)
button_calculeaza.place(x=180, y=120)



inapoi = Button(f2, text="Inapoi", bg='grey', command=lambda: raise_frame(f1))
inapoi.place(x=10, y=260)


font_var = StringVar()
schimb_font = ttk.Combobox(f2, textvariable=font_var, values=["normal" , "bold" , "italic"])
schimb_font.place(x=350, y=260)

def functie_font(fontul):
    if font_var.get() == "normal":
        schimb_font.selection_clear()
        number1_text.config(font='Helvetica 10 normal')
        number2_text.config(font='Helvetica 10 normal')
        button_calculeaza.config(font='Helvetica 10 normal')
        rezultat.config(font='Helvetica 10 normal')
        inapoi.config(font='Helvetica 10 normal')
        nume_utilizator = nume_entry.get()
        name_tag = Text(f2, width=20, height=1, font='Helvetica 10 normal', bg='grey')
        name_tag.insert(END, nume_utilizator)
        name_tag.place(x=10, y=10)
    if font_var.get() == "bold":
        schimb_font.selection_clear()
        number1_text.config(font='Helvetica 10 bold')
        number2_text.config(font='Helvetica 10 bold')
        button_calculeaza.config(font='Helvetica 10 bold')
        rezultat.config(font='Helvetica 10 bold')
        inapoi.config(font='Helvetica 10 bold')
        nume_utilizator = nume_entry.get()
        name_tag = Text(f2, width=20, height=1, font='Helvetica 10 bold', bg='grey')
        name_tag.insert(END, nume_utilizator)
        name_tag.place(x=9, y=10)
    if font_var.get() == "italic":
        schimb_font.selection_clear()
        number1_text.config(font='Helvetica 10 italic')
        number2_text.config(font='Helvetica 10 italic')
        button_calculeaza.config(font='Helvetica 10 italic')
        rezultat.config(font='Helvetica 10 italic')
        inapoi.config(font='Helvetica 10 italic')
        nume_utilizator = nume_entry.get()
        name_tag = Text(f2, width=20, height=1, font='Helvetica 10 italic', bg='grey')
        name_tag.insert(END, nume_utilizator)
        name_tag.place(x=10, y=10)


schimb_font.bind("<<ComboboxSelected>>", functie_font)


raise_frame(f1)
root.mainloop()
