from tkinter import *
from tkinter.messagebox import *
#some useful variable 
font=('Verdana',22)

#important function\
def clear():
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)
    

def all_clear():
    textField.delete(0,END)


def click_btn_function(event):
    print("btn clicked")
    b=event.widget
    text=b['text']
    print(text)

    if text == 'x':
        textField.insert(END,"*")
        return ;
   

    if text == '=':
        try:
            ex=textField.get()
            anser=eval(ex)
            textField.delete(0,END)
            textField.insert(0,anser)
        except Exception as e:
            print("ERROR..",e)
            showerror("ERROR",e)
        return ;
    
    textField.insert(END,text)
        



window=Tk()
window.geometry("450x475")
window.config(bg='pink')
window.title("Calculator By Ranju")
#heading text apply
headingLabel=Label(window,text="MY CALCULATOR",font=font,width='440',pady=0,padx=5,bg='orange')

headingLabel.pack(side=TOP,pady=10)
#textField
textField=Entry(window,font=font,justify=CENTER,width='450')
textField.pack(side=TOP,pady=10,padx=10)

#buttons
#frame is using for  grouping button
buttonFrame=Frame(window)
buttonFrame.pack(side=TOP,padx=10)
#adding button
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp),
        font=font,relief='ridge',width='5',activebackground='orange',activeforeground='white')
        btn.grid(row=i,column=j,padx=5,pady=5)
        temp=temp+1
        btn.bind('<Button-1>',click_btn_function)


zerobtn=Button(buttonFrame,text="0",font=font,relief='ridge',width='5',activebackground='orange',activeforeground='white')
zerobtn.grid(row=3,column=0)

dotbtn=Button(buttonFrame,text=".",font=font,relief='ridge',width='5',activebackground='orange',activeforeground='white')
dotbtn.grid(row=3,column=1)

equalbtn=Button(buttonFrame,text="=",font=font,relief='ridge',width='5',activebackground='orange',activeforeground='white')
equalbtn.grid(row=3,column=2)

plusbtn=Button(buttonFrame,text="+",font=font,relief='ridge',width='5',activebackground='orange',activeforeground='white')
plusbtn.grid(row=0,column=3)

minusbtn=Button(buttonFrame,text="-",font=font,relief='ridge',width='5',activebackground='orange',activeforeground='white')
minusbtn.grid(row=1,column=3)

multibtn=Button(buttonFrame,text="x",font=font,relief='ridge',width='5',activebackground='orange',activeforeground='white')
multibtn.grid(row=2,column=3)

divbtn=Button(buttonFrame,text="/",font=font,relief='ridge',width='5',activebackground='orange',activeforeground='white')
divbtn.grid(row=3,column=3)

clearbtn=Button(buttonFrame,text="<--",font=font,relief='ridge',width='11',activebackground='orange',activeforeground='white',command=clear)
clearbtn.grid(row=4,column=0,columnspan=2,)

allbtn=Button(buttonFrame,text="AC",font=font,relief='ridge',width='11',activebackground='orange',activeforeground='white',command=all_clear)
allbtn.grid(row=4,column=2,columnspan=2,)

plusbtn.bind('<Button-1>',click_btn_function)
minusbtn.bind('<Button-1>',click_btn_function)
multibtn.bind('<Button-1>',click_btn_function)
divbtn.bind('<Button-1>',click_btn_function)

zerobtn.bind('<Button-1>',click_btn_function)
dotbtn.bind('<Button-1>',click_btn_function)
equalbtn.bind('<Button-1>',click_btn_function)

window.mainloop()
