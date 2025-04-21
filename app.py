import streamlit as st
from speech_utils import listen_to_voice, speak
from gpt_engine import ask_gpt
from excel_lookup import get_medicine_for_symptom
from twilio_handler import make_reservation_call
from map_finder import get_pharmacy_link

st.set_page_config(layout="centered", page_title="Health Assistant", page_icon="💊")

st.markdown("<h1 style='text-align: center;'>🦳 Voice Health Assistant</h1>", unsafe_allow_html=True)

if st.button("🎹 Talk to Assistant"):
    with st.spinner("Listening..."):
        query = listen_to_voice()
        st.write(f"🔤 You said: {query}")

        speak("Let me help you.")
        response = ask_gpt(query)
        st.success(response)
        speak(response)

        st.subheader("🔎 Suggestions from database:")
        data = get_medicine_for_symptom(query)
        if data:
            for item in data:
                st.info(f"💊 {item['Medicine']} — {item['Dosage']}\n📄 {item['Instructions']}")
        else:
            st.warning("No medicine found for this symptom.")

        if st.button("📞 Call Pharmacy"):
            sid = make_reservation_call("+46760085141", "paracetamol")
            st.write(f"Reservation Call SID: {sid}")

st.markdown(f"[📍 Find Nearby Pharmacies]({get_pharmacy_link()})")
