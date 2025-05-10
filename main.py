import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x250")

btn = ctk.CTkButton(app, text="Botão 1", command=lambda: print("Você clicou no botão 1!"))
btn.pack(padx=20, pady=20)
btn = ctk.CTkButton(app, text="Botão 2", command=lambda: print("Você clicou no botão 2!"))
btn.pack(padx=20, pady=20)

app.mainloop()
