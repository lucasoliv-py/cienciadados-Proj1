




# A função que lê dois números

def leitora_numeros() -> list:
    """ Esta função pega dois números digitados pelo usuário"""
    i = 0
    numeros = []
    while i < 2:
        numeros.append(float(input(f"Digite o número {i+1} que deseja operar:")))
        i+=1
    return numeros


def leitora_operacao() -> str:
    operacao = input("""Digite a operação que deseja realizar. 
Pressione:
+ para adição;
- para subtração;
* para multiplicação;
/ para divisão""")
    return operacao


def leitora() -> list:
    lista_numeros = leitora_numeros()
    operacao = leitora_operacao()
    return [lista_numeros, operacao]


def escritora(resultado: float) -> None:
    """Esta função coloca o resultado na tela."""
    print(f"O resultado da minha operação é igual a {resultado}.")
