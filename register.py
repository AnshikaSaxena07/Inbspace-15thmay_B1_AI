import tkinter as tk

app=tk.Tk()
app.title('Registration Form')
app.geometry('600x600')
app.configure(background="cyan") 
 


label_0 = tk.Label(app, text="REGISTRATION FORM",width=20,fg="purple",font=("Comic Sans MS", 20 ,"bold"))
label_0.place(x=110,y=30)
 
 
label_1 =tk.Label(app, text="FULLNAME",width=20,font=("bold", 10))
label_1.place(x=60,y=130)
 
entry_1 =tk.Entry(app)
entry_1.place(x=270,y=130)
 
label_2 = tk.Label(app, text="EMAIL",width=20,font=("bold", 10))
label_2.place(x=60,y=230)
 
entry_2 =tk.Entry(app)
entry_2.place(x=270,y=230)
 

label_3 =tk.Label(app, text="CONTACT NUMBER",width=20,font=("bold", 10))
label_3.place(x=60,y=280)
 
entry_3 =tk.Entry(app)
entry_3.place(x=270,y=280)


label_4 =tk.Label(app, text="AGE",width=20,font=("bold", 10))
label_4.place(x=60,y=180)
 
entry_4 =tk.Entry(app)
entry_4.place(x=270,y=180)
 
b1=tk.Button(app, text='SUBMIT',width=20,bg='yellow',fg='black',font=("bold", 12)).place(x=160,y=450)
app.mainloop()
