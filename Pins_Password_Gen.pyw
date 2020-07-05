from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import random
import tkinter as tk
import tkinter.font as font
import pyperclip as pclip
BACKGROUND = "#FFFFFF"  # Original color: E9E6FF, FFFFFF
FOREGROUND = "#3B413C"  # Original color: 706993, 3B413C
PRVBACKGROUND = "#222725"
PRVFOREGROUND = "#7D94B5"
PRVHIGHLIGHT = "#BDD5EA"
HIGHLIGHT = "#D6D6D6"  # Original color: NONE, D6D6D6
WINGEOMETRY = "420x150+730+350"  # WidthxHeight+X+Y
BORD = "groove"

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
        #genButton["font"] = font.Font(size=16)
        passwDisplay["font"] = font.Font(size=10)
        GenButton["font"] = font.Font(size=10)
        lengthDescriber["font"] = font.Font(size=10)
        lengthInput["font"] = font.Font(size=8)
        prevButton["font"] = font.Font(size=8)
        defaultButton["font"] = font.Font(size=8)
    elif event.width in range(620, 820):
        #genButton["font"] = font.Font(size=16)
        passwDisplay["font"] = font.Font(size=14)
        GenButton["font"] = font.Font(size=18)
        lengthDescriber["font"] = font.Font(size=15)
        lengthInput["font"] = font.Font(size=18)
        prevButton["font"] = font.Font(size=18)
        defaultButton["font"] = font.Font(size=18)
    elif event.width > 820:
        #genButton["font"] = font.Font(size=32)
        passwDisplay["font"] = font.Font(size=18)
        GenButton["font"] = font.Font(size=18)
        lengthDescriber["font"] = font.Font(size=16)
        lengthInput["font"] = font.Font(size=20)
        prevButton["font"] = font.Font(size=20)
        defaultButton["font"] = font.Font(size=20)

def orig_col():
    root.configure(bg=PRVBACKGROUND)
    passwDisplay.configure(bg="#39413F")
    lengthDescriber.configure(bg=PRVBACKGROUND)
    GenButton.configure(bg=PRVBACKGROUND)
    prevButton.configure(bg=PRVBACKGROUND)
    defaultButton.configure(bg=PRVBACKGROUND)
    prevButton.configure(fg=PRVFOREGROUND)
    GenButton.configure(fg=PRVFOREGROUND)
    lengthDescriber.configure(fg=PRVFOREGROUND)
    passwDisplay.configure(fg=PRVFOREGROUND)
    defaultButton.configure(fg=PRVFOREGROUND)
    GenButton.configure(activebackground=PRVHIGHLIGHT)
    prevButton.configure(activebackground=PRVHIGHLIGHT)
    defaultButton.configure(activebackground=PRVHIGHLIGHT)

def default_col():
    root.configure(bg=BACKGROUND)
    passwDisplay.configure(bg="#D6D6D6")
    lengthDescriber.configure(bg=BACKGROUND)
    GenButton.configure(bg=BACKGROUND)
    prevButton.configure(bg=BACKGROUND)
    defaultButton.configure(bg=BACKGROUND)
    prevButton.configure(fg=FOREGROUND)
    GenButton.configure(fg=FOREGROUND)
    lengthDescriber.configure(fg=FOREGROUND)
    passwDisplay.configure(fg=FOREGROUND)
    defaultButton.configure(fg=FOREGROUND)
    GenButton.configure(activebackground=HIGHLIGHT)
    prevButton.configure(activebackground=HIGHLIGHT)
    defaultButton.configure(activebackground=HIGHLIGHT)

# Set our window
root = tk.Tk()
# Apparently you can't set a background image on widgets such as buttons without replacing text
# BGIMAGE = tk.PhotoImage("C:\\Users\\melis\\Desktop\\Python\\Password_Gen\\Possible icons\\starrynight.jpg")
root.title("Pins Password Generator - Credit to Saucy")
root.geometry(WINGEOMETRY)
root.configure(bg=BACKGROUND)
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
    bg="#D6D6D6", fg=FOREGROUND
    )
passwDisplay.place(anchor="n", relx=0.5, rely=0.06, relwidth=1)
passwDisplay["font"] = 10

# Custom length entry & label
lengthInput = tk.Entry(root, bg="#FFFFFF", width=22)
lengthInput.place(anchor="n", relx=0.5, rely=0.28, relwidth=0.33, relheight=0.16)

# Label for Entry.
lengthDescriber = tk.Label(
    root, bg=BACKGROUND, fg=FOREGROUND, width=16,
    text="Length: ", relief=BORD,
    )
lengthDescriber.place(anchor="w", relx=0.019, rely=0.36, relwidth=0.31, relheight=0.16)

# Generate button
GenButton = tk.Button(
    root, bd=2, bg=BACKGROUND, fg=FOREGROUND,
    text="Generate", command=custom_len_gen,
    width=16, activebackground=HIGHLIGHT,
    activeforeground=FOREGROUND, relief=BORD
    )
GenButton.place(anchor="e", relx=0.98, rely=0.36, relwidth=0.30, relheight=0.16)

# Button to change color scheme to preview colors!
prevButton = tk.Button(
    root, bg=BACKGROUND, fg=FOREGROUND,
    text="Preview new colors (Placeholder until further updates!)", command=orig_col,
    relief=BORD, wraplength=200, activebackground=HIGHLIGHT
    )
prevButton.place(anchor="e", relx=0.5, rely=0.75, relwidth=0.5, relheight=0.48)
# Button to change to default colors
defaultButton = tk.Button(
    root, bg=BACKGROUND, fg=FOREGROUND,
    text="Back to default colors", command=default_col,
    relief=BORD, wraplength=200, activebackground=HIGHLIGHT
    )
defaultButton.place(anchor="w", relx=0.5, rely=0.75, relwidth=0.5, relheight=0.48)

root.mainloop()