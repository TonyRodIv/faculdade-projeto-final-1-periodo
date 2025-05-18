from letterboxdpy import movie

filme = movie.Movie("The substance")

print(f"Título: {filme.title}")
print(f"Ano: {filme.year}")
print(f"Diretor: {filme.directors}")
print(f"Avaliação: {filme.rating}/5")
print(f"Gêneros: {filme.genres}")

import customtkinter as ctk
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class FileManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Arquivos")
        self.geometry("520x450")

        # Rótulo de instrução
        self.label = ctk.CTkLabel(self, text="Escolha uma opção abaixo:", font=("Sans", 16))
        self.label.pack(pady=10)

        # Frame para botões
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.pack(pady=5)

        # Botões de ação
        opções = [
            ("Criar Arquivo", self.criar_arquivo),
            ("Editar Arquivo", self.editar_arquivo),
            ("Ler Arquivo", self.ler_arquivo),
            ("Limpar Arquivo", self.limpar_arquivo),
            ("Criar Cópia", self.copiar_arquivo),
            ("Sair",      self.quit)
        ]
        for i, (texto, cmd) in enumerate(opções):
            btn = ctk.CTkButton(self.buttons_frame, text=texto, command=cmd)
            btn.grid(row=i//2, column=i%2, padx=10, pady=5, sticky="ew")

        # Área de texto de saída
        self.textbox = ctk.CTkTextbox(self, width=500, height=180)
        self.textbox.pack(pady=10)

        # Entradas de nome e texto
        self.filename_entry = ctk.CTkEntry(self, placeholder_text="Nome do arquivo (sem .txt)")
        self.filename_entry.pack(pady=5)
        self.text_entry = ctk.CTkEntry(self, placeholder_text="Texto para editar ou nome de destino")
        self.text_entry.pack(pady=5)

    def _limpar_textbox(self):
        self.textbox.delete("0.0", "end")

    def criar_arquivo(self):
        nome = self.filename_entry.get().strip()
        if not nome:
            self._limpar_textbox(); self.textbox.insert("0.0", "Nome inválido.")
            return
        arquivo = f"{nome}.txt"
        if os.path.exists(arquivo):
            msg = f"'{arquivo}' já existe."
        else:
            open(arquivo, "w", encoding="utf-8").close()
            msg = f"Arquivo '{arquivo}' criado."
        self._limpar_textbox(); self.textbox.insert("0.0", msg)

    def editar_arquivo(self):
        nome  = self.filename_entry.get().strip()
        texto = self.text_entry.get().strip()
        arquivo = f"{nome}.txt"
        if not nome or not texto:
            msg = "Informe nome e texto."
        elif not os.path.exists(arquivo):
            msg = f"'{arquivo}' não existe."
        else:
            with open(arquivo, "a", encoding="utf-8") as f:
                f.write(texto + "\n")
            msg = f"'{arquivo}' editado."
        self._limpar_textbox(); self.textbox.insert("0.0", msg)

    def ler_arquivo(self):
        nome = self.filename_entry.get().strip()
        arquivo = f"{nome}.txt"
        if not nome:
            self._limpar_textbox(); self.textbox.insert("0.0", "Nome inválido.")
            return
        if not os.path.exists(arquivo):
            self._limpar_textbox(); self.textbox.insert("0.0", f"'{arquivo}' não encontrado.")
            return
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
        self._limpar_textbox(); self.textbox.insert("0.0", conteudo)

    def limpar_arquivo(self):
        nome = self.filename_entry.get().strip()
        arquivo = f"{nome}.txt"
        if not nome or not os.path.exists(arquivo):
            msg = "Nome inválido ou arquivo não existe."
        else:
            open(arquivo, "w", encoding="utf-8").close()
            msg = f"'{arquivo}' limpo."
        self._limpar_textbox(); self.textbox.insert("0.0", msg)

    def copiar_arquivo(self):
        origem  = self.filename_entry.get().strip()
        destino = self.text_entry.get().strip()
        arq_o = f"{origem}.txt"; arq_d = f"{destino}.txt"
        if not origem or not destino or not os.path.exists(arq_o):
            msg = "Verifique nomes e existência do arquivo de origem."
        else:
            with open(arq_o, "r", encoding="utf-8") as src:
                linhas = src.readlines()
            with open(arq_d, "w", encoding="utf-8") as dst:
                dst.writelines(linhas)
            msg = f"Cópia criada: '{arq_d}'."
        self._limpar_textbox(); self.textbox.insert("0.0", msg)

if __name__ == "__main__":
    app = FileManagerApp()
    app.mainloop()
