import pandas as pd
import numpy as np
import statistics
import scipy.stats
from matplotlib import pyplot
# from statsmodels.graphics.gofplots import qqplot
# from scipy.stats import normaltest
# from statsmodels.stats.weightstats import ztest
# from scipy import stats
# from scipy.stats import shapiro

veri = pd.read_excel('C:/Users/DELL/Downloads/TitanicDataset.xlsx')

bosluk_sayisi_cabin = veri['Cabin'].isnull().sum()

veri.drop('Cabin', axis=1, inplace=True)

#AGE


aort = veri['Age'].mean()

bosluk_sayisi = veri['Age'].isnull().sum()

bosluk = veri[['Age']].fillna(method='ffill')

yuvarlama =np.ceil(bosluk['Age'])

aort2 = yuvarlama.mean()

gort = statistics.geometric_mean(yuvarlama)

mod = statistics.mode(yuvarlama)

medyan = statistics.median(yuvarlama)

varyans = statistics.variance(yuvarlama)

std_sapma = statistics.stdev(yuvarlama)

enbuyuk = yuvarlama.max()

enkucuk = yuvarlama.min()

aralık = np.ptp(yuvarlama)

carpiklik = scipy.stats.skew(yuvarlama)

basiklik = scipy.stats.kurtosis(yuvarlama)

yuzdelik25 = np.percentile(yuvarlama, 25)

yuzdelik75 = np.percentile(yuvarlama, 75)

cocuk = yuvarlama[yuvarlama < 18].count()

genc = yuvarlama[(yuvarlama >= 18) & (yuvarlama < 30)].count()

yetiskin = yuvarlama[(yuvarlama >= 30) & (yuvarlama < 60)].count()

yasli = yuvarlama[(yuvarlama >= 60)].count()

genc_yasli_kadin = yuvarlama[(yuvarlama >= 30) & (veri['Sex'] == 'female')]

genc_yasli_erkek = yuvarlama[(yuvarlama >= 30) & (veri['Sex'] == 'male')]

#FARE

degistirme = veri['Fare'].replace(0 , 4.0125)

aortfare = degistirme.mean()

gort2 = statistics.geometric_mean(degistirme)

mod2 = statistics.mode(degistirme)

medyan2 = statistics.median(degistirme)

varyans2 = statistics.variance(degistirme)

std_sapma2 = statistics.stdev(degistirme)

enbuyuk2 = degistirme.max()

enkucuk2 = degistirme.min()

aralık2 = np.ptp(degistirme)

carpiklik2 = scipy.stats.skew(degistirme)

basiklik2 = scipy.stats.kurtosis(degistirme)

yuzdelik25fare = np.percentile(degistirme, 25)

yuzdelik75fare = np.percentile(degistirme, 75)

yineleme = degistirme.drop_duplicates()

siralama2 = sorted(yineleme)

ucuz = degistirme[degistirme <= 12.65].count()

orta = degistirme[(degistirme > 12.65) & (degistirme <= 34.6542)].count()

pahali = degistirme[(degistirme > 34.6542) & (degistirme <= 512.3292)].count()

#PARCH

sifir = (veri['Parch'] == 0).sum()

ailecocuk = (veri['Parch'] > 0).sum()

#SIBSP

sifir2 = (veri['SibSp'] == 0).sum()

eskardes = (veri['SibSp'] > 0).sum()

#SEX

kadin = (veri['Sex'] == 'female').sum()

erkek = (veri['Sex'] == 'male').sum()

#EMBARKED

Southampton = (veri['Embarked'] == 'S').sum()

Cherbourg = (veri['Embarked'] == 'C').sum()

Queenstown = (veri['Embarked'] == 'Q').sum()

#PCLASS

lower = (veri['Pclass'] == 3 ).sum()

middle = (veri['Pclass'] == 2).sum()

upper = (veri['Pclass'] == 1).sum()

#SURVIVED

olu = (veri['Survived'] == 0).sum()

canli = (veri['Survived'] == 1).sum()

#COLUMN+DEATH

upperDeath = ((veri['Survived'] == 0) & (veri['Pclass'] == 1)).sum()

midddleDeath = ((veri['Survived'] == 0) & (veri['Pclass'] == 2)).sum()

lowerDeath = ((veri['Survived'] == 0) & (veri['Pclass'] == 3)).sum()

#---------------------------------------------------------------------

