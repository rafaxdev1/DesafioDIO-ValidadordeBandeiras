# Validador de Bandeiras de Cartão de Crédito com GitHub Copilot

## Descrição

Este projeto simples identifica a bandeira (Visa, MasterCard, American Express, Discover) de um cartão de crédito com base no número fornecido. O desenvolvimento foi acelerado com o uso do GitHub Copilot, que sugeriu trechos de código e auxiliou na implementação.

## Como Funciona

O programa analisa os primeiros dígitos do número do cartão para identificar a bandeira, seguindo regras comuns de prefixos:

- Visa: começa com 4
- MasterCard: começa com números entre 51 e 55
- American Express: começa com 34 ou 37
- Discover: começa com 6

## Como Usar

1. Clone o repositório.
2. Execute o script Python:
   ```
   python validador_bandeira.py
   ```
3. Veja o resultado da identificação para cartões de exemplo.

## Estrutura do Repositório

```bash
📦 validador-bandeiras-cartao/
├── validador_bandeira.py          # Código-fonte do validador
└── README.md                     # Documentação do projeto
```

## Tecnologias Utilizadas

- Python 3
- GitHub Copilot (assistente de codificação)

## Contribuição

Contribuições são bem-vindas! Faça um fork do projeto e envie pull requests.

## Licença

MIT License
