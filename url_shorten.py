import pyshorteners
from tkinter import *
from tkinter import messagebox
import pyperclip
def url_shortener():
    url = url_input.get()
    if url == '':
        messagebox.showerror('Invalid Input','Please Provide Input')
    else:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        print(short_url)
        result_label.config(text = ''+short_url)

def copy_url():
    url_to_copy = result_label['text']
    pyperclip.copy(url_to_copy)
    copy_button['text'] = "Copied!"

root = Tk()
root.title("url_shortener")
root.geometry('400x300')
root.config(bg='#123456')

frame_line=Frame(root,width=400,height=6,bg='Black')
frame_line.grid(row=0,column=0)
frame_line.pack(fill=X)

img_label = Label(root,text='Convert long URL to short URL',fg='white',bg='#123456')
img_label.pack(pady=(3,5))
img_label.config(font=('Helvetica',14,"bold"))

url_label = Label(root,text='Enter Url link',fg='White',bg='#123456')
url_label.pack(pady=(1,5))
url_label.config(font=('Helvetica',16,"bold"))

url_input = Entry(root,width=25)
url_input.pack(pady=(3,5))
url_input.config(font=('Helvetica',16,"normal"))

converter_button = Button(root,text='Display Output',font=('Helvetica',10,"bold"),bg='white',fg='black',width=15,command=url_shortener)
converter_button.pack(pady=(3,5))

result_label = Label(root,text='',width=40)
result_label.pack(pady=(3,5))

copy_button = Button(root, text="Copy URL", command=copy_url)
copy_button.pack(pady=(3,5))

root.mainloop()


