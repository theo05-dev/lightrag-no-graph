# LightRAG sem GraphRAG — Deploy para Render

Este repositório contém uma API FastAPI que utiliza o LightRAG **completamente sem GraphRAG**, ideal para uso com n8n e Render.

---

## 🚀 Endpoints

### POST /insert_pdf  
Envia um PDF para ser indexado.

### GET /query?q=...  
Realiza consultas na base vetorizada.

### GET /health  
Mostra se o grafo existe (deve sempre ser `false`).

---

## 🛠 Deploy no Render

1. Crie um novo Web Service no Render  
2. Conecte este repositório  
3. Render detecta o Dockerfile automaticamente  
4. Adicione variáveis do `.env.example` (NÃO USE PIPELINE_HOST)  
5. Deploy

---

## 🔗 Integração com n8n
Use HTTP Request Node:

- **POST** → `/insert_pdf`
- **GET** → `/query`
