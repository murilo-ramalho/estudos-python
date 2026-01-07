import requests
from typing import List

BASE_URL = "https://x"
GET_ENDPOINT = f"{BASE_URL}?param1=x&param2=y"
PATCH_ENDPOINT_TEMPLATE = f"{BASE_URL}/{{id}}"

ORIGIN = "https://x"
TIMEOUT = 60
HEADERS = {
    "Content-Type": "application/json",
    "Origin": ORIGIN
}
PATCH_BODY = [
    {
        "path": "/y",
        "op": "replace",
        "value": 2
    }
]

def pre_request() -> str:
    url = "https://x"

    headers = {
        "Content-Type": "application/json",
        "Origin": "https://x"
    }

    body = {
        "login": "x",
        "senha": "x"
    }

    response = requests.post(
        url,
        headers=headers,
        json=body,
        timeout=TIMEOUT
    )

    response.raise_for_status()
    print(response.json())

    token = response.json().get("token")

    if not token:
        raise RuntimeError("Token não retornado pela API de autenticação")

    return token


def get_ids_com_situacao_7() -> List[int]:
    print("Executando GET...")

    response = requests.get(
        GET_ENDPOINT,
        headers=HEADERS,
        timeout=TIMEOUT
    )
    response.raise_for_status()

    payload = response.json()

    items = payload.get("items", [])
    if not isinstance(items, list):
        raise ValueError("Formato inesperado: 'items' não é uma lista")

    ids = [
        item["id"]
        for item in items
        if item.get("y") == 1
    ]

    print(f"{len(ids)} registros com y = 1 encontrados")
    return ids


def patch_situacao(ids: List[int]):
    for id_ in ids:
        url = PATCH_ENDPOINT_TEMPLATE.format(id=id_)

        print(f"PATCH ID {id_}")

        response = requests.patch(
            url,
            headers=HEADERS,
            json=PATCH_BODY,
            timeout=TIMEOUT
        )

        if response.status_code in (200, 204):
            print(f"ID {id_} atualizado para y = 2")
        else:
            print(f"Erro ID {id_} → {response.status_code}")
            print(response.text)

def main():
    token = pre_request()

    HEADERS["Authorization"] = f"Bearer {token}"

    ids = get_ids_com_situacao_7()

    if not ids:
        print("Nenhum registro para atualizar")
        return
    
    patch_situacao(ids)


if __name__ == "__main__":
    main()
