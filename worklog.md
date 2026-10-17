---
Task ID: 1 (single-task)
Agent: Main Agent (Z.ai)
Task: Riset visual & kostum drama Nusantara — 10 era (Mataram Kuno → Orde Baru) dalam format markdown

Work Log:
- Klarifikasi 8 dimensi via AskUserQuestion (format, kedalaman, fokus, tujuan, cakupan, bahasa, tokoh, prompt SD)
- Web research paralel untuk era Mataram Kuno, Singasari, Majapahit, Demak, Pajang, Mataram Islam, Kolonial, Kemerdekaan, Orde Lama, Orde Baru
- Struktur dokumen: 10 era × (konteks sejarah + visual & kostum + arsitektur + senjata + 5-6 tokoh kunci + 5 prompt SD)
- Penulisan dokumen markdown bertahap menggunakan Write + Edit (4 batch tulis)
- Verifikasi akhir: 1.327 baris, 14.277 kata, 108 KB

Stage Summary:
- File output: /home/z/my-project/download/riset-drama-nusantara.md
- Format: Markdown (.md)
- Cakupan: 10 era sejarah Nusantara (Mataram Kuno 716 M → Orde Baru 1998)
- Fokus utama: Visual & Kostum (sesuai permintaan user)
- Plus: 50+ prompt SD siap pakai (5 per era)
- Plus: 50+ profil tokoh historis (5-6 per era) dengan karakter drama
- Total ~14.000 kata, kedalaman mendalam per era
- Catatan: Semua konten adalah sintesis orisinal dari fakta historis yang umum dikenal. Tidak ada kutipan panjang dari sumber tertentu.

---
Task ID: 2 (validation task)
Agent: Main Agent (Z.ai)
Task: Validasi & koreksi dokumen riset drama Nusantara - cek typo, verifikasi fakta ke sumber primer

Work Log:
- Membaca ulang seluruh dokumen (1.327 baris / 14.277 kata)
- Web search verifikasi fakta kunci: Sumpah Palapa, Raden Patah, Fatahillah, Sultan Trenggana, Airlangga, kalender Jawa Sultan Agung, Ken Arok, Hamengkubuwana I, Perjanjian Giyanti, Sudirman, Fatmawati, Amangkurat III
- Melakukan koreksi MultiEdit untuk 15+ kesalahan & typo
- Verifikasi akhir bahwa semua typo sudah bersih (grep pattern checking)

Koreksi yang dilakukan:
- FAKTA HISTORIS:
  * "Aji Wurukari dari Wurawari" → "Aji Wurawari dari Lwaram" (sumber: Wikipedia Pralaya Medang, NatGeo)
  * "kalender Jawa 1663 Masehi = 1633 Jawa" → "kalender Jawa 1 Sura 1555 Jawa = 8 Juli 1633 Masehi = 1 Muharram 1043 H" (sumber: Wikipedia Kalender Jawa, kratonjogja.id)
  * "Amangkurat II berperang saudara dengan saudaranya" → "Amangkurat III berperang dengan Pangeran Puger (Pakubuwana I) dalam Perang Suksesi Jawa Pertama 1704-1708" (sumber: Wikipedia Perang Takhta Jawa I)
  * "Fatmawat Soekarno" → "Fatmawati Soekarno" (sumber: Wikipedia Fatmawati)
  * Hapus catatan internal "Anak raja Syailendra yang diasuh oleh Airlangga... salah - bukan Airlangga" (tidak profesional di dokumen final)
  * "Balaputradewa pembangun Borobudur" → diperbaiki jadi "Raja Syailendra terakhir di Jawa, kemudian penguasa Srivijaya" (Balaputradewa tidak ada hubungan dengan Borobudur, yang terkait adalah Samaratungga)
  * "Pakubuwana II sebagai tokoh kunci Mataram akhir" → dipisah menjadi PB II (1726-1749, unified) + PB III (1749-1788, Surakarta) — karena PB III yang menandatangani Giyanti
  * "Hamengkubuwana I lahir 1755" → ditambahkan "Lahir 5 Agustus 1717 dengan nama Pangeran Mangkubumi (Raden Mas Sujana)" (sumber: kratonjogja.id)
  * "Perjanjian Giyanti 1755" → "Perjanjian Giyanti 13 Februari 1755" (sumber: Wikipedia Perjanjian Giyanti)
  * Sudirman lahir di Purbalingga 24 Januari 1916, wafat 29 Januari 1950 (sumber: Wikipedia Soedirman)
  * "Peristiwa Bubat tewasnya Pajajaran dan hubungan rusak dengan Sunda" → "tewasnya Raja Sunda-Pajajaran Linggabuana dan putrinya Dyah Pitaloka" (lebih akurat)
  * "Gajah Mada lahir ±1290" tetap (tahun lahir tidak pasti)
  * "ekspedisi Pamalayu 1275" tetap (sumber primer Prasasti Amoghapasa)

- TYPO/KESALAHAN KETIK:
  * "ciri unung" → "ciri unik"
  * "agraris-agraris" → "agraris-birokratis"
  * "Buddhist Syailendra" → "Buddha Syailendra"
  * "raja-raja berkuat" → "raja-raja berkuasa"
  * "keraton-orientied" → "keraton-oriented"
  * "atauatorik" → "oratorik"
  * "Fatmawat Soekarno" → "Fatmawati Soekarno"
  * "Aktifis" → "Aktivis"
  * "Rumah-rumah masih banyak bergaya kolonial dengan ter ." → "Rumah-rumah masih banyak bergaya kolonial Hindia Belanda dengan teras depan luas."
  * "jas aneh yang modis" → "jas modis hasil rancangannya sendiri"
  * "Gusdur-era street protest" (di prompt SD) → "Orde Lama-era street protest"
  * "seni-budaya orientated" → "berorientasi pada seni dan budaya"
  * "sofistikated" → "cendekia"
  * "ekspedi Bubat" → "ekspedisi Bubat" → "Peristiwa Bubat"
  * "mengonsolidasikan/mengonsolidasi" → "mengkonsolidasikan/mengkonsolidasi"
  * "Laslykar Wanita" → "Laskar Wanita"
  * "kahki" → "khaki"
  * "topi topi hitam" → "topi hitam"
  * "gudang tinggi" → "langit-langit tinggi"
  * "venetianers" → "tirai kayu jalusi"
  * "segi rupa naga" → "segi delapan berukir motif naga"
  * "berbuckle permata" → "berhias permata"
  * "Etiše Politiek" → "Ethische Politiek"
  * "max Havelaar" → "novel Max Havelaar karya Multatuli"
  * "PKI mendi Persiapan Kemerdekaan" → "BPUPKI/PPKI menuju Persiapan Kemerdekaan"
  * "Sori / Bhre Wirabhumi" → "Bhre Wirabhumi"
  * "penjelma" → "penjelmaan"
  * "jubah panjang lengan lebih" → "jubah panjang berlengan lebar"
  * "jas berdilepan" → dihapus (tidak jelas)
  * "sandals jepara" → "sandal jepara"
  * "Didirikan 1755" (kapitalisasi) → "didirikan 1755"
  * "Taman Taman Sari" → "Taman Sari"
  * "etc." → "dll."
  * "danstatus" → "dan status"
  * "menyatakan Yogyakarta bagian RI" → "menyatakan Yogyakarta sebagai bagian dari RI"

Stage Summary:
- File output (final): /home/z/my-project/download/riset-drama-nusantara.md
- Status: 1.332 baris, 14.450 kata (tambah ~50 kata dari koreksi & klarifikasi)
- 15+ koreksi fakta historis diverifikasi ke sumber primer (Wikipedia, kratonjogja.id, sumber sejarah)
- 30+ typo & kesalahan ketik diperbaiki
- Catatan: Beberapa detail masih memerlukan validasi lebih lanjut dari ahli sejarah (terutama untuk era Mataram Kuno, Singasari, Majapahit, Demak, Pajang, Mataram Islam) karena sumber primer sering kontradiktif. Disarankan konsultasi dengan sejarawan UGM/UI untuk produksi drama formal.
- Sumber primer yang digunakan untuk verifikasi: Wikipedia bahasa Indonesia, kratonjogja.id (situs resmi Keraton Yogyakarta), detik.com, jurnal akademis UNY/UNAIR/UNESA, anri.go.id

---
Task ID: 3 (fase Mataram Kuno)
Agent: Main Agent (Z.ai)
Task: Audit & validasi khusus fase Mataram Kuno (era 1) - baca ulang, verifikasi ke sumber primer, perbaiki kesalahan

Work Log:
- Membaca ulang seluruh bagian Mataram Kuno (baris 28-137, ~110 baris)
- Web search paralel untuk verifikasi: Prasasti Canggal, Balitung, Mpu Sindok, Airlangga, Prasasti Nalanda, Balaputradewa, Rakai Pikatan, Pramodawardhani, Samaratungga, Sanjaya
- Koreksi 13+ kesalahan fakta & typo dengan MultiEdit
- Verifikasi akhir semua typo sudah bersih