olukadin = ((veri['Survived'] == 0) &  (veri['Sex'] == 'female')).sum()

oluerkek = ((veri['Survived'] == 0) & (veri['Sex'] == 'male')).sum()

#-----------------------------------------------------------------------

oluailecocuk = ((veri['Survived'] == 0) & (veri['Parch'] > 0)).sum()

olueskardes = ((veri['Survived'] == 0) & (veri['SibSp'] > 0)).sum()

#----------------------------------------------------------------------

oluSouthampton = ((veri['Survived'] == 0) &  (veri['Embarked'] == 'S') ).sum()

oluCherbourg = ((veri['Survived'] == 0) &  (veri['Embarked'] == 'C')).sum()

oluQueenstown = ((veri['Survived'] == 0) &  (veri['Embarked'] == 'Q') ).sum()

#---------------------------------------------------------------------------------

cocukbool = yuvarlama < 18
gencbool = (18 < yuvarlama) & (30 > yuvarlama)
yetiskinbool = (30 < yuvarlama) & (60 > yuvarlama)
yaslibool = 60 < yuvarlama

olucocuk = ((veri['Survived'] == 0) & cocukbool ).sum()

olugenc = ((veri['Survived'] == 0) & gencbool ).sum()

oluyetiskin = ((veri['Survived'] == 0) & yetiskinbool ).sum()

oluyasli = ((veri['Survived'] == 0) & yaslibool ).sum()

#REALITIONSHIP

ucretaraligi1 = degistirme[(veri['Pclass'] == 1)]

ucretmax1 = ucretaraligi1.max()

ucretaraligi2 = degistirme[(veri['Pclass'] == 2)]

ucretmax2 = ucretaraligi2.max()

ucretaraligi3 = degistirme[(veri['Pclass'] == 3)]

ucretmax3 = ucretaraligi3.max()

#---------------------------------------------------

Southampton1 = ((veri['Pclass'] == 1) &  (veri['Embarked'] == 'S') ).sum()

Southampton2 = ((veri['Pclass'] == 2) &  (veri['Embarked'] == 'S')).sum()

Southampton3 = ((veri['Pclass'] == 3) &  (veri['Embarked'] == 'S') ).sum()

Cherbourg1 = ((veri['Pclass'] == 1) &  (veri['Embarked'] == 'C') ).sum()

Cherbourg2 = ((veri['Pclass'] == 2) &  (veri['Embarked'] == 'C')).sum()

Cherbourg3 = ((veri['Pclass'] == 3) &  (veri['Embarked'] == 'C') ).sum()

Queenstown1 = ((veri['Pclass'] == 1) &  (veri['Embarked'] == 'Q') ).sum()

Queenstown2 = ((veri['Pclass'] == 2) &  (veri['Embarked'] == 'Q')).sum()

Queenstown3 = ((veri['Pclass'] == 3) &  (veri['Embarked'] == 'Q') ).sum()

#--------------------------------------------------------------------------

Southamptonkadin = ((veri['Sex'] == 'female') &  (veri['Embarked'] == 'S') ).sum()

Southamptonerkek = ((veri['Sex'] == 'male') &  (veri['Embarked'] == 'S')).sum()

Cherbourgkadin = ((veri['Sex'] == 'female') &  (veri['Embarked'] == 'C') ).sum()

Cherbourgerkek = ((veri['Sex'] == 'male') &  (veri['Embarked'] == 'C') ).sum()

Queenstownkadin = ((veri['Sex'] == 'female') &  (veri['Embarked'] == 'Q')).sum()

Queenstownerkek = ((veri['Sex'] == 'male') &  (veri['Embarked'] == 'Q') ).sum()

#---------------------------------------------------------------------------------

def olu_sayisi(veri, cinsiyet, sinif):
    return ((veri['Survived'] == 0) & (veri['Sex'] == cinsiyet) & (veri['Pclass'] == sinif)).sum()

def olukadin_sayisi(veri, sinif):
    return olu_sayisi(veri, 'female', sinif)

def oluerkek_sayisi(veri, sinif):
    return olu_sayisi(veri, 'male', sinif)

olukadin1, olukadin2, olukadin3 = [olukadin_sayisi(veri, sinif) for sinif in range(1, 4)]
oluerkek1, oluerkek2, oluerkek3 = [oluerkek_sayisi(veri, sinif) for sinif in range(1, 4)]

#--------------------------------------------------------------------------------------------------

