import tkinter

window = tkinter.Tk()
widget = tkinter
window.configure(bg = "blue")

def add_function():
    a=int(textbox1.get())
    b=int(textbox2.get())
    import pandas as pd 
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    data=pd.read_csv("C:\\Users\\elcot\\Desktop\\machine learning tutorial\\real estate price prediction\\price.csv")
    #sns.heatmap(data.corr(),annot=True)
    
    x=data.iloc[:,[0,1]].values
    y=data.iloc[:,[8]].values
    
    from sklearn.model_selection import train_test_split  
    x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.20, random_state=0)  
    
    from sklearn.linear_model import LinearRegression
    reg=LinearRegression()
    reg.fit(x_train,y_train)
    y_pred=reg.predict(x_test)
    c=reg.predict([[a,b]])
    from sklearn.metrics import r2_score
    r2_score(y_test,y_pred)


    Label1.configure(text="home price:"+str(c))
    
    
name=widget.Label()
name.pack()
name.configure(text="ABC GROUP OF COMPANY",font = "bold",bg = 'blue',fg = 'yellow')
name.place(x=270,y=13,height=45,width=380)






textbox1 = widget.Entry()

textbox1.pack()
textbox1.place(x=360,y=74,height=25,width=150)

textbox2 =widget.Entry()
textbox2.pack()
textbox2.place(x=360,y=126,height=25,width=150)

button1 =widget.Button()
button1.pack()
button1.place(x=365,y=170,height=30,width=150)
button1.configure(text="Price of home",font = "bold",bg = 'green')
button1.configure(command=add_function)



bhk=widget.Label()
bhk.pack()
bhk.configure(text="BHK:",font = "bold",bg = 'blue')
bhk.place(x=305,y=70,height=24,width=50)

sqft=widget.Label()
sqft.pack()
sqft.configure(text="Sqft:",font = "bold",bg = 'blue')
sqft.place(x=305,y=130,height=20,width=50)


Label1=widget.Label()
Label1.pack()
Label1.configure(font = "bold",bg = 'skyblue')
Label1.place(x=300,y=300,height=70,width=400)



window.title("ABC group of company")
window.geometry("800x400")
window.mainloop()

