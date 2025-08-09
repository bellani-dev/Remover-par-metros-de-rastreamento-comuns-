# Ad Tracker Buster

🚫 **Objetivo**: Remover parâmetros de rastreamento comuns de URLs antes de acessar sites como Google Ads, Facebook Ads, entre outros.

## 📜 O que são os Parâmetros de Rastreamento?

Parâmetros de rastreamento são adicionados às URLs por plataformas como o Google Ads, Facebook Ads e outras ferramentas de marketing. Eles servem para monitorar a origem dos acessos e a performance das campanhas publicitárias. No entanto, eles podem coletar dados sobre sua navegação e seus hábitos online, o que pode ser uma preocupação para a privacidade.

Exemplos de parâmetros de rastreamento:
- `utm_source`
- `utm_medium`
- `utm_campaign`
- `gclid`
- `fbclid`

## 🚀 Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/ad-tracker-buster.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:
   ```bash
   python ad_tracker_buster.py
   ```

O script irá remover os parâmetros de rastreamento de uma URL de exemplo.

## 💡 Como Funciona?

Este script examina uma URL e remove os parâmetros de rastreamento comuns, como `utm_*` e `gclid`, deixando a URL limpa para ser acessada sem os rastros. 

### Exemplo de uso:

```python
url = "https://example.com/?utm_source=google&utm_medium=cpc&gclid=abc123"
clean_url = remove_tracking(url)
print(f"URL original: {url}")
print(f"URL limpa: {clean_url}")
```

## 🔧 Dependências

Não há dependências externas necessárias além do Python, mas se você quiser usar para testar URLs em larga escala, pode instalar o pacote `requests`:
```bash
pip install requests
```

## 🔒 Privacidade

Essa ferramenta ajuda a proteger a sua privacidade, removendo os rastros deixados em URLs quando você acessa sites com parâmetros de rastreamento. Isso ajuda a evitar o monitoramento e a coleta de dados sobre a sua navegação.

## 📑 Contribuições

Sinta-se à vontade para contribuir com este projeto! Se você deseja melhorar a ferramenta ou adicionar novos parâmetros de rastreamento à lista, envie um pull request.

---
**Autor**: Bellani Dev (https://github.com/bellani-dev)
