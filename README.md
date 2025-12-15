# AWS Lambda Echo API

Projeto simples para demonstrar integração entre **AWS Lambda**, **API Gateway** e **CloudWatch Logs** usando Python.

## 🚀 Funcionalidades

- Endpoint `/health` para verificação de status
- Endpoint `/echo` que retorna a mensagem enviada pelo cliente
- Validação de entrada JSON
- Logs estruturados no CloudWatch
- Versionamento com Git

## 🧱 Arquitetura

- AWS Lambda (Python 3.12)
- Amazon API Gateway (REST API)
- Amazon CloudWatch Logs

## 📌 Endpoints

### GET /health
Retorna o status da API.

**Resposta**
```json
{
  "status": "ok"
}
