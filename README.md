# PayShield Switch

## English

### Overview

PayShield Switch is an ISO8583 message parser and simulator for payment switching flows. It accepts ISO8583 message strings and decodes core fields (MTI, F2, F3, F4, F7, F11, F37, F39) into a friendly JSON representation. The project also demonstrates how to build a simple endpoint for generating new ISO8583 messages by encoding parameters. This repository is part of the PayShield Platform, which simulates the payment ecosystem for educational purposes.

### Architecture

```text
Client    -> POST /parse  ->  Parser   -> JSON fields
Client    -> POST /build  ->  Builder  -> ISO8583 message
```

The service exposes two endpoints: `/parse` to decode a message and `/build` to assemble a message.

### OpenAPI / Swagger Docs

After running the API (e.g. `uvicorn main:app --reload`), visit `/docs` to view the interactive Swagger UI generated from the FastAPI application. The API defines:

- **POST /parse** – Accepts a JSON body with a `message` field containing an ISO8583 message string and returns a JSON object with decoded fields.
- **POST /build** – Accepts a JSON body with ISO8583 parameters (`mti`, `f2`, etc.) and returns a newly constructed ISO8583 message string.

### Use Cases

- Validate ISO8583 messages during integration tests.
- Simulate issuing or acquiring switch behavior by assembling ISO8583 messages.
- Learn how ISO8583 fields map to a modern JSON representation for educational purposes.

### Roadmap

- Support additional ISO8583 data elements (e.g. F35, F48, custom fields).
- Implement message validation and detailed error handling.
- Provide a CLI tool for offline message packing/unpacking.
- Add support for binary/hexadecimal encoding formats.

### Screenshots

Include screenshots of the Swagger UI and example parse/build responses to showcase how the service works.

### Disclaimer

This is an educational project. The implementation uses simplified parsing logic and does not implement the full ISO8583 specification. It is not intended for production use.

---

## Português

### Visão Geral

PayShield Switch é um analisador e simulador de mensagens ISO8583 para fluxos de switching de pagamentos. Aceita strings de mensagem ISO8583 e decodifica campos centrais (MTI, F2, F3, F4, F7, F11, F37, F39) em uma representação JSON amigável. O projeto também demonstra como construir um endpoint simples para gerar novas mensagens ISO8583 codificando parâmetros. Este repositório faz parte da PayShield Platform, que simula o ecossistema de pagamentos para fins educacionais.

### Arquitetura

```text
Cliente  -> POST /parse  ->  Parser   -> Campos JSON
Cliente  -> POST /build  ->  Builder  -> Mensagem ISO8583
```

O serviço expõe dois endpoints: `/parse` para decodificar uma mensagem e `/build` para montar uma mensagem.

### Documentação (Swagger / OpenAPI)

Após executar a API (por exemplo, `uvicorn main:app --reload`), acesse `/docs` para ver a interface interativa gerada pelo Swagger. A API define:

- **POST /parse** – Aceita um corpo JSON com o campo `message` contendo uma mensagem ISO8583 e retorna um objeto JSON com os campos decodificados.
- **POST /build** – Aceita um corpo JSON com parâmetros ISO8583 (`mti`, `f2`, etc.) e retorna uma mensagem ISO8583 recém-construída.

### Casos de Uso

- Validar mensagens ISO8583 durante testes de integração.
- Simular o comportamento de um switch adquirente ou emissor montando mensagens ISO8583.
- Aprender como os campos ISO8583 se mapeiam para uma representação JSON moderna para fins educacionais.

### Roadmap

- Suportar elementos de dados adicionais ISO8583 (por exemplo, F35, F48, campos customizados).
- Implementar validação de mensagens e tratamento detalhado de erros.
- Fornecer uma ferramenta de linha de comando (CLI) para empacotamento/desempacotamento offline.
- Adicionar suporte para formatos binário/hexadecimal.

### Capturas de Tela

Inclua capturas de tela da interface Swagger e das respostas de exemplo de parse/build para mostrar como o serviço funciona.

### Disclaimer

Este é um projeto educacional. A implementação usa lógica de parsing simplificada e não implementa toda a especificação ISO8583. Não se destina ao uso em produção.
