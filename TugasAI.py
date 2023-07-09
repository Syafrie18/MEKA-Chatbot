from gtts import gTTS
import os
import streamlit as st
import speech_recognition as sr

def get_user_input():
    st.write("Masukkan kerusakan kendaraan anda:")
    user_input = st.text_input(">")
    return user_input

def get_voice_input():
    mendengar = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Mendengarkan...")
        audio = mendengar.listen(source, phrase_time_limit=2)
        audio = mendengar.listen(source)
    
    try :
        st.write("Mengenali suara...")
        query = mendengar.recognize_google(audio, language="id-ID")
        st.write(f"user said {query}\n")
    except Exception as e:
        st.write("Tolong ucapkan...")
        query = None 
    return query

st.write("Pendeteksi Kerusakan kendaraan")   

def ngomong(text):
    teks = (text)
    bahasa = 'id'
    namafile = 'Ngomong.mp3'
    def reading():
        suara = gTTS(text=teks, lang=bahasa, slow=False)
        suara.save(namafile)
        os.system(f'start {namafile}')
        
    reading()

def main():
    st.title("🤖 MEKA")
    choice_options = ["Keyboard", "Suara", "Keluar"]
    choice_selected = st.sidebar.selectbox("Metode input apa yang ingin anda gunakan?", options = choice_options)
       
    if choice_selected == "Keyboard":
        st.write("Halo Selamat datang!")
        user_input = get_user_input()
        process_input(user_input)
    elif choice_selected == "Suara":
        st.write("Halo Selamat datang!")
        user_input = get_voice_input()
        process_input(user_input)
    elif choice_selected == "Keluar":
        st.write("Terima kasih sampai jumpa.")
        

def process_input(user_input):
    daftar_kerusakan = {
        "Mobil tidak mau menyala":"Penyebab kerusakan adalah masalah pada sistem pengapian atau baterai lemah.",
        "Motor mengeluarkan asap putih":"Penyebab kerusakan adalah masalah pada sistem pendinginan atau pelumasan yang tidak mencukupi." ,
        "Rem kendaraan tidak berfungsi":"Penyebab kerusakan adalah keausan pada kampas rem atau kebocoran pada sistem rem." ,
        "Bunyi berdecit ketika membelok":"Penyebab kerusakan adalah masalah pada suspensi atau bearing roda yang aus.",
        "Aki kendaraan sering soak":"Penyebab kerusakan adalah alternator yang rusak atau kabel pengisian yang longgar.",
        "Transmisi bergesekan saat perpindahan gigi":"Penyebab kerusakan adalah kebocoran pada sistem transmisi atau masalah pada kopling.",
        "Suhu mesin naik secara tiba-tiba":"Penyebab kerusakan adalah kebocoran pada sistem pendinginan atau kerusakan pada termostat.",
        "mesin mati":"Penyebab kerusakan adalah pada sistem bahan bakar dan busi." ,
        "mesin panas":"Penyebab kerusakan adalah pada level pendingin dan radiator.",
        "suara tidak normal":"Penyebab kerusakan adalah suara knalpot dan sistem knalpot.",
        "gigi macet":"Penyebab kerusakan adalah pada transmisi dan kopling.",
        "slipping transmisi":"Penyebab kerusakan adalah pada kondisi minyak transmisi dan kopling.",
        "transmisi bocor":"Penyebab kerusakan adalah pada sistem kelistrikan dan cincin segel transmisi.",
        "rem aus":"Penyebab kerusakan adalah pada kampas rem dan sistem pengereman.",
        "rem tidak responsif":"Penyebab kerusakan adalah cairan rem dan sistem hidrolik.",
        "bunyi berdecit":"Penyebab kerusakan adalah kondisi kampas rem dan rotor.",
        "getaran berlebih":"Penyebab kerusakan adalah kondisi bantalan roda dan suspensi.",
        "shockbreaker bocor":"Penyebab kerusakan adalah kondisi shockbreaker dan per bushing.",
        "bunyi berisik":"Penyebab kerusakan adalah pada bagian suspensi dan stabilizer.",
       
        # Tambahkan kerusakan kendaraan lainnya sesuai kebutuhan
    }
    
    solutions = []
    for kerusakan, solution in daftar_kerusakan.items():
        if kerusakan.lower() in user_input.lower():
            solutions.append(solution)

    if solutions:
        st.write("Kerusakan yang mungkin terjadi pada kendaraan Anda:")
        for i, solution in enumerate(solutions):
            st.write(f"{i+1}. {solution}")
    else:
        st.write("Kerusakan kendaraan tidak dapat diidentifikasi.")

if __name__ == '__main__':
    main()
