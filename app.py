# %%
import requests
import pandas as pd
import time
import streamlit as st


url = "https://api.bling.com.br/Api/v3/produtos"

payload = ""
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer c55c223e2d04a73037d2e094ada255f26772201d',
  'Cookie': 'PHPSESSID=5t6jov8g01bdg7lhj12hd0h4cn'
}

# %%
lista = []
pagina = 1

for pagina in range(2):
  response = requests.get(url, headers=headers, data=payload, params={'pagina': pagina+1})
  response_ajustado_json = response.json()
  dados_response = response_ajustado_json.get('data')
  lista.extend(dados_response)
  time.sleep(0.5)


# %%
df = pd.DataFrame(lista, columns=['codigo', 'id', 'preco', 'estoque'])
df['estoque'] = df['estoque'].apply(lambda x: x['saldoVirtualTotal'] if isinstance(x, dict) else None)
# df

# %%
# df.to_excel('planilha lucas.xlsx', index=False)
# %%
st.title('Estoque')
sku_selecionado = st.sidebar.selectbox('SKU', df['codigo'])
# st.sidebar.markdown(sku_selecionado)
# sku = st.text_input('sku').strip()
estoque = df[df['codigo'] == sku_selecionado]['estoque']
if not estoque.empty:
    valor_estoque = int(estoque.values[0])  # Convertendo para inteiro para remover ".0"
    
    st.markdown(
        f"""
        <div style="padding: 10px; border-radius: 10px; background-color: #f0f2f6; text-align: center;">
            <h3 style="color: #333;">📦 Estoque disponível:</h3>
            <p style="font-size: 24px; font-weight: bold; color: #007BFF;">{valor_estoque}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

