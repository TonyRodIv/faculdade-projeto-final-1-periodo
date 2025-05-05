from tkinter import messagebox, simpledialog, Toplevel, Label, Entry, Button, StringVar, Frame, Listbox, Scrollbar, END

def mostrar_mensagem(titulo, conteudo):
    messagebox.showinfo(titulo, conteudo)

# Classe para representar um funcionário
class Funcionario:
    def __init__(self, id, nome, cargo, salario_base):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.salario_base = salario_base
        self.descontos = 0
        self.bonus = 0
    
    def calcular_salario_liquido(self):
        return self.salario_base - self.descontos + self.bonus
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.cargo} - R$ {self.salario_base:.2f}"

# Classe para gerenciar o banco de dados de funcionários
class BancoDados:
    def __init__(self):
        self.funcionarios = {}
        self.proximo_id = 1
    
    def adicionar_funcionario(self, nome, cargo, salario_base):
        id = self.proximo_id
        self.funcionarios[id] = Funcionario(id, nome, cargo, float(salario_base))
        self.proximo_id += 1
        return id
    
    def remover_funcionario(self, id):
        if id in self.funcionarios:
            del self.funcionarios[id]
            return True
        return False
    
    def obter_funcionario(self, id):
        return self.funcionarios.get(id)
    
    def listar_funcionarios(self):
        return list(self.funcionarios.values())

# Instância global do banco de dados
banco = BancoDados()

# Funções de diálogo
def adicionar_funcionario_dialog(parent):
    dialog = Toplevel(parent)
    dialog.title("Adicionar Funcionário")
    dialog.geometry("300x200")
    dialog.grab_set()  # Torna o diálogo modal
    
    # Variáveis para armazenar os dados
    nome_var = StringVar()
    cargo_var = StringVar()
    salario_var = StringVar()
    
    # Frame para organizar os widgets
    frame = Frame(dialog)
    frame.pack(padx=10, pady=10)
    
    # Campos de entrada
    Label(frame, text="Nome:").grid(row=0, column=0, sticky="w")
    Entry(frame, textvariable=nome_var, width=30).grid(row=0, column=1, pady=5)
    
    Label(frame, text="Cargo:").grid(row=1, column=0, sticky="w")
    Entry(frame, textvariable=cargo_var, width=30).grid(row=1, column=1, pady=5)
    
    Label(frame, text="Salário Base:").grid(row=2, column=0, sticky="w")
    Entry(frame, textvariable=salario_var, width=30).grid(row=2, column=1, pady=5)
    
    # Função para processar o cadastro
    def salvar():
        nome = nome_var.get()
        cargo = cargo_var.get()
        salario = salario_var.get()
        
        if not nome or not cargo or not salario:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        try:
            salario = float(salario)
            if salario <= 0:
                raise ValueError("Salário deve ser positivo")
        except ValueError:
            messagebox.showerror("Erro", "Salário inválido!")
            return
        
        # Adiciona o funcionário ao banco de dados
        id = banco.adicionar_funcionario(nome, cargo, salario)
        messagebox.showinfo("Sucesso", f"Funcionário cadastrado com ID: {id}")
        dialog.destroy()
    
    # Botões
    Button(dialog, text="Salvar", command=salvar).pack(side="left", padx=10, pady=10)
    Button(dialog, text="Cancelar", command=dialog.destroy).pack(side="right", padx=10, pady=10)

def listar_funcionarios_dialog(parent):
    dialog = Toplevel(parent)
    dialog.title("Lista de Funcionários")
    dialog.geometry("400x300")
    dialog.grab_set()
    
    # Frame para a listbox e scrollbar
    frame = Frame(dialog)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Listbox com scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")
    
    listbox = Listbox(frame, width=50, height=15)
    listbox.pack(side="left", fill="both", expand=True)
    
    # Configurar scrollbar
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    
    # Preencher a listbox com os funcionários
    funcionarios = banco.listar_funcionarios()
    for func in funcionarios:
        listbox.insert(END, str(func))
    
    if not funcionarios:
        listbox.insert(END, "Nenhum funcionário cadastrado")
    
    # Botão para fechar
    Button(dialog, text="Fechar", command=dialog.destroy).pack(pady=10)

