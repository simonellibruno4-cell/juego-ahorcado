import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Ahorcado Médico", page_icon="🏥")

st.title("🏥 Juego del Ahorcado: Medicina")

# 1. Inicializar el "Estado de la Sesión" (Para que la web no olvide el progreso)
if 'palabra' not in st.session_state:
    lista_palabras = [
        "jeringa", "guantes", "mascarilla", "desinfectante", "termometro", 
        "estetoscopio", "hospital", "medico", "enfermera", "vacuna", 
        "sintomas", "diagnostico", "neurocirugia", "cardiologia", "pediatria"
    ]
    st.session_state.palabra = random.choice(lista_palabras)
    st.session_state.letras_adivinadas = []
    st.session_state.intentos = 6
    st.session_state.juego_terminado = False

# 2. Lógica para procesar la letra ingresada
def intentar_letra():
    letra = st.session_state.letra_input.lower()
    if letra and letra not in st.session_state.letras_adivinadas:
        st.session_state.letras_adivinadas.append(letra)
        if letra not in st.session_state.palabra:
            st.session_state.intentos -= 1
    # Limpiar la caja de texto después de intentar
    st.session_state.letra_input = ""

# 3. Interfaz de usuario
st.write(f"Intentos restantes: **{st.session_state.intentos}**")

# Mostrar la palabra con guiones bajos
palabra_mostrada = ""
for letra in st.session_state.palabra:
    if letra in st.session_state.letras_adivinadas:
        palabra_mostrada += letra + " "
    else:
        palabra_mostrada += "_ "

st.header(palabra_mostrada.strip())

# 4. Control de Victoria o Derrota
if "_" not in palabra_mostrada:
    st.success(f"¡Felicidades! Adivinaste: {st.session_state.palabra.upper()} 🥳")
    st.session_state.juego_terminado = True
elif st.session_state.intentos <= 0:
    st.error(f"¡Perdiste! La palabra era: {st.session_state.palabra.upper()} 💀")
    st.session_state.juego_terminado = True

# 5. Entrada de datos (solo si el juego sigue activo)
if not st.session_state.juego_terminado:
    st.text_input("Introduce una letra:", key="letra_input", on_change=intentar_letra, max_chars=1)
else:
    if st.button("Jugar de nuevo"):
        # Limpiar todo para reiniciar
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

# Mostrar letras usadas
st.info(f"Letras intentadas: {', '.join(st.session_state.letras_adivinadas)}")
