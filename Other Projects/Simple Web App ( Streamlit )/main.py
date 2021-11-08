import streamlit as st
import pandas as pd
import base64



def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(set(list1)) + len(set(list2))) - intersection
    return float(intersection) / union


def random_jaccard_recommandation(user_input):
    jaccard_similarity_list = []
    user_input = user_input.lower()

    if user_input in categories_name:
        n = categories_name.index(user_input)
        recommendation = df["sentence"][df["category"] == user_input].sample().values[0]

        return categories_msg[n] + recommendation
    else:
        if len(user_input.split()) > 1:
            for i in range(len(df)):
                jaccard_similarity_list.append(jaccard_similarity(df["sentence_c"][i], user_input))
                max_index = jaccard_similarity_list.index(max(jaccard_similarity_list))
                recommendation = df['sentence'][max_index]
        else:
            recommendation = df["sentence"].sample().values[0]
        return recommendation


hayat = """

Hayatı yaşamanın iki yolu vardır: Biri hiçbir şeyin mucize oImadığını düşünmek, diğeri her şeyin mucize oIduğunu düşünmek.

Yanlışı savunup kalabalıkları arkama katmakansa, doğrumu savunup yalnız kalmayı tercih ederim.

Bir şey yanlışsa, milyonlarca kişi o yanlışı savunsa da, o yine yanlıştır.

Kendisini başkalarının kurtarmasını bekleyen kişiler yalnızca kölelerdir.

Benim merak ettiğim ölümden sonra değil, doğumdan sonra hayat olup olmadığıdır.

Son ağaç kesilip, son nehir kirletilip, son balık da tutulduktan sonra beyaz insanlar paranın yenmediğini anlayacaktır!

Evrenin başka yerlerinde de zeki canlıların var olduğunun en kesin kanıtı, şimdiye dek bizimle hiç irtibata geçmeye çalışmamış olmalarıdır.

Her gününüzü hayatınızın son günüymüş gibi yaşayın; bir gün haklı çıkacaksınız.

Korkaklar ecelleri gelmeden birkaç kere ölürler. Cesurlar ölümü bir kere tadarlar.

Gözlerin rengi, biçimi ne kadar farklı olursa olsun gözyaşlarının rengi aynıdır.

Küçük şeylere fazla önem verenler ellerinden büyük şeyler gelmeyenlerdir.

İnsan ancak anladığı şeyleri duyar.

Rüyaları gerçekleştirmenin en iyi yolu uyanmaktır.

Düşman isterseniz dostlarınızı geçmeye çalışınız. Dost isterseniz  bırakın  dostlarınız sizi geçsin.

Herkesin üç kişiliği vardır; Ortaya çıkardığı,  sahip olduğu,  sahip olduğunu sandığı.

"""

