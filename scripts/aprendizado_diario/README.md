# Aprendizado Jurídico Diário

Este módulo faz parte da inteligência contínua do Motor Tributário. Seu objetivo é buscar, processar e armazenar informações jurídicas atualizadas diariamente, como jurisprudências, atos legais, pareceres e benefícios fiscais.

---

## 📌 Objetivos

- Coletar dados automaticamente de fontes jurídicas (ex: STF, SEFAZ, GOV).
- Limpar e tratar o texto jurídico coletado.
- Gerar embeddings (vetores semânticos) com NLP.
- Salvar os dados em um motor vetorial (FAISS ou pgvector).
- Atualizar a base de conhecimento tributário por CNPJ, tese e UF.

---

## 📁 Estrutura de Arquivos

| Arquivo                      | Descrição                                                                 |
|-----------------------------|---------------------------------------------------------------------------|
| `run_diario.py`             | Orquestrador do pipeline completo                                         |
| `crawler_stf.py`            | Crawler que extrai jurisprudências do site do STF                         |
| `crawler_sefaz.py`          | Simulador/crawler de notícias fiscais por SEFAZ                           |
| `extrator_texto.py`         | Limpeza e unificação de textos jurídicos                                  |
| `gerar_embeddings.py`       | NLP com sentence-transformers (modelo MiniLM)                             |
| `integrador_motor.py`       | Integra os dados com o motor de conhecimento (banco ou FAISS)             |
| `faiss_index.py`            | Configuração e uso do índice vetorial FAISS para busca semântica          |
| `README.md`                 | Esta documentação                                                         |

---

## ▶️ Execução Manual

Para rodar o aprendizado diário manualmente:

```bash
python scripts/aprendizado_diario/run_diario.py



