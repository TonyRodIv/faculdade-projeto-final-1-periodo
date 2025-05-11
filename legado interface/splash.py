import tkinter as tk
from PIL import Image, ImageTk
import time
from main import MainApp 

splash = tk.Tk()
splash.overrideredirect(True)

largura_tela = splash.winfo_screenwidth()
altura_tela = splash.winfo_screenheight()
splash.geometry(f"750x422+{(largura_tela-750)//2}+{(altura_tela-422)//2}")

def ajustar_imagem(caminho, max_size):
    imagem = Image.open(caminho)
    escala = min(max_size[0]/imagem.width, max_size[1]/imagem.height)
    return imagem.resize(
        (int(imagem.width*escala), int(imagem.height*escala)), 
        Image.LANCZOS
    )

imagem_ajustada = ajustar_imagem("SPLASHTICKETS.jpg", (750, 422))
foto = ImageTk.PhotoImage(imagem_ajustada)

label_imagem = tk.Label(splash, image=foto)
label_imagem.pack(fill="both", expand=True)

def iniciar_app():
    for i in range(100, -1, -5):
        splash.attributes('-alpha', i/100)
        splash.update()
        time.sleep(0.03)
    splash.destroy()
    MainApp().mainloop()

splash.after(3000, iniciar_app)
splash.mainloop()
