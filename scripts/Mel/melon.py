# ========================================================
# MELON INDEX + GAUGE (Índice Melão + Medo/Ganância)
# ========================================================

import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import os

# ========================================================
# CONFIGURAÇÕES
# ========================================================
MAR_aa = 0.10            # taxa mínima anual
MAR = MAR_aa / 252       # taxa mínima diária
arquivo_ativos = "ativos.csv"

# ========================================================
# FUNÇÕES AUXILIARES
# ========================================================

def carregar_dados(ticker, fonte):
    """
    Carrega dados conforme a fonte:
    yahoo = baixa de yfinance
    local = arquivo csv local
    url   = arquivo online
    """
    if fonte == "yahoo":
        dados = yf.download(ticker, start="2015-01-01", auto_adjust=True)
        if "Close" not in dados.columns:
            raise ValueError(f"Coluna 'Close' não encontrada para {ticker}")
        return dados["Close"]

    elif fonte == "local":
        df = pd.read_csv(ticker)
        return df.iloc[:, 1]

    elif fonte == "url":
        df = pd.read_csv(ticker)
        return df.iloc[:, 1]

    else:
        raise ValueError(f"Fonte inválida: {fonte}")

def melao_index(retornos, MAR):
    """
    Calcula o Índice Melão de uma série de retornos.
    """
    excess = retornos - MAR

    # componente 1: downside deviation
    downside = np.sqrt(np.mean(np.minimum(excess, 0)**2))

    # componente 2: perdas severas (caudas)
    limite_cauda = excess.mean() - 2 * excess.std()
    caudas = np.mean(excess[excess < limite_cauda]**2)

    # componente 3: assimetria (skewness)
    skew_val = retornos.skew()
    skew = float(skew_val.iloc[0]) if hasattr(skew_val, 'iloc') else float(skew_val)

    # risco efetivo
    R_ef = downside + np.sqrt(caudas) + max(0, -skew)

    # retorno excedente médio
    Ret_excedente = excess.mean()

    # Índice Melão
    MeI = Ret_excedente / R_ef if R_ef != 0 else 0.0

    return MeI, Ret_excedente, R_ef

def normalizar_0_100(valores):
    """
    Converte a lista de valores em escala 0–100
    estilo 'Fear & Greed Index'
    """
    # força valores float
    valores = [float(v) if v is not None else 0.0 for v in valores]

    min_v = min(valores)
    max_v = max(valores)

    if max_v - min_v == 0:
        return [50.0] * len(valores)  # neutro se todos iguais

    return [(v - min_v) / (max_v - min_v) * 100 for v in valores]

# ========================================================
# CARREGAR ATIVOS
# ========================================================
if not os.path.exists(arquivo_ativos):
    raise FileNotFoundError(f"Arquivo {arquivo_ativos} não encontrado.")

ativos = pd.read_csv(arquivo_ativos)
ativos.columns = [c.strip().lower() for c in ativos.columns]

resultados = []

for _, row in ativos.iterrows():
    if not {"nome","ticker","fonte"}.issubset(row.index):
        continue
    
    nome = str(row["nome"]).strip()
    ticker = str(row["ticker"]).strip()
    fonte = str(row["fonte"]).strip().lower()

    if nome.lower() == "nome":
        continue  # ignora header mal interpretado

    print(f"Processando: {nome} ({ticker}) ...")

    try:
        precos = carregar_dados(ticker, fonte)
        ret = precos.pct_change().dropna()
        MeI, rex, ref = melao_index(ret, MAR)

        resultados.append({
            "nome": nome,
            "ticker": ticker,
            "MeI": float(MeI),
            "Retorno excedente": float(rex),
            "Risco efetivo": float(ref)
        })
    except Exception as e:
        print(f"Erro ao processar {nome}: {e}")

df = pd.DataFrame(resultados)

# ========================================================
# NORMALIZAR 0-100
# ========================================================
df["Score_0_100"] = normalizar_0_100(df["MeI"].fillna(0).tolist())
indicador_geral = df["Score_0_100"].mean()

if indicador_geral < 20:
    estado = "🟥 MEDO EXTREMO"
elif indicador_geral < 40:
    estado = "🟧 MEDO"
elif indicador_geral < 60:
    estado = "🟨 NEUTRO"
elif indicador_geral < 80:
    estado = "🟩 GANÂNCIA"
else:
    estado = "🟩🟩 GANÂNCIA EXTREMA"

# ========================================================
# RESULTADOS NO TERMINAL
# ========================================================
print("\n==============================")
print(" RESULTADOS — ÍNDICE MELÃO")
print("==============================")
print(df)

print("\n==============================")
print(" INDICADOR GERAL (0–100)")
print("==============================")
print(f"Apetite de risco: {indicador_geral:.2f}")
print(f"Classificação: {estado}")

# ========================================================
# PLOTLY GAUGE
# ========================================================
fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = indicador_geral,
    delta = {'reference': 50},
    title = {'text': "Indicador de Apetite ao Risco (Índice Melão)"},
    gauge = {
        'axis': {'range': [0, 100]},
        'bar': {'color': "black"},
        'steps': [
            {'range': [0, 20],  'color': "#b30000"},
            {'range': [20, 40], 'color': "#ff6600"},
            {'range': [40, 60], 'color': "#ffd11a"},
            {'range': [60, 80], 'color': "#7dd67d"},
            {'range': [80, 100],'color': "#00b300"}
        ],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.8,
            'value': indicador_geral
        }
    }
))

# Salvar como HTML
fig.write_html("velocimetro.html")
print("\nGráfico salvo como: velocimetro.html")
