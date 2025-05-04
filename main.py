import tkinter as tk
import folhaPagamentos as fpg

class Aplicativo:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("App Principal")
        self.root.geometry("400x350")
        self._configurar_interface()
        
    def _configurar_interface(self):
        """Cria os componentes da interface"""
        # Frame principal
        frame_principal = tk.Frame(self.root, padx=20, pady=10, bg="#f0f0f0")
        frame_principal.pack(fill="both", expand=True)
        
        # Título
        titulo = tk.Label(frame_principal, 
                         text="Sistema de Folha de Pagamentos", 
                         font=("Arial", 14, "bold"),
                         bg="#f0f0f0")
        titulo.pack(pady=10)
        
        # Cores para os botões
        cores = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6"]
        
        # Botões do sistema
        botoes = [
            ("Adicionar Funcionário", lambda: fpg.adicionar_funcionario_dialog(self.root)),
            ("Listar Funcionários", lambda: fpg.listar_funcionarios_dialog(self.root)),
            ("Calcular Salário", lambda: fpg.calcular_salario_dialog(self.root)),
            ("Gerar Relatório", lambda: fpg.gerar_relatorio_dialog(self.root)),
            ("Sobre", lambda: fpg.mostrar_mensagem("Sobre", "Sistema de Folha de Pagamentos\nVersão 1.0"))
        ]
        
        for i, (texto, comando) in enumerate(botoes):
            tk.Button(
                frame_principal,
                text=texto,
                command=comando,
                width=20,
                bg=cores[i],
                fg="white",
                font=("Arial", 10),
                relief=tk.RAISED,
                bd=2
            ).pack(pady=8)

    def executar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Aplicativo()
    app.executar()