aşk = """

Şimdi o gidiyor ya, ikiden bir çıkınca ne kalır geriye? Bir kalır değil mi? Öyle değilmiş işte. Yarım kalıyormuşsun...

Beni hapiste vurdular, ölmedim. Hastalandım, bir ciğerimi orada bıraktım gene ölmedim. Çok dövdüler beni, kan kustum ama ölmedim. Yaşadım, seni bir kez daha görebilmek için yaşadım...

Dünyanın ekseni kaydı Behzat. On iki santim yerinden oynadı. Sen bana bir santim bile yaklaşmadın!

Öyle bir kız ki, çocukluğumun bayram sabahları gibi. İnsan gözlerine bakarak nasıl söyler sevdiğini?

Sıfır bir değer değildir. Bir sayı bile değildir. Ancak başka bir sayının yanına gelince değer yaratır. Tıpkı sevda gibi... Sevdanın da tek başına değeri yok. İlle de biri olmalı. Sıfır ne kadar çoksa sayı o kadar çoğalır. Sevda da ne kadar çoksa insan o kadar çoğalır. Büyür...

Aşık olmak anlık bir şey. Birden her şeyin çok parlak göründüğü, birden en pastel renklerin bile ısınmaya başladığı, birden tüm yemeklerin bile çok daha lezzetli olduğu bir an bu. İnsan karar vererek aşık olmaz. Sadece bir bakar, olmuş...

Dünyadaki herkesin parmak izinin farklı olması, kimsenin sana benim gibi dokunamayacağının kanıtıdır

Ben sana değil resmine aşık oldum...

Bir insan ne zaman ölüyormuş biliyor musun? Sevdiğinin hayalinde yaşamadığını anladığı anda.

Bazen ilk görüşte bilirsin, o insan senin kaderindir. Bazen bir ömür ararsın... Bulunmaz

Asuman, sen şimdi arabalı vapurun güvertesinden denize bakacaksın ya, ciddiye alma! Bizim sevdamız ondan büyük...

Sana bakan dıştan şey der, dışın taştan; ama için...

Ziyanı yok, gülüşü yeter bize.

Nasıl bir şey bu biliyor musun? Hani karanlık bir gecede, ıssız bir yokuşu tek başına inerken, bir köşeye dönersin de deniz çıkar ya karşına. Sonra o denizde bir gemi belirir, şıkır şıkır ışıklarla geçip gider sen sevinirsin. Hiç nedensiz ama... Sonra için kıpırdar ya. Hani öyle işte... Seni tanıdığımdan beri bir gemi geçiyor içimden. hep ama...

Sonuçta biz gönül adamıyız tabii. Dağı severiz, taşı severiz, yeri gelir bir güvercine tutuluruz...

Hayat aldığımız nefeslerle değil, nefesimizi kesen anlarla ölçülür.

Birlikte olmayı hak etmeyen milyonlarca insan yan yanayken, ben neden hala senden ayrı nefes alıyorum?

Jeny ve ben, köfte ve patates gibiydik.

Aptal gibi gözükmeye razı değilsen, aşık olmayı hak etmiyorsun demektir.

Aşka tamamen teslim olana dek onun ne olduğunu asla bilemeyeceksin.

Ben senin hayatının bir bölümünde yer aldım ama sen benim hayatımın tamamıydın.

"""

şarkı = """

https://www.youtube.com/watch?v=mov_t3L4BG8

https://www.youtube.com/watch?v=PV_NGxZEo54

https://www.youtube.com/watch?v=ydkXLzQjhgY

https://www.youtube.com/watch?v=um3YRKbRKZI

https://www.youtube.com/watch?v=0CwGoEbHcSE

https://www.youtube.com/watch?v=dfQs2Ut-dhA

https://www.youtube.com/watch?v=Q0AdXAh-6gA

https://www.youtube.com/watch?v=VASO9VZi5hU

https://www.youtube.com/watch?v=CnMmGLEPgO4

https://www.youtube.com/watch?v=laF_VdHN8G8

"""

