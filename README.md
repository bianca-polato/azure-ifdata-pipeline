#Azure IFData Pipeline

Data pipeline: IFData API (Banco Central do Brasil) -> Azure Blob Storange -> Azure Data Factory (ingestion & processing)

#Stack 
- Python (requests, pandas)
- Azure Blob Storange 
- Azure Data Factory 

#Estrutura
- src/ingestion/ifdata_ingest.py -scrip de ingestão da API IFData
- data/lading/ - camada bronze(dados brutos)