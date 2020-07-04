from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import random
import tkinter as tk
import tkinter.font as font
import pyperclip as pclip
BACKGROUND = "#FFFFFF"  # Original color: E9E6FF, FFFFFF
FOREGROUND = "#3B413C"  # Original color: 706993, 3B413C
HIGHLIGHT = "#D6D6D6"  # Original color: 43484B, D6D6D6
WINGEOMETRY = "420x150+730+350"  # WidthxHeight+X+Y
BORD = "groove"

def gen_passw(length=8, text=f" has been copied to clipboard"):
    options = ascii_uppercase + ascii_lowercase + digits + punctuation
    generatedPW = "".join(random.choice(options) for _ in range(length))
    pclip.copy(generatedPW)
    passwDisplay.config(text=f"{generatedPW}"+text)

def custom_len_gen():
    userLength = lengthInput.get()
    try:
        if int(userLength) > 20 or int(userLength) < 8:
            gen_passw()
        else:
            gen_passw(int(userLength))
    except Exception as e:
        if userLength == "":
            gen_passw()
        else:
            logFile = open("log.txt", "a")
            logFile.write(f"Error: {e}\n\n")
            logFile.close()
            gen_passw(text=" has been copied to clipboard using default length (8)")

def font_resize(event):
    if event.width in range(420, 620):
        genButton["font"] = font.Font(size=16)
        passwDisplay["font"] = font.Font(size=10)
        customGenButton["font"] = font.Font(size=10)
        lengthDescriber["font"] = font.Font(size=10)
        lengthInput["font"] = font.Font(size=8)
    elif event.width in range(620, 820):
        genButton["font"] = font.Font(size=16)
        passwDisplay["font"] = font.Font(size=14)
        customGenButton["font"] = font.Font(size=18)
        lengthDescriber["font"] = font.Font(size=15)
        lengthInput["font"] = font.Font(size=18)
    elif event.width > 820:
        genButton["font"] = font.Font(size=32)
        passwDisplay["font"] = font.Font(size=18)
        customGenButton["font"] = font.Font(size=18)
        lengthDescriber["font"] = font.Font(size=16)
        lengthInput["font"] = font.Font(size=20)
# Set our window
root = tk.Tk()
# Apparently you can't set a background image on widgets such as buttons without replacing text
# BGIMAGE = tk.PhotoImage("C:\\Users\\melis\\Desktop\\Python\\Password_Gen\\Possible icons\\starrynight.jpg")
root.title("Pins Password Generator - Credit to Saucy")
root.geometry(WINGEOMETRY)
root.configure(bg=BACKGROUND)
root.iconphoto(False, tk.PhotoImage(
    file='C:\\Users\\melis\\Pictures\\Saved pictures\\Icons\\Espers Pinwheel.ico')
    )
root.bind("<Configure>", font_resize)
#root.resizable(width=0, height=0)

# Creating a frame to hold everything (GOT RID OF BUT MIGHT ADD BACK LATER, WAS UNEEDED.)
# frameForBG = tk.Frame(root, height=101, width=420   , bg=BACKGROUND)
# frameForBG.place(relheight=1, relwidth=1)

# Label for password
passwDisplay = tk.Label(
    root, text="Password appears here (Character limit of 8-20)",
     bg=BACKGROUND, fg=FOREGROUND
     )
passwDisplay.place(anchor="n", relx=0.5, rely=0.06, relwidth=1)
passwDisplay["font"] = 10

# Button for generation
genButton = tk.Button(
    root, text="Generate Password",
    bd=2, bg=BACKGROUND, fg=FOREGROUND,
    command=gen_passw, activebackground=HIGHLIGHT,
    activeforeground=FOREGROUND, relief=BORD
    )
genButton["font"] = font.Font(size=16)
genButton.place(anchor="n", relx=0.5, rely=0.5, relwidth=1, relheight=0.48)

# Custom length entry & label
lengthInput = tk.Entry(root, bg="#FFFFFF", width=22)
lengthInput.place(anchor="n", relx=0.5, rely=0.28, relwidth=0.30, relheight=0.16)

# Label for Entry.
lengthDescriber = tk.Label(
    root, bg=BACKGROUND, fg=FOREGROUND, width=18,
    text="Enter a desired length: ", relief=BORD,
    )
lengthDescriber.place(anchor="w", relx=0.020, rely=0.36, relwidth=0.33, relheight=0.16)

# Confirm button for length of password
customGenButton = tk.Button(
    root, bd=2, bg=BACKGROUND, fg=FOREGROUND,
    text="Generate (Custom)", command=custom_len_gen,
    width=19, activebackground=HIGHLIGHT,
    activeforeground=FOREGROUND, relief=BORD
    )
customGenButton.place(anchor="e", relx=0.98, rely=0.36, relwidth=0.33, relheight=0.16)

root.mainloop()