#!/usr/bin/env python3
import argparse
import hashlib

def calcular_checksum(texto: str, algoritmo: str) -> str:
    """Calcula o checksum do texto usando o algoritmo especificado."""
    if algoritmo not in hashlib.algorithms_available:
        raise ValueError(f"Algoritmo '{algoritmo}' não suportado.")
    
    hash_obj = hashlib.new(algoritmo)
    hash_obj.update(texto.encode('utf-8'))
    return hash_obj.hexdigest()

def main():
    parser = argparse.ArgumentParser(
        description="Calcula o checksum (hash) de uma string."
    )
    parser.add_argument(
        "texto",
        help="Texto para calcular o checksum."
    )
    parser.add_argument(
        "-a", "--algoritmo",
        default="sha256",
        help="Algoritmo de hash (ex: md5, sha1, sha256). Padrão: sha256"
    )

    args = parser.parse_args()

    try:
        resultado = calcular_checksum(args.texto, args.algoritmo)
        print(f"{args.algoritmo.upper()} checksum: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
