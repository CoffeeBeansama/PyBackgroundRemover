from rembg import remove
from PIL import Image
import tkinter as tk
from tkfilebrowser import askopenfilename


font = ("Roboto-Medium.ttf",40)
font2 = ("Roboto-Medium.ttf",28)

window = tk.Tk()
window.title("Background Remover")
window.geometry("400x200")

def browseFile():
    file = askopenfilename(parent=window, initialdir=' ', initialfile='png',
                           filetypes=[("Pictures", "*.png|*.jpg|*.JPG"),
                                      ("All files", "*")])
    return str(file)

rowText = tk.Label(window,text="Select Image",font=font2)
rowText.pack()
def removeBackground():
    path = browseFile()
    input = Image.open(path)
    output_path = path
    output = remove(input)
    output.save(output_path)


searchButton = tk.Button(window,text="Browse Image",command=removeBackground)
searchButton.pack()

window.mainloop()
