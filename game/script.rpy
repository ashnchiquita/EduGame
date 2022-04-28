# character
define g = Character("Ganesha")
define mc = Character("[name]")
define friend = Character("Jeanne")
# guru-guru
define mat = Character("Bu Tricia")
define ind = Character("Pak Bintang")
define ing = Character("Bu Poppy")
define pkn = Character("Pak Juna")

# images
# latar
image bg sekolah = im.Scale("outside hd.jpg",1920,1080)
image bg kelassantuy = im.Scale("kelas santuy hd.jpg",1920,1080)
image bg koridorrame = im.Scale("hallway hd.jpg",1920,1080)
image bg rooftop = im.Scale("rooftop hd.jpg",1920,1080)
image bg board = im.Scale("board hd.jpg",1920,1080)
image bg kelaskosong = im.Scale("class kosong.jpg",1920,1080)
image bg kelas = im.Scale("class hd.jpg",1920,1080)
image bg tangga = im.Scale("stairs hd.jpg",1920,1080)
image bg koridorsepi = im.Scale("corridor hd.jpg",1920,1080)
image bg school = im.Scale("school.jpeg",1920,1080)

# tokoh
image Ganesha = im.Scale("ganesha.png", 720,1080)
image friend sm = "mc smgirl.png"
image friend ss = "mc ssgirl.png"
image mc smboy = "mc smboy.png"
image mc ssboy = "mc ssboy.png"
image mat sm = "mat sm.png"
image mat ss = "mat ss.png"
image ind sm = "ind sm.png"
image ind ss = "ind ss.png"
image ing sm = "ing sm.png"
image ing ss = "ing ss.png"
image pkn sm = "pkn sm.png"
image pkn ss = "pkn ss.png"

# efek
image betul = im.Scale("betul.png",1208,540)
image salah = im.Scale("salah.png",1208,540)

# lain-lain
define disolve = Dissolve(1)

label start:
    scene bg sekolah
    # Transisi
    with disolve
    pause .5
    show Ganesha with disolve
    call var
    play music "audio/bgm.mp3" fadein 1.0 fadeout 1.0
    g "Halo!"
    g "Selamat datang di EduGame!"
    g "Aku Ganesha, pemandu kamu untuk menelusuri dunia EduGame. Salam kenal ya!"
    python:
        name = renpy.input(_("Siapa nama kamu?"))
    g "Halo [mc], ayo persiapkan dirimu untuk menyusuri petualangan di dunia EduGame!"
    $ day = 1
    $ jam = jam
    $ menit = menit
    jump hari_1
    