genel = """

İntikam ölümden güçlüdür.

Her ihanet sevgiyle başlar.

Emir almak başka, keyif almak başka..

Kaderimiz niye avucumuzun içinde yazılıdır bilir misin? Gerektiğinde gizleyebilelim diye.. Niye bilir misin? Çünkü güç gizden gelir.. Gerçek niyetini kimse bilmeyecek.. Kaderin sırrındır.. Kaderini kimseyle paylaşmayacaksın..

Kadere inanan insan tesadüfe inanmaz. Tesadüfe inanan adamsa kaderini kendi elinde tutamaz.

Kimsin sen? Şüphesiz sen, sen değilsin.

Ne kadar uzağa gidersen git başladığın yere dönersin sonunda. Ne kadar değişirsen değiş, nerede mutlu olduysan hep oraya çevirirsin kafanı.

Kırılmak istemiyorsan, kendini yere bırakmayacaksın.

Hesap görmek, hesap etmekten zordur.

Mesele ölmek değil dost bildiğin en güvendiğin adamın eliyle ölmekmiş mesele.

Sen fazlasını bilmek istemiyorsun arkadaş sen sadece birgün seninde sevilebileceğini bilmek istiyorsun ve ne yaparsan yap sevilmiyorsan eğer seni gerçekler değil sokatan seçtiğin rastgele birini kurban etmek kurtarır.

Olan olmuş. Artık hiçbir neden onu olmamış yapamaz.

Tanık dediğin suç ortağındır aslında.

Yanlız kalan bir insan, hiç yanlızlığından bir başkasına bahsedebilir mi?

Korkunçtur sonunda gördüğün gerçeğin en çıplak en gaddar en acımasız yüzü ama en korkuncu her şeye sahipken bile bir anının bir hayalin bir hayaletin peşinden koşmak.

Gerçeği yine de öğrenmek için yalanlardan örülü bir ipe tutunmak ne korkunçtur.

Hesap görmek, hesap etmekten zordur yeğenim.

Değişmek zordur yeğenim ama bazen aynı adam olmak daha zordur. Hayat öyle yüklenir ki üstüne durduğun yerde çatır çatır çatırdarsın.

Hayal ettiğin her şey bir gün bir ihtimal gerçek olabilir o ihtimali yok etmeden unutabilirmisin gerçekten sevdiğin tek insanı.

Gerçekleri saklayarak ulaşabilirmisin gerçeğe anıların içinde aradığın insanı bulabilirmisin hiç yaşanmamış hayata gerçek gibi tutunabilirmisin orada olmayan birinin seni hala koruduğuna inanabilirmisin gerçeğin o kadar çok yüzü var ki senin gördüğüne inanabilirmisin.

Eğer birisi seni aldatmışsa bu onun suçudur. Eğer o kişi seni pek çok kere aldatmışsa bu senin suçundur.

Bazen öyle acır ki için değiştin sanırsın şimdi dersin. Şimdi her şeyi yapabilirim.

Bazen hayat seni öyle zorlar ki yeğenim yolun başında kimdin. Unutursun.

En karanlık gününde, en çaresiz anında kendini ortaya atıyorsan eğer, en umutsuz anında, kendin için değil, çocukların için, kendini çare diye sunuyorsan eğer, yüreğinde çocuğunun sevgisini tutan, hiç kimse çaresiz değildir.

Bazen yeğen işleri yoluna koymak için sıkmayacaksın yumruğunu, açacaksın avucunu avucundakileri savuracaksın havaya. Bekleyeceksin, bekleyeceksin sana geri gelmelerini.

En iyi soygunlar girerken değil çıkarken bozulur yeğen. Haydutlar öyle iyi planlar ki girmeyi nasıl çıkacaklarını unuturlar. Çıkacaksan hemen çıkacaksın yeğen yoksa çekerler yoksa seni içeri.

Bir şey yapmadan önce eğer yaparsan sana ne yapacağımı bir düşün önce.

Bu gün bi köprünün tam ortasında durdum, aşağıda alevler, arkamda melek, önümde şeytan, ikisi de aynı soruyu sordu. Kimsin sen, kimin tarafındasın.

Zorunu benden duy yeğenim, herkese yalan söylemen yetmez artık. Bundan böyle bir başına kalsan da artık kendin olamazsın.

Kaderimiz olan aşka değil de aşkıyla kaderimizi değiştirene içelim!

Asıl çaresizlik derdin devasız olması değil, birini iyi edecek şeyin diğerinin kadehine zehir olmasıdır.

Kendi kanını kendi elleriyle kurutan bir adamım. İşte ben böyle bir adamım. Ömer benim de oğlum o benim son oğlum. Ben ne Allah’ım ne de Azrail. Ne alabilirim oğlunun canını ne de geri verebilirim sana. Yapamam.

Aşk mı intikam mı, mahkum mu, cellat mı. hep ikisinden birini seçmen istendi. Ama hep bir üçüncü şık var. O da ateşe atlamak.

Ölüm gibidir sadakat. Bir kere çizgiyi geçtin mi, geri dönüş yoktur.

Savaşmak aslında hasmınla savaşmak değil, sevdiklerinle savaşmaktır. Savaşırken göremezsin bazı savaşları kazanamazsın artık durmalı ve geri çekilmelisin.

Ne kadar değişirsen değiş, Nerede mutlu olduysan hep oraya çevirirsin kafanı.

Portakalı soymadan içinin iyi olup olmadığını anlayamazsın.

Ben her şeyi olan ve kaybedeceği hiçbir şey olmayan insanım.

Ezel duy sesimi! Bir kere ihanete uğradın mı anılar sana bataklık olur yeğen, hatırladıkça çekerler seni içeri, hatırladıkça affetmek istersin yeğen; çünkü affetmek unutmak demek, öncesini hatırladıkça sonrasını unutmak istersin, çırpınma boşuna yeğen, o hançer bir kere saplanınca sırtına çıkarmaya kalktıkça iyice kalbine gömersin.

Unutma! Bin kere dönsen o güne, bin kere ihanet edecekler sana. Herkes doğasının gereğini yapar. Bin kere ihanet etseler sana çaresi yok bin kere gidersin yanlarına.

Geçmişe dönmek başka, geçmişi silmek başka. Bir kere aktı mı zamanın içinden suyun yolu değişmez.

Değişmek zordur ama bazen aynı adam olmak daha da zordur.

Sadakat erdem değildir aslında sevgiden kör olmaktır, hep kaçtığın şeye eninde sonunda yakalanmaktır sadakat. Yemin etmeden bir daha düşün; çünkü sadakatle başlayan her şey ihanetle biter.

Asıl çaresizlik derdin devasız olması değil, Birini iyi edecek şeyin, diğerinin kadehine zehir olmasıdır.

Sakın bir daha seni seviyorum deme çünkü inanırım.

Kadere inanan insan tesadüfe inanmaz. Tesadüfe inanan adamsa kaderini kendi elinde tutamaz.

Sadakat ya birine doğru koşmaktır, ya birinden kaçmaktır.

"""

