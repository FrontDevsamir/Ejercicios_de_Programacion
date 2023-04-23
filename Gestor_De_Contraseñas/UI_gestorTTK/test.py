import tkinter as tk
from tkinter import ttk






root = tk.Tk()



style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="red")
style.configure("TButton", padding=6, relief="flat",
   background="blue")
style.map("TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

style.layout("TMenubutton", [
   ("Menubutton.background", None),
   ("Menubutton.button", {"children":
       [("Menubutton.focus", {"children":
           [("Menubutton.padding", {"children":
               [("Menubutton.label", {"side": "right", "expand": 1})]
           })]
       })]
   }),
])

style.theme_settings("default", {
   "TCombobox": {
       "configure": {"padding": 5},
       "map": {
           "background": [("active", "green2"),
                          ("!disabled", "green4")],
           "fieldbackground": [("!disabled", "green3")],
           "foreground": [("focus", "OliveDrab1"),
                          ("!disabled", "OliveDrab2")]
       }
   }
})



l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")
ttk.Button(text='Click').pack()

combo = ttk.Combobox().pack()

mbtn = ttk.Menubutton(text='Text')
mbtn.pack()

l1.pack()
l2.pack()


root.mainloop()

