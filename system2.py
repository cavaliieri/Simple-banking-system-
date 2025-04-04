import tkinter as tk
from tkinter import messagebox

# Dados iniciais
saldo = 0.0
limite = 500
extrato = []
saques_feitos = 0
LIMITE_SAQUES = 3

# Funções
def depositar():
    global saldo
    try:
        valor = float(entrada_valor.get())
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            messagebox.showinfo("Depósito", f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            messagebox.showwarning("Erro", "Informe um valor positivo para depósito.")
    except:
        messagebox.showerror("Erro", "Digite um valor válido.")

def sacar():
    global saldo, saques_feitos
    try:
        valor = float(entrada_valor.get())
        if saques_feitos >= LIMITE_SAQUES:
            messagebox.showwarning("Limite atingido", "Você atingiu o limite de saques diários.")
        elif valor > saldo:
            messagebox.showwarning("Saldo insuficiente", "Você não tem saldo suficiente.")
        elif valor > limite:
            messagebox.showwarning("Limite", f"O limite por saque é de R$ {limite:.2f}")
        elif valor <= 0:
            messagebox.showwarning("Erro", "Informe um valor positivo para saque.")
        else:
            saldo -= valor
            saques_feitos += 1
            extrato.append(f"Saque: R$ {valor:.2f}")
            messagebox.showinfo("Saque", f"Saque de R$ {valor:.2f} realizado com sucesso.")
    except:
        messagebox.showerror("Erro", "Digite um valor válido.")

def ver_saldo():
    messagebox.showinfo("Saldo", f"Seu saldo atual é: R$ {saldo:.2f}")

def ver_extrato():
    if extrato:
        historico = "\n".join(extrato)
    else:
        historico = "Nenhuma movimentação realizada."
    messagebox.showinfo("Extrato", f"{historico}\n\nSaldo atual: R$ {saldo:.2f}")

# Interface gráfica
janela = tk.Tk()
janela.title("Banco Tkinter")
janela.geometry("400x400")

# Entrada de valor
tk.Label(janela, text="Digite o valor:").pack(pady=10)
entrada_valor = tk.Entry(janela)
entrada_valor.pack(pady=5)

# Botões
tk.Button(janela, text="Depositar", command=depositar).pack(fill='x', padx=20, pady=5)
tk.Button(janela, text="Sacar", command=sacar).pack(fill='x', padx=20, pady=5)
tk.Button(janela, text="Ver Saldo", command=ver_saldo).pack(fill='x', padx=20, pady=5)
tk.Button(janela, text="Ver Extrato", command=ver_extrato).pack(fill='x', padx=20, pady=5)
tk.Button(janela, text="Sair", command=janela.quit).pack(fill='x', padx=20, pady=20)

janela.mainloop()
