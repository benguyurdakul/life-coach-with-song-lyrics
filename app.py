#Kullanilacak trmodel 'i indirmek icin : https://drive.google.com/drive/folders/1IBMTAGtZ4DakSCyAoA4j7Ch0Ft1aFoww?usp=drive_open

#https://github.com/akoksal/Turkish-Word2Vec

import re
import streamlit as st
import pandas as pd
import numpy as np
import base64
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

Aşk = """
İşte kuzu kuzu geldim 
Dilediğince kapandım dizlerine 
Bu kez gururumu ateşe verdim 
Yaktım da geldim 
- Tarkan!

Aşk bu kızıl ötesi, yaralı müzesi, hareket edemem - Serdar Ortaç!

Kalanlar gideni gönlünde taşır, aşk sevene yük olmaz - Tarkan!

Ben o şelale saçlara o ay o hilal kaşlara
Süzme bal o dudaklara
Öp öp öp öp doyamadım 
- Tarkan!

Bas gaza aşkım bas gaza 
Kim tutar seni? Bas gaza 
Yollar senin hiç durma 
Hadi uçur beni burdan
 - İsmail YK!

iki deli bir araya gelmemeliydik 
Belki de bu kadar sevmemeliydik 
İyi kötü atıyordu, vücuda yetiyordu 
Kalp işi biliyordu dinlemeliydik 
- Serdar Ortaç!

Hadi diyelim biri çok deli sevdi 
Senin için her şeyi her şeyi verdi 
Ya bi' gün olur sana bel kıvırırsa 
Binlerce dansöz var 
- Serdar Ortaç!

Bandıra bandıra ye beni Hiç doyamazsın tadıma - Yonca Evimcik!

Güne açan çiçekler gibiyiz Yalan, yalan 
Öyle saf ki sevgimiz Yalan 
Ayıramaz bizi hiç kimse Yalan, yalan 
Ölene dek beraberiz 
- Hepsi!

Gözü görmez başkasını Senle ben elmanın iki yarısı Bir ömür boyu beraber - Hepsi!

Çiçek gibi tazecik, kıymetli bi tanecik Ana sütü gibi tertemiz 
Dudu dudu dilleri, lıkır lıkır içmeli Gözleri derya deniz 
- Tarkan!

Ne bileyim işte kıskanıyorum 
Seni kendimden bile kıskanıyorum 
Kıskanıyorum, kıskanıyorum 
Kıskanmak aşkın kanununda var 
- Hakkı Bulut!

Bana kazak örmeli, 
Yalnız beni sevmeli artık, 
Bu kız beni görmeli 
- Musatafa Sandal!

Neremi neremi, Gözlerini
Neremi neremi, Gülyüzünü
Neremi neremi, Dudaklarını
Neremi neremi, Her yerini 
- Banu Alkan!

Karşıdan çapkın bakma öyle 
Hadi beni dansa kaldır
Kaldıramazsan kaldırırlar güzelim 
- Banu Alkan!

Aşka davet bu benden, Al bir demet gül benden - Kader!

Kız seni alan yaşadı Dertlerini de boşadı Mest oldum - Mustafa Sandal!

nerdesin aşkım - buradayım aşkım -nerdesin askim - buradayım aşkım - Hadise!

Aşk incelik ister canım hoyrat olma, 
beni böyle sev değiştirme boşver anlama 
- Tarkan!

Bize neler neler öğrettiler
Sevdalar üstüne
Aldatıldık aldatıldık
Sevda böyle değil
-Sezen Aksu!
"""

