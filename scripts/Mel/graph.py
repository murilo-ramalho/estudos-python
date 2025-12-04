# ========================================================
# GRÁFICO TIPO VELOCÍMETRO (GAUGE)
# ========================================================

import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = indicador_geral,
    delta = {'reference': 50},
    title = {'text': "Indicador de Apetite ao Risco (Índice Melão)"},
    gauge = {
        'axis': {'range': [0, 100]},
        'bar': {'color': "black"},
        'steps': [
            {'range': [0, 20],  'color': "#b30000"},   # medo extremo
            {'range': [20, 40], 'color': "#ff6600"},   # medo
            {'range': [40, 60], 'color': "#ffd11a"},   # neutro
            {'range': [60, 80], 'color': "#7dd67d"},   # ganância
            {'range': [80, 100],'color': "#00b300"}    # ganância extrema
        ],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.8,
            'value': indicador_geral
        }
    }
))

fig.update_layout(height=450)
fig.show()