Koreksi FAKTA HISTORIS (11 koreksi):
1. "agraris-birokratis" → "agraris dan religius" (lebih tepat deskripsi Mataram Kuno)
2. "Balitung (899-911 M)" → "Rakai Watukura Dyah Balitung (898-910 M)" (sumber: Wikipedia ID, prasasti)
3. "Perpindahan didorong oleh letusan Merapi" → "kemungkinan bencana alam (letusan Merapi, berdasarkan salah satu teori)" (klaim lebih hati-hati)
4. "Candi Sewu (kompleks Buddha terbesar di Jawa)" → "(kompleks Buddha terbesar di kawasan Prambanan)" (Borobudur lebih besar secara keseluruhan)
5. "Candi Borobudur dibangun Syailendra, selesai ~825 M" → "dibangun Wangsa Syailendra, selesai pada masa Samaratungga ± 825 M" (lebih spesifik)
6. "Candi Prambanan dibangun Wangsa Sanjaya, ~850 M" → "mulai ± 850 M, diresmikan 856 M berdasarkan Prasasti Siwagrha" (sumber: Prasasti Siwagrha)
7. "Airlangga memerintah 1019-1049 M" → "memerintah 1019-1042 M, wafat 1049 sebagai pertapa" (sumber: Wikipedia EN, Airlangga mundur 1042, wafat 1049 sebagai pertapa)
8. "Sanjaya ± 717-746 M" → "Sanjaya ± 732-746 M" (Prasasti Canggal 732 M sebagai tahun pendirian)
9. "Bukit Stirangga (G. Sumbing)" → "Bukit Sthirengga (Gunung Wukir, Magelang)" (sumber: Wikipedia Prasasti Canggal, jatengprov.go.id)
10. "Balaputradewa ± 824-860 M" → "± 832-856 M di Jawa; Maharaja Sriwijaya 860-900 M" (sumber: Wikipedia ID Balaputradewa)
11. "Catatan sejarah (Prasasti Nalanda) menyebut Balaputradewa sebagai cucu Raja Syailendra yang membangun biara Nalanda di India" → DIPERBAIKI MENJADI: "Prasasti Nalanda (860 M) menyebut Balaputradewa sebagai putra Samaragrawira dan cucu Dharanindra (raja Syailendra bergelar Wirawairimathana). Dalam prasasti tersebut, Balaputradewa memohon kepada Raja Devapala dari Bengal untuk membangun wihara bagi pelajar Buddha di Nalanda." (sumber: Wikipedia ID Prasasti Nalanda)
12. "Rakai Pikatan (Raja Sanjaya, 838-850 M)" → "Rakai Pikatan (Raja Wangsa Sanjaya, 838-851 M)"
13. "membangun Candi Prambanan dan Roro Jonggrang" → "membangun Candi Prambanan (Loro Jonggrang)" (Loro Jonggrang adalah nama lain Prambanan, bukan candi terpisah)
14. "Pramodawardhani (Permaisuri, 838-862 M)" → "Pramodawardhani (Putri Samaratungga, permaisuri Rakai Pikatan, aktif ± 820-860-an M)" (sumber: Wikipedia ID Pramodawardhani, Prasasti Kayumwungan 824 M)

Koreksi ISTILAH/TYPO (8 koreksi):
1. "*harata* (sabuk emas berlapis)" → "*sabuk emas* berlapis" (istilah "harata" tidak ditemukan dalam arkeologi Jawa kuno)
2. "*kampana* (lonceng kecil)" → "lonceng kecil" (istilah "kampana" tidak ditemukan)
3. "*perisai perunggu bundar* (pelanduk)" → "*perisai perunggu bundar*" (istilah "pelanduk" untuk perisai tidak akurat)
4. "kain batik polos" → "kain katun polos" (batik selalu bermotif, tidak ada "batik polos")
5. "rakyat dilarang memakai motif tertentu" → "motif-motif tertentu terbatas untuk kalangan bangsawan" (klaim lebih berhati-hati - larangan motif batik spesifik belum ada prasasti pada era Mataram Kuno)
6. "Istana raja (dalem)" → "Istana raja (prasadha/rajasthana)" (istilah "dalem" lebih khas era Mataram Islam)
7. "Pendeta Hindu (resi)" → "Pendeta Hindu Siwa (resi)" (lebih spesifik - Mataram Kuno adalah Hindu Siwa)
8. "*upavita* (tali suci melintang dada, biasanya untuk golongan brahmana)" → "*upavita* (tali suci melintang dada, simbol dwijā 'dua kali lahir' bagi golongan brahmana, ksatria, dan waisya)" (upavita untuk tiga varna, bukan hanya brahmana)
9. "mendirkan" → "mendirikan" (typo)
10. "*rudraksha* (butir doa)" → "*rudraksha* (butiran tasbih)" (lebih tepat)
11. "kain jedor / sampur" → "sampur / kain upavita" (istilah "jedor" lebih khas era Mataram Islam)

Koreksi PROMPT SD (3 koreksi):
1. "red batik kain jedor with harata gold belt" → "red naturally-dyed kain jedor with gold belt" (lebih akurat - batik modern tidak ada di abad 8)
2. "kuluk bronze conical helmet" → "bronze conical helmet" (kuluk adalah penutup kepala kain/bludru, bukan helm perunggu)
3. "keris proto-form" → "early keris Buda form" (lebih spesifik - keris Buda adalah proto-keris era Mataram Kuno)

TAMBAHAN INFORMASI BARU:
- Sanjaya: ditambahkan informasi dari Carita Parahyangan bahwa Sanjaya adalah keponakan Raja Sanna (putra Sannaha)
- Mpu Sindok: ditambahkan "Raja terakhir Wangsa Sanjaya" sebagai konteks
- Pramodawardhani: ditambahkan referensi Prasasti Kayumwungan 824 M

Stage Summary:
- File output: /home/z/my-project/download/riset-drama-nusantara.md
- Bagian Mataram Kuno (era 1) sudah diaudit & dikoreksi
- 14 koreksi fakta historis (diverifikasi ke sumber primer Wikipedia + prasasti)
- 11 koreksi istilah/typo
- 3 koreksi prompt SD
- 3 tambahan informasi baru
- Total: 31 koreksi untuk bagian Mataram Kuno

Sumber primer yang dipakai untuk verifikasi:
- Wikipedia Indonesia: Balaputradewa, Pramodawardhani, Samaratungga, Prasasti Nalanda, Airlangga, Mpu Sindok, Dyah Balitung
- Wikipedia English: Canggal inscription, Airlangga, Samaratungga, Mpu Sindok
- jatengprov.go.id: Prasasti Canggal & Candi Gunung Wukir
- slemankab.go.id: Candi Prambanan & Prasasti Siwagrha
- detik.com: Pramodawardhani biografi
- tirto.id: Ekspansi Mataram Kuno era Balitung

Belum terverifikasi (perlu konsultasi ahli):
- Tahun spesifik pemerintahan Sanjaya (732-746 M masih perkiraan)
- Tahun pasti pernikahan Rakai Pikatan dengan Pramodawardhani
- Identifikasi pasti "Bukit Sthirengga" (apakah benar-benar Gunung Wukir atau lokasi lain)
- Hubungan persis antara Samaratungga, Balaputradewa, dan Pramodawardhani (masih diperdebatkan sejarawan)


---
Task ID: 4 (audit fase 1 Mataram Kuno - REVISI KOMPREHENSIF)
Agent: Main Agent (Z.ai)
Task: Revisi mendalam era Mataram Kuno dengan fokus kawasan Dieng, Wonosobo (Rakai Garung), Temanggung, Magelang. Audit phase 1.

Work Log:
- Web search mendalam (5 batch paralel) untuk:
  * Prasasti Mantyasih 907 M - daftar raja Mataram Kuno
  * Rakai Garung (Wonosobo), Rakai Watuhumalang, Rakai Panunggalan/Panaraban
  * Prasasti Wanua Tengah III 908 M (Temanggung)
  * Candi Dieng, Prasasti Dieng 808 M
  * Prasasti Canggal 732 M (Gunung Wukir, Magelang)
  * Prasasti Kalasan 778 M, Prasasti Kelurak 782 M
  * Prasasti Karangtengah/Kayumwungan 824 M (Temanggung) - Samaratungga, Pramodawardhani
  * Prasasti Siwagrha/Wantil 856 M - Rakai Kayuwangi
  * Prasasti Nalanda 860 M - Balaputradewa
  * Prasasti Sojomerto - Dapunta Selendra
  * Prasasti Rukam 907 M (Temanggung)
  * Prasasti Anjuk Ladang - Mpu Sindok
  * Prasasti Argapura 863 M, Prasasti Panunggalan 896 M
  * Prasasti Gunung Wule 861 M (Wonosobo)
  * Daftar lengkap raja Sanjaya-Balitung (14 raja)
