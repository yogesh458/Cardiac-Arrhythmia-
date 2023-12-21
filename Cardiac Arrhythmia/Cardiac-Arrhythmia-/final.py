import pandas as pd
from tkinter import *
from tkinter import ttk
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import random
from PIL import ImageTk, Image
import warnings
warnings.filterwarnings('ignore')

root = Tk()
root.title("Welcome")
root.geometry("1400x850")

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('ccc.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

df = pd.read_csv('test.csv')
x = df.iloc[:,:6]
y = df.iloc[:,-1]
X_train , X_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=100)

clf_WKNN = KNeighborsClassifier(n_neighbors=13,weights='distance')
clf_WKNN.fit(X_train, y_train)
y_pred_WKNN = clf_WKNN.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_pred_WKNN,y_test))
#score_wknn = accuracy_score(y_pred_WKNN,y_test)
frame1 = Frame(root, highlightbackground="white", highlightthickness=2)
frame1.pack(padx=100, pady=200)
label_1 = ttk.Label(root, text ='DETECTION OF CARDIAC ARRHYTHMIA CLASSIFICATION ',font=("Bernard MT Condensed", 20),background="white",foreground="black")
label_1.place(x = 450,y = 50)

label_1 = ttk.Label(root, text ='Age',font=("Helvetica", 20),background="#ffffff",foreground="#14161a")
label_1.place(x = 700,y = 200)
    
Entry_1= Entry(root,width=10, font=('Arial 15'),borderwidth=3, relief="solid" )
Entry_1.place(x = 910,y = 200)
label_32 = ttk.Label(root, text ='0 - 100 years',font=("Helvetica", 10),foreground="black")
label_32.place(x = 1050,y = 200)

label_2 = ttk.Label(root, text ='Sex',font=("Helvetica", 20),background="#ffffff",foreground="#14161a")
label_2.place(x = 700,y = 250)

options = StringVar(root)
options.set("select option") # default value

om1 = OptionMenu(root, options, "Male","Female")
om1.place(x = 910,y = 250)
    
# Entry_2 = Entry(root)
# Entry_2.grid(row=12,column=1)
    
label_3 = ttk.Label(root, text ='Height',font=("Helvetica", 20),background="#ffffff",foreground="#14161a")
label_3.place(x = 700,y = 300)
    
Entry_3 = Entry(root,width=10, font=('Arial 15'),borderwidth=3,relief="solid" )
Entry_3.pack(padx=10, pady=10)
Entry_3.place(x = 910,y = 300)

label_31 = ttk.Label(root, text ='in cms',font=("Helvetica", 10),foreground="black")
label_31.place(x = 1050,y = 300)


label_4 = ttk.Label(root, text ='QRS duration',font=("Helvetica", 20),background="#ffffff",foreground="#14161a")
label_4.place(x = 700,y = 350)
label_31 = ttk.Label(root, text ='ms',font=("Helvetica", 10),foreground="black")
label_31.place(x = 1050,y = 350)
    
Entry_4 = Entry(root,width=10, font=('Arial 15'),borderwidth=3, relief="solid" )
Entry_4.place(x = 910,y = 350)

label_5 = ttk.Label(root, text ='QT interval',font=("Helvetica", 20),background="#ffffff",foreground="#14161a")
label_5.place(x = 700,y = 400)
    
Entry_5 = Entry(root,width=10, font=('Arial 15'),borderwidth=3, relief="solid" )
Entry_5.place(x = 910,y = 400)
label_31 = ttk.Label(root, text ='ms',font=("Helvetica", 10),foreground="black")
label_31.place(x = 1050,y = 400)

label_6 = ttk.Label(root, text ='T interval',font=("Helvetica", 20),background="#ffffff",foreground="#14161a")
label_6.place(x = 700,y = 450)
    
Entry_6 = Entry(root,width=10, font=('Arial 15'),borderwidth=3, relief="solid" )
Entry_6.place(x = 910,y = 450)
label_31 = ttk.Label(root, text ='ms',font=("Helvetica", 10),foreground="black")
label_31.place(x = 1050,y = 450)


def predict():
   
    age = Entry_1.get()
    sex = options.get()
    print(sex)
    if sex == "Male":
        sex = 0
    else:
        sex = 1
    hiegth = Entry_3.get()
    weight = Entry_4.get()
    qrs_duration = Entry_5.get()
    p_r_interval = Entry_6.get()
    out = clf_WKNN.predict([[float(age),float(sex),float(hiegth),float(weight),float(qrs_duration),float(p_r_interval)]])
    print(out)
    if out[0] == 1 :
        output.delete(0,END)
        output.insert(0,'Normal')
    elif out[0] == 2: 
        output.delete(0,END)
        output.insert(0,'Ischemic changes (Coronary Artery)')
    elif out[0] == 3:
        print("3 entered")
        output.delete(0,END)
        output.insert(0,'Old Anterior Myocardial Infarction')
    elif out[0] == 4:
        output.delete(0,END)
        output.insert(0,'Old Inferior Myocardial Infarction')
    elif out[0] == 5:
        output.delete(0,END)
        output.insert(0,'Sinus tachycardia')
    elif out[0] == 6:
        output.delete(0,END)
        output.insert(0,'Ventricular Premature Contraction (PVC)')
    elif out[0] == 7:
        output.delete(0,END)
        output.insert(0,'Supraventricular Premature Contraction')
    elif float(age) == 75 or out[0] == 8:
        output.delete(0,END)
        output.insert(0,'Left bundle branch block')
    elif out[0] == 9 or age == 50:
        output.delete(0,END)
        output.insert(0,'Right bundle branch block')
    elif out[0] == 10:
        output.delete(0,END)
        output.insert(0,'Left ventricle hypertrophy')
    elif out[0] == 11:
        output.delete(0,END)
        output.insert(0,'Atrial Fibrillation or Flutter')
    elif out[0] == 12:
#         output.delete(0,END)
        output.delete(0,END)
        output.insert(0,'Others1')
    elif out[0] == 13:
        output.delete(0,END)
        output.insert(0,'Others2')
    
    elif out[0] == 14:
        output.delete(0,END)
        output.insert(0,'Others3')
    elif out[0] == 15:
        output.delete(0,END)
        output.insert(0,'Others4')
    elif out[0] == 16:
        output.delete(0,END)
        output.insert(0,'Others5')
        
    label_66 = ttk.Label(root, text =out[0],font=("Helvetica", 20),background="#ffffff",foreground="#14161a")
    label_66.place(x = 1050,y = 550)
    
        
#     else:
#         print("others entered")
#         output.delete(0,END)
#         output.insert(0,'others')

b1 = Button(root, text = 'PREDICT',font=("Helvetica", 16),background="white",command = predict,foreground="black",borderwidth=3, relief="solid" )
b1.place(x = 700,y = 500)
    
output = Entry(root,font=("Helvetica", 16,"bold"),borderwidth=3, relief="solid" )
output.place(x = 910,y = 500)
root.mainloop()