label hari_1:
    call var
    $ jam = 07
    $ menit = 30
    with disolve
    scene bg school
    centered "{size=+50}{b}{color=#000000}Hari ke-[day]{/color}{/b}{/size}"
    scene bg koridorrame
    show mc smboy
    mc "Wah, ini hari pertamaku masuk sekolah!"
    show mc ssboy
    mc "Waktu sudah menunjukkan pukul [jam]:[menit]. Tapi kok masih teman-teman yang masih main dan ngobrol di luar ya? Aku ikut mereka gak ya?"
    # Sebelum ke kelas
    menu:
        "(Tetap masuk ke kelas.)":
            show mc smboy
            jump masuk
        "(Ikut ngobrol dan main sama yang lain.)":
            show mc smboy
            jump ngobrol
    label masuk:
        $ flag_menu = True
        $ poin += 10
        jump kelas_mtk
    label ngobrol:
        $ flag_menu = False
        $ poin -= 15
        $ menit += 5
        show mc ssboy
        "[mc] pun menyapa seorang temannya yang masih berdiam di koridor kelas."
        mc "Hai! Kenalin aku [mc] dari kelas A, kamu siapa?"
        hide mc ssboy
        show friend sm
        "???" "Wah, dari kelas A? Aku juga dari kelas A, sama dong!"
        show friend ss
        friend "Kenalin, aku Jeanne. Salam kenal yaa!"
        hide friend ss
        show mc smboy
        mc "Salam kenal juga, gak nyangka ternyata sekelas."
        hide mc smboy
        show friend ss
        friend "Iya!!"
        "Mereka pun terus mengobrol..."
        "Karena terlalu asik ngobrol, [mc] jadi terlambat masuk kelas. Waktu telah menunjukkan pukul [jam]:[menit]."
        hide friend sm
        show mc ssboy
        mc "Waduh, gawat, udah jam segini, kita harus cepat-cepat masuk ke kelas."
        hide mc ssboy
        show friend sm
        friend "Oh iya, duh lupa aku hehe."
        "[mc] dan Jeanne pun masuk ke dalam kelas keadaan terlambat."
        jump kelas_mtk
    label kelas_mtk:
        $ jam = 7
        $ menit = 40
        scene bg kelas with disolve
        "Pelajaran pertama, Matematika."
        scene bg board
        show mat sm
        mat "Kenalkan saya Tricia, yang akan mengajar pelajaran matematika di kelas ini."
        show mat ss
        mat "Baik, karena ini hari pertama sekolah, silakan berkenalan dulu dengan teman sekelas kalian sampai jam 8:00."
        scene bg kelas
        show mc ssboy
        mc "Baik Bu!"
        show mc smboy
        "[mc] pun berkenalan dengan seluruh teman sekelasnya dan juga sedikit berbincang-bincang dengan mereka."
        $ jam = 8
        $ menit = 01
        scene bg board with disolve
        show mat ss
        mat "Ya, karena sudah pukul [jam]:[menit], pelajaran dimulai. Saya akan mulai menjelaskan terkait perkalian bilangan. Buka buku paket halaman 2."
        play sound "audio/book.mp3"
        "Kelas" "Baik, Bu."
        scene bg kelas
        show mc smboy
        "Singkat cerita, [mc] pun mengikuti kelas ini dengan baik."
        $ jam = 8
        $ menit = 50
        scene bg board
        show mat sm
        mat "Baiklah anak-anak, sebelum berakhir, silakan kerjakan soal berikut ini."
        show screen soal_mtk()
        menu:
            "4":
                $ s_mtk+=80
                hide screen soal_mtk
                play sound "audio/yay.mp3"
                show betul with moveinleft
                pause 2.0
                hide betul with moveoutright
                show mat ss
                mat "Bagus. Jawabanmu sudah benar."
                scene bg kelas
                show mc ssboy
                mc "Yeay jawabanku benar!"
                jump kelas_pkn
            "5":
                $ s_mtk-=10
                hide screen soal_mtk
                play sound "audio/sad.mp3"
                show salah with moveinleft
                pause 2.0
                hide salah with moveoutright
                show mat sm
                mat "Jawabanmu masih salah. Belajar lagi."
                scene bg kelas
                show mc smboy
                mc "Yah jawabanku salah :(."
                jump kelas_pkn

    label kelas_pkn:
        $ jam = 9
        $ menit = 0
        scene bg kelas with disolve
        "Pelajaran Matematika telah berakhir, [mc] sudah mengikuti kelas Matematika dengan baik. Sekarang adalah pelajaran kedua, yaitu PKN."
        scene bg board
        show pkn sm
        pkn "Selamat pagi anak-anak, gimana kabarnya?"
        scene bg kelas
        show mc smboy
        "Kelas" "Baik Pak!!!"
        scene bg board
        show pkn ss
        pkn "Wah, pada semangat ya. Oke sebelum mulai, saya perkenalan dulu. Perkenalkan, saya Juna yang bakal ngajar PKN di kelas kalian." 
        show pkn ss
        pkn "Kali ini kita akan membahas tentang Pancasila nih. Yuk langsung mulai aja!"
        pkn "Pancasila terdiri dari 5 sila. Sila pertama ..."
        show pkn sm
        scene bg kelas
        show mc smboy
        "Kelas pun terus berjalan. Hingga tak terasa..."
        $ jam = 9
        $ menit = 45
        scene bg board
        show pkn sm
        pkn "Gak kerasa, udah mau berakhir aja nih jamnya. Biar afdol kita kuis kelas ya, hehe."
        show pkn ss
        pkn "Gampang kok! Materi tadi aja. Kerjain soalnya sebaik mungkin ya! Semangat!!!"
        show screen soal_pkn()
        menu:
            "Keadilan Sosial bagi Seluruh Rakyat Indonesia":
                $ s_pkn -= 10
                hide screen soal_pkn
                play sound "audio/sad.mp3"
                show salah with moveinleft
                pause 2.0
                hide salah with moveoutright
                show pkn ss
                pkn "Waduh, sila ketiga itu Persatuan Indonesia. Nanti catatannya dibaca lagi ya, [mc]!"
                scene bg kelas 
                show mc smboy
                mc "Duh, jawaban ku salah."
                scene bg kelas
                "Kelas PKN pun berakhir."
                jump istirahat
            "Persatuan Indonesia":
                $ s_pkn+=80
                hide screen soal_pkn
                play sound "audio/yay.mp3"
                show betul with moveinleft
                pause 2.0
                hide betul with moveoutright
                show pkn ss
                pkn "Wah, keren banget! Jawaban kamu betul!"
                scene bg kelas 
                show mc smboy
                mc "Yuhuu, jawabanku betul!"
                scene bg kelas
                "Kelas PKN pun berakhir."
                jump istirahat
            "Ketuhanan Yang Maha Esa":
                $ s_pkn-=10
                hide screen soal_pkn
                play sound "audio/sad.mp3"
                show salah with moveinleft
                pause 2.0
                hide salah with moveoutright
                show pkn ss
                pkn "Waduh, sila ketiga itu Persatuan Indonesia. Nanti catatannya dibaca lagi ya, [mc]!"
                scene bg kelas 
                show mc smboy
                mc "Duh, jawaban ku salah."
                scene bg kelas
                "Kelas PKN pun berakhir."
                jump istirahat
            "Kemanusiaan yang Adil dan Beradab":
                $ s_pkn-=10
                hide screen soal_pkn
                play sound "audio/sad.mp3"
                show salah with moveinleft
                pause 2.0
                hide salah with moveoutright
                show pkn ss
                pkn "Waduh, sila ketiga itu Persatuan Indonesia. Nanti catatannya dibaca lagi ya, [mc]!"
                scene bg kelas 
                show mc smboy
                mc "Duh, jawaban ku salah."
                scene bg kelas
                "Kelas PKN pun berakhir."
                jump istirahat
            "Kerakyatan yang Dipimpin Oleh Hikmat Kebijaksanaan dalam Permusyawaratan/Perwakilan":
                $ s_pkn-=10
                hide screen soal_pkn
                play sound "audio/sad.mp3"
                show salah with moveinleft
                pause 2.0
                hide salah with moveoutright
                show pkn ss
                pkn "Waduh, sila ketiga itu Persatuan Indonesia. Nanti catatannya dibaca lagi ya, [mc]!"
                scene bg kelas 
                show mc smboy
                mc "Duh, jawaban ku salah."
                scene bg kelas
                "Kelas PKN pun berakhir."
                jump istirahat
    label istirahat:
        $ jam = 10
        $ menit = 0
        scene bg kelassantuy
        "Tak terasa sudah jam [jam]:[menit]."
        play sound "audio/bell.mp3"
        "Bel istirahat pun menggema di sekolah."
        show mc ssboy
        mc "Katanya pemandangan di rooftop bagus, aku akan coba makan di rooftop."
        "[mc] pun berjalan menuju rooftop."
        play sound "audio/walk.mp3"
        scene bg koridorsepi with disolve 
        show mc ssboy
        pause 1.5
        scene bg tangga with disolve
        show mc smboy
        "[mc] pun segera menaiki tangga ke rooftop."
        "Di jalan, ia tidak sengaja bertemu dengan teman sekelasnya."
        hide mc smboy
        show friend ss
        friend "Eh, kamu [mc] kan? Masih inget aku gak? Kita baru aja kenalan tadi pagi lhoo! Mau ke rooftop juga buat makan?"
        hide friend ss
        show mc ssboy
        mc "Iya, Jeanne kan? Masih inget kok aku. Iya nih, mau ke rooftop. Kamu mau ke sana juga?"
        hide mc ssboy
        show friend sm
        friend "Iya. Mau barengan?"
        hide friend sm
        show mc smboy
        mc "Boleh."
        scene bg tangga
        play sound "audio/walk.mp3"
        "Mereka pun berjalan bersama ke rooftop."
        scene bg rooftop
        show mc smboy at left
        show friend ss at right
        friend "Wah bener kata orang-orang, pemandangan di sini indah banget!"
        show mc ssboy at left
        show friend sm at right
        mc "Iya ya. Kalau gitu selamat makan!"
        play sound "audio/eat.mp3"
        show mc smboy at left
        show friend ss at right
        friend "Selamat makan juga!"
        play sound "audio/eat.mp3"
        "Mereka pun memakan bekal yang dibawa masing-masing sembari mengobrol bersama."
        show friend sm at right

        $ jam = 10
        $ menit = 25
        scene bg rooftop with disolve
        show mc smboy at left
        show friend ss at right
        friend "Eh, udah jam [jam]:[menit] nih! Ke kelas yuk, daripada telat nanti."
        show mc ssboy at left
        show friend sm at right
        mc "Eh iya, ayo ke kelas."
        show mc smboy at left
        "Mereka pun segera turun ke kelas."
        play sound "audio/walk.mp3"
        scene bg tangga with disolve 
        show mc smboy at left
        show friend sm at right
        pause 1.5
        scene bg koridorsepi with disolve 
        show mc ssboy at left
        show friend sm at right
        pause 1.5
        scene bg kelassantuy with disolve

        $ jam = 10
        $ menit = 29
        scene bg kelassantuy
        show mc ssboy
        mc "Huft, untung kita gak telat."
        hide mc ssboy
        show friend ss
        friend "Iya. Habis ini pelajaran Bahasa Inggris kan?"
        hide friend ss
        show mc smboy
        mc "Eh, bukannya Bahasa Indonesia?"
        hide mc ssboy
        show friend sm
        friend "Oh iya, aku lupa hehe. Yaudah makasih ya, [mc]!"
        hide friend sm
        show mc smboy
        mc "Oke!"

    label kelas_ind:
        $ jam = 10
        $ menit = 30
        play sound "audio/bell.mp3"
        scene bg kelas with disolve
        "Istirahat telah usai. Sekarang pelajaran ketiga, Bahasa Indonesia."
        scene bg board
        show ind sm
        ind "Anak-anak, kita mulai kelasnya ya..."
        scene bg kelas
        show mc ssboy
        "Kelas" "Baik Pak!!!"
        scene bg board
        show ind sm
        ind "Bagaimana tadi istirahatnya? Sudah makan siang semua kan?"
        scene bg kelas
        show mc ssboy
        "Kelas" "Sudah Pak."
        scene bg board
        show ind sm
        ind "Kalau begitu harus semangat ya ngikutin pelajaran Bahasa Indonesianya. Baik, sekarang Bapak akan membahas tentang..."
        scene bg kelas
        show mc smboy
        "[mc] pun memperhatikan apa yang dijelaskan oleh Pak Bintang dengan saksama."
        "..."

        $ jam = 11
        $ menit = 20
        scene bg board with disolve
        show ind sm
        ind "Baiklah anak-anak, sebagai penutup, Bapak akan memberikan sebuah soal untuk kalian kerjakan."
        show screen soal_ind()
        menu:
            "Rama seharusnya mengambil terlebih dahulu sejumlah uang untuknya sebelum mengembalikan dompet itu.":
                $ s_ind-=10
                hide screen soal_ind
                play sound "audio/sad.mp3"
                show salah with moveinleft
                pause 2.0
                hide salah with moveoutright
                show ind ss
                ind "Jawabannya masih belum tepat ya..."
                scene bg kelas 
                show mc smboy
                mc "Waduh jawabanku salah!"
                jump kelas_ing
            "Tindakan yang dilakukan Rama sudah tepat":
                $ s_ind+=80
                hide screen soal_ind
                play sound "audio/yay.mp3"
                show betul with moveinleft
                pause 2.0
                hide betul with moveoutright
                show ind ss
                ind "Jawabannya sudah benar, bagus."
                scene bg kelas 
                show mc ssboy
                mc "Yeayy jawabanku benar!"
                jump kelas_ing
            "Rama seharusnya tidak usah mempedulikan dompet itu dan lanjut berjalan saja":
                $ s_ind-=10
                hide screen soal_ind
                play sound "audio/sad.mp3"
                show salah with moveinleft
                pause 2.0
                hide salah with moveoutright
                show ind ss
                ind "Jawabannya masih belum tepat ya..."
                scene bg kelas 
                show mc smboy
                mc "Waduh jawabanku salah!"
                jump kelas_ing
        
    label kelas_ing:
        $ jam = 11
        $ menit = 30
        scene bg kelas with disolve
        "Pelajaran terakhir, Bahasa Inggris."
        scene bg board
        show ing sm
        ing "Selamat siang gaes!! Ayo semangat ya ini pelajaran terakhir nih, jangan ngantuk dulu ya!"
        scene bg kelas
        show mc ssboy
        "Kelas" "Siap, Bu!"
        scene bg board
        show ing sm
        ing "Oke karena ini hari pertama, kita belajar yang gampang-gampang aja ya!"
        show ing ss
        ing "Kali ini kita akan membahas tentang partikel a/an ya! Jadi ..."
        scene bg kelas
        show mc smboy
        "[mc] pun memperhatikan pelajaran dengan saksama hingga akhir pelajaran."
        $ jam = 12
        $ menit = 15
        scene bg board with disolve
        show ing sm
        ing "Nah, 1 hal lagi nih sebelum kalian pulang. Kalian kerjain 1 soal ini dulu ya, hehe."
        show screen soal_ing()
        menu:
            "an hour":
                $ s_ing+=80
                hide screen soal_ing
                play sound "audio/yay.mp3"
                show betul with moveinleft
                pause 2.0
                hide betul with moveoutright
                show ing ss
                ing "Yeay! Selamat, jawaban kamu benar!"
                scene bg kelas
                show mc ssboy
                mc "Yeay!"
                jump ngobrol_piket
            "a hour":
                $ s_ing-=10
                hide screen soal_ing
                play sound "audio/sad.mp3"
                show salah with moveinleft
                pause 2.0
                hide salah with moveoutright
                show ing ss
                ing "Yah, jawabannya salah. Gapapa, belajar lagi ya!"
                scene bg kelas
                show mc smboy
                mc "Yah jawabanku salah. Gak papa deh."
                jump ngobrol_piket
            "an hours":
                $ s_ing-=10
                hide screen soal_ing
                play sound "audio/sad.mp3"
                show salah with moveinleft
                pause 2.0
                hide salah with moveoutright
                show ing ss
                ing "Yah, jawabannya salah. Gapapa, belajar lagi ya!"
                scene bg kelas
                show mc smboy
                mc "Yah jawabanku salah. Gak papa deh."
                jump ngobrol_piket
    label ngobrol_piket:
        $ jam = 12
        $ menit = 35
        play sound "audio/bell.mp3"
        scene bg kelassantuy
        "Bel sekolah pun berbunyi, pertanda pelajaran sekolah hari ini selesai."
        show mc ssboy
        "Wah, gak kerasa tadi udah pelajaran terakhir. Hari ini seru banget."
        "Tiba-tiba seseorang datang menghampiri [mc]."
        hide mc ssboy
        show friend ss
        friend "[mc]! Udah cek jadwal piket kelas belum? Aku dapatnya lusa. Kamu dapat kapan?"
        hide friend ss
        show mc smboy
        "[mc] pun segera mengecek jadwal piket dan mencari namanya."
        show mc ssboy
        mc "Oh, aku dapat hari ini."
        hide mc ssboy
        show friend sm
        friend "Oalah, berarti kamu gak langsung pulang ya? Harus bersih-bersih dulu."
        hide friend sm
        show mc ssboy
        menu:
            "Iya dong, aku kan harus piket!":
                $ poin += 20
                hide mc ssboy
                jump piket
            "Gak ah, males. Aku mau langsung pulang.":
                $ poin -= 20
                hide mc ssboy
                show friend ss
                friend "...Oh, oke."
                hide friend ss
                jump pulang
    label piket:
        scene bg kelassantuy
        show friend ss
        friend "Wah! Semangat ya!"
        show friend sm
        friend "Aku duluan ya, sampai jumpa besok!"
        hide friend sm
        show mc ssboy
        mc "Sip! Makasih ya Jeanne."
        hide mc ssboy
        show friend ss
        pause 0.5
        play sound "audio/walk.mp3"
        hide friend ss with disolve
        "Jeanne pun meninggalkan kelas dan pulang."

        $ jam = 12
        $ menit = 40
        show mc ssboy
        mc "Oke, ayo mulai bersih-bersih kelas!"
        "[mc] pun menjalankan tugas piketnya."
        play sound "audio/piket.mp3"
        scene bg kelassantuy
        $ jam = 12
        $ menit = 56
        pause 1.0
        scene bg kelaskosong with disolve
        "[mc] pun membersihkan kelas hingga kelas menjadi rapi."   
        show mc ssboy
        mc "Akhirnya kelas udah bersih! Aku bisa pulang deh."
        jump pulang
    label pulang:
        scene bg kelaskosong with disolve
        show mc smboy
        "[mc] pun segera berjalan menuju ke luar sekolah."
        play sound "audio/walk.mp3"
        scene bg koridorsepi with disolve
        show mc smboy
        pause 1.5
        scene bg school with disolve 
        show mc smboy
        "[mc] pun berjalan menuju rumahnya."
        jump end_day1
    label end_day1:
        scene bg sekolah with disolve
        show Ganesha
        g "Nah, petualangan kamu hari ini udah berakhir! Gimana perasaan kamu hari ini?"
        hide Ganesha
        show mc ssboy
        menu:
            "Seneng banget! Hari ini seru banget!":
                play sound "audio/yay.mp3"
                hide mc ssboy
                show Ganesha
                g "Wah, aku ikut senang mendengarnya."
                jump eval
            "Biasa saja.":
                hide mc ssboy
                show Ganesha
                g "Wihh, baik deh, yang penting gak ada yang bikin sedih hari ini."
                jump eval
            "Aku gak ngerasa seneng hari ini :(.":
                play sound "audio/sad.mp3"
                hide mc ssboy
                show Ganesha
                g "Yahh! Jangan sedih dong, hehe."
                jump eval
    return
