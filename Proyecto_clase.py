import streamlit as st
import streamlit.components.v1 as components

st.title('Manufacturer Analysis in PowerBI')
power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=a83d22ca-f8af-4671-8d23-2bdb2c401324&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64"
st.markdown(
       f"""
       <div style="display: flex; justify-content: center;">
           <iframe title="Informe de Power BI" width="1100" height="800" src="{power_bi_url}" frameborder="0" allowFullScreen="true"></iframe>
       </div>
       """,
       unsafe_allow_html=True
   )
