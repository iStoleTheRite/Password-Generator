from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from configparser import ConfigParser
import random
import tkinter as tk
import tkinter.font as font
import pyperclip as pclip
WINGEOMETRY = "420x200+730+350"  # WidthxHeight+X+Y
BORD = "groove"
CFGFILE = "PPGcfg.ini"
CFG = ConfigParser()
CFG.read(CFGFILE)
# Check if config file exists, if it doesn't create it and add proper section.
if not CFG.read(CFGFILE):
    print("Creating file...")
    with open(CFGFILE, "w") as config:
        CFG.add_section("aesthetic")
        CFG.set("aesthetic", "theme", "light")
        CFG.write(config)
else:
    pass

# Default colors (Light mode)
colors = {"bg": "#FFFFFF", "fg": "#3B413C",
          "hl": "#D6D6D6", "display": "#D6D6D6"}

if CFG['aesthetic']['theme'] == "dark":
    colors["bg"] = "#222725"
    colors["fg"] = "#C2FCF7"
    colors["hl"] = "#7D94B5"
    colors["display"] = "#39413F"

def gen_passw(length=8, text=f" copied to clipboard"):
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
            logFile.write(f"Error: {e}\n")
            logFile.close()
            gen_passw(text=" has been copied to clipboard using default length (8)")

def font_resize(event):
    if event.width in range(420, 620):
        passwDisplay["font"] = font.Font(size=10)
        GenButton["font"] = font.Font(size=10)
        lengthDescriber["font"] = font.Font(size=10)
        lengthInput["font"] = font.Font(size=8)
        dmButton["font"] = font.Font(size=8)
        lmButton["font"] = font.Font(size=8)
    elif event.width in range(620, 820):
        passwDisplay["font"] = font.Font(size=14)
        GenButton["font"] = font.Font(size=18)
        lengthDescriber["font"] = font.Font(size=15)
        lengthInput["font"] = font.Font(size=18)
        dmButton["font"] = font.Font(size=18)
        lmButton["font"] = font.Font(size=18)
    elif event.width in range(820, 1020):
        passwDisplay["font"] = font.Font(size=18)
        GenButton["font"] = font.Font(size=18)
        lengthDescriber["font"] = font.Font(size=20)
        lengthInput["font"] = font.Font(size=20)
        dmButton["font"] = font.Font(size=20)
        lmButton["font"] = font.Font(size=20)
    elif event.width in range(1020, 1220):
        passwDisplay["font"] = font.Font(size=22)
        GenButton["font"] = font.Font(size=22)
        lengthDescriber["font"] = font.Font(size=25)
        lengthInput["font"] = font.Font(size=25)
        dmButton["font"] = font.Font(size=25)
        lmButton["font"] = font.Font(size=25)
    elif event.width > 1220:
        passwDisplay["font"] = font.Font(size=34)
        GenButton["font"] = font.Font(size=26)
        lengthDescriber["font"] = font.Font(size=30)
        lengthInput["font"] = font.Font(size=30)
        dmButton["font"] = font.Font(size=30)
        lmButton["font"] = font.Font(size=30)

def savetheme(scheme):
    print(f"Theme changed to {scheme}")
    passwDisplay.config(text=f"{scheme.capitalize()} theme selected and saved")
    CFG.set("aesthetic", "theme", scheme)
    config = open(CFGFILE, "w")
    CFG.write(config)
    if scheme == "dark":
        root.after(0, lambda: root.config(bg="#222725"))
        passwDisplay.after(0, lambda: passwDisplay.config(bg="#39413F", fg="#C2FCF7"))
        lengthInput.after(0, lambda: lengthInput.config(bg="#222725", fg="#C2FCF7"))
        lengthDescriber.after(0, lambda: lengthDescriber.config(bg="#222725", fg="#C2FCF7"))
        GenButton.after(0, lambda: GenButton.config(bg="#222725", fg="#C2FCF7", activebackground="#7D94B5"))
        dmButton.after(0, lambda: dmButton.config(bg="#222725", fg="#C2FCF7", activebackground="#7D94B5"))
        lmButton.after(0, lambda: lmButton.config(bg="#222725", fg="#C2FCF7", activebackground="#7D94B5"))
    elif scheme =="light":
        root.after(0, lambda: root.config(bg="#FFFFFF"))
        passwDisplay.after(0, lambda: passwDisplay.config(bg="#D6D6D6", fg="#3B413C"))
        lengthInput.after(0, lambda: lengthInput.config(bg="#FFFFFF", fg="#3B413C"))
        lengthDescriber.after(0, lambda: lengthDescriber.config(bg="#FFFFFF", fg="#3B413C"))
        GenButton.after(0, lambda: GenButton.config(bg="#FFFFFF", fg="#3B413C", activebackground="#D6D6D6"))
        dmButton.after(0, lambda: dmButton.config(bg="#FFFFFF", fg="#3B413C", activebackground="#D6D6D6"))
        lmButton.after(0, lambda: lmButton.config(bg="#FFFFFF", fg="#3B413C", activebackground="#D6D6D6"))

