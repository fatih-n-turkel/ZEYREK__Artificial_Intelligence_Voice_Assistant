import speech_recognition as sr
import datetime
import webbrowser
import datetime
import time
from gtts import gTTS
from playsound import playsound
import random
from random import choice
import os
import requests
import json
import locale
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
import pytesseract
import math
from collections import deque
import face_recognition

r = sr.Recognizer()
an = datetime.datetime.now()
locale.setlocale(locale.LC_ALL, '')


##############################################  KONUŞTURMA  ###################################################

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak("Anlayamadım")
            return record()  # ben ekledim
        except sr.RequestError:
            speak("Sistem Çalışmıyor.")
        return voice



def response(voice):
    if "kimsin" in voice:
        pass

    else:
        yanlis()


def yuz_tanima():
    def face_id_alt():
        image_of_bill = face_recognition.load_image_file('md.jpg')
        bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

        image_of_steve = face_recognition.load_image_file('murat.jpg')
        steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]

        image_of_elon = face_recognition.load_image_file('fatih.jpg')
        elon_face_encoding = face_recognition.face_encodings(image_of_elon)[0]

        #  Create arrays of encodings and names
        known_face_encodings = [
            bill_face_encoding,
            steve_face_encoding,
            elon_face_encoding
        ]

        known_face_names = [
            "Muhammed Emir Gözcü",
            "Murat Türkel",
            "Fatih Naim Türkel"
        ]

        # Load test image to find faces in
        test_image = face_recognition.load_image_file('fotoface.jpg')

        # Find faces in test image
        face_locations = face_recognition.face_locations(test_image)
        face_encodings = face_recognition.face_encodings(test_image, face_locations)

        # Convert to PIL format
        pil_image = Image.fromarray(test_image)

        # Create a ImageDraw instance
        draw = ImageDraw.Draw(pil_image)

        # Loop through faces in test image
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Seni Tanimiyorum"

            # If match
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                print("Hoşgeldin ", name)
                speak("Hoşgeldin " + name)  # BUNU SPEAK YAP

            # Draw box
            draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0))

            # Draw label
            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(255, 255, 0),
                           outline=(255, 255, 0))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(0, 0, 0))

        del draw

        # Display image
        # pil_image.show()

        # Save image
        pil_image.save('identify.jpg')

    def foto_cek_2_faceid():
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        return_value, image = camera.read()
        cv2.imwrite('fotoface.jpg', image)
        camera.release()
        cv2.destroyAllWindows()
        face_id_alt()

    foto_cek_2_faceid()


def speak(string):
    tts = gTTS(string, lang="tr")
    rand = random.randint(1, 10000)
    file = "audio-" + str(rand) + ".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


def yanlis():
    speak("Lütfen başka bir emir verin")
    record()


yuz_tanima()

#print("Nasıl Yardımcı Olabilirim!")
#speak("Nasıl Yardımcı Olabilirim!")
# time.sleep(1)
#while 1:
    #voice = record()
    #print(voice)
    #response(voice)

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

from tkinter import *
import time
import requests
from bs4 import BeautifulSoup
from PIL import ImageTk, Image

