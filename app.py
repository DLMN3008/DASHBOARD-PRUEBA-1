import streamlit as st
import random

# ==========================
# CONFIGURACIÓN
# ==========================

st.set_page_config(
    page_title="Práctica de Ecuaciones",
    page_icon="🧮",
    layout="centered"
)

# ==========================
# FUNCIONES
# ==========================

def generar_ecuacion():

    # Solución siempre entre 1 y 10
    x = random.randint(1, 10)

    a = random.randint(2, 10)
    b = random.randint(-20, 20)

    c = a * x + b

    pregunta = f"{a}x + ({b}) = {c}"

    return pregunta, x


# ==========================
# VARIABLES DE SESIÓN
# ==========================

if "pregunta" not in st.session_state:
    pregunta, solucion = generar_ecuacion()
    st.session_state.pregunta = pregunta
    st.session_state.solucion = solucion

if "aciertos" not in st.session_state:
    st.session_state.aciertos = 0

if "errores" not in st.session_state:
    st.session_state.errores = 0


# ==========================
# INTERFAZ
# ==========================

st.title("🧮 Práctica de Ecuaciones de Primer Grado")

st.markdown(
    """
    Resuelve la ecuación y encuentra el valor de **x**.
    """
)

st.markdown("---")

st.subheader(st.session_state.pregunta)

respuesta = st.number_input(
    "Ingresa el valor de x",
    value=1,
    step=1
)

col1, col2 = st.columns(2)

# ==========================
# VERIFICAR
# ==========================

with col1:

    if st.button("✅ Verificar respuesta"):

        if int(respuesta) == st.session_state.solucion:

            st.session_state.aciertos += 1

            st.success(
                f"🎉 ¡Correcto! x = {st.session_state.solucion}"
            )

            # Animaciones
            st.balloons()

            st.markdown(
                """
                # ⭐⭐⭐⭐⭐
                # 🌟🌟🌟🌟🌟
                # ⭐⭐⭐⭐⭐
                """
            )

            st.markdown(
                """
                ## 🏆 ¡Excelente trabajo!
                Sigue así.
                """
            )

        else:

            st.session_state.errores += 1

            st.error(
                f"❌ Incorrecto. Inténtalo nuevamente."
            )

            st.markdown(
                """
                # 🤡 🤡 🤡
                # 🤡 😜 🤡
                # 🤡 🤡 🤡
                """
            )

            st.warning(
                "Sigue practicando. Tú puedes lograrlo."
            )

# ==========================
# NUEVA PREGUNTA
# ==========================

with col2:

    if st.button("🔄 Nueva pregunta"):

        pregunta, solucion = generar_ecuacion()

        st.session_state.pregunta = pregunta
        st.session_state.solucion = solucion

        st.rerun()

# ==========================
# ESTADÍSTICAS
# ==========================

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.metric(
        "🏆 Aciertos",
        st.session_state.aciertos
    )

with col4:
    st.metric(
        "❌ Errores",
        st.session_state.errores
    )

# ==========================
# INSTRUCCIONES
# ==========================

with st.expander("📖 Instrucciones"):

    st.write("""
    1. Resuelve la ecuación.
    2. Ingresa el valor de x.
    3. Presiona 'Verificar respuesta'.
    4. Si aciertas aparecerán estrellas y una animación.
    5. Si fallas aparecerán payasos.
    6. Presiona 'Nueva pregunta' para seguir practicando.
    """)
