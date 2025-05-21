import tkinter as tk
from tkinter import ttk, messagebox
from data.gerenciar_sala import carregar_salas
from data.gerenciar_filmes import filmes as lista_filmes
from data.gerenciar_assentos import (
    carregar_assentos, init_sala, gerar_mapa, salvar_assentos
)

class TicketApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Venda de Ingressos")
        self.geometry("600x500")
        # Carrega dados
        salas_list = carregar_salas()
        self.salas = {s['numero']: s for s in salas_list}
        self.filmes = lista_filmes
        self.assentos = carregar_assentos()

        # Frame de configurações
        cfg = tk.Frame(self)
        cfg.pack(pady=10, fill="x")

        tk.Label(cfg, text="Filme:").grid(row=0, column=0, sticky="w")
        self.cb_filmes = ttk.Combobox(cfg,
            values=[f['titulo'] for f in self.filmes],
            state="readonly"
        )
        self.cb_filmes.grid(row=0, column=1, padx=5)
        self.cb_filmes.bind("<<ComboboxSelected>>", self.on_filme)

        tk.Label(cfg, text="Sala:").grid(row=1, column=0, sticky="w")
        self.cb_salas = ttk.Combobox(cfg, values=[], state="disabled")
        self.cb_salas.grid(row=1, column=1, padx=5)
        self.cb_salas.bind("<<ComboboxSelected>>", self.on_sala)

        # Frame para mapa de assentos
        self.map_frame = tk.Frame(self)
        self.map_frame.pack(pady=20)

    def on_filme(self, event):
        """Popula combobox de salas ao escolher filme."""
        titulo = self.cb_filmes.get()
        film = next((f for f in self.filmes if f['titulo']==titulo), None)
        salas_disp = film.get('salas', []) if film else []
        self.cb_salas.config(values=salas_disp, state="readonly")
        if salas_disp:
            self.cb_salas.current(0)
            self.on_sala(None)

    def on_sala(self, event):
        """Gera e exibe o mapa de assentos para a sala selecionada."""
        # Limpa mapa antigo
        for w in self.map_frame.winfo_children():
            w.destroy()

        sala_num = self.cb_salas.get()
        if sala_num not in self.salas:
            return

        info = self.salas[sala_num]
        # Garante existência de entradas de assentos
        init_sala(self.assentos, sala_num,
                  info['linhas'], info['colunas'])
        mapa = gerar_mapa(self.assentos[sala_num])

        # Criar botões conforme o mapa
        for r, row in enumerate(mapa):
            for c, code in enumerate(row):
                if code == "XX":
                    btn = tk.Button(self.map_frame, text="XX",
                        width=4, state="disabled", bg="#e74c3c")
                else:
                    btn = tk.Button(self.map_frame, text=code,
                        width=4, bg="#2ecc71",
                        command=lambda seat=code: self.reservar(seat))
                btn.grid(row=r, column=c, padx=2, pady=2)

    def reservar(self, seat):
        """Marca o assento, persiste e atualiza o botão."""
        sala_num = self.cb_salas.get()
        if self.assentos[sala_num].get(seat):
            messagebox.showerror("Erro", "Assento já ocupado.")
            return

        # Confirmação
        if not messagebox.askyesno(
            "Confirmação",
            f"Reservar assento {seat} em sala {sala_num}?"
        ):
            return

        # Marca e salva
        self.assentos[sala_num][seat] = True
        salvar_assentos(self.assentos)
        messagebox.showinfo(
            "Sucesso",
            f"Ingresso vendido:\n{self.cb_filmes.get()} - Sala {sala_num} - Assento {seat}"
        )
        # Atualiza mapa
        self.on_sala(None)

if __name__ == "__main__":
    app = TicketApp()
    app.mainloop()
