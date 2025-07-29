def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "baixo peso"
    elif imc < 25:
        return "peso adequado"
    elif imc < 30:
        return "sobrepeso"
    elif imc < 35:
        return "obesidade grau I"
    elif imc < 40:
        return "obesidade grau II"
    else:
        return "obesidade grau III"

def main():
    print("Calculadora de IMC")
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros): "))
    
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    
    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

# Executa a função principal
if __name__ == "__main__":
    main()
