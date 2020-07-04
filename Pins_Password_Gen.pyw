from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import random
import tkinter as tk
import tkinter.font as font
import pyperclip as pclip
BACKGROUND = "#FFFFFF"  # Original color: E9E6FF, FFFFFF
FOREGROUND = "#3B413C"  # Original color: 706993, 3B413C
HIGHLIGHT = "#D6D6D6"  # Original color: 43484B, D6D6D6

def gen_pass(length=8):
    options = ascii_uppercase + ascii_lowercase + digits + punctuation
    generatedPW = "".join(random.choice(options) for _ in range(length))
    pclip.copy(generatedPW)
    passDisplay.config(text=f"{generatedPW} has been copied to clipboard")

def custom_len_gen():
    userLength = lengthInput.get()
    try:
        if int(userLength) > 20 or int(userLength) < 8:
            gen_pass()
        else:
            gen_pass(int(userLength))
    except Exception as e:
        if userLength == "":
            gen_pass()
        else:
            logFile = open("log.txt", "a")
            logFile.write(f"Error: {e}\n\n")
            logFile.close()
            gen_pass()

def font_resize(event):
    if event.width in range(420, 800):
        genButton["font"] = font.Font(size=16)
        passDisplay["font"] = font.Font(size=10)
        customGen["font"] = font.Font(size=10)
        lengthDescriber["font"] = font.Font(size=10)
        lengthInput["font"] = font.Font(size=8)
    elif event.width in range(600, 1200):
        genButton["font"] = font.Font(size=32)
        passDisplay["font"] = font.Font(size=24)
        customGen["font"] = font.Font(size=24)
        lengthDescriber["font"] = font.Font(size=19)
        lengthInput["font"] = font.Font(size=18)
    elif event.width > 1200:
        genButton["font"] = font.Font(size=54)
        passDisplay["font"] = font.Font(size=32)
        customGen["font"] = font.Font(size=32)
        lengthDescriber["font"] = font.Font(size=30)
        lengthInput["font"] = font.Font(size=28)

# Set our window
root = tk.Tk()
# Apparently you can't set a background image on widgets such as buttons without replacing text
# BGIMAGE = tk.PhotoImage("C:\\Users\\melis\\Desktop\\Python\\Password_Gen\\Possible icons\\starrynight.jpg")
root.title("Pins Password Generator - Credit to Saucy")
root.geometry("420x150") # originally 250x150
root.iconphoto(False, tk.PhotoImage(
    file='C:\\Users\\melis\\Pictures\\Saved pictures\\Icons\\Espers Pinwheel.ico')
    )
root.bind("<Configure>", font_resize)
#root.resizable(width=0, height=0)

# Creating a frame to hold everything
frameName = tk.Frame(root, height=101, width=420   , bg=BACKGROUND)
frameName.place(relheight=1, relwidth=1)

# Label for password
passDisplay = tk.Label(
    root, text="Password appears here (Character limit of 8-20)",
     bg=BACKGROUND, fg=FOREGROUND
     )
passDisplay.place(anchor="n", relx=0.5, relwidth=1)
passDisplay["font"] = 10

# Button for generation
genButton = tk.Button(
    root, text="Generate Password",
    bd=2, bg=BACKGROUND, fg=FOREGROUND,
    command=gen_pass, activebackground=HIGHLIGHT,
    activeforeground=FOREGROUND,
    )
genButton["font"] = font.Font(size=16)
genButton.place(anchor="n", relx=0.5, rely=0.5, relwidth=1, relheight=0.55)

# Custom length entry & label
lengthInput = tk.Entry(root, bg="#FFFFFF", width=22)
lengthInput.place(anchor="n", relx=0.5, rely=0.28, relwidth=0.30, relheight=0.15)

# Label for Entry.
lengthDescriber = tk.Label(root, bg=BACKGROUND, fg=FOREGROUND, width=18, text="Enter a desired length: ")
lengthDescriber.place(anchor="w", relx=0.020, rely=0.345, relwidth=0.33, relheight=0.18)

# Confirm button for length of password
customGen = tk.Button(
    root, bd=2, bg=BACKGROUND, fg=FOREGROUND,
    text="Generate (Custom)", command=custom_len_gen,
    width=19, activebackground=HIGHLIGHT,
    activeforeground=FOREGROUND
    )
customGen.place(anchor="e", relx=0.999, rely=0.355, relwidth=0.34, relheight=0.16)

root.mainloop()