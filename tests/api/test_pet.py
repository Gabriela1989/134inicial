# bibliotecas
import json

import requests

# variaveis públicas
url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


# definições das funcções
def teste_incluir_pet():
    # 1 - configura
    # Dados de entrada provém do pet1.json

    # resultados esperados
    status_code_esperado = 200
    pet_id_esperado = 1280950
    pet_nome_esperado = "Thanos"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"

    # 2 - executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\dell\\PycharmProjects\\134inicial\\vendors\\json\\pet1.json')
    )
    # 3 - valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado


def teste_consultar_pet():
    # 1 - configura
    # Entrada/Parametro
    pet_id = '1280950'

    # resultados esperados
    status_code_esperado = 200
    pet_id_esperado = 1280950
    pet_nome_esperado = "Thanos"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"

    # 2 - executa
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers,
    )

    # 3 - valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)
    # imprimir como formato json
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado


def teste_alterar_pet():
    # 1 - configura
    # Dados de entrada provém do pet2.json

    # resultados esperados
    status_code_esperado = 200
    status_code_esperado = 200
    pet_id_esperado = 1280950
    pet_nome_esperado = "Thanos"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"


    # 2 - executa
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('C:\\Users\dell\\PycharmProjects\\134inicial\\vendors\\json\\pet2.json')
    )
    # 3 - valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)
    # imprimir como formato json
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado
