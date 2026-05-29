import streamlit as st
from PyPDF2 import PdfReader
from openai import OpenAI

st.set_page_config(
    page_title="Resumen Ejecutivo de PDF",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Generador de Resumen Ejecutivo")

st.write(
    "Carga un archivo PDF y obtén un resumen ejecutivo generado por IA."
)

uploaded_file = st.file_uploader(
    "Seleccione un archivo PDF",
    type=["pdf"]
)

if uploaded_file:

    try:
        reader = PdfReader(uploaded_file)

        texto = ""

        for page in reader.pages:
            contenido = page.extract_text()
            if contenido:
                texto += contenido + "\n"

        st.success(
            f"PDF cargado correctamente ({len(reader.pages)} páginas)"
        )

        if st.button("Generar Resumen Ejecutivo"):

            with st.spinner("Analizando documento..."):

                client = OpenAI(
                    api_key=st.secrets["OPENAI_API_KEY"]
                )

                prompt = f"""
                Analiza el siguiente documento y genera:

                1. Resumen ejecutivo.
                2. Objetivo principal.
                3. Hallazgos relevantes.
                4. Riesgos identificados.
                5. Recomendaciones.
                6. Conclusión ejecutiva.

                Documento:
                {texto[:100000]}
                """

                response = client.chat.completions.create(
                    model="gpt-4.1",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                resumen = response.choices[0].message.content

                st.subheader("📋 Resumen Ejecutivo")
                st.markdown(resumen)

                st.download_button(
                    label="📥 Descargar Resumen",
                    data=resumen,
                    file_name="resumen_ejecutivo.txt",
                    mime="text/plain"
                )

    except Exception as e:
        st.error(f"Error procesando PDF: {e}")