rast_gele = """

Bu maymun nerden çıktı? Kendileri Pembe’nin muhterem dedesi olurlar. Pembe maymundan geldi bilmiyor musunuz? Ulan! Ben hiç değilse kalkıp gelmişim. Sen hiç gelememişsin. Maymun olarak kalmışsın.

Hade sabah ola hayrola, bu ne biçim karyola.

Anam ayatta izin vermez be Ferat.

Tokmak mort et müziği.

Tüh! Gitti milyarlık mobilya.

Bu ülkenin kanunu var Pembe. Kanunu varsa tamburu da var sazı da komiserim.

Salih! At bunları dışarı.

Yaparız şip şak.

Feratlar ve küpekler giremez.

Bu ne biçim şaka be Pembe Abla ya, biraz ayıp olmuyor mu yani he

Salih, at bunları dışarı

Ferhat oğlum, söylemeyi unuttum ha, Cuma günleri yasak kalkıyor. Ama yasak sadece küpeklere kalkıyor, Ferhatlar yine giremiyorlar ahah.

Ya anlamadınız mı be abicim işte bunu lehimize çevirip pembe'yi oyuna getireceğiz ardından ferhat'la sultan'ı evlendireceğiz işte ya -Beter Ali

Kelmangee kakoo kakoo şugarkee magee kakoo.

Demek Muharreme kız istiycez ha, ulan bu kütük bile evlenir ben hâlâ bekarım adalet mi bu bee.

Şimdi efendim ne demişler, gönül bu demişler, hani ota da konar boka da konar demişler. Bizim Muharreminki değil mi Muharremcim ota konmamış yani gitmiş Menekşenin başına konmuş.

Sultan evden kaçmış doğru söyleyin bana burda mıdır - Ne o bizim evin kapısında kayıp eşya bürosu mu yazar?

Taç mı ? Tak kız şimdi o tacı. Gördün mü baba erif benim kraliçe olduğumu anlamış bana taç göndermiş. Ee tabi asil biri olduğum emen anlaşılır.

Bir dakika, kavga başlayalı ne kadar oluyor, neredesin sen??

Kelmangeeeee kakaooo kakooo

Kelmangeeeee kakaooo kakooo, şugarkeeeee mage kakaoooo, yandan geeell mage kaakooo kakaoo

"""

