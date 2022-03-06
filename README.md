### programlama-uygulamalari-kuzukuzu
TÜRKÇE
======
Kullanıcının moduna göre kullanıcıdan girdi ister ve şarkı sözleri ile yanıt verir. 

Girdi bir kelime, bir cümle veya bir paragraf olabilir.

*Word2Vec algortiması, Jaccard ve Cosine benzerliği* uygulandı. 
Daha sonra uygulama *Streamlit'e* yüklendi.

[Kodu çalıştırmak için şu kütüphaneyi indirmelisiniz](https://drive.google.com/drive/folders/1IBMTAGtZ4DakSCyAoA4j7Ch0Ft1aFoww?usp=drive_open "TRMODEL")

[Kaynak](https://github.com/akoksal/Turkish-Word2Vec)

# Gerçek Hayata Uygulaması
 Üzgün, mutlu, heyecanlı, endişeli, kızgın hissettiğimizde, iyi ya da kötü bir haber aldığımızda, ders çalıştığımızda, iş yaptığımızda, boş bir anımızda, yürürken, otururken, uyumaya çalışırken, uyanmaya çalışırken bütün insanlığın ortak bir
sığınağı vardır: Müzik.
 
Günümüzde birçok insanın yaşamın koşuşturmasından veya insanlardan dolayı problemleri olabiliyor. Böyle zamanlarda da derdini söyleyebileceği ve ya yol
gösterecek ya da içini rahatlatacak şeyler duymak istiyor. Ama insanlar her zaman dinleme ve öğüt verme konusunda güvenilir olamayabiliyor. Ya da o kişi sıkıntısını başkalarıyla paylaşmak konusunda kendisini rahat hissetmiyor ve sorunu kendi içinde
çözmeye çalışıyor.

İşte böyle bir anda hem sizin derdinizi dinleyecek hem de size Türkçe pop kültürünün önemli şarkılarından parçalar sunacak olan programımız devreye giriyor.
Ayrıca sadece dertleşmeye değil aynı zamanda dinlemek istediğiniz temaya göre şarkı sözleri ve şarkıların sahibini de sizlere sunar.

# Kod Yapısı
- Dataframe üzerinde kolayca işlem yapabilmek ve anlaşılır kılabilmek için **Pandas**,

- Matrisleri kolayca kullanabilmek için **Numpy**,

- Metni düzenlemek ve metinden alt parçaları elde etmek için **Re**,

- Encoding binary verileri metne dönüştürmek için **Base64**,

- Cosine-smilarity fonksiyonunu kullanabilmek için **Scikit-Learn**,
 
- Word2Vec için **Gensim**,

- İnternet sitesine taşıyabilmek için de **streamlit**

kullanıldı.

## Dot product
![alt text](https://github.com/benguyurdakul/programlama-uygulamalari-kuzukuzu/blob/main/dot%20product.PNG)

## Norm
![alt text](https://github.com/benguyurdakul/programlama-uygulamalari-kuzukuzu/blob/main/norm.PNG)

## Cosine Similarity
![alt text](https://github.com/benguyurdakul/programlama-uygulamalari-kuzukuzu/blob/main/cosine%20similarity.PNG)


ENGLISH
======
According to the user's mode, it prompts for input from the user and responds with lyrics.

Input can be a word, a sentence, or a paragraph.

*Word2Vec algorithm, Jaccard and Cosine similarity* were applied.Then the application was uploaded to *Streamlit.*

[You should download the library](https://drive.google.com/drive/folders/1IBMTAGtZ4DakSCyAoA4j7Ch0Ft1aFoww?usp=drive_open "TRMODEL")

[Source](https://github.com/akoksal/Turkish-Word2Vec)

# Code Structure
- **Pandas** in order to be able to operate on the data frame easily and make it understandable,

- **Numpy** to use matrices easily,

- **Re** to edit the text and extract sub-parts from the text,

- **Base64** for encoding binary data to text,

- **Scikit-Learn** to use the cosine-similarity function,
 
- **Gensim** for Word2Vec,

- **streamlit** for transferring to the website

used.