olukizcocuk =  ((veri['Survived'] == 0) &  (veri['Sex'] == 'female') & cocukbool).sum()

oluerkekcocuk = ((veri['Survived'] == 0) &  (veri['Sex'] == 'male') & cocukbool).sum()

olugenckiz = ((veri['Survived'] == 0) &  (veri['Sex'] == 'female') & gencbool).sum()

olugencerkek = ((veri['Survived'] == 0) &  (veri['Sex'] == 'male') & gencbool).sum()

oluyetiskinkadin = ((veri['Survived'] == 0) &  (veri['Sex'] == 'female') & yetiskinbool).sum()

oluyetiskinerkek = ((veri['Survived'] == 0) &  (veri['Sex'] == 'male') & yetiskinbool).sum()

oluyaslikadin = ((veri['Survived'] == 0) &  (veri['Sex'] == 'female') & yaslibool).sum()

oluyaslierkek = ((veri['Survived'] == 0) &  (veri['Sex'] == 'male') & yaslibool).sum()

#--------------------------------------------------------------------------------------------------

def olucocuk_sayisi(veri, pclass, cocukbool):
    return ((veri['Survived'] == 0) & (veri['Pclass'] == pclass) & cocukbool).sum()

olucocuk1, olucocuk2, olucocuk3 = [olucocuk_sayisi(veri, pclass, cocukbool) for pclass in range(1, 4)]

def olugenc_sayisi(veri, pclass, gencbool):
    return ((veri['Survived'] == 0) & (veri['Pclass'] == pclass) & gencbool).sum()

olugenc1, olugenc2, olugenc3 = [olugenc_sayisi(veri, pclass, gencbool) for pclass in range(1, 4)]

def oluyetiskin_sayisi(veri, pclass, yetiskinbool):
    return ((veri['Survived'] == 0) & (veri['Pclass'] == pclass) & yetiskinbool).sum()

oluyetiskin1, oluyetiskin2, oluyetiskin3 = [oluyetiskin_sayisi(veri, pclass, yetiskinbool) for pclass in range(1, 4)]

def oluyasli_sayisi(veri, pclass, yaslibool):
    return ((veri['Survived'] == 0) & (veri['Pclass'] == pclass) & yaslibool).sum()

oluyasli1, oluyasli2, oluyasli3 = [oluyasli_sayisi(veri, pclass, yaslibool) for pclass in range(1, 4)]


#PLOTS


pyplot.figure()
histogram_fare = pyplot.hist(veri.Fare, bins=50)
pyplot.title('Ücretin Histogram Grafiği')

pyplot.figure()
histogram_age = pyplot.hist(veri.Age, color= 'orange')
pyplot.title('Yaşların Histogram Garfiği')

#qq_fare = qqplot(veri.Fare, line='s')
#qq_age = qqplot(veri.Age, line='q')

pyplot.figure()  
pyplot.bar(['Upper', 'Middle', 'Lower'], [upperDeath, midddleDeath, lowerDeath], color ='purple')
pyplot.title('Sosyal Sınıfa Göre Ölümler')

pyplot.figure()
pyplot.pie([olukadin, oluerkek], labels=['Kadın', 'Erkek'], colors=['pink', 'lightblue'], autopct='%1.1f%%')
pyplot.title('Cinsiyete Göre Ölümler')

pyplot.figure()
pyplot.bar(['Ebeveyni ya da çocuğu ölenler', 'Eşi ya da kardeşi ölenler'], [oluailecocuk, olueskardes], color=['red', 'green'])
pyplot.title('Yakınını Kaybedenler')

pyplot.figure()
pyplot.pie([oluSouthampton, oluCherbourg, oluQueenstown], labels=['Southampton', 'Cherbourg', 'Queenstown'], colors=['red', 'yellow', 'blue'], autopct='%1.1f%%')
pyplot.title('Biniş Limanına Göre Ölümler')

pyplot.figure()  
pyplot.bar(['Çocuk', 'Genç', 'Yetişkin', 'Yaşlı'], [olucocuk, olugenc, oluyetiskin, oluyasli], color='brown')
pyplot.title('Yaş Sınıfına Göre Ölümler')

pyplot.figure()
histogram_ucretaraligi1 = pyplot.hist(ucretaraligi1, bins=25, color='green')
pyplot.title('1. Sınıfın Ücret Aralığı Histogramı')