label eval:
    scene bg sekolah
    show Ganesha
    g "Nah, gimana sih hasil akhir dari evaluasi petualangan kamu selama ini?"
    g "Pasti kamu udah kepo kan."
    g "Kalau gitu langsung ditunjukin aja ya..."
    play sound "audio/drumroll.mp3"
    scene bg sekolah
    show Ganesha
    g "1, 2, 3!"
    jump nilai_akhir

label nilai_akhir:
    $ totalpoin =  poin + s_mtk +  s_ind + s_ing + s_pkn  
    if totalpoin >= 370:
        scene bg koridorsepi
        play sound "audio/yay.mp3"
        centered "{size=+20}{color=#000000}Selamat, {b}Good Ending!{/b} [mc] dinyatakan lulus.{/color}{/size}"
    else:
        scene bg koridorsepi
        play sound "audio/sad.mp3"
        centered "{size=+20}{color=#000000}Yah, sayang sekali. {b}Bad Ending!{/b} [mc] dinyatakan tidak lulus.{/color}{/size}"
    return
   
label var:
    $ poin = 50
    $ s_mtk = 0
    $ s_pkn = 0
    $ s_ind = 0
    $ s_ing = 0
    $ jam = "--"
    $ menit = "--"
    $ flag_menu = False
    return
