# -*- coding: utf-8 -*-
"""Spark.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vpt9os-dSSEOVjJZvBY3btkvd8aUnk5y
"""

!pip install pyspark

import pyspark 
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("Colab")
#code 'sc = SparkContext()' dakhel colab faghat dar run aval in nemooneh bayad sakhteh shavad va baed az an dar test haye baed comment shavad
#sc = SparkContext()

#daryaft vorudi az tarigh barghozari file dakhel google colab va sepas moarefi dar inja
input = sc.textFile("almizan(utf-8).txt")
#input2 = input.decode('utf-8') #bejay taghir incode dar inja besoorat local file ra ba coding 'utf-8' save kardam ta dar arabi be moshkel nakhorad

#tamam vaj haye farsi va arabi amade dar matn (az khoruji test haye map reduce rooye dataset mojud bedast amadeh)
vajha : list = ['ا','ش', 'ح','م','و','ذ','ع','أ','ن', 'خ', 'ك','ي','ث','آ','ء','ک', 'ب','پ', 'ق', 'ت','س', 'ل', 'ف','ه', 'ج', 'ط','ض', 'إ','ص','ز', 'ر','ظ', 'غ','د','گ']



#joda sazi kalamat ba har space ba tabe flatmap ke agar dadeh vorudi struct avaliyeh ee dashteh bashad an hara nadide migirad va khoruji list
#mosattah ast keh sakhtar ghabli ra az dast dadeh
words = input.flatMap(lambda x: x.split(" "))
#words2 = words.collect().decode('utf-8')  #be jay in kar besoorat local encode txt ra be utf-8 tagheer dadam
#joft = words.map(lambda x: (x[0],1))


#dar in bakhsh dar haghighat mikhahim kalamati ke gheir horuf hastand az punctuaition ha ta adad va .. ra hazf konim
#halat dovom yani 'letter[0] in vajha' dorost kar nemikonad cherake error string out of range midahad keh ghaedatan nabayad error midasht
#vali string.isalpha() baray zaban arabi ham kar rah andaz ast
kalamat = words.filter(lambda letter: letter.isalpha())
#letters = words.filter(lambda letter: letter[0] in vajha)


#agar englisi bood 'word[0].lower' mineveshtim ta hamantor ke ghofteh shod horoof bozorg va koochack tamayoz ijad nakonad
#dar haghighat marhale asli map ke har vaj ebtedaee ro be yek 1 map mikonad
vajha2 = kalamat.map(lambda word: (word[0],1))



#dar in marhale ke reduce ast keh kol joft haye pass shode az bala ra survey mikonad va bar asas barabari key ; value hara jame mikonad va
#be onvan khoruji yek joft (key , value) reduce shode baz migardanad
counts = vajha2.reduceByKey(lambda value, x: value + x)


print(words.count())
print(kalamat.count())
print("khoruji az tedad vaj hay avaliyeh ghabl az reduce : ")
print(vajha2.collect())
print("khoruji az tedad vaj hay avaliyeh baed az reduce : ")
print(counts.collect())

#khoriji gereftan az tedad ha besyar soraat koruji ro payin miyareh va colab hang mikoneh faleza be hamoon 'counts.collect()' basandeh kardim.
#Counts2 = counts.countByValue()
#for vaj in Counts2.items():
 #       print("tedad tekrar vaj  " + str(vaj[0][0]) + "  barabar ast ba :"  + str(vaj[0][1]))





#tozih : teke code bala be rahati az tarigh yek halghe bakhshe mapreduce an ghabel pyadeh sazi bood amma hamantor ke farmodid ta had momken az
#halghe bayad ejtenab sjvad va az tavabe lambda va mp va filter va ... estefadeh shavad