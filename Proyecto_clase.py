import streamlit as st
import streamlit.components.v1 as components

st.title('Manufacturer Analysis in PowerBI')
power_bi_url = "<iframe title="Power BI Sample" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNWE3ZjA4YTctMDZmMy00ZjhlLTg0NWItYjU3YjQxYjNlNGFhIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>"
st.markdown(
       f"""
       <div style="display: flex; justify-content: center;">
           <iframe title="Informe de Power BI" width="1100" height="800" src="{power_bi_url}" frameborder="0" allowFullScreen="true"></iframe>
       </div>
       """,
       unsafe_allow_html=True
   )