def arayuz():
    root = Tk()
    root.title('ZEYREK 1.0')
    root.iconbitmap('logo4.ico')
    root.geometry("1080x1080")
    root.attributes('-fullscreen', True)
    #root.state('zoomed')
    #root.attributes('-alpha', 0.5)
    root.wm_attributes('-transparentcolor', '#60b26c')

    #########################################################################################

    ############################################################################################

    def asistan():
        ###########################         ZEYREK 1.0        #############################
        #############################################################################################
        #                                                                                             #
        ################################################### LIB #######################################################

        import speech_recognition as sr
        import datetime
        import webbrowser
        import datetime
        import time
        from gtts import gTTS
        from playsound import playsound
        import random
        from random import choice
        import os
        import requests
        import json
        import locale
        from bs4 import BeautifulSoup
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        import pyautogui
        import cv2
        import cv2 as cv
        import numpy as np
        from matplotlib import pyplot as plt
        from PIL import Image, ImageDraw
        import pytesseract
        import math
        from collections import deque
        import face_recognition

        r = sr.Recognizer()
        an = datetime.datetime.now()
        locale.setlocale(locale.LC_ALL, '')

        ##############################################  KONUŞTURMA  ###################################################

        def record(ask=False):
            with sr.Microphone() as source:
                if ask:
                    speak(ask)
                audio = r.listen(source)
                voice = ""
                try:
                    voice = r.recognize_google(audio, language="tr-TR")
                except sr.UnknownValueError:
                    speak("Anlayamadım")
                    return record()  # ben ekledim
                except sr.RequestError:
                    speak("Sistem Çalışmıyor.")
                return voice
            ########################################## BURAYA KADAR SÖYLEDİĞİN SÖZÜ ALGILAYIP EKRANA ÇIKTISINI VERİYOR

        def response(voice):
            if "kimsin" in voice:
                kendini_tanitma()

            elif "nasılsın" in voice:
                speak("iyidir ne olsun, yaşayıp gidiyoruz. sende ne var ne yok, hayat nasıl gidiyor?")

            elif "naber" in voice:
                speak("iyidir ne olsun, yaşayıp gidiyoruz. sende ne var ne yok, hayat nasıl gidiyor?")

            elif "iyiyim" in voice:
                speak("Allah iyilik versin")

            elif "kötü" in voice:
                speak("Hayırdır, canını sıkan bir durum mu oldu? canını sıkanın canını sıkarız.")

            elif "teşekkür" in voice:
                speak("ne demek, vazifemiz!")

            elif "Sağ ol" in voice:
                speak("ne demek, vazifemiz!")

            elif "eyvallah" in voice:
                speak("eyvallah")

            elif "iyi" in voice:
                speak("evet")

            elif "Evet" in voice:
                speak(" güzel")

            elif "Hayır" in voice:
                speak("peki")

            elif "yaratıcı" in voice:
                speak("Allah")

            elif "güzel" in voice:
                speak("evet")

            elif "çalış" in voice:
                speak("kolay gelsin")

            elif "orada" in voice:
                speak("evet")

            elif "saat" in voice:
                speak(datetime.datetime.now().strftime("%H:%M:%S"))

            elif "arama" in voice:
                arama()

            elif "tamamdır" in voice:
                speak("Görüşürüz!")
                time.sleep(1)
                uyku_modu()  # sadece bunu sil
                # speak("Bu arada beni çağırmak için hey! diyebilirsin")
                # exit() yorum satırını kaldırınca tamamdır deyince çıkış yapıyor
                # bu alttaki kodlar bana ait def speak e kadar

            elif "kapat" in voice:
                speak("selametle")
                time.sleep(1)
                exit()

            elif "hey" in voice:
                speak("Nasıl yardımcı olabilirim?")
                time.sleep(1)
                while 1:
                    voice = record()
                    print(voice)
                    response(voice)

            elif "Fıkra" in voice:
                fikra()

            elif "hava" in voice:
                hava_durumu()

            elif "not" in voice:  # not yazmak için
                ajanda()

            elif "Ajanda" in voice:  # notu okumak için
                ajandaoku()

            elif "araştır" in voice:
                arastir()

            elif "gün" in voice:
                zaman_gun()
            elif "ay" in voice:
                zaman_ay()
            elif "yıl" in voice:
                zaman_yil()
            elif "tarih" in voice:
                zaman_bugun()

            elif "dakika" in voice:
                son_dakika_haber()

            elif "mesaj" in voice:
                whatsapp_web_mesaj_gonder()

            elif "izle" in voice:
                youtube()

            elif "çevir" in voice:
                ceviri()

            elif "kimdir" in voice:
                unlu_bio()

            elif "açık mı" in voice:
                calisma_saatleri()

            elif "fotoğraf" in voice:
                fotograf_goster()

            elif "namaz" in voice:
                namaz_vakitleri()

            elif "yol" in voice:
                navigasyon()

            elif "mekan" in voice:
                mekan_bul()

            elif "Spor" in voice:
                spor()

            elif "hesaplama" in voice:
                matematiksel_islemler()

            elif "film" in voice:
                film_ac()

            elif "dizi" in voice:
                dizi_ac()

            elif "döviz hesapla" in voice:
                doviz_hesapla()

            elif "döviz kuru" in voice:
                doviz_kuru()

            elif "ucuz" in voice:
                en_ucuz_cimricom()

            elif "N11" in voice:
                n11_alisveris_yap()

            elif "trendyol" in voice:
                trendyol_alisveris_yap()

            elif "hepsi burada" in voice:
                hepsiburada_alisveris_yap()

            elif "GittiGidiyor" in voice:
                gittigidiyor_alisveris_yap()

            elif "vatan" in voice:
                vatanbilgisayar_alisveris_yap()

            elif "teknosa" in voice:
                teknosa_alisveris_yap()

            elif "mediamarkt" in voice:
                mediamarkt_alisveris_yap()

            elif "aliexpress" in voice:
                aliexpress_alisveris_yap()

            elif "kamera" in voice:
                speak("kapatmak için q tuşuna basın")
                kamera_ac()

            elif "Fotoğraf" in voice:
                fotograf_cek()

            elif "video" in voice:
                speak("durdurmak için q tuşuna basın")
                video_cek()

            elif "renk" in voice:
                speak("durdurmak için q tuşuna basın")
                renk_algilama()

            elif "Metin" in voice:
                speak("fotoğrafın ismi nedir?")
                fotograftaki_yaziyi_oku()

            elif "el" in voice:
                speak("lütfen elinizi ekrandaki alandan ayırmayın")
                el_hareketleri_algilama()

            elif "gülümseme" in voice:
                speak("çıkmak için q tuşuna basın")
                gulumseme_algilama()

            elif "insan" in voice:
                speak("çıkmak için q tuşuna basın")
                insan_bedeni_algilama()

            elif "100" in voice:
                speak("çıkmak için q tuşuna basın")
                yuz_algilama()

            elif "göz" in voice:
                speak("çıkmak için q tuşuna basın")
                goz_algilama()

            elif "çizim" in voice:
                speak("çıkmak için q tuşuna basın")
                speak("ekrana mavi bir cisimle yazı yazdırın")
                ekrana_cizim_yapma()

            elif "görüyorsun" in voice:
                nesne_algilama_yolo()

            elif "makyaj" in voice:
                speak("büyük bir zevkle")
                saka_makyaji()

            elif "arttır" in voice:
                ses_arttirma_kontrol()

            elif "azalt" in voice:
                ses_azaltma_kontrol()

            elif "kes" in voice:
                ses_kapat_ac()

            elif "bilgisayarı" in voice:
                bilgisayari_kapatma()

            elif "yeniden" in voice:
                bilgisayari_yeniden_baslatma()

            elif "uyku" in voice:
                bilgisayari_uyku_moduna_alma()

            elif "screen shot" in voice:
                pass
                ekran_fotosu_ss()

            elif "uygulamayı" in voice:
                uygulama_kapatma()

            else:
                yanlis()

        ###############################################   İÇERİK  #####################################################

        def fikra():
            fikralar = [
                'Lise çağındaki bir çocuk okula kayıt olmak için gider. Müdür sorar, Oğlum adın ne?. Çocuk: Memehmet yayayayakut. Müdür: Oğlum kekeme misin sen? Çocuk: Hayır hocam, babam kekemeydi',
                'Temel aldığı bir daktiloyu bozuk diye geri götürdü. Satıcı; Neresi bozuk, dün aldığında sağlamdı. Temel:İki tane "a" yok, saat yazamıyorum.',
                'Hoca bir gün anahtarını kaybetmiş. Bahçede döne döne ararken hanımı sormuş:Anahtarını nerede düşürdün bey? Bre kadın, nerede düşürdüğümü bilsem hiç arar mıyım?']

            secim = choice(fikralar)
            speak(secim)

        def hava_durumu():
            import requests
            import json

            api_url = 'http://api.openweathermap.org/data/2.5/weather?q=Istanbul,tr&APPID=378c60283dcc17cfe37eb295b61c5c37'

            result = requests.get(api_url)
            result1 = json.loads(result.text)

            sicaklik = int((result1["main"]["temp"]) - 273)
            durum = result1["weather"][0]["description"]

            speak(f"istanbul {sicaklik} derece ve şuan {durum}")

        def ajanda():  # kod aslında tamam fakat tarih (t) girdisini input ile değil voice ile alamıyorum
            locale.setlocale(locale.LC_ALL, '')  # tr çeviri
            an = datetime.datetime.now()  # bugün
            ay = datetime.datetime.strftime(an, '%B')  # bulunduğumuz ay
            gun = datetime.datetime.strftime(an, '%A')  # bulunduğumuz gün
            resulttakvim1 = datetime.datetime.strftime(an, 'bugünün tarihi %d.%m.%Y.')
            resulttakvim2 = datetime.datetime.strftime(an, 'bugün %d.%B.%A.%Y.')

            # t = '27 Mayıs saat 12:34'
            # t = input("gün ay saat saat: ")
            speak("gün ay saat ve saat söyler misiniz?")
            t = record()
            gün, ay, saat = [i for i in t.split() if 'saat' not in i]
            # print(gün)
            # print(saat)

            with open(f"{t[:]}.txt", "a+", encoding='utf-8') as dosya:
                speak("buyrun sizi dinliyor ve kaydediyorum.")
                notgir = record()
                ekle = (f"{t} tarihi için. {notgir} notunuz bulunmaktadır.")
                dosya.write(ekle)
                speak("notunuz kaydedilmiştir")

        def ajandaoku():
            speak("Tarih söyleyin")
            tarihsoyle = record()
            print(tarihsoyle)
            with open(f"{tarihsoyle}.txt", "r", encoding='utf-8') as dosya:
                ic = dosya.read()
                speak(ic)

        def arama():
            speak("ne aramak istiyorsunuz? ")
            search = record()
            driver = webdriver.Chrome()
            url = "https://www.google.com/search?q=" + search
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)
            speak(search + "hakkında bulduklarım")

            time.sleep(1)
            speak("hangi sıradakini ziyaret etmek istiyorsunuz")
            sitenedir = record()
            siteInput = driver.find_element_by_xpath(
                f'//*[@id="rso"]/div[{sitenedir}]/div/div/div[1]/a/div/cite').click()

        def arastir():
            speak("araştırmak istediğiniz şey nedir")
            vikisearch = record()
            vikiurl = "https://tr.wikipedia.org/wiki/" + vikisearch
            webbrowser.get().open(vikiurl)

            urls = ["https://tr.wikipedia.org/wiki/" + vikisearch]
            text = f"{vikisearch}"

            # list = ["h1", "h2", "h3", "p", "a", "ul", "span", "input"]
            list = ["p"]

            with open(vikisearch + ".txt", "w", encoding="utf-8") as outfile:
                for url in urls:

                    website = requests.get(url)
                    soup = BeautifulSoup(website.content, "lxml")
                    tags = soup.find_all(list)
                    text = ["".join(s.findAll(text=True)) for s in tags]

                    text_len = len(text)

                    for item in text:
                        print(item, file=outfile)

            with open(vikisearch + ".txt", "r", encoding="utf-8") as vikidosya:
                vikioku = vikidosya.readline()
                speak(vikioku)

        def zaman_bugun():
            speak(datetime.datetime.strftime(an, '%d %B %Y'))

        def zaman_gun():
            speak(datetime.datetime.strftime(an, '%A'))

        def zaman_ay():
            speak(datetime.datetime.strftime(an, '%B'))

        def zaman_yil():
            speak(datetime.datetime.strftime(an, '%Y'))

        def son_dakika_haber():
            r = requests.get("https://www.haberler.com/son-dakika/")
            source = BeautifulSoup(r.content, "lxml")
            print(source.find("p").text)
            speak(source.find("p").text)

        def uyku_modu():
            bekleme = record()
            if "Zeyrek" in bekleme:
                speak("buyrun")
                a = record()
                response(a)
            else:
                print("beklemedeyim")
                # print(bekleme)
                return uyku_modu()

        def youtube():
            speak("ne izlemek istiyorsunuz? ")
            girdi = record()
            driver = webdriver.Chrome()
            url = "https://www.youtube.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle

            driver.switch_to.window(main_window)

            searchInput = driver.find_element_by_xpath('//*[@id="search"]')
            searchInput.send_keys(girdi)
            time.sleep(1)
            searchInput.send_keys(Keys.ENTER)

            speak("hangi sıradaki videoyu açmak istiyorsunuz? ")
            videonedir = record()
            if "bir" in videonedir:
                videonedir = "1"

            videoInput = driver.find_element_by_xpath(f'//*[@id="contents"]/ytd-video-renderer[{videonedir}]').click()
            speak("tam ekran ya da durdur diyebilirsin")
            videodurum = record()
            if "tam ekran" in videodurum:
                pyautogui.press("f")
            elif "dur" in videodurum:
                pyautogui.press("space")
            elif "devam" in videodurum:
                pyautogui.press("space")
            elif "sayfa" in videodurum:
                driver.find_element_by_xpath('//*[@id="logo-icon"]').click()
            elif "ileri sar" in videodurum:
                pyautogui.press("right")
            elif "geri sar" in videodurum:
                pyautogui.press("left")
            elif "sesi kıs" in videodurum:
                pyautogui.press("down")
            elif "sesi aç" in videodurum:
                pyautogui.press("up")

        def whatsapp_web_mesaj_gonder():
            driver = webdriver.Chrome()
            url = "https://web.whatsapp.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            time.sleep(2.5)
            speak("Kaçıncı sıradaki sohbete mesaj göndermek istiyorsunuz? ya da aramak istediğiniz kişi?")
            sira = record()
            if "birinci" in sira:
                siraInput = driver.find_element_by_xpath(
                    '//*[@id="pane-side"]/div[1]/div/div/div[11]').click()  # listedeki birinci kişi
                searchInput = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
                speak("ne yazmak istersiniz?")
                girdi = record()
                searchInput.send_keys(girdi)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                time.sleep(1)
                # searchInputa = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
                searchInput.send_keys(Keys.ENTER)
                # return response(voice)
            elif "2" in sira:
                siraInput = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[10]').click()
                searchInput = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
                speak("ne yazmak istersiniz?")
                girdi = record()
                searchInput.send_keys(girdi)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                # return response(voice)
            elif "3" in sira:
                siraInput = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[9]').click()
                searchInput = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
                speak("ne yazmak istersiniz?")
                girdi = record()
                searchInput.send_keys(girdi)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                # return response(voice)
            elif "4" in sira:
                siraInput = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[8]').click()
                searchInput = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
                speak("ne yazmak istersiniz?")
                girdi = record()
                searchInput.send_keys(girdi)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                # return response(voice)
            elif "5" in sira:
                siraInput = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[7]').click()
                searchInput = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
                speak("ne yazmak istersiniz?")
                girdi = record()
                searchInput.send_keys(girdi)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                # return response(voice)
            elif "6" in sira:
                siraInput = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[6]').click()
                searchInput = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
                speak("ne yazmak istersiniz?")
                girdi = record()
                searchInput.send_keys(girdi)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                # return response(voice)
            elif "ara" in sira:
                speak("kimi aramak istiyorsunuz?")
                araa = record()
                arama = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')  # arama butonu
                arama.send_keys(araa)
                time.sleep(1)
                arama.send_keys(Keys.ENTER)
                time.sleep(1)
                aranan = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[4]').click()

                searchInput = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
                speak("ne yazmak istersiniz?")
                girdi = record()
                searchInput.send_keys(girdi)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                time.sleep(1)
                searchInput.send_keys(Keys.ENTER)
                # return response(voice)

        def ceviri():
            speak("hangi dilden çevireceksiniz")
            birincidil = record()
            print(birincidil)
            if "Türkçe" in birincidil:
                birincidil = "tr"
            elif "İngilizce" in birincidil:
                birincidil = "en"
            elif "Almanca" in birincidil:
                birincidil = "de"
            elif "Rusça" in birincidil:
                birincidil = "ru"
            else:
                birincidil = "auto"
            speak("hangi dile çevireceksiniz")
            ikincidil = record()
            print(ikincidil)
            if "Türkçe" in ikincidil:
                ikincidil = "tr"
            elif "İngilizce" in ikincidil:
                ikincidil = "en"
            elif "Almanca" in ikincidil:
                ikincidil = "de"
            elif "Rusça" in ikincidil:
                ikincidil = "ru"
            else:
                speak("şuan sadece türkçe ingilizce almanca ve rusçaya çeviriyoruz.")

            driver = webdriver.Chrome()
            url = f"https://translate.google.com.tr/?hl=tr&tab=TT&sl={birincidil}&tl={ikincidil}&op=translate"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            speak("sizi dinliyorum")
            dinl = record()
            ceviriInput = driver.find_element_by_xpath(
                '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
            time.sleep(1)
            ceviriInput.send_keys(dinl)
            ceviriInput.send_keys(Keys.ENTER)
            time.sleep(1)

            if ceviriInput.send_keys(Keys.ENTER) == True:
                time.sleep(1)
                sonhali = driver.find_element_by_xpath('//*[@id="ow305"]/div[1]/span/button/span[2]').click()

                # NOT: NEDENSE ASİSTAN BU SESLİ OKUMA BUTONUNA BASAMIYOR, İF BLOĞUNU KALDIRINCA DA İLK BAŞTA BUTON GÖZÜKMEDİĞİ İÇİN HATA VERİYOR

        # sesli cevap vermiyor

        def unlu_bio():
            speak("kimin hakkında bilgi öğrenmek istiyorsunuz")
            girdibioyas = record()

            driver = webdriver.Chrome()
            url = 'http://www.kimkimdir.net.tr/'
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)
            bioyasInput = driver.find_element_by_xpath('//*[@id="s"]')
            bioyasInput.send_keys(girdibioyas)
            time.sleep(1)
            bioyasInput.send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="search-result-people"]/div[1]/div[1]/div[1]/div[2]/h2/a').click()

            content = driver.find_element_by_xpath("//div[@class='single-people-bio']").text
            speak(content)

        def calisma_saatleri():
            speak("hangi firma:")
            firmaa = record()
            firma = f"{firmaa} harita"
            driver = webdriver.Chrome()
            url = "https://www.google.com.tr/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            arama.send_keys(firma)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)

            calisma_saatleri_goster = driver.find_element_by_xpath(
                '//*[@id="rso"]/div[1]/div/div/div[2]/div/div[4]/div[1]/div/div/a[1]/div/span/div[2]').text
            speak(calisma_saatleri_goster)

        def fotograf_goster():
            speak("ne aramak istiyorsunuz:")
            foto = record()
            driver = webdriver.Chrome()
            url = "https://www.google.com.tr/imghp?hl=tr&tab=ri&authuser=0&ogbl"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
            arama.send_keys(foto)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)
            speak("bulduğum sonuçlar:")

        def namaz_vakitleri():
            driver = webdriver.Chrome()
            url = "https://namazvakitleri.diyanet.gov.tr/tr-TR/9541/istanbul-icin-namaz-vakti"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            kac_dk_liste = []
            kac_dk = driver.find_element_by_xpath("//div[@class='remaning-time']").text
            kac_dk_liste.append(kac_dk)
            hangi_vakte = driver.find_element_by_xpath("//div[@class='tr-vakit-txt']").text
            speak(hangi_vakte + kac_dk_liste[0][1] + "saat" + kac_dk_liste[0][3:5] + "dakika")

        def navigasyon():
            speak("nereye gidiyoruz:")
            nereye = record()
            driver = webdriver.Chrome()
            url = "https://www.google.com.tr/maps?hl=tr&tab=rl&authuser=0"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('//*[@id="searchboxinput"]')
            arama.send_keys(nereye)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            a = time.sleep(5)
            if a == True:
                yol_tarifi_butonu = driver.find_element_by_xpath(
                    '//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div/button').click()
                speak("buyrun")

        # sadece en sondaki yol tarifi butonuna basmıyor

        def mekan_bul():
            speak("nasıl bir mekan arıyoruz:")
            mekan = record()
            driver = webdriver.Chrome()
            url = "https://www.google.com.tr/maps?hl=tr&tab=rl&authuser=0"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('//*[@id="searchboxinput"]')
            arama.send_keys(mekan)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            speak(f"sizin için bulduğum {mekan} sonuçları")

        def spor():
            speak("hangi takım")
            takim = record()

            driver = webdriver.Chrome()
            url = 'https://www.fanatik.com.tr/'
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)
            arama = driver.find_element_by_xpath('/html/body/header/div/div/div/button[1]/i').click()
            time.sleep(2)
            bioyasInput = driver.find_element_by_xpath('//*[@id="txtSearchForm"]')
            bioyasInput.send_keys(takim)
            time.sleep(1)
            bioyasInput.send_keys(Keys.ENTER)
            time.sleep(1)

        # haberi sesli okumuyor

        def matematiksel_islemler():
            speak("işlem:")
            islem = record()
            driver = webdriver.Chrome()
            url = "https://web2.0calc.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)
            time.sleep(3)
            driver.find_element_by_xpath(
                '//*[@id="qc-cmp2-ui"]/div[2]/div/button[1]').click()  # ilk açıldığında çıkan disagree butonu için
            islem_yaz = driver.find_element_by_xpath('//*[@id="input"]')
            time.sleep(1)
            islem_yaz.send_keys(islem)
            time.sleep(1)
            islem_yaz.send_keys(Keys.ENTER)
            time.sleep(1)
            islem_oku = driver.find_element_by_xpath('//*[@id="hist"]/button[2]').click()
            time.sleep(1)
            islem_oku2 = driver.find_element_by_xpath('//*[@id="histframe"]/ul/li[1]/p[1]').text
            speak(islem_oku2)

        def film_ac():  # rastgele o günün popüler filmini açar
            url = "https://yabancidizi.pw/kesfet/eyJjb250ZW50IjoiMSJ9"
            page = webbrowser.get().open(url)

        def dizi_ac():
            url = "https://yabancidizi.pw/kesfet/bnVsbA=="
            page = webbrowser.get().open(url)

        def doviz_kuru():
            driver = webdriver.Chrome()
            url = "https://www.doviz.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            altin1 = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[1]/a/span[1]').text
            altin2 = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[1]/a/span[2]').text

            dolar1 = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[2]/a/span[1]').text
            dolar2 = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[2]/a/span[2]').text

            euro1 = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[3]/a/span[1]').text
            euro2 = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[3]/a/span[2]').text

            sterlin1 = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[4]/a/span[1]').text
            sterlin2 = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[4]/a/span[2]').text

            bitcoin1 = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[6]/a/span[1]').text
            bitcoin2 = driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[6]/a/span[2]').text

            speak(altin1 + " " + altin2)
            speak(dolar1 + " " + dolar2)
            speak(euro1 + " " + euro2)
            speak(sterlin1 + " " + sterlin2)
            speak(bitcoin1 + " " + bitcoin2)

        def doviz_hesapla():
            speak("evet: ")
            doviz = record()
            driver = webdriver.Chrome()
            url = "https://www.google.com.tr/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            arama.click()
            arama.send_keys(doviz)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)

            sonuc1 = driver.find_element_by_xpath(
                '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
            sonuc2 = driver.find_element_by_xpath(
                '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[2]').text
            speak(sonuc1 + " " + sonuc2)

        def en_ucuz_cimricom():
            speak("hangi ürünü merak ediyorsunuz:")
            urun = record()
            driver = webdriver.Chrome()
            url = "https://www.cimri.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/div/div/div[2]/div[1]/div/input')
            arama.click()
            arama.send_keys(urun)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)
            speak("bulduğum sonuçlar")

        def n11_alisveris_yap():
            speak("hangi ürünü merak ediyorsunuz:")
            urun = record()
            driver = webdriver.Chrome()
            url = "https://www.n11.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('//*[@id="searchData"]')
            arama.click()
            arama.send_keys(urun)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)
            speak("bulduğum sonuçlar")

        def trendyol_alisveris_yap():
            speak("hangi ürünü merak ediyorsunuz:")
            urun = record()
            driver = webdriver.Chrome()
            url = "https://www.trendyol.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('//*[@id="auto-complete-app"]/div/div[2]/input')
            arama.click()
            arama.send_keys(urun)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)
            speak("bulduğum sonuçlar")

        def hepsiburada_alisveris_yap():
            speak("hangi ürünü merak ediyorsunuz:")
            urun = record()
            driver = webdriver.Chrome()
            url = "https://www.hepsiburada.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('//*[@id="SearchBoxOld"]/div/div/div[1]/div[2]/input')
            arama.click()
            arama.send_keys(urun)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)
            speak("bulduğum sonuçlar")

        def gittigidiyor_alisveris_yap():
            speak("hangi ürünü merak ediyorsunuz:")
            urun = record()
            driver = webdriver.Chrome()
            url = "https://www.gittigidiyor.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath(
                '//*[@id="main-header"]/div[3]/div/div/div/div[2]/form/div/div[1]/div[2]/input')
            arama.click()
            arama.send_keys(urun)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)
            speak("bulduğum sonuçlar")

        def vatanbilgisayar_alisveris_yap():
            speak("hangi ürünü merak ediyorsunuz:")
            urun = record()
            driver = webdriver.Chrome()
            url = "https://www.vatanbilgisayar.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('//*[@id="navbar-search-input"]')
            arama.click()
            arama.send_keys(urun)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)
            speak("bulduğum sonuçlar")

        def teknosa_alisveris_yap():
            speak("hangi ürünü merak ediyorsunuz:")
            urun = record()
            driver = webdriver.Chrome()
            url = "https://www.teknosa.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('//*[@id="js-site-search-input search-input"]')
            arama.click()
            arama.send_keys(urun)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)
            speak("bulduğum sonuçlar")

        def mediamarkt_alisveris_yap():
            speak("hangi ürünü merak ediyorsunuz:")
            urun = record()
            driver = webdriver.Chrome()
            url = "https://www.mediamarkt.com.tr/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('//*[@id="search-autocomplete"]/form/input[1]')
            arama.click()
            arama.send_keys(urun)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)
            speak("bulduğum sonuçlar")

        def aliexpress_alisveris_yap():
            speak("hangi ürünü merak ediyorsunuz:")
            urun = record()
            driver = webdriver.Chrome()
            url = "https://tr.aliexpress.com/"
            driver.get(url)
            driver.maximize_window()
            main_window = driver.current_window_handle
            driver.switch_to.window(main_window)

            arama = driver.find_element_by_xpath('//*[@id="search-key"]')
            arama.click()
            arama.send_keys(urun)
            time.sleep(1)
            arama.send_keys(Keys.ENTER)
            time.sleep(1)
            speak("bulduğum sonuçlar")

        def alarm_hatirlatici():  # CPU yu çok kötü bir şekilde şişireceği için bu kodu atlıyorum.
            pass

        def el_hareketleri_ile_ses_kontrol():  # hareket algılamada kararsızlık olduğu için bu kodu yazmak tehlikeli
            pass

        def ses_arttirma_kontrol():
            pyautogui.press('volumeup')
            pyautogui.press('volumeup')
            pyautogui.press('volumeup')
            pyautogui.press('volumeup')
            pyautogui.press('volumeup')

        def ses_azaltma_kontrol():
            pyautogui.press('volumedown')
            pyautogui.press('volumedown')
            pyautogui.press('volumedown')
            pyautogui.press('volumedown')
            pyautogui.press('volumedown')

        def ses_kapat_ac():
            pyautogui.press('volumemute')
            pyautogui.press('volumemute')
            pyautogui.press('volumemute')
            pyautogui.press('volumemute')
            pyautogui.press('volumemute')

        def ekran_fotosu_ss():
            pyautogui.hotkey('win', 'prtsc')

        def uygulama_acma():  # uygulama yolu üzerinden açılıyor fakat her pc de farklı olduğu için yazmaya gerek duymadım
            pass

        def uygulama_kapatma():
            pyautogui.hotkey('alt', 'f4')

        def bilgisayari_kapatma():  # 720p-1080p için geçerli
            pyautogui.moveTo(10, 1069)  # başlat
            pyautogui.click()

            pyautogui.moveTo(10, 1010)  # genel kapatma butonu
            pyautogui.click()

        def bilgisayari_uyku_moduna_alma():  # 720p-1080p için geçerli
            pyautogui.moveTo(10, 1069)  # başlat
            pyautogui.click()

            pyautogui.moveTo(30, 860)  # uyku modu
            pyautogui.click()

        def bilgisayari_yeniden_baslatma():  # 720p-1080p için geçerli
            pyautogui.moveTo(10, 1069)  # başlat
            pyautogui.click()

            pyautogui.moveTo(30, 940)  # yeniden başlat
            pyautogui.click()

        ###############################################  KONUŞTURMA-2  ####################################################

        def speak(string):
            tts = gTTS(string, lang="tr")
            rand = random.randint(1, 10000)
            file = "audio-" + str(rand) + ".mp3"
            tts.save(file)
            playsound(file)
            os.remove(file)

        def yanlis():
            speak("Lütfen başka bir emir verin")
            record()

        def kendini_tanitma():
            speak("Merhaba! benim adım ZEYREK 1 nokta 0")
            speak("Genel komutlarım şu şekilde: ")
            speak("nasılsın, "
                  "gün, "
                  "ay, "
                  "yıl, "
                  "saat, "
                  "fıkra, "
                  "arama yap, "
                  "not al, "
                  "ajanda, "
                  "araştırma yap, "
                  "son dakika, "
                  "izle (youtube için), "
                  "hava durumu, "
                  "mesaj, "
                  "çeviri "
                  "kimdir (biyografi)"
                  "açık mı (mağaza)"
                  "fotoğraf (googleden)"
                  "namaza ne kadar kaldı"
                  "yol tarifi"
                  "mekan bul"
                  "spor (haber)"
                  "hesaplama (mat)"
                  "film aç"
                  "dizi aç"
                  "döviz kuru"
                  "döviz hesapla"
                  "en ucuz"
                  "N11"
                  "trendyol"
                  "hepsiburada"
                  "gittigidiyor"
                  "vatan bilgisayar"
                  "teknosa"
                  "mediamarkt"
                  "aliexpress"
                  "alarm (şuanlık devredışı)"
                  "kamera(aç)"
                  "fotoğraf(çek)"
                  "video(çek)"
                  "renk(algıla)"
                  "metin (resimden okuma)"
                  "el hareketleri"
                  "gülümseme algıla"
                  "insan algıla"
                  "yüz algıla"
                  "göz algıla"
                  "çizim yap"
                  "ne görüyorsun"
                  "makyaj (yap)"
                  "(sesi) arttır"
                  "(sesi) azalt"
                  "(sesi) kes"
                  "uygulamayı (kapat)"
                  "bilgisayarı (kapat)"
                  "yeniden (başlat-pc)"
                  "uyku (modu-pc)"
                  "ekran (fotoğrafı-SS)"
                  "diyebilirsin.")
            speak("beni kapatmak için kapat!, uyku moduna almak için tamamdır! ve uyandırmak için Sadık! diyebilirsin")

        def bos():  # pyqt5 ile uygulama kapatmadan devre dışı bırakma için
            buton = "pyqt5 te ekranda aktif ve pasif için buton olur"
            if buton == "aktif":
                response(voice)
            # elif buton == "pasif":
            else:
                bos()

        ############################################### ARAYÜZ TASARIMI #################################################

        def arayuz():
            pass

        ############################################## ÇEVRİMDIŞI MODÜLÜ ################################################

        def offline():  # bu kısmı yazınca bunu class a dönüştür, üsttekileri de online class isminde açıp içine yaz, net bağlantı durumuna göre iki class dönüşümlü olarak çalışsın.
            pass

        ################################################## VERİTABANI ###################################################

        def veritabani():  # her yeni eklenen kişiye otomatik oluşturulan bir veritabanı lazım ve hafıza dolunca en eski veritabanından silmeye başlamak lazım
            pass

            def kisi():  # tanışılan kişileri burda (daha sonra class yap bunu)
                pass

        ################################################ GÖRÜNTÜ İŞLEME #################################################

        def kamera_ac():
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            while True:
                ret, frame = cap.read()

                if ret == 0:
                    break
                    # bu komut eğer video vs. koyarsak video bittiğinde ekranı kapatıyor.

                frame = cv2.flip(frame, 1)

                cv2.imshow("Webcam", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                    # bu komut da q ya basınca ekranı kapatıyor. Aynı zamanda waitkey yanında 1 yazdık, bu sayı arttıkça video hızı artıyor.
            cap.release()
            cv2.destroyAllWindows()

        def fotograf_cek():
            camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Video çekmeye başla
            return_value, image = camera.read()  # İlk fotğrafı al
            cv2.imwrite('test.jpg', image)  # Kaydet
            speak("çektim")
            camera.release()  # ?
            cv2.destroyAllWindows()  # Tüm ekranları kapat

        def video_cek():
            # Dosyadan video okumak için
            # cap = cv.VideoCapture('TomandJerry.mp4')

            # IP Kamera bağlantısı için
            # cap = cv.VideoCapture('http://192.168.1.105:8080/video')

            # Kamera bağlantısı için (Cihazınıza bağlı diğer kameralar için 0-1-2-3 deneyebilirsiniz.)
            cap = cv.VideoCapture(0)
            # ==========================================================================================

            # codec tanımlama ve VideoWriter nesnesi oluşturma bilgi için bkz: https://www.fourcc.org/codecs.php
            fourcc = cv.VideoWriter_fourcc(*'XVID')

            # Yukarıdaki işlemi aşağıdaki gibi de yapabiliriz.
            # fourcc = cv.VideoWriter_fourcc('X','V','I','D')

            # Kaydedilecek video dosyasının adı, uzantısı, konumu, saniyedeki çerçeve sayısı ve çözünürlüğü
            out = cv.VideoWriter('output.avi', fourcc, 60.0, (640, 480))

            # Görüntü alma başarılı olduğu süre boyunca kaydetmeye devam et.
            while (cap.isOpened()):
                # Videodan görüntü oku ve geri döndür.
                ret, frame = cap.read()

                # Görüntü okuma başarılı ise
                if ret == True:
                    # cv.flip(src, flipCode, dst) 2 boyutlu diziyi dikey yatay veya her iki eksen etrafında döndürür.
                    # 0 => dikey döndürme
                    # 1 => yatay döndürme
                    # 2 => hem yatay hem dikey döndürme
                    frame = cv.flip(frame, 1, dst=None)

                    # Döndürülen görüntüyü video dosyasına yaz.
                    out.write(frame)

                    # Görüntüyü ekranda göster.
                    cv.imshow('frame', frame)

                    # q tuşuna basıldığında çık.
                    if cv.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break

            # İşin bittikten sonra her şeyi serbest bırak.
            cap.release()
            out.release()
            cv.destroyAllWindows()

        # video alırken ses kaydetmiyor.

        def renk_algilama():
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            def nothing(x):
                pass

            cv2.namedWindow("Trackbar")
            cv2.resizeWindow("Trackbar", 500, 500)

            cv2.createTrackbar("Lower - H", "Trackbar", 0, 180, nothing)
            cv2.createTrackbar("Lower - S", "Trackbar", 0, 255, nothing)
            cv2.createTrackbar("Lower - V", "Trackbar", 0, 255, nothing)

            cv2.createTrackbar("Upper - H", "Trackbar", 0, 180, nothing)
            cv2.createTrackbar("Upper - S", "Trackbar", 0, 255, nothing)
            cv2.createTrackbar("Upper - V", "Trackbar", 0, 255, nothing)

            cv2.setTrackbarPos("Upper - H", "Trackbar", 180)
            cv2.setTrackbarPos("Upper - S", "Trackbar", 255)
            cv2.setTrackbarPos("Upper - V", "Trackbar", 255)

            while True:
                ret, frame = cap.read()
                frame = cv2.flip(frame, 1)

                frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                lower_h = cv2.getTrackbarPos("Lower - H", "Trackbar")
                lower_s = cv2.getTrackbarPos("Lower - S", "Trackbar")
                lower_v = cv2.getTrackbarPos("Lower - V", "Trackbar")

                upper_h = cv2.getTrackbarPos("Upper - H", "Trackbar")
                upper_s = cv2.getTrackbarPos("Upper - S", "Trackbar")
                upper_v = cv2.getTrackbarPos("Upper - V", "Trackbar")

                lower_color = np.array([lower_h, lower_s, lower_v])
                upper_color = np.array([upper_h, upper_s, upper_v])

                mask = cv2.inRange(frame_hsv, lower_color, upper_color)

                cv2.imshow("Original", frame)
                cv2.imshow("Mask", mask)

                if cv2.waitKey(20) & 0xFF == ord("q"):
                    break

            cap.release()
            cv2.destroyAllWindows()

        def fotograftaki_yaziyi_oku():
            isim = record()
            try:
                im = Image.open(f"{isim}.jpg")
                text = pytesseract.image_to_string(im, lang="eng")
                print(text)
                speak(text)
            except FileNotFoundError:
                speak("bulamadım, lütfen tekrar söyleyin")
                fotograftaki_yaziyi_oku()
            except:
                pass

        def el_hareketleri_algilama():
            speak("çıkmak için ESC ye basın")
            vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            while (1):

                try:

                    ret, frame = vid.read()
                    frame = cv2.flip(frame, 1)
                    kernel = np.ones((3, 3), np.uint8)

                    roi = frame[100:300, 100:300]

                    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
                    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

                    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
                    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

                    mask = cv2.inRange(hsv, lower_skin, upper_skin)

                    mask = cv2.dilate(mask, kernel, iterations=4)

                    mask = cv2.GaussianBlur(mask, (5, 5), 100)

                    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                    cnt = max(contours, key=lambda x: cv2.contourArea(x))

                    epsilon = 0.0005 * cv2.arcLength(cnt, True)
                    approx = cv2.approxPolyDP(cnt, epsilon, True)

                    hull = cv2.convexHull(cnt)

                    areaHull = cv2.contourArea(hull)
                    areaCnt = cv2.contourArea(cnt)

                    areaRatio = ((areaHull - areaCnt) / areaCnt) * 100

                    hull = cv2.convexHull(approx, returnPoints=False)
                    defects = cv2.convexityDefects(approx, hull)

                    l = 0

                    for i in range(defects.shape[0]):
                        s, e, f, d = defects[i, 0]
                        start = tuple(approx[s][0])
                        end = tuple(approx[e][0])
                        far = tuple(approx[f][0])

                        a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                        b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                        c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                        s = (a + b + c) / 2
                        ar = math.sqrt(s * (s - a) * (s - b) * (s - c))

                        d = (2 * ar) / a

                        angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

                        if angle <= 90 and d > 30:
                            l += 1
                            cv2.circle(roi, far, 3, [255, 0, 0], -1)

                        cv2.line(roi, start, end, [0, 255, 0], 2)

                    l += 1

                    font = cv2.FONT_HERSHEY_SIMPLEX
                    if l == 1:
                        if areaCnt < 2000:
                            cv2.putText(frame, 'Put your hand in the box', (0, 50), font, 1, (0, 0, 255), 3,
                                        cv2.LINE_AA)
                        else:
                            if areaRatio < 12:
                                cv2.putText(frame, '0', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                                # speak("sıfır")
                            elif areaRatio < 17.5:
                                cv2.putText(frame, 'Best luck', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                                # speak("pekiyi")

                            else:
                                cv2.putText(frame, '1', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                                # speak("bir")

                    elif l == 2:
                        cv2.putText(frame, '2', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                        # speak("iki")

                    elif l == 3:

                        if areaRatio < 27:
                            cv2.putText(frame, '3', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                            # speak("üç")
                        else:
                            cv2.putText(frame, '3', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                            # speak("üç")

                    elif l == 4:
                        cv2.putText(frame, '4', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                        # speak("dört")

                    elif l == 5:
                        cv2.putText(frame, '5', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                        # speak("beş")

                    elif l == 6:
                        cv2.putText(frame, 'reposition', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

                    else:
                        cv2.putText(frame, 'reposition', (10, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

                    cv2.imshow('mask', mask)
                    cv2.imshow('frame', frame)
                except:
                    pass

                k = cv2.waitKey(5) & 0xFF
                if k == 27:
                    break

            cv2.destroyAllWindows()
            vid.release()

        def gulumseme_algilama():
            vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            smile_cascade = cv2.CascadeClassifier('smile.xml')
            face_cascade = cv2.CascadeClassifier('frontalface.xml')

            while 1:
                ret, frame = vid.read()
                frame = cv2.flip(frame, 1)

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.5, 9)

                for (x, y, w, h) in faces:

                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    roi_gray = gray[x:x + w, y:y + h]
                    roi_img = frame[x:x + w, y:y + h]

                    smiles = smile_cascade.detectMultiScale(roi_gray, 1.5, 9)
                    for (ex, ey, ew, eh) in smiles:
                        cv2.rectangle(roi_img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                cv2.imshow('videos', frame)

                if cv2.waitKey(5) & 0xFF == ord('q'):
                    break

            vid.release()
            cv2.destroyAllWindows()

        def insan_bedeni_algilama():
            vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            body_cascade = cv2.CascadeClassifier("fullbody.xml")

            while 1:
                ret, frame = vid.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                bodies = body_cascade.detectMultiScale(gray)

                for (x, y, w, h) in bodies:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                cv2.imshow('video', frame)

                if cv2.waitKey(5) & 0xFF == ord('q'):
                    break

            vid.release()
            cv2.destroyAllWindows()

        def yuz_algilama():
            vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            face_cascade = cv2.CascadeClassifier("frontalface.xml")
            while 1:
                ret, frame = vid.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.4, 1)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                cv2.imshow('video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            vid.release()
            cv2.destroyAllWindows()

        def goz_algilama():
            vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            face_cascade = cv2.CascadeClassifier("frontalface.xml")
            eye_cascade = cv2.CascadeClassifier("eye.xml")

            while 1:
                ret, frame = vid.read()
                frame = cv2.flip(frame, 1)
                frame = cv2.resize(frame, (480, 360))

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    roi_gray = gray[y:y + h, x:x + w]
                    roi_frame = frame[y:y + h, x:x + w]

                    eyes = eye_cascade.detectMultiScale(roi_gray)

                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

                cv2.imshow('video', frame)

                if cv2.waitKey(5) & 0xFF == ord('q'):
                    break

            vid.release()
            cv2.destroyAllWindows()

        def ekrana_cizim_yapma():
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            lower_blue = np.array([100, 60, 60])
            upper_blue = np.array([140, 255, 255])

            blue_points = [deque(maxlen=512)]
            green_points = [deque(maxlen=512)]
            red_points = [deque(maxlen=512)]
            yellow_points = [deque(maxlen=512)]

            blue_index = 0
            green_index = 0
            red_index = 0
            yellow_index = 0

            colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
            color_index = 0

            paintWindow = np.zeros((471, 636, 3)) + 255

            paintWindow = cv2.rectangle(paintWindow, (40, 1), (140, 65), (0, 0, 0), 2)
            paintWindow = cv2.rectangle(paintWindow, (160, 1), (255, 65), colors[0], -1)
            paintWindow = cv2.rectangle(paintWindow, (275, 1), (370, 65), colors[1], -1)
            paintWindow = cv2.rectangle(paintWindow, (390, 1), (485, 65), colors[2], -1)
            paintWindow = cv2.rectangle(paintWindow, (505, 1), (600, 65), colors[3], -1)

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(paintWindow, "CLEAR ALL", (49, 33), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(paintWindow, "BLUE", (185, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(paintWindow, "GREEN", (298, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(paintWindow, "RED", (420, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(paintWindow, "YELLOW", (520, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.namedWindow("Paint")

            while 1:
                ret, frame = cap.read()
                frame = cv2.flip(frame, 1)
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                frame = cv2.rectangle(frame, (40, 1), (140, 65), (0, 0, 0), 2)
                frame = cv2.rectangle(frame, (160, 1), (255, 65), colors[0], -1)
                frame = cv2.rectangle(frame, (275, 1), (370, 65), colors[1], -1)
                frame = cv2.rectangle(frame, (390, 1), (485, 65), colors[2], -1)
                frame = cv2.rectangle(frame, (505, 1), (600, 65), colors[3], -1)

                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, "CLEAR ALL", (49, 33), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
                cv2.putText(frame, "BLUE", (185, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "GREEN", (298, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "RED", (420, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "YELLOW", (520, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                if ret is False:
                    break

                mask = cv2.inRange(hsv, lower_blue, upper_blue)

                mask = cv2.erode(mask, (5, 5), iterations=2)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, (5, 5))
                mask = cv2.dilate(mask, (5, 5), iterations=1)

                _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                center = None

                if len(contours) > 0:
                    max_contours = sorted(contours, key=cv2.contourArea, reverse=True)[0]
                    ((x, y), radius) = cv2.minEnclosingCircle(max_contours)
                    cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 0), 3)

                    M = cv2.moments(max_contours)
                    # center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                    if M["m00"] != 0:
                        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                        if center[1] <= 65:
                            if 40 <= center[0] <= 140:

                                blue_points = [deque(maxlen=512)]
                                green_points = [deque(maxlen=512)]
                                red_points = [deque(maxlen=512)]
                                yellow_points = [deque(maxlen=512)]

                                blue_index = 0
                                green_index = 0
                                red_index = 0
                                yellow_index = 0

                                paintWindow[67:, :, :] = 255

                            elif 160 <= center[0] <= 255:
                                color_index = 0

                            elif 275 <= center[0] <= 370:
                                color_index = 1

                            elif 390 <= center[0] <= 485:
                                color_index = 2

                            elif 505 <= center[0] <= 600:
                                color_index = 3

                        else:

                            if color_index == 0:
                                blue_points[blue_index].appendleft(center)

                            elif color_index == 1:
                                green_points[green_index].appendleft(center)

                            elif color_index == 2:
                                red_points[red_index].appendleft(center)

                            elif color_index == 3:
                                yellow_points[yellow_index].appendleft(center)
                    else:
                        center = 0

                else:
                    blue_points.append(deque(maxlen=512))
                    blue_index += 1

                    green_points.append(deque(maxlen=512))
                    green_index += 1

                    red_points.append(deque(maxlen=512))
                    red_index += 1

                    yellow_points.append(deque(maxlen=512))
                    yellow_index += 1

                points = [blue_points, green_points, red_points, yellow_points]

                for i in range(len(points)):
                    for j in range(len(points[i])):
                        for k in range(1, len(points[i][j])):
                            if points[i][j][k - 1] is None or points[i][j][k] is None:
                                continue

                            cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                            cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

                cv2.imshow("Frame", frame)
                cv2.imshow("Paint", paintWindow)

                if cv2.waitKey(3) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

        def nesne_algilama_yolo():
            camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Video çekmeye başla
            return_value, image = camera.read()  # İlk fotğrafı al
            cv2.imwrite('algilama.jpg', image)  # Kaydet
            camera.release()  # ?
            cv2.destroyAllWindows()  # Tüm ekranları kapat

            img = cv2.imread("algilama.jpg")
            # print(img)

            img_width = img.shape[1]
            img_height = img.shape[0]

            # %% 2. Bölüm

            img_blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), swapRB=True, crop=False)

            labels = ["insan", "bisiklet", "araba", "motorsiklet", "uçak", "otobüs", "tren", "kamyon", "tekne",
                      "trafik lambası", "yangın musluğu", "dur işareti", "park metre", "bank", "kuş", "kedi",
                      "köpek", "at", "koyun", "inek", "fil", "ayı", "zebra", "zürafa", "sırt çantası",
                      "şemsiye", "el çantası", "kravat", "bavul", "frizbi", "kayak", "snowboard", "top",
                      "uçurtma", "beysbol sopası", "beyzbol eldiveni", "kaykay", "sörf tahtası", "Tenis raketi",
                      "şişe", "wineglass", "Fincan", "çatal", "bıçak", "kaşık", "kap", "muz", "elma",
                      "sandviç", "portakal", "brokoli", "havuç", "sosisli", "pizza", "donut", "kek", "sandalye",
                      "kanepe", "saksı bitkisi", "yatak", "yemek masası", "tuvalet", "televizyon", "laptop", "mouse",
                      "kumanda", "klavye", "telefon", "mikrodalga", "fırın", "tost makinası", "lavabo", "buzdolabı",
                      "kitap", "saat", "vazo", "makas", "oyuncak ayı", "saç kurutma makinesi", "diş fırçası"]

            colors = ["0,255,255", "0,0,255", "255,0,0", "255,255,0", "0,255,0"]
            colors = [np.array(color.split(",")).astype("int") for color in colors]
            colors = np.array(colors)
            colors = np.tile(colors, (18, 1))

            # %% 3. Bölüm

            model = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")

            layers = model.getLayerNames()
            output_layer = [layers[layer[0] - 1] for layer in model.getUnconnectedOutLayers()]

            model.setInput(img_blob)

            detection_layers = model.forward(output_layer)

            ############## NON-MAXIMUM SUPPRESSION - OPERATION 1 ###################

            ids_list = []
            boxes_list = []
            confidences_list = []

            ############################ END OF OPERATION 1 ########################

            # %% 4. Bölüm

            for detection_layer in detection_layers:
                for object_detection in detection_layer:

                    scores = object_detection[5:]
                    predicted_id = np.argmax(scores)
                    confidence = scores[predicted_id]

                    if confidence > 0.20:
                        label = labels[predicted_id]
                        bounding_box = object_detection[0:4] * np.array([img_width, img_height, img_width, img_height])
                        (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype("int")

                        start_x = int(box_center_x - (box_width / 2))
                        start_y = int(box_center_y - (box_height / 2))

                        ############## NON-MAXIMUM SUPPRESSION - OPERATION 2 ###################

                        ids_list.append(predicted_id)
                        confidences_list.append(float(confidence))
                        boxes_list.append([start_x, start_y, int(box_width), int(box_height)])

                        ############################ END OF OPERATION 2 ########################

            ############## NON-MAXIMUM SUPPRESSION - OPERATION 3 ###################

            max_ids = cv2.dnn.NMSBoxes(boxes_list, confidences_list, 0.5, 0.4)

            for max_id in max_ids:
                max_class_id = max_id[0]
                box = boxes_list[max_class_id]

                start_x = box[0]
                start_y = box[1]
                box_width = box[2]
                box_height = box[3]

                predicted_id = ids_list[max_class_id]
                label = labels[predicted_id]
                confidence = confidences_list[max_class_id]

                ############################ END OF OPERATION 3 ########################

                end_x = start_x + box_width
                end_y = start_y + box_height

                box_color = colors[predicted_id]
                box_color = [int(each) for each in box_color]

                # label = "{}: {:.2f}%".format(label, confidence * 100)
                # print("predicted object {}".format(label))

                labell = "Karşımda " + "{:.0f}%".format(confidence * 100) + " oranında " + f"{label} görüyorum."
                labelll = f"Karşımda {label} görüyorum"
                print(labell)
                speak(labelll)

                cv2.rectangle(img, (start_x, start_y), (end_x, end_y), box_color, 1)
                cv2.putText(img, label, (start_x, start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 1)

            cv2.imshow("Detection Window", img)
            speak("çıkmak için q tuşuna basın")
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        def saka_makyaji():
            def makyaj_fotosu():
                camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                return_value, image = camera.read()
                cv2.imwrite('fotomakeup.jpg', image)
                camera.release()
                cv2.destroyAllWindows()
                makyaj()

            def makyaj():
                image = face_recognition.load_image_file("fotomakeup.jpg")

                # Find all facial features in all the faces in the image
                face_landmarks_list = face_recognition.face_landmarks(image)

                pil_image = Image.fromarray(image)
                for face_landmarks in face_landmarks_list:
                    d = ImageDraw.Draw(pil_image, 'RGBA')

                    # Make the eyebrows into a nightmare
                    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
                    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
                    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
                    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

                    # Gloss the lips
                    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
                    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
                    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
                    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

                    # Sparkle the eyes
                    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
                    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

                    # Apply some eyeliner
                    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
                    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

                    pil_image.show()
                    speak("HaHaHa nasıl, beğendin mi?")

            makyaj_fotosu()

        def duygu_tespiti():  # göz ve ağız hareketlerinden
            pass

        ################################################## YAPAY ZEKA ###################################################

        def sohbet():
            pass

        def santranc():  # yapay zeka |ZEYREK ile santrac oyna (aslında pc ye karşı)
            pass

        ##################################################### MAİN ######################################################

        # kendini_tanitma()
        #yuz_tanima()
        # time.sleep(1.5)
        print("Nasıl Yardımcı Olabilirim!")
        speak("Nasıl Yardımcı Olabilirim!")
        # time.sleep(1)

        while 1:
            voice = record()
            print(voice)
            response(voice)

        #################################################################################################################
        #################################################################################################################

        # ---------------------|
        # YAPILACAKLAR LİSTESİ |
        # ---------------------|

        # google mapsten bir ülke açma ve o ülke hakkında bilgi edinme
        # cv2 ile basit kamera aç, renk algıla tarzı basit komutlar ekle

        # TAVSİYE: (komut)
        # bilgisayarı kontrol et ses kısma ekran parlaklığı ya da spotify müzik çalma ve oynatma listesi gibi, program çalıştırma gibi
        # yarın hava nasıl veya bir haftalık durum vs isteme ekle

        # TAVSİYE: (sistem)
        # sesli asistan 1 deki gibi söylenenleri kelime kelime ayır ve sadık kelimesini duyduğun an aktifleş
        # sesli asistan 4 teki gibi her bir komutu çağırmak için birsürü sesli komutu liste içine al ve mesela nasilisin = ["nasılsın","naber"] dediysek if nasilsin in voice: falan de
        # çevrimdışı kullanımlar için pyttsx3 modülü üzerinden de eklenti getir.
        # face id için yeni kayıt veritabanını oluştur.

        # TAVSİYE (TASARIM)
        # siri arkaplanı ile google asistan karışımı güzel olabilir. siri gibi konuşurken ses dalgası efekti ile google asistan gibi sohbet tarzı bir arayüz (raspberry ye bağlanacak ekran için de aynı zamanda)

        # TAVSİYE (body)
        # raspberry pi + mini fan + dokunmatik ekran + kamera modülü + mikrofon/hoparlör kiti + 3D yazıcıdan çıkmış yüz + servo motorlar

        #################################################################################################################
        #################################################################################################################

        # NOT:

        # bütün kütüphaneleri pip install ile yükle
        # || pip install lxml 'yi yükle
        # || pip install PyAudio için bu siteye göre yükle: https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14
        # || pip install face-recognition' u kurabilmek için; ilk önce pip install cmake 'yi yükle sonra da pip install dlib' i yükle, ondan sonra pip install face-recognition yazıp kurabilirsin. EĞER DLİB YÜKLENMİYORSA BU SİTEYE GİT VE DENİLENİ YAP: https://stackoverflow.com/questions/62881032/dlib-latest-version-installation-error-for-python-3-7-3-8-on-windows-10-with
        # kamera açılınca warning hatası alıyorsan kamera için cv2.VideoCapture(0) yerine; cv2.VideoCapture (0, cv2.CAP_DSHOW) yaz.
        # selenium için chrome driver yükle ve py dosyasının yanına koy
        # resimden metin okuma için pyteserract yükle
        # gülümseme, göz ve yüz algılama için; smile.xml ve frontalface.xml | insan bedeni için; fullbody.xml | göz algılama için; eye.xml | dosyalarını py dosyasının yanına koy
        # nesne algılama için; yolov3.cfg ve yolov3.weights dosyalarını py dosyasının yanına koy.

        #################################################################################################################
        #################################################################################################################

    class hava_durumu():
        import requests
        import json

        api_url = 'http://api.openweathermap.org/data/2.5/weather?q=Istanbul,tr&APPID=378c60283dcc17cfe37eb295b61c5c37'

        result = requests.get(api_url)
        result1 = json.loads(result.text)

        sicaklik = int((result1["main"]["temp"]) - 273)
        durum = result1["weather"][0]["description"]

        sd = (f"istanbul {sicaklik} °C  {durum}")

    #############################################################3
    r = requests.get("https://www.haberler.com/son-dakika/")
    source = BeautifulSoup(r.content,"lxml")

    ############################################################################################

    def clock():
        hour = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        day = time.strftime("%A")
        am_pm = time.strftime("%p")
        time_zone = time.strftime("%Z")

        my_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
        my_label.after(1000, clock)

        my_label2.config(text=time_zone + " " + day)

    def update():
        my_label.config(text="New Text")

    my_label = Label(root, text="", font=("Helvetica", 48), fg="white", bg="#60b26c")
    my_label.grid(row=0, column=28, columnspan=3,ipady=4)

    my_label2 = Label(root,text="", font=("Helvetica", 15), fg="white", bg="#60b26c")
    my_label2.grid(row=3, column=28, columnspan=3,ipady=4)


    clock()

    ############################################################################################

    #my_frame = Frame(root, width=5000, height=5000, bg="#60b26c")
    #my_frame.pack(pady=20, ipady=20, ipadx=20)



    ###########################################################################################3

    # First one
    frame1 = LabelFrame(root, text="Son Dakika", fg="white", bg="#60b26c")
    frame1.grid(row=7, column=5, columnspan=7, ipady=4)

    my_message = Message(frame1,
                             text=source.find("p").text,
                             font=("segoe Print", 11),
                             aspect=150,
                             justify=RIGHT, fg="white", bg="#60b26c")
    my_message.grid(row=7, column=5, columnspan=7, ipady=4, pady=25)

    # Second One
    frame2 = LabelFrame(root, text="Hava Durumu", fg="white", bg="#60b26c")
    frame2.grid(row=27, column=5, columnspan=7,ipady=4,pady=100)

    my_message2 = Message(frame2, text=hava_durumu.sd,
        font=("segoe Print", 12),
        aspect=100,
        justify=LEFT, fg="white", bg="#60b26c")
    my_message2.grid(row=27, column=5, columnspan=7,ipady=4)


    #def boss():
    #    print("beklemedeyim")
    # Button
    my_button = Button(root, text="Çalıştır", bg="white", command=asistan)
    my_button.grid(row=100, column=100, columnspan=10,ipady=10, ipadx= 20)

    #my_button2 = Button(root, text="Kapat", bg="gray", command=boss)
    #my_button2.grid(row=100, column=120, columnspan=10,ipady=10, ipadx= 20)

    ############################################################################################
    my_img = ImageTk.PhotoImage(Image.open("rsz_fatih.jpg"))
    my_label11 = Label(image=my_img)
    my_label11.grid(row=0, column=1000, columnspan=10,ipady=10, ipadx= 20)
    my_label11.config(width=120, height=150)

    my_canvas11 = Canvas(root, width=120, height=150)
    my_canvas11.create_image(0, 0, image=my_img, anchor="nw")

    my_label22 = Label(root, text="GİRİŞ YAPAN: FATİH NAİM TÜRKEL",fg="white",bg="#60b26c", font=("Helvetica", 12))
    my_label22.grid(row=2, column=1000, columnspan=10,ipady=10, ipadx= 20)
    #############################################################################################

    root.configure(background= "#60b26c")
    root.mainloop()
arayuz()