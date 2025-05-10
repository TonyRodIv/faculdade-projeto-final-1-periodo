import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")  

app = ctk.CTk()
app.geometry("500x350")
app.title("Open Tickets App")


title = ctk.CTkLabel(app, text="Bem vindo ao Open Tickets", font=("Arial", 18, "normal"), wraplength=400)
title.pack(pady=5)
title = ctk.CTkLabel(app, text="Qual tipo de usuário vai acessar a aplicação?", font=("Arial", 22, "bold"), wraplength=400)
title.pack(pady=10)

btn = ctk.CTkButton(app, text="Administrador", fg_color="purple", command=lambda: print("Você clicou no botão 1!"))
btn.pack(padx=10, pady=10)
btn = ctk.CTkButton(app, text="Vendedor", command=lambda: print("Você clicou no botão 2!"))
btn.pack(padx=10, pady=10)

app.mainloop()