pyplot.figure()
histogram_ucretaraligi2 = pyplot.hist(ucretaraligi2, bins=25, color='green')
pyplot.title('2. Sınıfın Ücret Aralığı Histogramı')

pyplot.figure()
histogram_ucretaraligi3 = pyplot.hist(ucretaraligi3, bins=25, color='green')
pyplot.title('3. Sınıfın Ücret Aralığı Histogramı')

#-----------------------------------------------------------------------------------------------------

pyplot.figure()
labels = ['1. Sınıf', '2. Sınıf', '3. Sınıf']
Southampton = [Southampton1, Southampton2, Southampton3]
Cherbourg = [Cherbourg1, Cherbourg2, Cherbourg3]
Queenstown = [Queenstown1, Queenstown2, Queenstown3]

x = range(len(labels))
width = 0.2

pyplot.bar(x, Southampton, width=width, label='Southampton', color='red')
pyplot.bar([i + width for i in x], Cherbourg, width=width, label='Cherbourg', color='purple')
pyplot.bar([i + width*2 for i in x], Queenstown, width=width, label='Queenstown', color='orange')
pyplot.title('Biniş Limanına ve Sosyal Sınıfa Göre Ayrım')
pyplot.xticks([i + width for i in x], labels)
pyplot.legend()

#----------------------------------------------------------------------------------------------------

pyplot.figure()
labels = ['Southampton', 'Cherbourg', 'Queenstown']
kadinlar = [Southamptonkadin, Cherbourgkadin, Queenstownkadin]
erkekler = [Southamptonerkek, Cherbourgerkek, Queenstownerkek]

x = range(len(labels))
width = 0.35

pyplot.bar(x, kadinlar, width=width, label='Kadın', color='pink')
pyplot.bar([i + width for i in x], erkekler, width=width, label='Erkek', color='lightblue')
pyplot.title('Biniş Limanına ve Cinsiyete Göre Ayrım')
pyplot.xticks([i + width/2 for i in x], labels)
pyplot.legend()

#-------------------------------------------------------------------------------------------------------

pyplot.figure()
siniflar = range(1, 4)

olukadin_sayilari = [olukadin_sayisi(veri, sinif) for sinif in siniflar]
oluerkek_sayilari = [oluerkek_sayisi(veri, sinif) for sinif in siniflar]

bar_genislik = 0.35
fig, ax = pyplot.subplots()

bar1 = ax.bar([sinif - bar_genislik/2 for sinif in siniflar], olukadin_sayilari, bar_genislik, label='Kadın', color ='pink')
bar2 = ax.bar([sinif + bar_genislik/2 for sinif in siniflar], oluerkek_sayilari, bar_genislik, label='Erkek' , color ='lightblue')

ax.set_title('Cinsiyet ve Sınıfa Göre Ölenlerin Dağılımı')
ax.set_xticks(siniflar)
ax.legend()

#-----------------------------------------------------------------------------------------------------------

pyplot.figure()

gruplar = ['Çocuk', 'Genç', 'Yetişkin', 'Yaşlı']
oluler_kadinlar = [olukizcocuk, olugenckiz, oluyetiskinkadin, oluyaslikadin]
oluler_erkekler = [oluerkekcocuk, olugencerkek, oluyetiskinerkek, oluyaslierkek]

bar_genislik = 0.35
fig, ax = pyplot.subplots()

bar1 = ax.bar([i - bar_genislik/2 for i in range(len(gruplar))], oluler_kadinlar, bar_genislik, label='Kadın' , color ='pink')
bar2 = ax.bar([i + bar_genislik/2 for i in range(len(gruplar))], oluler_erkekler, bar_genislik, label='Erkek', color = 'lightblue')

ax.set_title('Cinsiyet ve Yaş Grubuna Göre Ölenlerin Dağılımı')
ax.set_xticks(range(len(gruplar)))
ax.set_xticklabels(gruplar)
ax.legend()

#------------------------------------------------------------------------------------------------------------

pyplot.figure()

siniflar = range(1, 4)
gruplar = ['Çocuk', 'Genç', 'Yetişkin', 'Yaşlı']

fig, ax = pyplot.subplots()


bar1 = ax.bar([sinif - 0.3 for sinif in siniflar], [olucocuk1, olucocuk2, olucocuk3], width=0.2, label='Çocuk')

bar2 = ax.bar([sinif - 0.1 for sinif in siniflar], [olugenc1, olugenc2, olugenc3], width=0.2, label='Genç')