Kızgınlık = """
Seni çöpe atacağım poşete yazık Bi sigara yakacağım ateşe yazık - Serdar Ortaç!

Takmış koluna elin adamını beni orta yerimden çatlatıyor 
Ağzında sakızı şişirip şişirip Arsız arsız patlatıyor 
- Tarkan!

Seni gidi fındıkkıran Yılanı deliğinden çıkaran Kaderim püsküllü belam - Tarkan!

Kimi yazacak tarih? Bizi mi? Bu ne uyumsuz bir çift seçimi - Hande Yener!

Hiç utanmıyosun di mi? Kavganın da adabı var - Sıla!

Kalbimi kapatmışım sen gibilere, sen de kendin gibi bir şerefsize aç - Demet Akalın!

Yürek yemiş sanki mübarek, neyine güvendin evladım? - Gülşen!

Ondan gelecek yarar da zarardan beter, vicdanıyla kalsın Sayın Çokbilmiş. - Hadise!

Söyle gerçek sevgi bu mu, 
Yaptığına şantaj denir, 
Böyle aşka montaj denir, 
Şantaj, montaj, şantaj, montaj 
- Ceylan!

Takmış takıştırmış, Sürmüş sürüştürmüş, Bir dağınıklık, bir rüküşlük, Kıl oldum abi - Tarkan!

Anneme şimdi ne derim yar? Ben seni sevmiştim kör olasın,a Anneme şimdi ne derim yar? - Kader!

Ben ne sana taparım ne seni ararım ne trip atarım - Tarkan!

Sevgilim sevgilim nasılsın? 
Burnun kapıya kısılsın, 
Çok güzel araban var ama 
Yolda tekeri patlasın 
Oooh ohh olsun. 
- Barbaros Hayrettin!

Sevgilim sevgilim nasılsın? 
Soguk iç sesin kısılsın, 
Köpüklü banyo yaparken 
Birden sular kesilsin 
-Barbaros Hayrettin!

Allah belanı versin 
Allah seni kahretsin 
Bana gelen sana gelsin 
Hayatımı sen mahvettin 
Acımadın neler çektim 
Kader seni de kör etsin 
- ismail YK!

Çocuklar gibi benle oynama Vallahi öptürmem - Asya!

Çok gerilince sinirlerim, 
Tutamam çenimi söylenirim, 
Kulağı vardır şşşşt her yerin, 
Zararı küpüne sirkenin 
- Şenay Yüzbaşıoğlu!
"""

Hayat =  """
Sana bi' önerim olacak hayatından, mikropları at - Serdar Ortaç!

Hayat sana güzel ama asıl soru, gönül razı mı yarım ekmek arasına? - Murat Boz!

Aklın varsa kendine sakla felsefe yapma
Kimi doğru, kimi yanlış, kafana takma
Herkes bir şey anlatır kendine göre
Kimi haklı, kimi haksız , boş ver sana ne
- Musatafa Topaloğlu!

Yıkılmam inan dünya üstüme gelse Koparır alırım delikanlı gibi  - Çılgın Sedat!

Konuşuyoruz ama nece konuşuyoruz, 
Konuşuyoruz ama anlamıyoruz, 
Konuşuyoruz ama nece konuşuyoruz, 
Konuşuyoruz bomboş 
- Uf-Er!

Ben sana dedim, Sen dinlemedin, Oyunlara geldin - Ve Volkan!

Demedim demedim bir şey demedim 
Derdimi kimseye söylemedim 
-Şenay Yüzbaşıoğlu!

Size birşey söyleyeyim, ben yoruldum. 
Bir de şunu söyleyeyim, ben yoruldum. 
Ha bir de şu var, ben yoruldum. 
Yine söylüyorum ben yoruldum 
- Kuzey Yılmaz!

Şurup gibiyim şurup turp gibiyim turp turp - Ajdar Anık!

Hiç hiçbir şeyi bilmiyorlar, bilmek istemiyorlar. 
Hiç hiçbir şeyi görmüyorlar, görmek istemiyorlar. 
Şu cahillere bak, dünyanın sahibi onlar 
Şu cahillere bak, dünyanın hakimi onlar.
Onlardan değilsen eğer, sana zalim derler.
Onlara aldırma Hayyam. Dostum.
- Siya Siyabend!

İşime gelmeyince hep, 
Hayatın kendisi sebep, 
Sen onca fırsatı tep, 
Ben aptal mıyım? 
- Nil Karaibrahimgil!

Pes etmem ben en zor günümde, Kanatlandım özgürüm bende  - Nil Karaibrahimgil!

Karanlıkta yanabilirim 
Boşlukta durabilirim 
Düşmem ben kanatlarım var ruhumda 
- Nil Karaibrahimgil!

Ah be kardeşim başına ne geldi - Yalın!

Dün hayat durdu benim için, Sanki bugün herşey farklı - Yalın!

Bazen herkesden sıkıldığın oluyordur 
Fişi çekip dükkanı kapatasın geliyordur 
Kavgası tasası savaşı aşkı derdi 
Ah be kardeşim başına ne geldi
-Yalın!
"""

