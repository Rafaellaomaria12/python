capitais = {
    "Acre":"Rio Branco",
    "Alagoas":"Maceió",
    "Amapá":"Macapá",
    "Amazonas":"Manaus",
    "Bahia":"Salvador",
    "Ceará":"Fortaleza",
    "Espirito Santo":"Vitória",
    "Goiás":"Goiânia",
    "Maranhão":"São Luís",
    "Mato Grosso":"Cuiabá",
    "Mato Grosso do Sul":"Campo Grande",
    "Minas Gerais":"Belo Horizonte",
    "Pará":"Belém",
    "Paraíba":"João Pessoa",
    "Paraná":"Curitiba",
    "Pernambuco":"Recife",
    "Piauí":"Teresina",
    "Rio de Janeiro":"Rio de Janeiro",
    "Rio Grande do Norte":"Natal",
    "Rio Grande do Sul":"Porto Alegre",
    "Rondônia":"Porto Velho",
    "Roraima":"Boa Vista",
    "Santa Catarina":"Florianópolis",
    "Sergipe":"Aracaju",
    "Tocantins":"Palmas",
    "Distrito Federal":"Brasília (capital do país e sede do governo)"
}
# for i in capitais:
# print(i)
# dicionario n le como a gente faz por lista - Informação pelo nome da chave nome que vem antes dos ':'
# print(capitais[0:6])

print(capitais["Acre"])
# Pegar os seis primeiros itens 
ps = 1
for i in capitais:
    if ps < 6:
        print(i+" a capital é "+capitais[i])
    else:
        break
    ps+=1

'''SE ps for menor que 6 aparece no print se não quebra (break)'''