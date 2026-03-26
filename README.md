# Azure SGS Selic Pipeline

Data pipeline: API SGS (BCB Selic - série 11) → Landing (JSON) → Silver (CSV limpo) → Azure Blob / Orquestração.

## Stack

- Python (requests, pandas)
- Azure Blob Storage
- Azure Data Factory / Databricks (próximas etapas)

## Estrutura

- src/ingestion/sgs_selic_ingest.py – ingestão série SGS Selic (bronze em data/landing)
- src/transformation/sgs_selic_silver.py – limpeza e ordenação (silver em data/silver)
