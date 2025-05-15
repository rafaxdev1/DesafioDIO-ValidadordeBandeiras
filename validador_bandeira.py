def identificar_bandeira(numero_cartao: str) -> str:
    """Identifica a bandeira do cartão com base no número inicial."""
    numero_cartao = numero_cartao.replace(" ", "")  # Remove espaços

    if numero_cartao.startswith("4"):
        return "Visa"
    elif numero_cartao[:2] in [str(n) for n in range(51, 56)]:
        return "MasterCard"
    elif numero_cartao.startswith("34") or numero_cartao.startswith("37"):
        return "American Express"
    elif numero_cartao.startswith("6"):
        return "Discover"
    else:
        return "Bandeira desconhecida"

if __name__ == "__main__":
    teste = [
        "4111 1111 1111 1111",
        "5500 0000 0000 0004",
        "3400 0000 0000 009",
        "6011 0000 0000 0004",
        "1234 5678 9012 3456"
    ]
    for cartao in teste:
        print(f"Número: {cartao} -> Bandeira: {identificar_bandeira(cartao)}")