# Set our window
root = tk.Tk()
# Apparently you can't set a background image on widgets such as buttons without replacing text
# BGIMAGE = tk.PhotoImage("C:\\Users\\melis\\Desktop\\Python\\Password_Gen\\Possible icons\\starrynight.jpg")
root.title("Pinwheel's Password Generator - Credit to Saucy")
root.geometry(WINGEOMETRY)
root.configure(bg=colors["bg"])
# Possible menu for themes. Not sure if I'd rather have this or the buttons.

# menubar = tk.Menu(root)
# themeMenu = tk.Menu(menubar, tearoff=0)
# themeMenu.add_command(label="Dark mode", command=lambda: savetheme("dark"))
# themeMenu.add_command(label="Light mode", command=lambda: savetheme("light"))
# menubar.add_cascade(label="Themes", menu=themeMenu)
# root.config(menu=menubar)

# Icon for app.
# root.iconphoto(False, tk.PhotoImage(
#     file='/Icons/Espers Pinwheel.ico')  # Needs fixing
#     )
root.bind("<Configure>", font_resize)
#root.resizable(width=0, height=0)

# Creating a frame to hold everything (GOT RID OF BUT MIGHT ADD BACK LATER, WAS UNEEDED.)
# frameForBG = tk.Frame(root, height=101, width=420   , bg=BACKGROUND)
# frameForBG.place(relheight=1, relwidth=1)

# Label for password
passwDisplay = tk.Label(
    root, text="Password appears here (Character limit: 24)",
    bg=colors["display"], fg=colors["fg"],
    )
passwDisplay.place(anchor="n", relx=0.5, rely=0.06, relwidth=1)
passwDisplay["font"] = 10

# Custom length entry & label
lengthInput = tk.Entry(root, bg="#FFFFFF", width=22)
lengthInput.place(anchor="n", relx=0.5, rely=0.28, relwidth=0.33, relheight=0.16)

# Label for Entry.
lengthDescriber = tk.Label(
    root, bg=colors["bg"], fg=colors["fg"], width=16,
    text="Length: ", relief=BORD,
    )
lengthDescriber.place(anchor="w", relx=0.019, rely=0.36, relwidth=0.31, relheight=0.16)

# Generate button
GenButton = tk.Button(
    root, bd=2, bg=colors["bg"], fg=colors["fg"],
    text="Generate", command=custom_len_gen,
    width=16, activebackground=colors["hl"], relief=BORD
    )
GenButton.place(anchor="e", relx=0.98, rely=0.36, relwidth=0.30, relheight=0.16)

# Button to change color scheme to darkmode colors!
dmButton = tk.Button(
    root, bg=colors["bg"], fg=colors["fg"],
    text="Darkmode", command=lambda: savetheme("dark"),
    relief=BORD, wraplength=200, activebackground=colors["hl"]
    )
dmButton.place(anchor="e", relx=0.5, rely=0.75, relwidth=0.5, relheight=0.48)
# Button to change to light colors
lmButton = tk.Button(
    root, bg=colors["bg"], fg=colors["fg"],
    text="Lightmode", command=lambda: savetheme("light"),
    relief=BORD, wraplength=200, activebackground=colors["hl"]
    )
lmButton.place(anchor="w", relx=0.5, rely=0.75, relwidth=0.5, relheight=0.48)

root.mainloop()