Rastgele = """
Onun arabası var, güzel mi, güzel? 
Şoförü de var, özel mi, özel? 
Bastı mı gaza, gider mi, gider? 
Maalesef ruhu yok 
- Mustafa Sandal!

O onu dedi, bu bunu dedi, sen sustun mu ki? - Yıldız Tilbe!

Bu kadar güvenme hiç kendine, kimse şah değil padişah değil - Sibel Can!

Aboneyim abone 
Biletleri cebimde 
Ballı lokma tatlısı 
Aman haydi hayırlısı 
- Yonca Evimcik!

Miniksin ufacıksın sen tatlı bir kaçıksın - Peker!

Hadi yine iyisin, iyisin iyisin, 
Sen işini bilirsin, bilirsin bilirsin, 
Deli dolu birisin, birisin birisin  
Reçeteni ister misin Muck 
- Tayfun!

Anneni bizim eve gönder, 
Beni sizin evinize aldır, 
Aldıramazsan aldırırlar canım 
- Banu Alkan!

Acı domates gibi kızarıyorum - Serdar Ortaç!

Ben sizin babanızım, 
ben ne dersem o olur 
Önce yemek yiyicem, 
Ve diskoya gidicem, 
Orda hop hop yapıcam 
- Barbaros Hayrettin!

Yeldeğirmenlerine karşı Don Kişot muyum? 
Uçuyorum durmadan ben pilot muyum 
- İlhan İrem!

Bakınız çok oldunuz siz, 
iğne yaparım e eey
Fazla konuşursanız 
Serum bağlarım size 
-Erol Köse!

Kel başa şimşir tarak , 
Bu ayakları artık bırak, 
Ne işin var ki diskoryumda? 
Yanında bir kız sarımtırak 
- Grup Vitamin!

Lagaluga dalavere hebelübe lübünüz 
Daradori dart dart darlanma dallama 
Hebelübü hübülübü dürülülü hebelüb 
Tremola kafakola kokakola hebelüb 
- Uf-Er!

İstemiyorum baba, 
İstemiyorum baba,
Birisi bir edi, 
Bana sarman dedi, 
Birisi bir büdü, 
Bilmem büyüdü mü?, No no no 
- Rüya Ersavcı!

Abdülkadir sen ne dedin yavrum, şşşt tutturursun, 
Gülen bir kaset yapacaksan milenyumda yap, 
Milenyumda yapmazsan uranyumda yap 
- Süheyl ve Behzat!

Çocukta yaparım kariyer de - Nil Karaibrahimgil!
"""

Üzgünlük = """
Kulaklarım patlıyor sessizliğinden Yorgunluğundan ölüyorum - Teoman!

Senle yaşadığıma sözüm yok, yaşanan kısmet. 
Sonrasını da ben konuşmam, sevmem nisbet 
- Murat Dalkılıç!

Zaten merhem olmazsın sen benim gönül yarama - Gökhan Özen!

Eğer bıçak kemiğe dayandıysa, niye bu amansız acıya göz yumuyorsun? - Ajda Pekkan!

Caka satıyor utanması yok, o kendini üstün buluyor ama yanılıyor... - Tarkan!

Köprüleri yakalı, kaldırıp kenara atalı; yüzünü unutalı uzun zaman oluyor - Emrah Karaduman!

Unutamam dedin, yalan mı söyledin? 
Ben böyle pare pare zehir oldu yediğim içtiğim, reva mı ettiğin? 
Aynı son aynı hikaye, bırak beni bırak gideyim 
- Gülden Mutlu!

Ne olur bir şey sorma anne, Ne oldu diye bana sorma - Çelik!

Anladım yoksun artık, Ben gönlünden taşındım - Ali Güven!

Üzülmemek diye birşey yok , Üzülmem gerek - Yalın!
"""


categories = [Hayat, Aşk, Kızgınlık, Üzgünlük, Rastgele]
categories_name = ["Hayat", "Aşk", "Kızgınlık", "Üzgünlük", "Rastgele"]
categories_show = ["Hayatın hakkında ne düşünüyorum merak ediyor musun?", "Acaba aşk hayatın ne durumda?", "Kızgın veya gergin hissediyorsun...", "Duydum ki ağlamak istiyormuşsun.", "Benden sana rastgele bir tavsiye"]
for i in range(len(categories)):
    categories[i] = categories[i].split("!")

veri = pd.DataFrame(columns=['Şarkı', 'Kategori'])


for i in range(len(categories_name)):
    for j in range(len(categories[i])):
        veri = veri.append( {'Şarkı': categories[i][j], 
                             'Kategori': categories_name[i], 
                             'Ekranda_Gösterilen_Bölüm': categories_show[i]}, 
                             ignore_index=True)
                             
        veri = veri[veri['Şarkı'] != ""]
        veri.reset_index(drop=True, inplace=True)
        
        
veri["cleaned_sentence"]=veri['Şarkı'].copy()

for i in range(len(veri)):
    veri["cleaned_sentence"][i] = re.sub('[!@#’‘?.,\'$]', '', veri["cleaned_sentence"][i])
    veri["cleaned_sentence"][i] = veri["cleaned_sentence"][i].lower()

word_vectors = KeyedVectors.load_word2vec_format('trmodel', binary=True)


class kuzuKuzu:
    
    def jaccard_similarity(str1, str2):
        a = set(str1.split()) 
        b = set(str2.split())
        intersection = a.intersection(b)
        union = len(a) + len(b) - len(intersection)

        return float(len(intersection) / union)

    def recomendation_random_jaccard(cevap):
        jaccard_score_list = []
        if len(cevap.split()) > 1:
            for i in range(len(veri)):
                jaccard_score_list.append(kuzuKuzu.jaccard_similarity(veri["cleaned_sentence"][i], cevap))        
                max_index = jaccard_score_list.index(max(jaccard_score_list))
                recommendation = veri['Şarkı'][max_index]

            st.text(recommendation)

        else:
            if(cevap in categories_name):
                recommendation = veri["Şarkı"][veri["Kategori"]==cevap].sample(n=1).values[0]

            else:
                recommendation = veri["Şarkı"].sample(n=1).values[0]
                
            st.text(recommendation)
            
    def construct_wv_matrices(veri, cevap):
        word_matrix = np.zeros((len(veri), 400))
        for i in range(len(veri)):
            wv_sum = np.zeros((1, 400))
            for j in veri.iloc[i]['cleaned_sentence'].split(' '):
                try:
                    wv_sum += word_vectors[j]
                except: 
                    pass
            word_matrix[i] = np.divide(wv_sum, len(veri.iloc[i]['cleaned_sentence'].split(' ')))

            answer_vector = np.zeros((1, 400))
            for k in cevap.split(' '):
                try:
                    answer_vector += word_vectors[k]
                except: 
                    pass
            answer_vector = np.divide(answer_vector, len(cevap.split(' ')))

        return word_matrix, answer_vector

    def recommendation_wv():
        st.header("İşte kuzu kuzu geldim!")
        yol = st.selectbox("İçini dökmek ister misin yoksa sadece seçim mi yapacaksın?", ["İçimi dökeceğim.", "Seçenekler arasından seçim yapacağım."])
        if (yol == "İçimi dökeceğim."):
            cevap = st.text_input("Ruh halini en az bir kelime ile anlat").lower()
            word_matrix, answer_vector = kuzuKuzu.construct_wv_matrices(veri, cevap)

            score_board = []
            for i in range(len(veri)):
                score = cosine_similarity(word_matrix[i].reshape(1,400), answer_vector.reshape(1,400))
                score_board.append(score)
            recommendation = veri.iloc[score_board.index(max(score_board))].Şarkı
        
            st.text(recommendation)
            
        elif(yol == "Seçenekler arasından seçim yapacağım."):
            cevap = st.selectbox("Kuzu kuzu secimini yap", [secenek for secenek in categories_name])
            kuzuKuzu.recomendation_random_jaccard(cevap)

               
            
               


st.title("Kuzu Kuzu Gel Ruh Halini Şarkı Sözleri İle Yansıtayım!")
st.markdown('Tarkan sunar...')
st.caption('made by Çisem Kaplan & Bengü Yurdakul ')
st.sidebar.header("KUZU KUZU")
st.sidebar.write("İster at, ister öp beni. Ama önce dinle bak gözlerime!")
file_ = open("tarkangif.gif", "rb") #C:/Users/admin/Dropbox/My PC (DESKTOP-CQS9CBD)/Desktop/
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.sidebar.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

result = st.sidebar.slider("Kuzu Kuzu tahminimi nasıl buldun? ", 0,100)
if (result == 100):
    st.balloons()  
elif (result < 100):
    st.sidebar.write("Nerden kırdın " , int(100-result) , "puanı kuzum?")

file_ = open("kuzu.mp4", "rb") #C:/Users/admin/Dropbox/My PC (DESKTOP-CQS9CBD)/Desktop/
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
display_bg_video = f"""
                    <!-- The video -->
                    <video autoplay="autoplay" muted loop src="data:video/mp4;base64,{data_url}" type="video/mp4"
                    id="myVideo" mimeType="application/mp4"></video>
                    """
st.markdown(display_bg_video, unsafe_allow_html=True)

kuzuKuzu.recommendation_wv()

    