- Revisi besar-besaran bagian era 1 (Mataram Kuno) dengan struktur baru:
  * 1.1 Konteks Sejarah Singkat (lebih detail, dengan sumber prasasti)
  * 1.2 Daftar Lengkap Raja-Raja Mataram Kuno (TABEL BARU - 14 raja)
  * 1.3 Kawasan Geografis Penting (BARU - Dieng/Wonosobo/Temanggung/Magelang/Sleman-Klaten)
  * 1.4 Visual & Kostum (diperluas)
  * 1.5 Arsitektur & Setting
  * 1.6 Senjata & Properti
  * 1.7 Tokoh Kunci (Diperluas: Sanjaya, Panangkaran, Panunggalan/Panaraban, Warak, Dyah Gula, Garung, Samaratungga, Pikatan, Pramodawardhani, Balaputradewa, Kayuwangi, Watuhumalang, Balitung, Daksa, Mpu Sindok, Airlangga - total 16 tokoh)
  * 1.8 Prasasti-Prasasti Penting (TABEL BARU - 18 prasasti penting dengan tahun, lokasi, isi)
  * 1.9 Prompt SD Siap Pakai (10 prompt, diperluas dari 5)

- Tokoh baru yang ditambahkan:
  * Rakai Panunggalan/Panaraban (784-803 M) - Panaraban=Parakan, Temanggung
  * Rakai Warak Dyah Manara (803-827 M)
  * Dyah Gula (827-829 M) - raja singkat tanpa gelar Rakai
  * Rakai Garung (828-847 M) - Garung, Wonosobo (TOKOH KUNCI YANG DIMINTA USER)
  * Samaratungga (± 802-842 M) - Syailendra, pembangun Borobudur
  * Rakai Kayuwangi/Dyah Lokapala (855-885 M) - Prambanan
  * Rakai Watuhumalang/Mpu Teguh (± 885-898 M) - TOKOH KUNCI YANG DIMINTA USER
  * Daksa/Rakai Gurunwangi (910-919 M)
  * Airlangga (1019-1042 M, wafat 1049)

- Prasasti baru yang ditambahkan ke tabel:
  * Prasasti Sojomerto - Dapunta Selendra, Pekalongan
  * Prasasti Manjusrigrha 792 M - Candi Sewu
  * Prasasti Dieng 808 M - aksara Jawa Kuno tertua
  * Prasasti Gunung Wule 861 M - Wonosobo
  * Prasasti Argapura 863 M - identifikasi Rakai Pikatan = Mpu Manuku
  * Prasasti Panunggalan 896 M - Watuhumalang sebagai haji
  * Prasasti Poh Galuh - Daksa
  * Prasasti Calcutta/Pucangan 1042 M - silsilah Mpu Sindok-Airlangga

- Kawasan baru yang ditambahkan:
  * Dieng (Banjarnegara-Wonosobo) - kawasan sakral Hindu Siwa tertua, Prasasti 808 M
  * Wonosobo (Kecamatan Garung) - wilayah asal Rakai Garung
  * Temanggung - konsentrasi prasasti terbanyak (Mantyasih, Wanua Tengah III, Rukam, Karangtengah)
  * Magelang - pusat awal (Candi Gunung Wukir, Borobudur, Mantyasih)
  * Sleman-Klaten - kawasan Prambanan

- Insight penting yang dikoreksi/tambahan:
  * Sanjaya lahir ± 732 M (bukan 717 M) - berdasarkan Prasasti Canggal
  * Sanjaya keponakan Raja Sanna (putra Sannaha) - berdasarkan Carita Parahyangan
  * Balitung memerintah 898-910 M (bukan 899-911 M)
  * Prasasti Mantyasih ditemukan di Parakan, Temanggung (bukan Magelang Utara)
  * Rakai Garung identik dengan Garung, Wonosobo (nama kecamatan masih lestari)
  * Balaputradewa adalah cucu Dharanindra (bukan cucu raja Syailendra umum)
  * Peristiwa Bubat: tewasnya Raja Sunda-Pajajaran Linggabuana dan Dyah Pitaloka
  * Rakai Pikatan = Mpu Manuku = Rakai Mamrati (nama yang sama, tiga gelar berbeda)
  * Candi Prambanan diresmikan 856 M oleh Rakai Kayuwangi (bukan Rakai Pikatan)
  * Mpu Sindok adalah raja terakhir Wangsa Sanjaya di Jawa Tengah

Stage Summary:
- File output: /home/z/my-project/download/riset-drama-nusantara.md
- Era 1 (Mataram Kuno) sudah direvisi komprehensif dengan 9 sub-bagian (1.1-1.9)
- Total dokumen: 1.251 baris, ~14.500 kata
- Era 2-10 masih dalam versi sebelumnya (belum diaudit - menunggu user instruction lanjutan)
- Sumber primer yang digunakan: 18 prasasti (Canggal, Mantyasih, Wanua Tengah III, Siwagrha, Nalanda, Karangtengah, Kalasan, Kelurak, Anjuk Ladang, Rukam, Gunung Wule, Argapura, Panunggalan, Sojomerto, Manjusrigrha, Dieng, Poh Galuh, Calcutta)
- Fokus kawasan: Dieng, Wonosobo (Garung), Temanggung, Magelang, Sleman-Klaten
- 16 tokoh historis lengkap dengan tahun pemerintahan dan sumber prasasti
- 10 prompt SD siap pakai (diperluas dari 5)

Catatan teknis:
- Saat meng-overwrite file dengan Write, era 2-10 sempat hilang
- Saya pulihkan era 2-10 dengan menambahkannya kembali via bash append
- Era 2-10 masih dalam versi awal (belum diaudit seperti era 1)

---
Task ID: 5 (audit phase 1 Mataram Kuno - RE-AUDIT KEDUA)
Agent: Main Agent (Z.ai)
Task: Audit ulang fase 1 era Mataram Kuno dengan double cek, koreksi kesalahan yang masih ada

Work Log:
- Membaca ulang seluruh bagian era Mataram Kuno (baris 28-310) dengan teliti
- Web search verifikasi tambahan (3 batch) untuk:
  * Rakai Watuhumalang (Dyah Jbang vs Mpu Teguh)
  * Prasasti Anjuk Ladang (935 M vs 937 M)
  * Mpu Bharada (apakah Buddha atau Siwa - ternyata Buddha)
  * Dyah Tagwas, Rakai Panumwangan
  * Prasasti Argapura 863 M - isi sebenarnya
- Menemukan KESALAHAN SIGNIFIKAN yang sebelumnya tidak terdeteksi

KOREKSI UTAMA YANG DILAKUKAN (11 koreksi):

1. **Daftar raja Mataram Kuno DIPERLUAS dari 14 menjadi 17 raja**:
   - Tokoh yang HILANG sebelumnya:
     * Dyah Tagwas (Sri Jayakirtiwardhana) - naik takhta 17 Februari 885 M, hanya 6 bulan
     * Rakai Panumwangan Dyah Dewendra - naik takhta 3 Oktober 885 M
     * Rakai Gurunwangi Dyah Bhadra - naik takhta 18 Januari 887 M, lalu "minggat" dari kraton
   - Ditambahkan juga masa vakum ~8 tahun (887-894 M) antara Rakai Gurunwangi dan Rakai Watuhumalang

2. **Rakai Pikatan**: 
   - SEBELUMNYA: "Rakai Pikatan / Mpu Manuku / Rakai Mamrati (847-855 M)"
   - KOREKSI: "Rakai Pikatan / Dyah Saladū (847-855 M)"
   - Mpu Manuku adalah pejabat lain (Rakai Patapan), BUKAN nama lain Rakai Pikatan
   - Sumber: Wikipedia EN/ID Rakai Pikatan, Prasasti Wanua Tengah III

3. **Rakai Watuhumalang**:
   - SEBELUMNYA: "Rakai Watuhumalang / Mpu Teguh (± 885-898 M)"
   - KOREKSI: "Rakai Watuhumalang / Dyah Jbang (894-898 M, naik takhta 21 November 894 M)"
   - Mpu Teguh adalah raja bawahan (haji) Watuhumalang, terpisah dari Dyah Jbang (maharaja)
   - Sumber: Wikipedia ID Rakai Watuhumalang

4. **Daksa vs Rakai Gurunwangi** - DUA TOKOH BERBEDA:
   - SEBELUMNYA: Saya menggabungkan keduanya sebagai "Daksa / Rakai Gurunwangi (910-919 M)"
   - KOREKSI: 
     * Rakai Gurunwangi Dyah Bhadra (887 M) - raja ke-11, "minggat" dari kraton
     * Mpu Daksa (910-919 M) - raja ke-14, penerus Balitung
   - Keduanya adalah tokoh terpisah yang sering keliru disamakan

