import tkinter as tk
from tkinter import ttk, messagebox

# --- LÓGICA DO SEU SISTEMA ---
def processar_cadastro():
    nome = entry_nome.get().strip()
    cidade = entry_cidade.get().strip()
    
    try:
        mensalidade = float(entry_mensalidade.get().replace(",", "."))
        cameras = int(entry_cameras.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos para Mensalidade e Câmeras.")
        return

    if not nome or not cidade:
        messagebox.showwarning("Aviso", "Preencha o Nome e a Cidade!")
        return

    # Lógica de tomada de decisão (Sua regra de negócio)
    if mensalidade >= 200:
        tipo_cliente = "Cliente Premium 💎"
    elif mensalidade >= 100:
        tipo_cliente = "Cliente Intermediário 🔵"
    else:
        tipo_cliente = "Cliente Básico 🟢"

    if cameras >= 5:
        tipo_residencia = "Residência Grande 🏠"
    elif cameras >= 2:
        tipo_residencia = "Residência Média 🏡"
    else:
        tipo_residencia = "Residência Pequena 🏠"

    lbl_res_cliente.config(text=f"Status: {tipo_cliente}")
    lbl_res_residencia.config(text=f"Tamanho: {tipo_residencia}")
    lbl_res_resumo.config(
        text=f"Cliente: {nome} | Cidade: {cidade}\nMensalidade: R$ {mensalidade:.2f} | Câmeras: {cameras}"
    )

# --- 🆕 NOVA FUNÇÃO PARA LIMPAR TUDO ---
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_mensalidade.delete(0, tk.END)
    entry_cameras.delete(0, tk.END)
    
    lbl_res_cliente.config(text="Status: Aguardando dados...")
    lbl_res_residencia.config(text="Tamanho: Aguardando dados...")
    lbl_res_resumo.config(text="")

# --- JANELA PRINCIPAL ---
janela = tk.Tk()
janela.title("VISITECH - Sistema de Cadastro v0.1")
janela.geometry("1032x600")
janela.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

lbl_titulo = ttk.Label(janela, text="VisiTech - Cadastro de Clientes", font=("Helvetica", 16, "bold"))
lbl_titulo.pack(pady=15)

# --- FORMULÁRIO DE ENTRADA ---
frame_form = ttk.LabelFrame(janela,text=" DADOS DO CONTRATO ", padding=15)
frame_form.pack(fill="x", padx=20, pady=5)

ttk.Label(frame_form, text="Nome do Cliente:").grid(row=0, column=0, sticky="w", pady=5)
entry_nome = ttk.Entry(frame_form, width=35)
entry_nome.grid(row=0, column=1, pady=5)

ttk.Label(frame_form, text="Cidade:").grid(row=1, column=0, sticky="w", pady=5)
entry_cidade = ttk.Entry(frame_form, width=35)
entry_cidade.grid(row=1, column=1, pady=5)

ttk.Label(frame_form, text="Valor da Mensalidade (R$):").grid(row=2, column=0, sticky="w", pady=5)
entry_mensalidade = ttk.Entry(frame_form, width=35)
entry_mensalidade.grid(row=2, column=1, pady=5)

ttk.Label(frame_form, text="Câmeras no Contrato:").grid(row=3, column=0, sticky="w", pady=5)
entry_cameras = ttk.Entry(frame_form, width=35)
entry_cameras.grid(row=3, column=1, pady=5)

# --- BOTÕES ---
btn_processar = ttk.Button(janela, text="Processar Dados 🚀", command=processar_cadastro)
btn_processar.pack(pady=5)
btn_relatorio = ttk.Button(janela, text="Relatório ",command=processar_cadastro)
btn_relatorio.pack(pady=6)

# 🆕 BOTÃO DE LIMPAR
btn_limpar = ttk.Button(janela, text="Limpar Dados 🧹", command=limpar_campos)
btn_limpar.pack(pady=5)

# --- PAINEL DE RESULTADOS ---
frame_resultado = ttk.LabelFrame(janela, text=" RESULTADOS DA ANÁLISE ", padding=15)
frame_resultado.pack(fill="x", padx=20, pady=5)

lbl_res_cliente = ttk.Label(frame_resultado, text="Status: Aguardando dados...", font=("Helvetica", 10, "bold"))
lbl_res_cliente.pack(anchor="w", pady=2)

lbl_res_residencia = ttk.Label(frame_resultado, text="Tamanho: Aguardando dados...", font=("Helvetica", 10, "bold"))
lbl_res_residencia.pack(anchor="w", pady=2)

lbl_res_resumo = ttk.Label(frame_resultado, text="", font=("Helvetica", 9), foreground="#555555")
lbl_res_resumo.pack(anchor="w", pady=5)

janela.mainloop()