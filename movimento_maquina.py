"""Algoritmo para movimentar uma máquina com base em 0 e 1."""


def movimentar_maquina(sequencia):
    """Converte uma sequencia binária em movimentos e calcula a posiçãoo final."""
    movimentos = []
    posicao = 0

    for indice, digito in enumerate(sequencia):
        if digito == "0":
            movimentos.append("Esquerda")
            posicao -= 1
        elif digito == "1":
            movimentos.append("Direita")
            posicao += 1
        else:
            raise ValueError(
                f"Digito invalido na posição {indice}: {digito!r}. "
                "Use apenas 0 e 1."
            )

    return movimentos, posicao


def main():
    while True:
        sequencia = input(
            "Digite uma sequência de 0 e 1 ou escreva 'sair' para terminar: "
        ).strip()

        if sequencia.lower() == "sair":
            print("Programa terminado.")
            break

        if not sequencia:
            print("Nenhum comando informado.\n")
            continue

        try:
            movimentos, posicao = movimentar_maquina(sequencia)
        except ValueError as erro:
            print(f"Erro: {erro}\n")
            continue

        print("Movimentos da máquina:")
        for passo, movimento in enumerate(movimentos, start=1):
            print(f"{passo}. {movimento}")

        print(f"Posição final: {posicao}\n")


if __name__ == "__main__":
    main()
