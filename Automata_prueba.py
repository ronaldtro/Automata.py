from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA
from tkinter import *
def automata():
    dfa=DFA(
    states={"q0","q1","q2","q3","q4"},
    input_symbols = {"a","b"},
    transitions={
    "q0":{"a":"q1","b":"q4"},
    "q1":{"b":"q2","a":"q4"},
    "q2":{"a":"q1","b":"q3"},
    "q3":{"a":"q1","b":"q4"},
    "q4":{"a":"q4","b":"q4"}
    },
    initial_state="q0",
    final_states={"q1"}
    )
    dfa = VisualDFA(dfa)
    dfa.show_diagram()
    palabra =palabra1.get()
    llego.set(dfa.input_check(palabra))
    

ventana = Tk()
ventana.geometry("800x800")
ventana.configure(background="black")

img = PhotoImage(file=str("imagen.png"))
imagen = Label(image = img)
imagen.place(x=35,y=400)
imagen.pack()

palabra1 =StringVar()
llego= StringVar()
ingplabra = Label(text="INGRESAR PALABRA",bg="black",fg="#0DBFF8") 
ingplabra.place(x=340,y=50)
palabra1_entry =Entry(textvariable=palabra1, width="40",bg="black",fg="#0DBFF8").place(x=260, y = 100)
boton_btn = Button(ventana,text="VALIDAR",command=automata,width="30",height="1",bg="black",fg="#0DBFF8").place(x=32,y= 200)
#palabra=input("Ingrese palabras para la expresion regular \nA(BBA U BA)*\n\n ")
mostrar = Label(text="RESULTADO",bg="black",fg="#0DBFF8") 
mostrar.place(x=340,y=250)
mostrar1 = Entry(textvariable=llego, width="120",bg="black",fg="#0DBFF8")
mostrar1.place(x=35, y = 300)


ventana.mainloop()

