# -----------------------------------------
# BASE IMAGE
# -----------------------------------------
FROM python:3.11-slim

# -----------------------------------------
# SYSTEM DEPENDENCIES
# (precisa para plotly offline e https requests)
# -----------------------------------------
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------------------
# WORKDIR
# -----------------------------------------
WORKDIR /app

# -----------------------------------------
# COPIAR ARQUIVOS DO PROJETO
# (certifique-se de que melon.py e ativos.csv
# estão na mesma pasta do Dockerfile)
# -----------------------------------------
COPY melon.py .
COPY ativos.csv .

# -----------------------------------------
# INSTALAR DEPENDÊNCIAS
# -----------------------------------------
RUN pip install --no-cache-dir \
    yfinance \
    numpy \
    pandas \
    plotly \
    requests

# -----------------------------------------
# COMANDO PADRÃO
# -----------------------------------------
CMD ["python", "melon.py"]
