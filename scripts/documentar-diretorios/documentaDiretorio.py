import os
import tkinter as tk
from tkinter import filedialog, messagebox

def carregar_regras_ignore(caminho):
    if not os.path.exists(caminho):
        return []
    with open(caminho, encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip() and not l.startswith("#")]

def ignorar_path(path, regras):
    path = path.replace("\\", "/")
    ignorar = False
    for r in regras:
        negacao = r.startswith("!")
        regra = r[1:] if negacao else r
        regra = regra.rstrip("/")

        if regra.startswith("**/"):
            regra_dir = regra[3:]
            if f"/{regra_dir}/" in f"/{path}/" or path.endswith(regra_dir):
                ignorar = not negacao
        elif "/" not in regra:
            if os.path.basename(path) == regra:
                ignorar = not negacao
        else:
            if path == regra:
                ignorar = not negacao
    return ignorar

def processar_pasta(path, rel_path, regras_ignore, nivel=0, contador=None, linhas=None):
    if contador is None: contador = []
    if linhas is None: linhas = []

    nome = os.path.basename(path)
    if rel_path and ignorar_path(rel_path, regras_ignore):
        return

    while len(contador) <= nivel:
        contador.append(0)
    contador[nivel] += 1
    for i in range(nivel+1, len(contador)):
        contador[i] = 0

    numero = ".".join(str(c) for c in contador[:nivel+1] if c > 0)
    linhas.append(f"{'    '*nivel}{numero}. {nome} /")

    try:
        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
            item_rel = os.path.join(rel_path, item) if rel_path else item
            if os.path.isdir(item_path) and not ignorar_path(item_rel, regras_ignore):
                processar_pasta(item_path, item_rel, regras_ignore, nivel+1, contador, linhas)
    except PermissionError:
        pass

    return linhas

def gerar_arvore_numerada(root_path, output_file, ignore_file="ignore.txt"):
    regras_ignore = carregar_regras_ignore(ignore_file)
    linhas = ["# Índice de Pastas\n"] + processar_pasta(root_path, "", regras_ignore)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

def selecionar_pasta():
    pasta = filedialog.askdirectory(title="Selecione a pasta a ser analisada")
    if pasta:
        entrada_pasta.delete(0, tk.END)
        entrada_pasta.insert(0, pasta)

def selecionar_saida():
    arquivo = filedialog.asksaveasfilename(
        title="Salvar como", defaultextension=".md", filetypes=[("Markdown", "*.md")]
    )
    if arquivo:
        entrada_saida.delete(0, tk.END)
        entrada_saida.insert(0, arquivo)

def gerar():
    pasta, saida = entrada_pasta.get().strip(), entrada_saida.get().strip()
    if not pasta or not saida:
        messagebox.showwarning("Aviso", "Selecione a pasta e o arquivo de saída")
        return
    try:
        gerar_arvore_numerada(pasta, saida)
        messagebox.showinfo("Sucesso", f"Index gerado com sucesso!\nArquivo: {saida}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

root = tk.Tk()
root.title("Gerador de Índice de Pastas")

tk.Label(root, text="Pasta a ser analisada:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entrada_pasta = tk.Entry(root, width=50)
entrada_pasta.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Selecionar", command=selecionar_pasta).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Arquivo de saída:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entrada_saida = tk.Entry(root, width=50)
entrada_saida.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Selecionar", command=selecionar_saida).grid(row=1, column=2, padx=5, pady=5)

tk.Button(root, text="Gerar", width=20, command=gerar).grid(row=2, column=0, columnspan=3, pady=15)

root.mainloop()
