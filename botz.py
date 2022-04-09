import os

from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
load_dotenv()

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session = os.environ.get("SESSION")

user = Client(session, api_id, api_hash)
username_channel = os.environ.get("CHANNEL_ASAL")  # Ganti Disini
channel_tujuan = os.environ.get("CHANNEL_TUJUAN")  # Tujuannya ganti disitu
photo_url = os.environ.get("PHOTO_URL")  # Link Foto


@user.on_message(filters.chat(username_channel))
async def get_new_post(c: Client, m: Message):
    if m.caption and "Jangan Lupa" in m.caption:
        """ ^^^ 
        kalo ada caption dan teks 'jangan lupa' di caption, di skip, lu bisa ubah2 apa aja yg jgn 
        kebawa pas mau kirim ke channel lu nya
        """
        return
    """
    contoh teks:
    💥 TOTOMACAU SORE 16:15 WIB 💥 -> indeks 0
                                    -> indeks 1
📆 Hari & Tgl: MINGGU, 13 MARET 2022 -> indeks 2
📩 RESULT:9497 -> indeks 3
☯️ SHIO: HARIMAU -> indeks 4
🏆 Selamat Kepada Pemenang Member KINGCOBRATOTO ! -> indeks 5
    """
    caption = m.caption.split("\n")
    # caption.split("\n") itu buat misahin setiap kalimat yang ada, nanti hasilnya bakal kepisah 1 1
    # setelah dipisah dia bakal ada indeksnya masing" yang udah ada di contoh teks itu
    city = caption[0].replace("🔥", "💥").strip()
    # caption[0] berarti ngambil indeks ke 0, replace itu ngubah teks awal, jadi teks akhir sesuai apa yg lu mau
    # disitu contohnya api berubah jadi emot meledak, bisa lu ubah jg
    # strip itu biar gada spasi tambahan di awal dan akhir kalimat
    tgl = caption[2].split(":")[1].strip()
    # caption[2] ngambil indeks 2, split itu buat misahin juga, disini dia misahin titik 2
    # jadi bakal ada 2 indeks, 0 dan 1, nah [1] itu buat ngambil indeks kesatu yg dri hasil split tadi
    result = caption[3].split(":")[1].strip()
    # sama kek yg tgl
    shio = caption[4].split(":")[1].strip()
    # sama kek yg tgl
    text = (
        f"{city}\n\n"
        # f"{city}" itu buat masukin kata awalnya buat variable city yang diatas tadi
        # \n itu buat bikin baris baru, karena dobel, dia bikin dua baris baru
        f"📆 Hari & Tgl: {tgl}\n"
        # sama kek yang tadi, kalo yang ini dia masukin teksnya dulu
        f"📩 RESULT:{result}\n"
        # sama
        f"☯️ SHIO: {shio.upper()}\n\n"
        # upper itu biar ngebuat teksnya jadi kapital semua
        "🏆 **Selamat Kepada Pemenang Member KINGCOBRATOTO !**\n"
        # sama kek yg hari & tgl
        "Salam Kenal\n"
        # kalo buat masukin teks, gaperlu f"", cukup ""
        "Salam JP"
        # sama kek yg salam kenal
    )
    #return await m.copy(channel_tujuan, caption=text) # -> kalo mau pake foto bawaan apus tanda pagar yg ini
    return await c.send_photo(channel_tujuan, photo_url, caption=text) # -> kalo mau pake foto lu, pake yg ini


user.run()