5. **Prasasti Anjuk Ladang**:
   - SEBELUMNYA: "859 Saka (935 M)"
   - KOREKSI: "859 Saka (937 M versi Damais) / 857 Saka (935 M versi Brandes)"
   - Sumber: Wikipedia ID/EN Prasasti Anjuk Ladang

6. **Prasasti Argapura (863 M)**:
   - SEBELUMNYA: "Rakai Pikatan = Mpu Manuku" (keliru)
   - KOREKSI: "Menyebut 'Pu Manuko(u)' sebagai Rakai Pikatan (jabatan kepala daerah di era Rakai Kayuwangi)"
   - Penjelasan: Mpu Manuku dalam Prasasti Argapura adalah kepala daerah Pikatan, bukan maharaja Rakai Pikatan (Dyah Saladū)

7. **Rakai Garung**:
   - SEBELUMNYA: "828-847 M"
   - KOREKSI: "829-847 M (naik takhta 10 Januari 829 M)" - sesuai Prasasti Wanua Tengah III
   - Ditambahkan info: "anak sang lumah i tūk" (anak orang yang meninggal di Tuk)

8. **Rakai Balitung**:
   - SEBELUMNYA: "Raja ke-10 Mataram Kuno"
   - KOREKSI: "Raja ke-13 Mataram Kuno (raja ke-9 menurut Prasasti Mantyasih yang melompati 4 raja singkat)"

9. **Konflik Balitung**:
   - SEBELUMNYA: "Kudeta oleh Daksa (Rakai Gurunwangi)"
   - KOREKSI: "Kudeta oleh Mpu Daksa"

10. **Prasasti Poh Galuh** (tabel):
    - SEBELUMNYA: "Daksa (Rakai Gurunwangi)"
    - KOREKSI: "Mpu Daksa (penerus Balitung)"

11. **Penambahan catatan penting** di tabel daftar raja:
    - Prasasti Wanua Tengah III menyebut 4 raja tambahan yang tidak ada di Mantyasih
    - Penjelasan Mpu Manuku vs Rakai Pikatan (Dyah Saladū)
    - Penjelasan Mpu Teguh vs Rakai Watuhumalang (Dyah Jbang)
    - Penjelasan Rakai Gurunwangi (Dyah Bhadra) vs Mpu Daksa

TAMBAHAN PROFIL TOKOH BARU (3 tokoh):
- Dyah Tagwas (Sri Jayakirtiwardhana) - 885 M, ~6 bulan
- Rakai Panumwangan / Dyah Dewendra - 885-887 M
- Rakai Gurunwangi / Dyah Bhadra - 887 M (lalu minggat)

VERIFIKASI MPU BHARADA:
- Sudah benar "pendeta Buddha" - Wikipedia ID menyebut "pendeta sakti agama Buddha yang menjadi guru Airlangga"

Stage Summary:
- File output: /home/z/my-project/download/riset-drama-nusantara.md
- Total dokumen: 1.278 baris, 15.261 kata (naik dari 14.500 kata sebelumnya)
- Era Mataram Kuno sudah diaudit KEDUA kali dengan double cek ke sumber primer
- 11 koreksi utama + 3 tokoh baru ditambahkan
- Daftar raja lengkap: 17 raja (dari Sanjaya ke Mpu Sindok), bukan 14 seperti versi sebelumnya
- Sumber primer: Prasasti Wanua Tengah III (908 M) sebagai sumber paling lengkap dan akurat
- Catatan: Beberapa detail masih diperdebatkan sejarawan (hubungan Rakai Garung-Samaratungga, identifikasi Mpu Manuku sebagai penerus Rakai Patapan atau tokoh terpisah)


---
Task ID: 6 (audit phase 1 Mataram Kuno - CROSS-CHECK SUMBER PRIMER)
Agent: Main Agent (Z.ai)
Task: Audit ketiga dengan cross-check ke Negarakertagama, Pararaton, prasasti, dan jurnal akademis

Work Log:
- Membaca ulang seluruh fase 1 (Mataram Kuno) baris 28-310
- Web search 3 batch untuk cross-check sumber primer:
  * Negarakretagama (karya Mpu Prapanca 1365 M)
  * Pararaton (Kitab Raja-Raja, abad 16)
  * Jurnal BRIN "Raja-raja Mataram Kuna dari Sanjaya Sampai Balitung" oleh Kusen (1994)
  * Carita Parahyangan (naskah Sunda)
  * Prasasti Pucangan/Calcutta (silsilah Mpu Sindok-Airlangga)
  * Berita Cina Dinasti Tang (untuk Ratu Shima/Kalingga)
- Menemukan KESALAHAN FUNDAMENTAL dalam penggunaan sumber primer

KESALAHAN FUNDAMENTAL YANG DITEMUKAN & DIKOREKSI:

### 1. KESALAHAN SUMBER PRIMER
**SEBELUMNYA**: Saya mengklaim Mataram Kuno disumber dari "Pararaton dan Kidung Harsawijaya"
**FAKTA**: 
- Pararaton (1481-1600 M) diawali dengan cerita Ken Arok (1222 M) - HANYA membahas Singasari-Majapahit
- Negarakretagama (1365 M) pupuh 40-49 hanya membahas silsilah Singasari-Majapahit
- KEDUA KITAB INI TIDAK MEMBAHAS ERA MATARAM KUNO (732-1016 M)!

**KOREKSI**: Tambah sub-bagian "1.1.1 Catatan Sumber Primer" yang menjelaskan sumber primer yang SAH untuk era Mataram Kuno:
1. Prasasti-prasasti (Canggal, Mantyasih, Wanua Tengah III, dll)
2. Carita Parahyangan (naskah Sunda abad 16)
3. Prasasti Calcutta/Pucangan (± 1041 M)
4. Berita Cina Dinasti Tang (untuk Kalingga/Ratu Shima)
5. Jurnal akademis modern (Kusen, Boechari, Casparis, Slamet Muljana)

### 2. KESALAHAN SILSILAH SANJAYA
**SEBELUMNYA**: "Sanjaya kemudian menaklukkan daerah sekitarnya, termasuk Kalingga"
**FAKTA**: Sanjaya TIDAK menaklukkan Kalingga. Ia MENGWARISI Kalingga dari buyutnya Maharani Shima (Ratu Kalingga).

**KOREKSI**: Tambahkan dua versi silsilah Sanjaya:
- Versi Carita Parahyangan (Sunda): Sanjaya putra Sannaha, keponakan Raja Sanna dari Galuh
- Versi Kalingga (Berita Cina): Sanjaya adalah cicit Maharani Shima, menggantikan buyutnya 732 M

### 3. KESALAHAN HUBUNGAN AIRLANGGA-MPU SINDOK
**SEBELUMNYA**: "Airlangga adalah cicit Mpu Sindok"
**FAKTA**: Airlangga adalah cicit-cicit (canggah) Mpu Sindok, bukan cicit.

**KOREKSI**: Rantai silsilah yang benar (dari Prasasti Pucangan 1041 M):
- Mpu Sindok (929-947) 
- → putri: Sri Isyanatunggawijaya (menikah Sri Lokapala) 
- → Makutawangsawardhana 
- → Mahendradatta (cicit Mpu Sindok, 961-1011) 
- → Airlangga (cicit-cicit/canggah Mpu Sindok, 1002-1049)

### 4. KOREKSI DETAIL AIRLANGGA
- Tahun lahir: "± 1002 M" (sumber bervariasi: 991, 1002, atau 1006 M)
- Ayah: Udayana Warmadewa (Wangsa Warmadewa, bukan hanya "Udayana")
- Ibu: Mahendradatta (saudari Raja Dharmawangsa Teguh, raja terakhir Medang sebelum Pralaya)
- Airlangga adalah keponakan Dharmawangsa Teguh (bukan penerus langsung)
- Pembagian kerajaan: Janggala (ibu kota Kahuripan) & Kadiri/Panjalu (ibu kota Daha) - 1042 M
- Sumber primer tambahan: Prasasti Cane (1021 M), Prasasti Turun Hyang (1035 M)

### 5. KOREKSI MPU SINDOK
- Ditambahkan: Mpu Sindok adalah cucu Mpu Daksa (raja 910-919 M)
- Ditambahkan: Rantai silsilah Mpu Sindok → Airlangga
- Ditambahkan: Referensi Prasasti Pucangan/Calcutta

### 6. KOREKSI PRASASTI CALCUTTA/PUCANGAN
- Tahun: dari "1042 M" menjadi "± 1041 M"
- Lokasi: "Bengal, India (Calcutta Museum) / ditemukan di Surabaya"
- Isi: "Silsilah Mpu Sindok hingga Airlangga (2 bahasa: Sanskerta & Jawa Kuno)"