def calcular_salario_dialog(parent):
    # Primeiro, pede o ID do funcionário
    id_str = simpledialog.askstring("Consulta", "Digite o ID do funcionário:")
    if not id_str:
        return
    
    try:
        id = int(id_str)
    except ValueError:
        messagebox.showerror("Erro", "ID inválido!")
        return
    
    # Busca o funcionário
    funcionario = banco.obter_funcionario(id)
    if not funcionario:
        messagebox.showerror("Erro", "Funcionário não encontrado!")
        return
    
    # Abre um diálogo para mostrar e calcular o salário
    dialog = Toplevel(parent)
    dialog.title(f"Calcular Salário - {funcionario.nome}")
    dialog.geometry("350x250")
    dialog.grab_set()
    
    # Variáveis
    descontos_var = StringVar(value=str(funcionario.descontos))
    bonus_var = StringVar(value=str(funcionario.bonus))
    
    # Frame principal
    frame = Frame(dialog)
    frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Dados do funcionário
    Label(frame, text=f"ID: {funcionario.id}").grid(row=0, column=0, columnspan=2, sticky="w", pady=2)
    Label(frame, text=f"Nome: {funcionario.nome}").grid(row=1, column=0, columnspan=2, sticky="w", pady=2)
    Label(frame, text=f"Cargo: {funcionario.cargo}").grid(row=2, column=0, columnspan=2, sticky="w", pady=2)
    Label(frame, text=f"Salário Base: R$ {funcionario.salario_base:.2f}").grid(row=3, column=0, columnspan=2, sticky="w", pady=2)
    
    # Campos para descontos e bônus
    Label(frame, text="Descontos (R$):").grid(row=4, column=0, sticky="w", pady=5)
    Entry(frame, textvariable=descontos_var, width=10).grid(row=4, column=1, sticky="w", pady=5)
    
    Label(frame, text="Bônus (R$):").grid(row=5, column=0, sticky="w", pady=5)
    Entry(frame, textvariable=bonus_var, width=10).grid(row=5, column=1, sticky="w", pady=5)
    
    # Função para atualizar o salário líquido
    def atualizar_salario():
        try:
            funcionario.descontos = float(descontos_var.get())
            funcionario.bonus = float(bonus_var.get())
            salario_liquido = funcionario.calcular_salario_liquido()
            resultado_label.config(text=f"Salário Líquido: R$ {salario_liquido:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos!")
    
    # Botão para calcular
    Button(frame, text="Calcular", command=atualizar_salario).grid(row=6, column=0, columnspan=2, pady=10)
    
    # Label para mostrar o resultado
    resultado_label = Label(frame, text="Salário Líquido: R$ 0.00")
    resultado_label.grid(row=7, column=0, columnspan=2, pady=5)
    
    # Atualiza o salário inicialmente
    atualizar_salario()
    
    # Botão para fechar
    Button(dialog, text="Fechar", command=dialog.destroy).pack(pady=5)

def gerar_relatorio_dialog(parent):
    # Abre um diálogo para mostrar o relatório completo
    dialog = Toplevel(parent)
    dialog.title("Relatório de Folha de Pagamento")
    dialog.geometry("500x400")
    dialog.grab_set()
    
    # Frame para a listbox e scrollbar
    frame = Frame(dialog)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Listbox com scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")
    
    listbox = Listbox(frame, width=70, height=20, font=("Courier New", 10))
    listbox.pack(side="left", fill="both", expand=True)
    
    # Configurar scrollbar
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    
    # Cabeçalho do relatório
    listbox.insert(END, "RELATÓRIO DE FOLHA DE PAGAMENTO")
    listbox.insert(END, "-" * 65)
    listbox.insert(END, f"{'ID':<5}{'Nome':<30}{'Cargo':<20}{'Salário Base':<15}{'Líquido':<15}")
    listbox.insert(END, "-" * 65)
    

    funcionarios = banco.listar_funcionarios()
    total_folha = 0
    
    for func in funcionarios:
        salario_liquido = func.calcular_salario_liquido()
        total_folha += salario_liquido
        listbox.insert(END, f"{func.id:<5}{func.nome:<30}{func.cargo:<20}R$ {func.salario_base:<12.2f}R$ {salario_liquido:<12.2f}")
    
    listbox.insert(END, "-" * 65)
    listbox.insert(END, f"Total da Folha de Pagamento: R$ {total_folha:.2f}")
    
    if not funcionarios:
        listbox.insert(END, "Nenhum funcionário cadastrado")
    
    # Botão para fechar
    Button(dialog, text="Fechar", command=dialog.destroy).pack(pady=10)