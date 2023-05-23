import streamlit as st

def rekom_film(genre):
    # Fungsi ini akan mengembalikan rekomendasi film berdasarkan genre yang dipilih
    # Kamu dapat menggunakan logika atau algoritma rekomendasi film yang sesuai di sini
    # Untuk contoh ini, kita akan menggunakan daftar film statis

    if genre == "Action":
        return ["John Wick 4 - ", "The Covenant", "Transformers: Rise of the Beasts", "Guardians of The Galaxy Vol. 3", "Fast X", "The Roundup: No Way Out", "Ant-Man and The Wasp: Quantumania"]
    elif genre == "Horror":
        return ["Hidayah", "Khanzab", "Sewu Dino", "Evil Dead Rise", "Jin Khodam"]
    elif genre == "Perang":
        return ["Ghosts of War", "The Tomorrow War", "The East", "Zeros and Ones", "Redemption Day"]
    elif genre == "Romantis":
        return ["Cinta dengan Mertuamu","Bukannya Aku Tidak Mau Nikah", "Bismillah Kunikahi Suamimu", "Hati Suhita", "Mantan Tapi Menikah", "Kamu nanyak ? : Dilan 1990"]
    else:
        return []

# Judul aplikasi
st.title("Rekomendasi Film")

# Daftar genre film
genres = ["", "Action", "Horror", "Perang", "Romantis"]

# Pilihan genre film
selected_genre = st.selectbox("Pilih Genre", genres)

if selected_genre != " ":
    # Memperoleh rekomendasi film berdasarkan genre yang dipilih
    recommendations = rekom_film(selected_genre)

    # Menampilkan rekomendasi film
    st.subheader("Rekomendasi Film")
    if recommendations:
        for movie in recommendations:
            st.write(" " + movie)
    else:
        st.write("Film tidak ada")
