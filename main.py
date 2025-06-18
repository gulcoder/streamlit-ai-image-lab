import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Ladda API-nyckel
load_dotenv()
api_key = os.getenv("OPEN_AI_API_KEY")

if not api_key:
    st.error("❗ Lägg till din OPEN_AI_API_KEY i .env-filen.")
    st.stop()

client = OpenAI(api_key=api_key)

# UI
st.title("🎨 Bildgenerering med OpenAI + Streamlit")
st.write("Skriv en beskrivning så genereras en bild med DALL·E 3!")

prompt = st.text_area("Vad vill du se för bild?", placeholder="Ex: A flying ship over a futuristic city at sunset")

if st.button("Generera bild"):
    if not prompt.strip():
        st.warning("Skriv något först!")
        st.stop()

    with st.spinner("Genererar bild..."):
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        st.image(image_url, caption=prompt)