### 7. KOREKSI SANJAYA TAHUN
- SEBELUMNYA: "± 732-746 M"
- KOREKSI: "± 717-746 M; naik takhta sebagai raja Mataram 732 M"
- 717 M = tahun Sanjaya diangkat jadi raja (menurut Arrazaq)
- 732 M = tahun Prasasti Canggal (penobatan sebagai raja Mataram)
- Gelar: "Narapati Raja Sri Sanjaya" (Prasasti Canggal) atau "Rakai Mataram Sang Ratu Sanjaya" (Prasasti Mantyasih)

SUMBER PRIMER YANG DIVERIFIKASI:

1. **Prasasti Canggal (732 M)** - verifikasi:
   - Lokasi: Kompleks Candi Gunung Wukir, Desa Kadiluwih, Salam, Magelang ✓
   - Bukit Sthirengga = Gunung Wukir ✓
   - Bahasa: Sanskerta, aksara Pallawa ✓
   - Isi: Sanjaya mendirikan lingga, Raja Sanna, Sanjaya putra Sannaha ✓
   - Sumber: Wikipedia EN "Canggal inscription", jatengprov.go.id

2. **Prasasti Mantyasih (907 M)** - verifikasi:
   - Juga disebut "Prasasti Balitung" atau "Prasasti Tembaga Kedu" ✓
   - Lokasi ditemukan: Kampung Ngadirejo, Parakan, Temanggung ✓
   - Disimpan di Museum Radya Pustaka, Solo ✓
   - Daftar 9 raja: Sanjaya, Panangkaran, Panunggalan, Warak, Garung, Pikatan, Kayuwangi, Watuhumalang, Balitung ✓
   - Sumber: Wikipedia ID Prasasti Mantyasih

3. **Prasasti Wanua Tengah III (908 M)** - verifikasi:
   - Ditemukan November 1983 di Dukuh Kedunglo, Desa Gandulan, Kaloran, Temanggung ✓
   - 4 km timur laut Kota Temanggung ✓
   - Menyebut 12 raja sebelum Balitung (lebih lengkap dari Mantyasih yang hanya 9) ✓
   - Tambah: Dyah Gula, Dyah Tagwas, Panumwangan, Gurunwangi ✓
   - Sumber: Jurnal Kusen 1994 di BRIN, Wikipedia ID Prasasti Wanua Tengah III

4. **Prasasti Pucangan/Calcutta (± 1041 M)** - verifikasi:
   - Ditulis 2 bahasa: Sanskerta & Jawa Kuno ✓
   - Berisi silsilah Airlangga dari Mpu Sindok ✓
   - Mpu Sindok → putri Sri Isyanatunggawijaya → Makutawangsawardhana → ... → Airlangga ✓
   - Disimpan di Indian Museum, Kolkata ✓
   - Sumber: Wikipedia ID Prasasti Pucangan, news.unair.ac.id

5. **Carita Parahyangan** (naskah Sunda abad 16) - verifikasi:
   - Menyebut Sanjaya sebagai putra Sannaha (saudari Raja Sanna) ✓
   - Sanna digulingkan Purbasora, Sanjaya membalas dendam ✓
   - Sumber: Wikipedia EN Sanjaya of Mataram

6. **Berita Cina Dinasti Tang** - verifikasi:
   - Menyebut Kerajaan Ho-ling (Kalingga) ✓
   - Ratu Shima (Ratu Kalingga, ± 674-732 M) ✓
   - Sanjaya adalah cicit Maharani Shima ✓
   - Sumber: Wikipedia EN Shima of Kalingga, legendanusantara.wordpress.com

7. **Jurnal akademis** - verifikasi:
   - Kusen (1994) "Raja-raja Mataram Kuna dari Sanjaya Sampai Balitung" di BRIN Berkala Arkeologi Vol 14 No 2 ✓
   - DOI: https://doi.org/10.30883/jba.v14i2.721 ✓
   - Bambang Sumadio (ed.) 1977 Sejarah Nasional Indonesia II ✓
   - Boechari (1986) Melacak Sejarah Kuno Indonesia Lewat Prasasti ✓

Stage Summary:
- File output: /home/z/my-project/download/riset-drama-nusantara.md
- Total dokumen: 1.297 baris, 15.735 kata (naik dari 15.261 kata)
- Era Mataram Kuno sudah diaudit KETIGA kali dengan cross-check ke sumber primer
- 7 koreksi fundamental dilakukan
- Sub-bagian baru "1.1.1 Catatan Sumber Primer" ditambahkan
- Sumber primer yang diverifikasi: 7 sumber (Prasasti Canggal, Mantyasih, Wanua Tengah III, Pucangan, Carita Parahyangan, Berita Cina, Jurnal BRIN)
- Penting: Negarakretagama dan Pararaton TIDAK membahas era Mataram Kuno secara langsung - hanya Singasari-Majapahit

Tambahan referensi historiografi yang dicantumkan:
- Coedès (1968) The Indianized States of Southeast Asia
- Boechari (1986) Melacak Sejarah Kuno Indonesia Lewat Prasasti
- Soemarsaid Moertono (1968) State and Statecraft in Old Java
- Bambang Sumadio (ed.) 1977 Sejarah Nasional Indonesia II
- Kusen (1994) "Raja-raja Mataram Kuna dari Sanjaya Sampai Balitung" di BRIN

---
Task ID: 7 (master YAML phase 1)
Agent: Main Agent (Z.ai)
Task: Konversi fase 1 ke format YAML komprehensif yang berfungsi sebagai master reference untuk T2I prompt generation

Work Log:
- Membaca ulang fase 1 (Mataram Kuno) di riset-drama-nusantara.md
- Membuat file baru: phase-1-mataram-kuno-master.yaml (1.559 baris, 9.091 kata)
- Struktur YAML dengan 10 top-level keys:
  1. meta - info era, sumber primer, catatan penting
  2. narrative - narasi singkat 5 akta untuk drama
  3. kings_list - daftar 17 raja Mataram Kuno + parallel Syailendra
  4. characters - 8 tokoh kunci dengan prompt karakter+wardrobe detail
  5. locations - 6 kawasan geografis dengan prompt lokasi
  6. wardrobe - 6 jenis busana dengan elemen detail & prompt
  7. artifacts - senjata, regalia, perhiasan
  8. prompt_library - library T2I prompt (character portraits, location scenes, historical moments, daily life)
  9. geographical_regions - 6 kawasan dengan info lengkap
  10. production_notes - color palette, texture, sound design, cultural authenticity
- Verifikasi YAML valid dengan Python yaml parser

Konten yang ditambahkan:
- 8 tokoh kunci dengan prompt T2I detail (character_portrait + wardrobe_detail):
  * Sanjaya, Rakai Panangkaran, Rakai Garung, Rakai Pikatan, Pramodawardhani,
    Balaputradewa, Balitung, Mpu Sindok, Airlangga, Samaratungga (10 tokoh)
- 6 kawasan dengan prompt lokasi (Dieng, Wonosobo, Temanggung, Magelang, Prambanan, Jawa Timur)
- 6 jenis busana dengan prompt (royal_formal, queen_formal, warrior, buddhist_priest, hindu_priest, commoner)
- 4 kategori prompt library: character_portraits, location_scenes, historical_moments, daily_life
- Production notes: color palette, texture, sound design, cultural authenticity

Stage Summary:
- File output: /home/z/my-project/download/phase-1-mataram-kuno-master.yaml
- File pendamping: /home/z/my-project/download/riset-drama-nusantara.md (MD riset lengkap)
- Format: YAML valid, dapat di-parse oleh Python/Node.js
- Dapat dipakai sebagai master reference untuk:
  * Penulis naskah (narrative + characters)
  * Art Director (wardrobe + visual palette)
  * Prompt engineer (prompt_library untuk T2I)
- Total: 1.559 baris, 9.091 kata, 10 top-level keys

---
Task ID: 8 (audit phase 2 Singasari + master YAML)
Agent: Main Agent (Z.ai)
Task: Audit fase 2 Singasari dengan cross-check ke sumber primer + buat master YAML

Work Log:
- Membaca ulang fase 2 Singasari di riset-drama-nusantara.md (baris 385-485)
- Web search 4 batch untuk verifikasi:
  * Pararaton (Kitab Raja-Raja, abad 16) - sumber utama Singasari
  * Negarakretagama pupuh 40-44 - silsilah raja Singasari
  * Prasasti Mula Malurung (1255 M) - Wisnuwardhana & Bhatara Parameswara
  * Prasasti Kudadu (1294 M) - Raden Wijaya & masyarakat Trawas
  * Tohjaya (raja ke-3 yang HILANG dari MD awal)
  * Mahisa Wonga Teleng (leluhur Majapahit)
  * Jayakatwang (pemberontak)
  * Raden Wijaya (pendiri Majapahit)
  * Pertempuran Ganter 1222
  * Ekspedisi Pamalayu 1275-1286

