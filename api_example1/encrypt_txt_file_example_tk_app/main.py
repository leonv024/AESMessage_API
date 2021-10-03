#!/usr/bin/env python3
import requests, sys, platform, json
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from ttkbootstrap import Style
from itertools import count, cycle
if platform.system() == 'Linux':
    from PIL import Image, ImageTk
else:
    import PIL.Image, PIL.ImageTk


class ImageLabel(Label):
    def load(self, im):
        if isinstance(im, str):
            im = PIL.Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(PIL.ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

class mainwindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(string = "Secure Text File - Created with AESMessage.com API")
        self.resizable(0,0)
        self.configure(background = 'black')
        self.style = Style(theme='superhero')

        self.bind("<Escape>", self.exit) # Press ESC to quit app

        self.options = {
            'filepath' : StringVar(),
            'passwd' : StringVar(),
        }

        self.options['passwd'].set('securepassword')

        label2 = ImageLabel(self)
        label2.load('images/main.gif')
        label2.grid(row = 0, column = 0, columnspan = 12, rowspan = 11)

        Entry(self, textvariable = self.options['filepath'], width = 35, state=DISABLED).grid(row = 0, column = 5)
        select_file = Button(self, text = "Select File", command = self.fileopener, width = 18, style='info.TButton').grid(row = 1, column = 5)

        passwd = Entry(self, textvariable = self.options['passwd'], show ='●', width = 35).grid(row = 8, column = 5)

        global encrypt_file
        global decrypt_file
        encrypt_file = Button(self, text = "Encrypt", command = self.encrypt, width = 9, style='danger.TButton', state = DISABLED)
        encrypt_file.grid(row = 9, column = 5)
        decrypt_file = Button(self, text = "Decrypt", command = self.decrypt, width = 9, style='success.TButton', state = DISABLED)
        decrypt_file.grid(row = 10, column = 5)


    def encrypt(self):
        path = self.options['filepath'].get()
        passwd = self.options['passwd'].get()
        with open(path, 'rb') as read:
            fdata = read.read()
            payload = {'option':'encrypt','text':fdata, 'passwd':passwd}
            r = requests.post('https://aesmessage.com/api_v1.py', data=payload)
            foo = json.loads(r.text)
            read.close()

        with open(path + '.AES', 'wb') as f:
            f.write(foo[1]['message'].encode())
            f.close()

        a = messagebox.askokcancel('SUCCESS', 'File has been encrypted and saved to: %s' % (path + '.AES'))

    def decrypt(self):
        a = messagebox.askokcancel('AESMessage.com', 'Paste the encrypted text on AESMessage.com and enter the password to decrypt!')

    def fileopener(self):
        path = askopenfile(title = 'Select text file', filetypes=(("text files", "*.txt"), ("AES files", "*.AES")))
        if path:
            self.options['filepath'].set(path.name)
            encrypt_file.config(state = "normal")
            decrypt_file.config(state = "normal")
    def exit(self, event):
        sys.exit(0)
    def exit_click(self):
        sys.exit(0)



start = mainwindow()
start.mainloop()
