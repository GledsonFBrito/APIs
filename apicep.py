import requests

while True:
    print('*' * 25)
    cep = (input("Digite seu CEP: "))
    if len(cep) == 8:

        try:
            cep = int(cep)
            r_cep = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            r_cep = r_cep.json()
            cep_da_cidade = f'Cep: {r_cep["cep"]}'
            localidade = f'Cidade: {r_cep["localidade"]}'
            bairro = f'Bairro: {r_cep["bairro"]}'



            print(cep_da_cidade)
            print(localidade)
            print(bairro)
        except:
            print('Cep não encontrado!')
    else:
        print("Cep deve conter apenas 8 numero sem caracteres especiais!")
