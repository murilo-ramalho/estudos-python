import tkinter as tk
from tkinter import scrolledtext
import re

def excel_to_markdown(text):
    """
    Converte texto copiado do Excel (TABs) para Markdown simples,
    sem alinhamento e sem formatação visual extra.
    """

    # Remover linhas vazias
    lines = [line for line in text.split("\n") if line.strip()]

    # Quebra cada linha em colunas (TAB)
    rows = [line.split("\t") for line in lines]

    # Número total de colunas
    max_cols = max(len(r) for r in rows)

    # Normaliza o número de colunas
    for r in rows:
        while len(r) < max_cols:
            r.append("")

    # Cabeçalho
    header = "| " + " | ".join(rows[0]) + " |"

    # Separador estilo GitHub
    separator = "| " + " | ".join("---" for _ in range(max_cols)) + " |"

    # Corpo
    body = "\n".join("| " + " | ".join(r) + " |" for r in rows[1:])

    return header + "\n" + separator + "\n" + body


def markdown_to_excel(text):
    """
    Converte tabela Markdown para formato tipo Excel (TABs)
    """
    lines = [line.strip() for line in text.strip().split("\n") if "|" in line and "---" not in line]

    converted = []
    for line in lines:
        parts = [col.strip() for col in line.split("|")[1:-1]]  # remove bordas
        converted.append("\t".join(parts))

    return "\n".join(converted)


def detect_format(text):
    """
    Detecta automaticamente se o texto é Markdown ou tabela Excel
    """
    if "\t" in text:
        return "excel"
    if re.search(r"\|\s*.*\s*\|", text):
        return "markdown"
    return "unknown"


def convert():
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "Nenhum texto inserido.")
        return

    fmt = detect_format(input_text)

    if fmt == "excel":
        result = excel_to_markdown(input_text)
    elif fmt == "markdown":
        result = markdown_to_excel(input_text)
    else:
        result = "Formato não reconhecido. Cole tabela do Excel ou Markdown."

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)


# ==========================
#     GUI (Tkinter)
# ==========================
root = tk.Tk()
root.title("Conversor Tabela ↔ Markdown")

tk.Label(root, text="Entrada (Cole sua tabela aqui):").pack()
text_input = scrolledtext.ScrolledText(root, width=80, height=15)
text_input.pack()

tk.Button(root, text="Converter", command=convert, bg="#4CAF50", fg="white").pack(pady=10)

tk.Label(root, text="Saída (Resultado da conversão):").pack()
text_output = scrolledtext.ScrolledText(root, width=80, height=15)
text_output.pack()

root.mainloop()