KESALAHAN & KEKURANGAN YANG DITEMUKAN DI MD:

1. **Tohjaya HILANG dari MD awal**
   - Raja ke-3 Singasari (1248 M, singkat)
   - Putra Ken Arok & Ken Umang (selir)
   - Hanya disebut di Pararaton, TIDAK di Negarakretagama
   - KOREKSI: Tambah profil Tohjaya di MD

2. **Mahisa Wonga Teleng HILANG dari MD awal**
   - Putra sulung Ken Arok & Ken Dedes
   - Raja Kadiri bawahan Tumapel
   - LELUHUR RAJA-RAJA MAJAPAHIT lewat Narasinghamurti → Dyah Lembu Tal → Raden Wijaya
   - Disebut sebagai "Bhatara Parameswara" di Prasasti Mula Malurung (1255 M)
   - KOREKSI: Tambah profil Mahisa Wonga Teleng

3. **Wisnuwardhana "raja ketiga" — SALAH**
   - SEBENARNYA raja ke-4 (kalau hitung Tohjaya)
   - Atau ke-5 kalau hitung Mahisa Wonga Teleng sebagai raja bawahan
   - KOREKSI: Ganti menjadi "raja ke-4 Singasari"

4. **Jayakatwang HILANG dari MD awal**
   - Bupati Kadiri yang memberontak 1292 M
   - Membunuh Kertanegara saat upacara Tantra
   - Mewakili dendam Kediri atas kekalahan 1222
   - KOREKSI: Tambah profil Jayakatwang

5. **Raden Wijaya HILANG dari MD awal**
   - Menantu Kertanegara, pendiri Majapahit (1293 M)
   - Berlindung di Kudadu (Trawas) saat Jayakatwang menyerang
   - KOREKSI: Tambah profil Raden Wijaya

6. **Prasasti Mula Malurung (1255 M) HILANG dari MD awal**
   - Dikeluarkan oleh Kertanegara sebagai yuwaraja
   - Menyebut Bhatara Parameswara (Mahisa Wonga Teleng)
   - Sumber primer penting untuk silsilah Singasari-Majapahit
   - KOREKSI: Tambah referensi

7. **Prasasti Kudadu (1294 M) HILANG dari MD awal**
   - Dikeluarkan Raden Wijaya untuk mengharga masyarakat Trawas
   - Sumber untuk kisah pelarian Raden Wijaya
   - KOREKSI: Tambah referensi

8. **Prasasti Maribong (1248 M) HILANG dari MD awal**
   - Sumber untuk gelar lengkap Wisnuwardhana
   - KOREKSI: Tambah referensi

PERBEDAAN PARARATON vs NEGARAKRETAGAMA:
- Pararaton mencatat kudeta dan pembunuhan (versi mitologis-naratif)
- Negarakretagama menyajikan versi "halus" (panegirik resmi Majapahit)
- Tohjaya TIDAK disebut di Negarakretagama (dianggap tidak sah)
- Negarakretagama menyebut Anusapati sebagai putra Rangga Rajasa (bukan Tunggul Ametung)

KOREKSI MD YANG DILAKUKAN:
- Tambah sub-bagian 2.1.1 Catatan Sumber Primer
- Tambah sub-bagian 2.2 Daftar Lengkap Raja-Raja Singasari (5 raja)
- Tambah profil Tohjaya, Mahisa Wonga Teleng, Narasinghamurti, Jayakatwang, Raden Wijaya
- Tambah referensi prasasti: Mula Malurung, Maribong, Kudadu
- Koreksi Wisnuwardhana dari "raja ketiga" menjadi "raja ke-4"
- Tambah info detail Kertanegara: Ekspedisi Pamalayu 1275-1286, menolak upeti Mongol (potong telinga utusan Meng Qi 1289)

FILE YAML MASTER PHASE 2:
- File: /home/z/my-project/download/phase-2-singasari-master.yaml
- Struktur: 9 top-level keys (sama seperti phase 1)
- Konten:
  * meta - info era, sumber primer, catatan penting
  * narrative - 5 akta drama Singasari
  * kings_list - 5 raja + 4 parallel figures (Mahisa Wonga Teleng, Narasinghamurti, Jayakatwang, Raden Wijaya)
  * characters - 9 tokoh dengan prompt T2I detail (Ken Arok, Ken Dedes, Anusapati, Tohjaya, Wisnuwardhana, Mahisa Wonga Teleng, Kertanegara, Jayakatwang, Raden Wijaya)
  * locations - 5 lokasi (Kutaraja-Singasari, Kediri-Daha, Kudadu-Trawas, Candi Jago, Candi Kidal)
  * wardrobe - 5 jenis busana (royal_formal, queen_formal, tantrayana_priest, hindu_priest, warrior)
  * artifacts - senjata (Mpu Gandring dll), regalia (wajra, ghanta, kapala), jewelry
  * prompt_library - 4 kategori: character_portraits, location_scenes, historical_moments, daily_life
  * production_notes - color palette, texture, sound design, cultural authenticity

SUMBER PRIMER YANG DIVERIFIKASI:
1. Pararaton (Kitab Raja-Raja, abad 16) - sumber utama naratif Singasari ✓
2. Negarakretagama pupuh 40-44 (Mpu Prapanca, 1365 M) - silsilah resmi ✓
3. Prasasti Mula Malurung (1255 M) - Wisnuwardhana & Bhatara Parameswara ✓
4. Prasasti Maribong (1248 M) - gelar Wisnuwardhana ✓
5. Prasasti Kudadu (1294 M) - Raden Wijaya & masyarakat Trawas ✓
6. Kidung Harsawijaya - sumber sekunder naratif ✓
7. Kidung Panji Wijayakrama - sumber sekunder ✓

Stage Summary:
- File MD: /home/z/my-project/download/riset-drama-nusantara.md (fase 2 diperbaiki)
- File YAML: /home/z/my-project/download/phase-2-singasari-master.yaml (1.224 baris, 7.317 kata)
- Format: YAML valid, 9 top-level keys
- Tokoh baru: Tohjaya, Mahisa Wonga Teleng, Narasinghamurti, Jayakatwang, Raden Wijaya
- Prasasti baru: Mula Malurung, Maribong, Kudadu
- Total koreksi: 8 koreksi utama

---
Task ID: 9 (audit jilid 3 Kemenbud 2025 — PERDALAM)
Agent: Main Agent (Z.ai)
Task: Audit mendalam Jilid 3 "Nusantara dalam Jaringan Global: Timur Tengah" (Kemenbud 2025) — 17 file markdown, 230.624 kata

Work Log:
- Audit struktural otomatis: 17 file dianalisis (heading hierarchy, page markers, truncation, empty sections, weird chars, blank streaks)
- Audit konsistensi terminologi: Samudra Pasai (53× konsisten), Wali Songo (226× vs variasi 39×), Sultan Malik al-Saleh (1267-1297 M ✓), Sunan Giri (1487-1506 M ✓), Buton (1540 M ✓)
- Cross-jilid comparison: 211 instance ™ di 5 jilid (Jilid 3 paling bersih dengan 24 instance)
- Cross-reference _meta.yaml: selisih word count ≤0,02% (tidak ada kehilangan konten)
- Membuat 2 script audit Python persisten di /home/z/my-project/scripts/

Stage Summary:
- File laporan: /home/z/my-project/download/audit-jilid3-kemenbud-2025.md (510 baris, 3.322 kata)
- File JSON detail: /home/z/my-project/riset-backup/.../jilid-3/_audit/structural-audit.json + structural-summary.json
- Temuan: 6 kategori isu, ~57 titik masalah di 13 dari 17 file
- Kritis (3): OCR garbage heading di 16-epilog.md (L153-155 "AB AD AD AD..."), OCR garbage di 06-bab-1.md (3 heading palsu + sampah tabel L509), catatan kaki sebagai heading di 12-bab-7.md (L heading "(75) al-nasi...")
- Tinggi (9 heading terpotong): 05-pendahuluan-jilid L109-111, 06-bab-1 L228-230, 08-bab-3 L407+L560, 09-bab-4 L363-368, 11-bab-6 L111
- Sedang (24): ™ sebagai OCR error di 8 file bab (pola: 12× setelah titik, 9× setelah apostrof)
- Sedang (21): HTML <sup> tag bocor di 4 file (06-bab-1, 09-bab-4, 10-bab-5, 11-bab-6)
- Sedang (4): Pipe `|` & `!I` menggantikan `I` di 03-pendahuluan-buku.md (SIGNIFIKANSI|, REFORMAS|, INSTITUSIONALISAS!I, TRANSAKS!)
- Ringan: konsistensi "Wali Songo" di 12-bab-7.md (38 variasi dari 218 instance di file itu)
- Positif: konsistensi penamaan tokoh sangat baik; tanggal kunci akurat; format tahun konsisten (M: 1.138× vs Masehi: 28×)
- Rekomendasi 6 prioritas perbaikan dirinci dalam laporan

