from include import api
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import time

from threading import Thread
chck = None
def Progress(tk):
    progress['value'] = 5
    tk.update_idletasks()
    time.sleep(2)
    progress['value'] = 10
    tk.update_idletasks()
    time.sleep(4)
    progress['value'] = 15
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 20
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 25
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 30
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 35
    tk.update_idletasks()
    progress['value'] = 40
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 45
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 50
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 55
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 60
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 65
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 70
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 75
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 80
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 85
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 90
    tk.update_idletasks()
    time.sleep(6)
    progress['value'] = 95
    tk.update_idletasks()
    time.sleep(8)
    progress['value'] = 100
    tk.update_idletasks()
    chck = 'Baixando Video Aguade!'
    tk.update_idletasks()



def ReturnErro():
    if len(link.get()) <= 21 :
        return 'Link Invalido!'

def Download():
    fail = ReturnErro()
    if fail != None:
        messagebox.showerror(title='Error 404', message=fail)
    else:
        global response
        response = api.Yt(link.get())
        movie = response.DownloadMovie()
        name = response.ShowNameMovie()
        msg =f'''
        Video: {name}\nDownload Concluido!
        '''
        messagebox.showinfo(title='Download Concluido', message=msg)
            

class Window(Tk):
    def __init__(self):
        chck = 'Chegando Link...'
        self.app = Tk()
        self.app.title('BvMidia')
    
        
    def quit(self):
        exit()   
        
   
        
    
    def Play(self):
        Progress(self.app)
        Thread(target=Download).start()
        
    
    def run(self):
        
        Label(self.app, text='BvMidia', font='Courier 20').grid(row=1, column=2)
        
        Label(self.app, text='Link:', font='Arial 10').grid(row=5, column=1)
        
        global link
        link = Entry(self.app, width='25')
        link.grid(row=5, column=2)
        line = None
        Label(self.app, text=line).grid(row=6, column=2)
        btn = Button(self.app, text='Download', command=Window().Play)
        btn.grid(row=7,column=2)
        line = None
        Label(self.app, text=line).grid(row=8, column=2)
        
        global progress
        progress = Progressbar(self.app, orient=HORIZONTAL ,length=250, mode='determinate')
        progress.grid(row=9,column=2)
        
        Label(self.app, text=chck, font='Courier 8', foreground='#11D116' ).grid(row=10, column=2)
        
        btn_quit = Button(self.app, text='Exit', command=Window().quit)
        btn_quit.grid(row=11, column=2)
        
        
        self.app.mainloop()
        
        
        
Window().run()