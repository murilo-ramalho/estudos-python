import argparse
import hashlib
import blake3
import random
import string
import unicodedata

# Fonemas base
CONSOANTES = [
    "b", "d", "f", "g", "h", "j", "k", "l", "m", "n",
    "p", "r", "s", "t", "v", "z", "y", "w", "x", "ch",
    "sh", "th", "qu", "c", "ç", "ñ", "zh", "ph", "gh", "ng", "ts", "dz"
]

VOGAIS_COM_ACENTO = [
    "a", "e", "i", "o", "u", "á", "é", "í"
]

VOGAIS_SEM_ACENTO = [
    "a", "e", "i", "o", "u"
]

def remover_acentos(s: str) -> str:
    """Remove acentos de uma string"""
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def gerar_silaba(bits, usar_acentos=True):
    consoante_idx = int(bits[:5], 2) % len(CONSOANTES)
    vogais = VOGAIS_COM_ACENTO if usar_acentos else VOGAIS_SEM_ACENTO
    vogal_idx = int(bits[5:], 2) % len(vogais)
    return CONSOANTES[consoante_idx] + vogais[vogal_idx]

def gerar_nome(hash_bin: str, num_silabas: int, usar_acentos: bool) -> str:
    nome = ""
    for i in range(num_silabas):
        start = i * 8
        bloco = hash_bin[start:start+8]
        if len(bloco) < 8:
            bloco = bloco.ljust(8, "0")
        silaba = gerar_silaba(bloco, usar_acentos)
        nome += silaba
    return nome.capitalize()

def aplicar_hash(entrada: str, algoritmo: str = "blake3") -> str:
    entrada_bytes = entrada.encode()
    h = blake3.blake3(entrada_bytes).hexdigest()
    return bin(int(h, 16))[2:].zfill(len(h) * 4)

def gerar_salt(tamanho=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

def gerar_nomes(input_base: str, num_silabas: int, rodadas: int = 10, algoritmo: str = "blake3", usar_acentos=True):
    if not (2 <= num_silabas <= 7):
        raise ValueError("Número de sílabas deve estar entre 2 e 7.")

    nomes = []
    for _ in range(rodadas):
        salt = gerar_salt()
        entrada = f"{input_base}::{salt}"
        hash_bin = aplicar_hash(entrada, algoritmo)
        nome = gerar_nome(hash_bin, num_silabas, usar_acentos)
        nomes.append(nome)
    return nomes

# CLI
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🔤 Gerador de Nomes Fonéticos Universais")
    parser.add_argument("--entrada", "-e", required=True, help="Texto base para gerar os nomes")
    parser.add_argument("--silabas", "-s", type=int, required=True, help="Número de sílabas (2–7)")
    parser.add_argument("--sem-acento", "-na", action="store_true", help="Remover acentos das vogais nas sílabas")

    args = parser.parse_args()

    try:
        nomes = gerar_nomes(
            input_base=args.entrada,
            num_silabas=args.silabas,
            usar_acentos=not args.sem_acento
        )
        print("\nNomes gerados:")
        for i, nome in enumerate(nomes, 1):
            print(f"{i}. {nome}")
    except ValueError as e:
        print(f"Erro: {e}")
