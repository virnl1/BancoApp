import tkinter as tk
from tkinter import messagebox
from main import ContaBancaria  # Importa a classe POO


class BancoApp:
    def __init__(self, master, conta):
        self.master = master
        self.conta = conta
        master.title("Sistema Bancário")

        # Título
        self.label = tk.Label(master, text=f"Bem-vindo, {self.conta.titular}!", font=("Arial", 14))
        self.label.pack(pady=10)

        # Entrada de valor
        self.valor_entry = tk.Entry(master, width=20)
        self.valor_entry.pack(pady=5)

        # Botões
        tk.Button(master, text="Depositar", command=self.depositar).pack(pady=5)
        tk.Button(master, text="Sacar", command=self.sacar).pack(pady=5)
        tk.Button(master, text="Ver Saldo", command=self.ver_saldo).pack(pady=5)

    # Funções dos botões
    def depositar(self):
        try:
            valor = float(self.valor_entry.get())
            if self.conta.depositar(valor):
                messagebox.showinfo("Depósito", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                messagebox.showwarning("Erro", "Valor inválido para depósito.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico.")
        self.valor_entry.delete(0, tk.END)

    def sacar(self):
        try:
            valor = float(self.valor_entry.get())
            if self.conta.sacar(valor):
                messagebox.showinfo("Saque", f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                messagebox.showwarning("Erro", "Saldo insuficiente ou valor inválido.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico.")
        self.valor_entry.delete(0, tk.END)

    def ver_saldo(self):
        saldo = self.conta.get_saldo()
        messagebox.showinfo("Saldo", f"Saldo atual: R$ {saldo:.2f}")

            
            # Execução da aplicação
if  __name__ == "__main__":
    conta = ContaBancaria("Marcos Vinicius", 1000)  # Exemplo de criação de conta
    root = tk.Tk()
    app = BancoApp(root,conta)
    root.mainloop()