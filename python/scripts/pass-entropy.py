import argparse
import math
import string

def detect_charset(password):
    charset_size = 0
    used = set()

    if any(c in string.ascii_lowercase for c in password):
        charset_size += 26
        used.add("minúsculas")
    if any(c in string.ascii_uppercase for c in password):
        charset_size += 26
        used.add("maiúsculas")
    if any(c in string.digits for c in password):
        charset_size += 10
        used.add("dígitos")
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)
        used.add("símbolos")
    if any(c not in string.printable for c in password):
        charset_size += 100  # ajuste para unicode ou outros caracteres
        used.add("caracteres especiais")

    return charset_size, used

def calculate_entropy_from_password(password):
    charset_size, used_types = detect_charset(password)
    length = len(password)
    if charset_size == 0 or length == 0:
        return 0
    entropy = length * math.log2(charset_size)
    return entropy

def calculate_crack_time(entropy_bits, attempts_per_second):
    total_possibilities = 2 ** entropy_bits
    average_attempts = total_possibilities / 2
    seconds = average_attempts / attempts_per_second
    return seconds

def format_time(seconds):
    time_units = [
        ("segundos", 60),
        ("minutos", 60),
        ("horas", 24),
        ("dias", 365.25),
        ("anos", 1000),
        ("milênios", 1000),
        ("milhões de anos", 1000),
        ("bilhões de anos", 1000),
    ]

    value = seconds
    unit = "segundos"

    for name, factor in time_units:
        if value < factor:
            break
        value /= factor
        unit = name

    if value < 1:
        return f"< 1 {unit}"
    elif value < 10:
        return f"{value:.2f} {unit}"
    elif value < 100:
        return f"{value:.1f} {unit}"
    else:
        return f"{value:,.0f} {unit}".replace(",", ".")

def main():
    parser = argparse.ArgumentParser(description="Calcula o tempo médio para quebrar uma senha com base na entropia ou na própria senha.")
    parser.add_argument("entropy", type=float, nargs='?', help="Entropia da senha (em bits)")
    parser.add_argument("-a", "--attempts", type=float, default=1e9, help="Tentativas por segundo (padrão: 1e9)")
    parser.add_argument("-s", "--senha", type=str, help="Senha para calcular a entropia automaticamente")

    args = parser.parse_args()

    # Determina a entropia
    if args.senha:
        entropy = calculate_entropy_from_password(args.senha)
        print(f"Entropia calculada: {entropy:.2f} bits")
    elif args.entropy is not None:
        entropy = args.entropy
    else:
        print("Erro: forneça uma entropia ou uma senha com a flag -s/--senha.")
        return

    seconds = calculate_crack_time(entropy, args.attempts)
    readable_time = format_time(seconds)

    print(f"Tentativas por segundo: {args.attempts:,.0f}")
    print(f"Tempo médio estimado para quebra: {readable_time}")

if __name__ == "__main__":
    main()