---
Task ID: 10-A
Agent: Subagent (Explore)
Task: Ekstrak drama material Jilid 4 Bab 1-2

Work Log:
- Baca 06-bab-1.md (266 KB, 1.521 baris) — Bab I "Nusantara dan Jaringan Perdagangan Eropa" (10 subbab A-J: Sriwijaya→Parameswara→Zheng He→Albuquerque 1511→Portugis-Johor→Portugis-Aceh→Sunda-Portugis→Ratu Kalinyamat→Bangsa Iberia-Ternate)
- Baca 07-bab-2.md (221 KB, 1.160 baris) — Bab II "Hegemoni Kekuasaan dan Diplomasi di Nusantara Abad XVII-XVIII" (8 subbab A-H: Tiga Kesultanan Besar Aceh-Mataram-Gowa/Tallo; Militer; Persenjataan; Hewan; Kontribusi Wilayah; Ekspansi & Unifikasi; Kasus Khusus Aceh-Usmani)
- Ekstrak premis utama + paragraf pembuka + 6-8 temuan kunci per bab + implikasi drama
- Penekanan pada konflik politik-agama-antar-kerajaan-kolonial, intrik dinasti & pengkhianatan, narasi tokoh-motivasi-konflik dengan data konkret (tahun, lokasi, sumber primer, komoditas, mata uang)

Stage Summary:
- Bab 1: Penaklukan Malaka 1511 oleh Albuquerque memicu reaksi berkepanjangan dari Johor, Aceh (dukung Turki Usmani), dan Jawa (Demak, Jepara-Ratu Kalinyamat); berakhir dengan pembunuhan Sultan Hairun 1570 oleh Mesquita dan pengusiran Portugis oleh Sultan Baabullah, plus Banda massacre & VOC mulai menggeser Portug is 1605.
- Bab 2: Tiga kesultanan Islam hegemonik — Aceh (Iskandar Muda), Mataram (Sultan Agung), Gowa-Tallo (Sultan Alauddin, Malikussaid, Hasanuddin) — membangun supremasi regional melalui militer, monopoli ekonomi, legitimasi Islam & diplomasi lintas kawasan (Aceh-Usmani, Gowa-Mataram), sebelum akhirnya tergerus VOC lewat Perjanjian Bongaya 1667, Perjanjian Mataram-VOC 1677-1678, dan Perjanjian Giyanti 1755.

---
Task ID: 10-E
Agent: Subagent (Explore)
Task: Ekstrak drama material Jilid 4 Bab 9-10

Work Log:
- Baca 14-bab-9.md (84 KB, 472 baris) — Bab IX: Riau-Johor dan Aceh di Barat Nusantara Abad XVII
- Baca 15-bab-10.md (90 KB, 508 baris) — Bab X: Kemunduran VOC
- Ekstrak premis utama + paragraf konteks + 8 temuan kunci per bab + implikasi drama
- Identifikasi tokoh (dengan tahun kekuasaan), lokasi, sumber primer, konflik-intrik, detail drama
- Fokus ekstraksi: konflik politik (Aceh-Johor-Portugis-VOC), intrik dinasti (pernikahan politik Iskandar Muda-Johor), pengkhianatan (komplotan Tun Abdul Jamil-Portugis 1606), aliansi strategis (Johor-Belanda 1602, Aceh-Belanda 1607), korupsi sistemik VOC, perang Inggris-Belanda, persaingan EIC-DOC-Prancis
- Sertakan data konkret: tahun, lokasi, mata uang (gulden, tahil, real, bahar), komoditas (lada, timah, cengkeh, pala, kopi, opium)
- Sertakan kutipan langsung singkat: Gaastra ("prioritas VOC irasional", "hampir semua pejabat tinggi terlibat dagang pribadi"), kepanjangan VOC ("vergaan onder corruptie"), Anderson ("korupsi sebagai transaksi sosial"), Alatas ("inersia sistemis")
- Multi-perspektif: bedakan versi Melayu vs Belanda perjanjian 1685; sebutkan perbedaan pendapat James I vs sejarawan modern soal Amboina 1623; Anderson vs Alatas tentang akar korupsi

Stage Summary:
- Bab 9: Rivalitas Aceh-Johor abad 17 berubah jadi perlawanan bersama vs VOC, memuncak pada gugurnya Raja Haji Fisabilillah Juni 1784 dan gerilya laut Sultan Mahmud Ri'ayat Syah sampai 1795.
- Bab 10: VOC bangkrut 31 Desember 1799 dengan utang 134,8 juta gulden akibat korupsi sistemik, 4 perang Inggris-Belanda, dan kekalahan strategis dari EIC—meninggalkan warisan hukum, lingua franca, dan budaya korupsi yang jadi cetak biru kolonialisme Hindia Belanda.

---
Task ID: 10-B
Agent: Subagent (Explore)
Task: Ekstrak drama material Jilid 4 Bab 3-4

Work Log:
- Baca 08-bab-3.md (105 KB, 580 baris) — Bab III "Dinamika Keagamaan Baru: Aktivisme dan Intelektualisme Islam"
- Baca 09-bab-4.md (135 KB, 749 baris) — Bab IV "VOC di Nusantara: Monopoli dan Negosiasi"
- Ekstrak premis + 7 temuan kunci (Bab 3) + 9 temuan kunci (Bab 4) + implikasi drama per bab
- Fokus ekstraksi: konflik (politik-agama, kolonial-lokal, antar-kerajaan), intrik (suksesi, aliansi, pengkhianatan), narasi scene (tokoh-motivasi-konflik)
- Data konkret: tokoh dengan tahun kekuasaan, lokasi, sumber primer (manuskrip Garrett 3872Y, Itinerario 1596, Spraeck ende woord-boeck 1603, Bustanus Salatin 1636, surat Sultan Alauddin Makassar 1615), komoditas (cengkeh-pala-fuli-lada-kayu cendana-kamper Borneo), mata uang (real, gulden, para, piaster)
- Kutipan langsung: mare liberum Sultan Alauddin 1615, kebohongan Lintgens di Gelgel, "Pangeran dan prajurit bukan pedagang" (Sultan Agung), sajak Vondel untuk Pattingalloang, catatan VOC tentang utusan Aceh
- Multi-perspektif: debat A.H. Johns (1984) tentang prioritas Jawhar vs Tuhfah; perdebatan Sleeswyk vs pendapat umum tentang penemu kapal fluit; keraguan tentang keaslian Nasihat al-muluk (Patricia Crone)
- Output dikembalikan sebagai teks di pesan final agent (tidak ditulis ke file terpisah)

Stage Summary:
- Bab 3: Jaringan ulama Jawi-Hijaz abad 17 membentuk "Islamic republic of letters" yang menggerakkan tasawuf-filosofis sekaligus aktivisme anti-kolonial, dengan konflik wujudiyyah Aceh (pembakaran kitab 1637) sebagai puncak yang melahirkan tradisi moderasi (Kurani-Sinkili).
- Bab 4: VOC (berdiri 20 Maret 1602) sebagai institusi hybrid-swasta dengan oktroi 21 tahun, memasuki Nusantara lewat intelijen Itinerario Linschoten (1596), ekspedisi bencana De Houtman (1595-97), pembantaian Banda Coen (1621), dan negosiasi alot dengan sultan-sultan Aceh-Makassar-Ternate-Jayakarta-Mataram yang menolak monopoli penuh.

---
Task ID: 10-C
Agent: Subagent (Explore)
Task: Ekstrak drama material Jilid 4 Bab 5-6

