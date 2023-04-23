import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import os


class ventana(tk.Frame):

    def __init__(self, master, **kwg):
        super().__init__(master, **kwg)

        self.master = master

        self.path = ''
        self.links = ''

        self.label = tk.Label(text='DOWNLOAD FILE')

        self.write_links = tk.Text()

        self.select_path = tk.Button(
            text='SELECT', command=self.open_filedialog)

        self.download = tk.Button(text='DOWNLOAD', command=self.get_links)

        # ubicacion de los widgets en la ventana
        self.label.pack()
        self.write_links.pack()
        self.select_path.pack()
        self.download.pack()

    def open_filedialog(self):
        self.path = filedialog.askdirectory(title='SELECCIONA LA CARPETA')

    def get_links(self):

        links = []

        for i in self.write_links.get(1.0, 'end').split(','):
            links.append(i[:-1])

        download_file(self.path, links)


def download_file(path, links):

    files = []
    input(path + '  -----  ' + str(links))

    for i in links:
        print(f'{type(i) = }')
        yt = YouTube(i)
        mp3 = yt.streams.filter(only_audio=True).first()
        files.append(mp3)

    for i in files:
        out_file = i.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)


if __name__ == '__main__':

    root = tk.Tk()
    ventana(root)

    root.mainloop()