# DATABASE#
categories = [hayat, aşk, şarkı, genel, rast_gele]
categories_name = ["hayat", "aşk", "şarkı", "genel", "rastgele"]
categories_msg = ["Hayat sana ne mi diyor: ", "'O' ne mi düşünüyor: ", "Çok güzel bir şarkı önereyim sana: ",
                  "Havadan sudan: ", "Rast gele: "]

for i in range(len(categories)):
    categories[i] = categories[i].split("\n")

df = pd.DataFrame(columns=['sentence', 'category', 'category_msg'])

for i in range(len(categories_name)):
    for j in range(len(categories[i])):
        df = df.append(
            {'sentence': categories[i][j], 'category': categories_name[i], 'category_msg': categories_msg[i]},
            ignore_index=True)

    df = df[df['sentence'] != ""]
    df.reset_index(drop=True, inplace=True)

df["sentence_c"] = df['sentence'].copy()


def rp_string(string: str):
    myString = ""
    for k in range(len(string)):
        if string[k].isalpha() or string[k].isdigit() or string[k].isspace():
            myString += string[k]
    return myString


for i in range(len(df)):
    df["sentence_c"][i] = df["sentence_c"][i].lower()
    df["sentence_c"][i] = rp_string(df["sentence_c"][i])

# ARKAPLAN VİDEO#
file_ = open("Falci_Pembe.mp4", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
display_bg_video = f"""
            <!-- The video -->
            <video autoplay="autoplay" muted loop src="data:video/mp4;base64,{data_url}" type="video/mp4" 
            id="myVideo" mimeType="application/mp4"></video>
            <div class="top-content">
                <h2>FALCI PEMBE</h1> 
            </div>
            <div class="content">
                <h2>ALTILI GANYANI BİLEN MEŞUR FALCI PEMBE</h2>
                <h5>Merak etmeyin, hepinizin ganyan falına bakacam, hepinizi zengin yapacam Allah'ın izniyle</h5>
            </div>
            """
st.markdown(display_bg_video, unsafe_allow_html=True)

# HTML & CSS#
hide_streamlit_style = """
                        
            <style>
            #myVideo {
              position: fixed;
              left: 17.5%;
              bottom: 0;
              min-width: 90%;
              max-width: 90%;
              min-height: 90%;
            }

            .content {
              position: fixed;
              left: 17.5%;
              bottom: 0;
              text-align: center;
              background: rgba(0, 0, 0, 0.75);
              color: #f1f1f1;
              width: 90%;
              padding: 20px;
            }
            .top-content {
              position: fixed;
              left: 77.5%;
              top: 0;
              text-align: center;
              background: rgba(0, 0, 0, 0.75);
              color: #f1f1f1;
              width: 16%;
              padding: 0 10px;
            }
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            section {background-color: black;}
            .css-zw9mgv.edgvbvh6 {visibility:hidden;}
            </style>

            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# SIDEBAR#
st.sidebar.header("FALCI PEMBE")
st.sidebar.write("Neyse bahtın, çıksın falın!")
user_input = st.sidebar.text_input("Pembe abla, gözünü seveyim falıma bak bea:",
                                   help="--Konu Başlıkları--\n\n1 - Hayat\n\n2 - "
                                        "Aşk\n\n3 - Şarkı\n\n4- Genel\n\n5- Rastgele"
                                        "\n\nDipnot: Rast gelsin işlerin be*"
                                        "\n\nİpucu: Merak ettiğiniz konu için konu ismini yazınız.")

st.sidebar.write(random_jaccard_recommandation(rp_string(str(user_input).lower())))