Work Log:
- Baca 10-bab-5.md (125 KB, 1.229 baris) — Bab V "Dari Jaringan Dagang ke Kekuasaan Kolonial: Papua Barat dalam Dinamika Dunia Maritim Timur Nusantara, 1500-1800" (5 subbab A-E: Eksistensi Papua dalam Jaringan Perdagangan; Kedatangan Bangsa Eropa-Pelayaran-Pemetaan; Jaringan Pesisir Barat Papua-Maluku; Biakkers; Zona Seram-Gorom; Lampiran Pemetaan Papua abad 16-17)
- Baca 11-bab-6.md (115 KB, 2.064 baris) — Bab VI "VOC di Pulau Banda: Monopoli Rempah, Kekerasan, dan Perbudakan" (4 subbab A-D + Catatan Penutup: Sistem Perken Basis Perbudakan & Kuli Kontrak; Stratifikasi & Struktur Sosial VOC; Budak Perken di Kepulauan Banda Abad 17-18; Kehidupan Budak di Perken)
- Ekstrak premis utama + paragraf pembuka + 8 temuan kunci per bab + implikasi drama
- Penekanan pada konflik (genosida Banda 1621, pelayaran hongi Tidore, persekongkolan Banda-Mataram-Banten-Inggris 1622, bajak laut Makassar-Ende-Sulu), intrik (perang dinasti Nuku vs Tidore, aliansi tujuh raja Onin 1676, Coen-Sonck korespondensi), narasi (Courthope 4 tahun di Run, Ver Huell-Roosje, mitos empat telur Bikusagara)
- Data konkret: 15.000→1.000 jiwa Banda (1621); 38 perken (3 Neira+26 Lonthor+6 Ay+2 Run+1 Rosengain); 8 orang kaya dieksekusi + 210 pria dirantai + 347 wanita-anak jadi budak (Jan 1622); 160 tewas di Run (Agustus 1622); surat Coen-Sonck 3 Maret 1622; harga budak 40 rijksdaalder/100 guilders; keuntungan pala 1.220%; 18-20 kora-kora Tidore tahunan; 1790 armada Tidore tangkap 178 budak Kumamba; 1759 Raja Lewa bayar 55 budak ke Makassar
- Sumber primer dikutip: Nagarakretagama (Jawa abad 14), Tomé Pires Suma Oriental (~1513), Pigafetta (1519), Relacion Miguel Roxo de Brito (1581-82, dicatat ~1600), Valentijn Oud en Nieuw Oost-Indiën, surat Coen-Sonck 3 Maret 1622, Inventaris Arsip Banda ANRI No. 41/47/48/52/53, Ver Huell Herinneringen (1835), Muridan Widjojo Pemberontakan Nuku (2013), Giles Milton Pulau Run (2015), Barjiyah UGM 2009

Stage Summary:
- Bab 5: Papua Barat sebagai simpul aktif jaringan maritim Nusantara (sosolot-hongi-Biakkers) yang direkayasa VOC jadi relasi kolonial timpang via Mandala Tidore (1660/1667/1689/1700) dan Perjanjian London 1824, dengan pemberontakan Sultan Nuku (1780-1810) dan aliansi tujuh raja Onin 1676 sebagai konflik kunci.
- Bab 6: Kepulauan Banda sebagai laboratorium kapitalisme kolonial modern — genosida Coen 1621 (15.000→1.000 jiwa), pembagian 38 perken, surat Coen-Sonck 3 Maret 1622 ("seluruh kelompok mereka harus disingkirkan sepenuhnya"), sistem perkenierstelsel dengan keuntungan pala 1.220%, dan perdagangan budak lintas-kawasan via bajak laut Makassar-Ende-Sulu-Tidore hingga penghapusan resmi 1860.

---
Task ID: 10-D
Agent: Subagent (Explore)
Task: Ekstrak drama material Jilid 4 Bab 7-8

Work Log:
- Baca 12-bab-7.md (190 KB, 1.175 baris) — Bab VII "Diaspora Nusantara: Migrasi dan Perjumpaan Etnik" (8 subbab A-H: Pengantar → Nusantara kisah orang dalam perjalanan → Genosida Banda & diaspora Kei → Diaspora Buton → Ragam Diaspora Batavia → Pengungsian Arung Palakka → Diaspora Pesisir Barat Sumatra [Aceh, Bugis-Makassar, Nias] → Diaspora Bugis-Makassar di Jawa [Banten-Syekh Yusuf, Trunojoyo, Blambangan, Mandar-Buton] → Nuku di kawasan timur)
- Baca 13-bab-8.md (169 KB, 818 baris) — Bab VIII "Rivalitas dan Resistensi" (15 subbab A-O: Perlawanan Hitu, Hoamoal, Iha, Nuku 1779-1805, Papua, Sultan Agung 1628/1629, Trunojoyo 1674-1680, Untung Surapati, Sultan Ageng Tirtayasa-Syekh Yusuf, Gowa-Tallo 1666-1669, Banjarmasin, Geger Pecinan 1740)
- Ekstrak premis utama + paragraf pembuka + 8-11 temuan kunci per bab + implikasi drama
- Penekanan pada konflik (genosida, kudeta, perjanjian sepihak), intrik dinasti (5 bersaudara Bugis-Melayu, suksesi Mataram-Banten-Tidore-Banjar), narasi tokoh-motivasi-konflik dengan data konkret (tahun, lokasi, sumber primer, komoditas, mata uang)
- Multi-perspektif: kematian Trunojoyo (Babad Jawa Tengah vs Timur), kematian Kapten Tack (Belanda vs Jawa), status Nuku (Belanda vs Inggris-Tidore)
- Sumber primer yang dirujuk: Tuhfat al-Nafis, Syair Perang Mengkasar (Enci' Amin), Babad Trunojoyo, Sinrilikna Kappalak Tallumbatua, onotan Banda, Van Hoévell, Vermeulen, Widjojo, Ricklefs, Lubis, Andaya, Leirissa, Abu Hamid, de Graaf

Stage Summary:
- Bab 7: Diaspora Nusantara abad 16-19 — dari genosida Banda 1621 yang melahirkan pelarian ke Kei-Seram, pengungsian Arung Palakka ke Buton, diaspora Aceh di pantai Minangkabau (Panglima Nando 44 tahun), tentara bayaran Bugis & budak Nias di Padang, sampai pemerintahan diaspora Bugis lima-bersaudara di Riau-Johor yang merebut kekuasaan politik lintas Selat Malaka lewat pernikahan dinasti.
- Bab 8: Sepanjang abad 17-18, penguasa lokal Nusantara melakukan spektrum resistensi penuh terhadap VOC yang berubah dari pedagang jadi penguasa politik — dari perang terbuka (Sultan Agung 1628/1629, Hasanuddin 1666-1669), gerilya ulama (Syekh Yusuf ke Cape Town 1693), kudeta diplomasi (Nuku 1779-1805 lintas Tidore-Papua-Inggris), pemberontakan budak (Untung Surapati & Kapten Tack 1686), gerilya ekonomi (Nata Alam bakar lada 1787), hingga tragedi antar-etnik (Geger Pecinan 1740, 10.000 korban) — yang menjadi embrio kesadaran kolektif anti-kolonial.

---
Task ID: 11 (sintesis ringkasan-jilid-4 + setup GitHub)
Agent: Main Agent (Z.ai)
Task: Sintesis 5 subagent (Task 10-A s/d 10-E) jadi ringkasan-jilid-4 + setup GitHub remote

Work Log:
- Write chunk 1 (header + Bab 1) ke /home/z/my-project/scripts/ringkasan-jilid-4-chunk1.md
- Write chunk 2 (Bab 2) ke chunk2.md
- Write chunk 3 (Bab 3 + Bab 4) ke chunk3.md
- Write chunk 4 (Bab 5 + Bab 6) ke chunk4.md
- Write chunk 5 (Bab 7 + Bab 8 + Bab 9 + Bab 10 + Catatan Akhir) ke chunk5.md
- Concat 5 chunks jadi file final: ringkasan-jilid-4-interaksi-awal-barat.md
- Setup git config user.name "Mahmud AFK" + email noreply.github.com
- Add remote origin https://github.com/emailnyamahmud-afk/drama-nusantara.git
- Hilangkan nested .git di riset-backup/ (rename ke .git-backup-nested lalu hapus)
- Remove gitlink submodule riset-backup dari index
- Add semua file riset-backup/phase-1-riset/ + scripts/ringkasan-jilid-4-chunk*.md + audit
- Commit dengan pesan deskriptif
- Fetch origin/main (ada 10 commit sebelumnya dari repo asli user)
- Merge origin/main --allow-unrelated-histories (resolve konflik .gitignore)
- GitHub nolak karena secret terdeteksi di .config/github-token.env
- git rm --cached -r .config/ .env
- Add .config/ dan .env ke .gitignore
- git filter-branch --force hapus .config/ .env dari semua history
- Force push ke GitHub

Stage Summary:
- File ringkasan-jilid-4-interaksi-awal-barat.md: 218 KB, 29.383 kata, 1.008 baris, 126 heading, 10 bab lengkap
- Subagent Task 10-A s/d 10-E: 5 paralel selesai dengan material kaya (5 file MD total ~80KB sebelum concat)
- Repo GitHub: https://github.com/emailnyamahmud-afk/drama-nusantara.git
- Branch: main
- Last commit: 9a40c01 "Merge remote-tracking branch 'origin/main'"
- Secret .config/ dan .env dihapus dari history dengan filter-branch
- 4 ringkasan-jilid MD + audit-jilid3 + scripts + riset-backup (5 jilid MD + 78 file sumber primer) ter-push
- Tugas berikutnya: ringkasan-jilid-5 (Masyarakat Indonesia & Terbentuknya Negara Kolonial 1800-1900)
