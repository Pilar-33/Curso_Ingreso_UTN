from customtkinter import*

app = CTk()

def button_on_click():
    print("Vamos a aprender python!!")

button =CTkButton(master=app, text="Clik me!", command=button_on_click)
button.grid()

app.mainloop()