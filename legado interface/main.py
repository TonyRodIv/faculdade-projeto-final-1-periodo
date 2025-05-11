import customtkinter as ctk
from adm import alterar_interface
class MainApp(ctk.CTk): 
    def __init__(self):
        super().__init__()
        self.geometry("500x350")
        self.title("Open Tickets App")
        
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        
        self.title1 = ctk.CTkLabel(
            self, 
            text="Bem vindo ao Open Tickets",
            font=("Arial", 18)
        )
        self.title1.pack(pady=5)
        
        self.title2 = ctk.CTkLabel(
            self,
            text="Qual tipo de usuário vai acessar a aplicação?",
            font=("Arial", 22, "bold"),
            wraplength=400
        )
        self.title2.pack(pady=10)
        
        self.btn_admin = ctk.CTkButton(
            self,
            text="Administrador",
            fg_color="purple",
            command=lambda: alterar_interface(self, True)
        )
        self.btn_admin.pack(padx=10, pady=10)
        
        self.btn_vendedor = ctk.CTkButton(
            self,
            text="Vendedor",
            command=lambda: print("Vendedor selecionado")
        )
        self.btn_vendedor.pack(padx=10, pady=10)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()