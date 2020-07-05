from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from configparser import ConfigParser
import random
import tkinter as tk
import tkinter.font as font
import pyperclip as pclip
WINGEOMETRY = "420x150+730+350"  # WidthxHeight+X+Y
BORD = "groove"
CFGFILE = "PPGcfg.ini"
CFG = ConfigParser()
CFG.read(CFGFILE)
COLORS = {"bg": "#FFFFFF", "fg": "#3B413C",
          "hl": "#D6D6D6", "display": "#D6D6D6"}
          
if CFG['aesthetic']['theme'] == "dark":
    COLORS["bg"] = "#222725"
    COLORS["fg"] = "#7D94B5"
    COLORS["hl"] = "#BDD5EA"
    COLORS["display"] = "#39413F"

def gen_passw(length=8, text=f" has been copied to clipboard"):
    options = ascii_uppercase + ascii_lowercase + digits + punctuation
    generatedPW = "".join(random.choice(options) for _ in range(length))
    pclip.copy(generatedPW)
    passwDisplay.config(text=f"{generatedPW}"+text)

def custom_len_gen():
    logFile = open("log.txt", "a")
    userLength = lengthInput.get()
    try:
        if int(userLength) > 24:
            logFile.write(f"User tried to use a length of {userLength}\n\n")
            logFile.close()
            gen_passw()
        else:
            gen_passw(int(userLength))
    except Exception as e:
        if userLength == "":
            gen_passw()
        else:
            logFile.write(f"Error: {e}\n\n")
            logFile.close()
            gen_passw(text=" has been copied to clipboard using default length (8)")

def font_resize(event):
    if event.width in range(420, 620):
        passwDisplay["font"] = font.Font(size=10)
        GenButton["font"] = font.Font(size=10)
        lengthDescriber["font"] = font.Font(size=10)
        lengthInput["font"] = font.Font(size=8)
        dmButton["font"] = font.Font(size=8)
        defaultButton["font"] = font.Font(size=8)
    elif event.width in range(620, 820):
        passwDisplay["font"] = font.Font(size=14)
        GenButton["font"] = font.Font(size=18)
        lengthDescriber["font"] = font.Font(size=15)
        lengthInput["font"] = font.Font(size=18)
        dmButton["font"] = font.Font(size=18)
        defaultButton["font"] = font.Font(size=18)
    elif event.width in range(820, 1020):
        passwDisplay["font"] = font.Font(size=18)
        GenButton["font"] = font.Font(size=18)
        lengthDescriber["font"] = font.Font(size=20)
        lengthInput["font"] = font.Font(size=20)
        dmButton["font"] = font.Font(size=20)
        defaultButton["font"] = font.Font(size=20)
    elif event.width in range(1020, 1220):
        passwDisplay["font"] = font.Font(size=22)
        GenButton["font"] = font.Font(size=22)
        lengthDescriber["font"] = font.Font(size=25)
        lengthInput["font"] = font.Font(size=25)
        dmButton["font"] = font.Font(size=25)
        defaultButton["font"] = font.Font(size=25)
    elif event.width > 1220:
        passwDisplay["font"] = font.Font(size=26)
        GenButton["font"] = font.Font(size=26)
        lengthDescriber["font"] = font.Font(size=30)
        lengthInput["font"] = font.Font(size=30)
        dmButton["font"] = font.Font(size=30)
        defaultButton["font"] = font.Font(size=30)

def savetheme(scheme):
    print("Theme changed")
    CFG.set("aesthetic", "theme", scheme)
    config = open(CFGFILE, "w")
    CFG.write(config)

# Set our window
root = tk.Tk()
# Apparently you can't set a background image on widgets such as buttons without replacing text
# BGIMAGE = tk.PhotoImage("C:\\Users\\melis\\Desktop\\Python\\Password_Gen\\Possible icons\\starrynight.jpg")
root.title("Pins Password Generator - Credit to Saucy")
root.geometry(WINGEOMETRY)
root.configure(bg=COLORS["bg"])
# root.iconphoto(False, tk.PhotoImage(
#     file='C:\\Users\\melis\\Desktop\\Python\\Password_Gen\\Icons\\Espers Pinwheel.ico')  # Needs fixing
#     )
root.bind("<Configure>", font_resize)
#root.resizable(width=0, height=0)

# Creating a frame to hold everything (GOT RID OF BUT MIGHT ADD BACK LATER, WAS UNEEDED.)
# frameForBG = tk.Frame(root, height=101, width=420   , bg=BACKGROUND)
# frameForBG.place(relheight=1, relwidth=1)

# Label for password
passwDisplay = tk.Label(
    root, text="Password appears here (Character limit: 24)",
    bg=COLORS["display"], fg=COLORS["fg"],
    )
passwDisplay.place(anchor="n", relx=0.5, rely=0.06, relwidth=1)
passwDisplay["font"] = 10

# Custom length entry & label
lengthInput = tk.Entry(root, bg="#FFFFFF", width=22)
lengthInput.place(anchor="n", relx=0.5, rely=0.28, relwidth=0.33, relheight=0.16)

# Label for Entry.
lengthDescriber = tk.Label(
    root, bg=COLORS["bg"], fg=COLORS["fg"], width=16,
    text="Length: ", relief=BORD,
    )
lengthDescriber.place(anchor="w", relx=0.019, rely=0.36, relwidth=0.31, relheight=0.16)

# Generate button
GenButton = tk.Button(
    root, bd=2, bg=COLORS["bg"], fg=COLORS["fg"],
    text="Generate", command=custom_len_gen,
    width=16, activebackground=COLORS["hl"], relief=BORD
    )
GenButton.place(anchor="e", relx=0.98, rely=0.36, relwidth=0.30, relheight=0.16)

# Button to change color scheme to darkmode colors!
dmButton = tk.Button(
    root, bg=COLORS["bg"], fg=COLORS["fg"],
    text="Darkmode (restart to save)", command=lambda: savetheme("dark"),
    relief=BORD, wraplength=200, activebackground=COLORS["hl"]
    )
dmButton.place(anchor="e", relx=0.5, rely=0.75, relwidth=0.5, relheight=0.48)
# Button to change to default colors
defaultButton = tk.Button(
    root, bg=COLORS["bg"], fg=COLORS["fg"],
    text="Lightmode (restart to save)", command=lambda: savetheme("light"),
    relief=BORD, wraplength=200, activebackground=COLORS["hl"]
    )
defaultButton.place(anchor="w", relx=0.5, rely=0.75, relwidth=0.5, relheight=0.48)

root.mainloop()