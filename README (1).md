
# 🏋️‍♂️ API de Atletas

API desenvolvida com **FastAPI** para gerenciamento de **atletas**, **categorias esportivas** e **centros de treinamento**.

## 📚 Sumário

- [Tecnologias](#tecnologias)
- [Recursos da API](#recursos-da-api)
- [Estrutura dos endpoints](#estrutura-dos-endpoints)
- [Exemplo de uso com paginação](#exemplo-de-uso-com-paginação)
- [Licença](#licença)

---

## 🚀 Tecnologias

- Python 3.12+
- FastAPI
- SQLAlchemy 2
- Uvicorn
- PostgreSQL
- fastapi-pagination

---

## 🔧 Recursos da API

- **Atletas**
  - Criar, listar, buscar por ID, atualizar e deletar atletas
  - Filtros por `nome` e `cpf`
  - Paginação com `limit` e `offset`
  - Validação e retorno customizado de erros de integridade (ex: CPF duplicado)
- **Categorias**
  - CRUD completo
- **Centros de Treinamento**
  - CRUD completo

---

## 📌 Estrutura dos endpoints

### Atletas

| Método | Endpoint           | Descrição                          |
|--------|--------------------|------------------------------------|
| GET    | `/atletas/`        | Lista todos os atletas             |
| GET    | `/atletas/{id}`    | Consulta atleta por ID             |
| POST   | `/atletas/`        | Cria um novo atleta                |
| PATCH  | `/atletas/{id}`    | Edita um atleta                    |
| DELETE | `/atletas/{id}`    | Remove um atleta                   |

### Filtros de busca disponíveis:

- `nome`
- `cpf`

Exemplo:

```
GET /atletas/?nome=João&cpf=12345678900
```

---

## 🔄 Exemplo de uso com paginação

A API suporta:

- `limit` – número de itens por página
- `offset` – número de itens a pular

Exemplo:

```
GET /atletas/?limit=10&offset=0
```

---

## ❗ Tratamento de erros

- Se o CPF já estiver cadastrado:

```json
{
  "detail": "Já existe um atleta cadastrado com o cpf: 12345678900"
}
```
Status: `303 See Other`

---