bar3 = ax.bar([sinif + 0.1 for sinif in siniflar], [oluyetiskin1, oluyetiskin2, oluyetiskin3], width=0.2, label='Yetişkin')

bar4 = ax.bar([sinif + 0.3 for sinif in siniflar], [oluyasli1, oluyasli2, oluyasli3], width=0.2, label='Yaşlı')

ax.set_title('Sınıf ve Yaş Grubuna Göre Ölenlerin Dağılımı')
ax.set_xticks(siniflar)
ax.set_xticklabels(['1. Sınıf', '2. Sınıf', '3. Sınıf'])
ax.legend()

#--------------------------------------------------------------------------------------------------------------------------

# kkare_testi = normaltest(sample)
# print(k2_testi)

# H0 = "Yaş sütununun ortalaması yaş sütunundan alınan bir örneklemin ortalamasından daha büyüktür."

# # 500 tane random değer seçip normal dağılım yapma
# np.random.seed(42)  # Tekrarlanabilirlik için seed ayarı
# population_mean = 29.595959595959595  # Anakütle ortalaması
# population_std = 14.554066015700798  # Anakütle standart sapması
# population = np.random.normal(population_mean, population_std, 500)

# # 500 değer için yaş ortalaması
# population_mean_calculated = np.mean(population)

# # 100 tane random değer seçip normal dağılım yapma
# sample = np.random.choice(population, 100)

# # 100 değer için yaş ortalaması
# sample_mean = np.mean(sample)

# # Z testi yapma
# z_stat, p_value = ztest(sample, value=population_mean)

# # Hipotezi doğru mu değil mi kontrol etme
# alpha = 0.05 # Anlamlılık seviyesi
# if p_value < alpha:
#     hypothesis_result = "H0 reddedildi: Yaş sütununun ortalaması yaş sütunundan alınan bir örneklemin ortalamasından daha küçüktür."
# else:
#     hypothesis_result = "H0 kabul edildi: Yaş sütununun ortalaması yaş sütunundan alınan bir örneklemin ortalamasından daha büyüktür."

# # Sonuçları yazdırma
# print("Anakütle Ortalaması (Hesaplanan):", population_mean_calculated)
# print("Örneklem Ortalaması:", sample_mean)
# print("Z istatistiği:", z_stat)
# print("p-değeri:", p_value)
# print(hypothesis_result)

# pyplot.figure()
# histogram_sample_age = pyplot.hist(sample)

# #-----------------------------------------------------------------------------------------------------------------------------

# # shapirowilk = shapiro(sample2)
# # print(shapirowilk)

# H0 = "Ücret sütununun ortalaması ücret sütunundan alınan bir örneklemin ortalamasından daha büyüktür."

# # 500 tane random değer seçip normal dağılım yapma
# np.random.seed(42)  # Tekrarlanabilirlik için seed ayarı
# population_mean2 =  32.27175847362514 # Anakütle ortalaması
# population_std2 = 49.65227002770733  # Anakütle standart sapması
# population2 = np.random.normal(population_mean2, population_std2, 500)

# # 500 değer için yaş ortalaması
# population_mean_calculated2 = np.mean(population2)

# # 100 tane random değer seçip normal dağılım yapma
# sample2 = np.random.choice(population2, 25)

# # 100 değer için yaş ortalaması
# sample_mean2 = np.mean(sample2)

# # T testi yapma
# t_stat, p_value2 = stats.ttest_1samp(sample2, population_mean2)

# # Hipotezi doğru mu değil mi kontrol etme
# alpha = 0.05 # Anlamlılık seviyesi
# if p_value2 < alpha:
#     hypothesis_result = "H0 reddedildi: Ücret sütununun ortalaması ücret sütunundan alınan bir örneklemin ortalamasından daha küçüktür."
# else:
#     hypothesis_result = "H0 kabul edildi: Ücret sütununun ortalaması ücret sütunundan alınan bir örneklemin ortalamasından daha büyüktür."

# # Sonuçları yazdırma
# print("Anakütle Ortalaması (Hesaplanan):", population_mean_calculated2)
# print("Örneklem Ortalaması:", sample_mean2)
# print("T istatistiği:", t_stat)
# print("p-değeri:", p_value2)
# print(hypothesis_result)

# pyplot.figure()
# histogram_sample_fare = pyplot.hist(sample2, color='orange')




































