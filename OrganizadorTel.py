def processar_telefones():
    print("Digite os números de telefone seguidos das datas (um por linha). Digite 'ok' para finalizar:")

    dados = []
    while True:
        linha = input()
        if linha.strip().lower() == "ok":
            break
        dados.append(linha)

    telefones = " / ".join([linha.split("\t")[0] for linha in dados if "\t" in linha])
    print("\nTelefones formatados:\n" + telefones)

while True:
    processar_telefones()
    opcao = input("\nDigite 1 para uma nova inserção ou 2 para finalizar: ").strip()
    if opcao == "2":
        print("Finalizando o programa...")
        break
