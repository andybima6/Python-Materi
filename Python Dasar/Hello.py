# print("hello World")

# print(1+2)

# print("Hello World!")

# print(10)
# print(7.5)

# print('Hello',10)

# print('Hello' * 3) # akan menduplicate string Hello sebanyak 3 kali
# print(10 * 20) # akan mengalikan bilangan tersebut

# print('Hello' + 'World') # akan menggabungkan kedua string tersebut
# print(10 + 20) # akan menambahkan kedua bilangan tersebut

# Untuk memberi komentar kita menggunakan sintaks # untuk single-line comment atau """ untuk multi-line comment.
""" Program ini bertujuan untuk
      menampilkan angka 5 
      dengan menggunakan fungsi print """

# print(5) # Menampilkan angka 5

""" split() -> Digunakan untuk memisahkan string sesuai dengan separator yang kita inginkan dan mengembalikan hasilnya sebagai sebuah list."""
# teks = "halo, nama saya, budi"
# x = teks.split(", ")
# print(x)

""" islower() -> Digunakan untuk mengecek apakah semua element dalam string adalah huruf kecil, akan mengembalikan True jika iya, dan False jika tidak"""
# a = "HaLo"
# b = "halo"
# print(a.islower())
# print(b.islower())
"""output"""
False
True

""" count()-> Digunakan untuk menghitung berapa kali sebuah value muncul dalam sebuah string"""
# teks = "Halo semuanya, disini saya bersama dengan budi semuanya,semuanya"
# x = teks.count("semuanya")
# print(x)

# wow = (4//5)
# print(wow)

""" int() -> Digunakan untuk mengubah nilai yang ditentukan menjadi bilangan bulat. Contohnya:"""
# x = int("12")
# y = int(12.5)
# print(x)
# print(y)
"""output"""
# 12
# 12

""" pow() -> Digunakan untuk mendapatkan nilai pangkat dari suatu bilangan. Contohnya:"""
# x = pow(3, 3) # 3 pangkat 3
# y = pow(3, -3) # 3 pangkat -3
# print(x)
# print(y)

"""output"""
# 27
# 0.015625

"""str() -> Digunakan untuk mengubah sebuah objek menjadi string. Contohnya:"""
# x = str(12)
# y = str(12.5)
# print(type(x))
# print(type(y))
"""output"""
# <class 'str'>
# <class 'str'>


""" input Function"""
# berat = float(input("Masukkan berat anda dalam kg: "))
# tinggi = float(input("Masukkan tinggi anda dalam m: "))

# bmi = (berat/(tinggi ** 2))
# print("BMI Anda =",bmi)

""" Comparison Operators  hubungan ukuran dua operan yang sebanding, seperti angka dan string, dalam istilah seperti lebih besar dari atau kurang dari.
 Hasil dari operasi ini dikembalikan sebagai Benar atau Salah. Tipe data yang memiliki nilai True atau False disebut Boolean."""
# print('Result of 10 > 5: ', 10 > 5)
# print('Result of 5 < 1: ', 5 < 1)
# print('Result of 5 == 5', 5 == 5)
# print('Result of 5 != 5', 5 != 5)
# print("Result of 'a' > 'b': ", 'a' > 'b')

""" Comparison Operator Is & In
 Operator is memeriksa apakah kedua objek itu sama. Perbedaannya dengan operator == adalah operator == memeriksa nilai dari kedua objek."""
a = 1
b = 1.0
print(a == b)
print(a is b)
""" Baris ketiga menggunakan operator == untuk memeriksa apakah kedua nilai tersebut sama. Karena kedua nilai sama, sehingga hasilnya adalah True.
 Baris keempat memeriksa apakah kedua objek itu sama. Karena a adalah bilangan integer sedangkan b adalah bilangan float, kedua objek tidak sama. Dengan kata lain, mereka disimpan dalam memori yang berbeda dan oleh karena itu, hasilnya adalah False."""

"""Comparison Operator In
Operator in memeriksa untuk melihat apakah kedua string cocok sebagian. Operator in sering digunakan untuk menentukan apakah ada karakter yang cocok di dalam string, apabila terdapat kecocokan maka akan mengembalikan nilai True dan jika tidak akan mengembalikan nilai False."""
# print('aaa' in 'aaa-bbb-ccc')
# print('bbb' in 'aaa-bbb-ccc')
# print('ddd' in 'aaa-bbb-ccc')
"""output"""
# True
# True
# False

"""pass statement dan komentar adalah intrepreter tidak mengeksekusi kode yang merupakan komentar"""
# num = 2
# if num % 2 == 0:
#     print('Nomor genap')
# if num % 3 == 0:
#     pass

"""If-Else Statement"""
"""Sebagai contoh untuk if-else statement"""
# hour = 10
# if hour < 12:
#       print('it is moring.')
# else:
#       print('it is afternoon')

"""2 (dua) if statement"""
# hour = 12
# if hour < 13:
#       print('it is moring.')  
# if hour >= 12:
#       print('it is afternoon')

"""Nested Conditional Statement"""
"""If dan else statement juga dapat disusun sebagai nested if-else statement """
# num = -100
# if num < 0:
#     print(num, 'adalah bilangan negatif. ')
# else:
#     print(num, 'adalah bukan bilangan negatif ')
#     if num % 2 == 0:
#         print(num, 'adalah bilangan genap')
#     else:
#         print(num, 'adalah bilangan ganjil')

# """For Loop"""
# for i in range(5):
#     print('Welcome to everyone!!')

"""While Loop Syntax"""
# i = 0 # initial value
# while i < 5: # kode didalam block akan dieksekusi selama kondisi True
#     print('Wlecome to everyone!!')
#     i += 1

"""Inifinite loop"""
# i = 10
# while i > 4:
#      if i == 5:
#           i = 10
#      i -= 1
#      print(i)

"""Break"""
st = 'Programming'
# fungsi akan di eksekusi selama huruf adalah konsonan
# for wow in st:
#     if wow in ['a','e','i','o','u']:
#         break # stop loop jika menemukan huruf vokal
#     print(wow)
# print('The end')
#output
"""
P
r
The end"""


"""Continue"""
st = 'Programming'
# fungsi akan di eksekusi selama huruf adalah konsonan
# for ch in st:
#     if ch in ['a','e','i','o','u']:
#         continue # skip eksekusi kode dibawah jika huruf vokal
#     print(ch)
# print('The end')
#output
"""
P
r
g
r
m
m
n
g
The end"""


# for i in range(2,10):
#     for j in range(1,10):
#         print('{}x{} = {:2d}, '.format(i, j, i*j), end = '')
#     print()

"""Mutable"""
"""list merupakan tipe data mutable sehingga kita dapat merubah variabel yang merupakan sebuah list, hal ini dapat dilakukan salah satunya menggunakan fungsi append():"""
# a = ['apple','banana','orange']
# print(id(a))

# a.append('grapes')
# print(id(a))
# print(a)

# output:
# 140372445629448
# 140372445629448
# ['apple','banana','orange','grapes']

"""Immutable
string merupakan tipe data immutable dan value tipe data string tidak dapat kita ubah selain dengan membuat objek baru."""
# Contoh 1
# message = "Welcome to Skilvul"
# message[0] = 'p'
# print(message)

# output:
# message[0] = 'p'
# TypeError: 'str' object does not support item assignment

# Contoh 2
# e = 'Halo, semua!'
# print(id(e))
# e = 'Halo, Apa kabar?'
# print(id(e))
# print(e)
# Output:
# 140595675113648
# 140595675113776
# 'Halo, Apa kabar?'

"""List - Declaration"""
# score_list = [87,84,95,67,88,94,63]
# print(score_list[0],score_list[5])

"""List Declaration"""
# Contoh 1
# buah = ['gedang','apel','jeruk,durian']
# print(buah)
# campur_list = [100,200,'apel',400]
# print(campur_list)

# contoh 2
list4 = list(range(1,10))
print(list4)

"""List - Indexing"""
"""Gunakan fungsi len() untuk menghitung jumlah item dalam list, yang dengan kata lain panjang dari sebuah list."""
n_list = [11,22,33,44,55,66]
print(n_list)
print(len(n_list))
#output
[11,22,33,44,55,66]
6

"""Contoh kode untuk mengakses sebuah list:"""
n_list = [11,22,33,44,55,66]
print(n_list[0]) # indeks item pertama dari list adalah 0
print(n_list[1]) # index item kedua dari list adalah 1
#output
11
22

"""List - Addition and Deletion"""
person1 = ['David Doe', 20,1,180.0,100.0]
person2 = ['John Smith', 25,1,170.0,70.0]

person_list = person1 + person2
print(person_list)

#output
['David Doe', 20,1,180.0,100.0,'John Smith', 25,1,170.0,70.0]

"""append()  dimana fungsi ini adalah metode untuk menambahkan item baru ke akhir sebuah list yang sudah ada."""
a_list = ['a','b','c','d','e']
a_list.append('f') # menambahkan karakter f
print(a_list)
#output
['a','b','c','d','e','f']

"""extend()"""
"""digunakan untuk menambahkan list atau item di belakang sebuah list."""
list1 = ['a','b','c']
list2 = [1,2,3]
list1.extend(list2)
print(list1)
list1.extend('d')
print(list1)
#output
['a','b','c',1,2,3]
['a','b','c',1,2,3,'d']

"""Deletion"""
"""dapat menghapus item dalam indeks yang diinginkan."""
n_list = [11,22,33,44,55,66]
print(n_list) # print seluruh items

del n_list[3] # delete 44
print(n_list)

#output
[11,22,33,44,55,66]
[11,22,33,55,66]

"""pop()"""
"""pop() juga mengembalikan value index yang dihapus. Apabila kita tidak mengisi index dalam metode pop() maka elemen terakhir yang akan dihilangkan dari list."""
n_list = [50,10,20,30]
print(n_list) # print seluruh items

n = n_list.pop()
print('n = ',n)
print('n_list =',n_list)

#output
[50,10,20,30]
n = 30
n_list = [50,10,20]

"""remove()"""
"""menghapus nilai tertentu dari list berdasarkan nilai itu sendiri."""
n_list = [11,22,33,44,55,66]
print(n_list)

n_list.remove(44)
print(n_list)

#output
[11,22,33,44,55,66]
[11,22,33,55,66]

"""List - Slicing"""
# Slicing item dari awal hingga akhir(akhir -1) tidak termasuk dari indekx akhir
a_list = [10,20,30,40,50,60,70,80]
a_list[1:5]
# Slicing item dari awal hingga akhir list.slicing bagian akhir dari list
a_list [1:]
# Slicing item dari awal hingga akhir -1 indeks
a_list [:5]
# Slicing keseluruhan List
a_list [:]
# Slicing dua item dari akhir
a_list [-2:]
# slicing seluruh item dari awal kecuali dua item terakhir
a_list [:-2]
# import semua item teteapi dalam urutan terbalik
a_list [::-1]
# slicing dua item pertama dalam urutan terbalik
a_list [1::-1]

"""Tuple-basics"""
# Contoh 1
colors = ("red","hijau","biru")
print(colors)


"""Sequence Data Types - Iterator"""
# List
list1 = [11,22,33,44] * 2
print(list1)
#output
[11,22,33,44,11,22,33,44]

# Tuples
tup1 = (1,2,3)
print(tup1 * 2)
#output
(1,2,3,1,2,3)

# String
str2 = 'hello'
print(str2 * 3)
#output
# hellohellohello

# Range
"""kita juga tidak bisa menggunakan operator * untuk tipe data range dan kita bisa menggunakan operator * untuk tipe data range dengan mengubah tipe data tersebut ke dalam list atau tuple terlebih dahulu."""
# contoh 1
ran = list(range(5)) * 3
print(ran)
#output
[0,1,2,3,4,0,1,2,3,4,0,1,2,3,4]

# Contoh 2
ran = tuple(range(5)) * 3
print(ran)
#output
(0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)

"""Sequence Data Types - Count Method"""
# list1
list1 = [11,11,11,22,33,44] 
print(list1.count(11)) # mencari total angka 11 dalam list
#output
3

# Tuple
tup1 = (11,11,11,22,33,44) 
print(tup1.count(11)) # mencari total angka 11 dalam tuple
#output
3

# String
"""Kita juga bisa menghitung jumlah sebuah karakter didalam sebuah string"""
str1 = 'hello world'
print(str1.count('l')) # mencari total huruf l dalam string
#output
3

# Contoh penggunaan dan aplikasi metode count() dalam kode:
"""Pada sisi lain, ketika menggunakan metode count() untuk melihat berapa banyak angka 2 dalam variabel yang dijalankan, itu akan mencetak 1 karena hanya ada satu angka 2 dari range 0 hingga 5."""
ran = range(0,8,1)
print(len(ran))
print(ran.count(2))
#output
5
1

"""Sequence Data Types - Linking"""
# lists
list1 = [11,22,33,44]
list2 = [55,66]
print(list1)
print(list1 + list2)
#output
[11,22,33,44]
[11,22,33,44,55,66]

# tuples
tup1 = (1,2,3)
tup2 = (4,5,6)
print(tup1 + tup2)
#output
(1,2,3,4,5,6)

# strings
str1 = 'hello'
str2 = 'world'
print(str1 + str2)
#output
# hello world

# range:
"""seperti yang sudah dijelaskan sebelumnya, kita tidak bisa menggunakan operator + untuk tipe data range"""
print(list(range(10)) + list(range(10,20)))
print(tuple(range(10)) + tuple(range(10,20)))

#output
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)

"""Sequence Data Types - Operators"""
# dalam list
list1 = [10,20,30,40]
print(10 in list1)
print(10 not in list1)
#output
True
False

# dalam tuples
tup = (1,2,3,4)
print(3 in tup)
#output
True

# dalam strings
print('a' in 'abcd')
#output
True

# dalam range
print(11 in range(10))
#output
False

"""Dictionary - Key Value Pair"""
person = {'Name' : 'andy','age' : 18,'weight' : 68}
print(person['Name'])
print(person['age'])
print(person['weight'])

"""Dictionary - Adding, Modifying, Delete Values"""
# Adding Items
person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
person['Job'] = 'Data Scientist' # Key baru: masukkan nilai dari key tersebut
print(person)
#output
{'Name': 'David Doe', 'Age': 26, 'Weight' : 82, 'Job': 'Data Scientist'}

# Modifying Items
person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
person['Age'] = 27 # Ubah value dari key yang sudah ada 'Age' 
print(person)
#output
{'Name': 'David Doe', 'Age': 27, 'Weight' : 82}

# Deleting Items
# person = {'Name': 'David Doe', 'Age': 26, 'Weight' : 82}
# del person['Age'] # Delete value dari key yang sudah ada 'Age' 
# print(person)
# #output
# {'Name': 'David Doe','Weight' : 82}

"""Dictionary - Function and Operators"""
# len() function dan in operator
# a = {'abc':100,'def':200}
# print(len(a))
# print('Job' in a)
# #output
# 2

"""Creating 2D Lists"""
# list_array = [[1,3,5],[7,9,11],[13,15,17]]
# for i in list_array :
#       for j in i:
#             print(j,end = ' ')
#       print()

# list_array = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# print(list_array[1])

# list_array = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# print(list_array[1][2])

# """Double Loop 2D Lists"""
# # 2D Lists dengan Single For Loop
# list_array = [[1,2,3],[4,5,6],[7,8,9]]
# for item in list_array:
#   print('item =',item)
# #output
# item = [1,2,3]
# item = [4,5,6]
# item = [7,8,9]

# 2D Lists dengan Double For Loop
list_array = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
for i  in list_array:
      for j in i:
            print(j,end = ' ')
      print()

"""Dictionary - Get Method"""
# Fungsi get() dapat kita gunakan untuk mendapatkan value dari key yang spesifik.
# Mengakses Item Dalam Dictionary
# contoh 1
dic = {'a':10,'b':20,'c':30,'d':40}
a = dic.get('b') # fungsi get untuk mendapatkan value dari key a
print(a)
#output
20

# Contoh 2
dic = {'a':10,'b':20,'c':30,'d':40}
b = dic.get('z',45) # tidak terdapat key z dalam dictionary dic sehingga dikembalikan value 0
print(b)
#output
45

"""menghapus item dalam Dictionary"""
# Contoh 1
dic = {'a':10,'b':20,'c':30,'d':40} # bentuk tipedata Tuple
print(dic.pop('c')) # tidak terdapat key z dalam dictionary dic sehingga dikembalikan value 0
print(dic)

# Contoh 2
dic2 = {'a':10,'b':20,'c':30,'d':40,'e': 50}
print(dic2.popitem()) 

# Contoh 3
dic3 = {'a':10,'b':20,'c':30,'d':40,'e': 50}
dic3.clear()
print(dic3)

"""Merubah Item Dalam Dictionary"""
dic4 = {'a':10,'b':20,'c':30,'d':40,'e': 50}
dic4.update(a=90,f = 85)
print(dic4)

"""Membuat Replika Dari Dictionary"""
# Contoh 1
# A
x = {'a' : 0,'b' : 0,'c' : 0,'d' : 0,}
y = x.copy()
print(x is y)
print (x == y)

# B
x = {'a': {'python':'2.7'},'b':{'python':'3.6'}}
y = x.copy()
y['a']['python'] = '2.7.15' # merubah value dari key a - python
print(x)
print(y)

#output
# {'a': {'python':'2.7.15'},'b':{'python':'3.6'}}
# {'a': {'python':'2.7.15'},'b':{'python':'3.6'}}

# Contoh 2
x = {'a':{'python':'2.7'},'b':{'python':'3.6'},'c':{'wow'}}
import copy # memanggil copy modul
y = copy.deepcopy(x) #deep copy menggunakan deepcopy function dari copy module

y['a']['python'] = '2.7.15' #merubah value dari keyy a - python
print(x)
print(y)
#output
# {'a': {'python':'2.7'},'b':{'python':'3.6'}}
# {'a': {'python':'2.7.15'},'b':{'python':'3.6'}}

"""Dictionary - Items, Keys, Values"""
# Contoh 1
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.keys()) # mengakses seluruh key yang ada dalam dictionary
#output
# dict_keys(['a','b','c','d'])

# Contoh 2
"""selain itu kita juga dapat menampilkan seluruh value yang ada di dalam sebuah dictionary dengan fungsi values()"""
dic#dictionary = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.values()) # mengakses seluruh values yang ada dalam dictionary
#output
# dict_values([10,20,30,40])

# Contoh 3
"""Jika fungsi items() digunakan menggunakan for loop maka akan mengembalikan sebuah tipe data tuple yang berisi (key,value) """
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.items()) # mengakses seluruh items yang ada dalam dictionary
#output
# dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])

# kita juga bisa menggunakan *for loop* untuk mengakses seluruh *item* satu per satu
for wow,anjay, in dic.items():
    print(wow,':',anjay)
#output
a : 10
b : 20
c : 30
d : 40

"""Dictionary - Default Dict"""
# . Fungsi defaultdict() ini akan membantu kita agar mencegah KeyError dan akan mengembalikan default value

from collections import defaultdict # import default dict method dari collections module
keys = ('a','b','c','d')
y = dict.fromkeys(keys,100)
y = defaultdict(int) # set default value sebagai integer

print(y['z']) # mengakses key z dari dictionary y

#output
0

"""Dictionary - Double Dictionary"""
terrestrial_planet ={
'Mercury': {
'mean_radius': 2439.7,
'mass': 3.3022E+23,
'orbital_period': 87.969
},
'Venus':{
'mean_radius': 6051.8,
'mass': 4.8676E+24,
'orbital_period': 224.70069,
},
'Earth':{
'mean radius': 6371.0,
'mass': 5.97219E+24,
'orbital_period': 365.25641,
},
'Mars':{
'mean_radius': 3389.5,
'mass': 6.4185E+23,
'orbital_period': 686.9600,
}
}
print (terrestrial_planet['Venus']['mean_radius'])

"""Dictionary - From Keys Method"""
keys = ['a','b','c','d']
x = dict.fromkeys(keys)
print(x)
#output
{'a':None , 'b': None, 'c': None, 'd': None}

# Selain membuat dictionary dari tipe data list, kita juga dapat membuat dictionary dari tipe data tuple dengan cara dan hasil yang sama seperti kode di bawah ini:
keys = ('a','b','c','d')
x = dict.fromkeys(keys)
print(x)
#output
{'a':None , 'b': None, 'c': None, 'd': None}

# Berikut contoh penggunaan dari default value dengan fungsi fromkeys():
keys = ('a','b','c','d')
y = dict.fromkeys(keys,100)
print(y)
#output
{'a':100 , 'b': 100, 'c': 100, 'd': 100}

"""Set - Definition and Declaration"""
# Berikut contoh penerapannya dalam kode untuk membuat set dari list serta membuat set dari tuple :
# Contoh 1
days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' , 'Sun' ] # list
days_set = set(days_list) # membuat set dari list
print(days_set)
#output
{'Sun', 'Sat', 'Wed', 'Fri', 'Thu', 'Mon', 'Tue'}

# Contoh 2
fruits_tuple = ('apple','orange','water melon')
fruits_set = set(fruits_tuple) # membuat set dari tuple
print(fruits_set)
#output
{'water melon', 'apple', 'orange'}

"""Set - Check Value in Sets"""
# Untuk mengakses value yang ada di dalam set, kita bisa menggunakan for loop untuk melakukan *iterasi *untuk mendapatkan item yang ada di dalam set
numbers = {2,1,3}
for x in numbers:
  print(x)
#output
2
1
3

# kita juga bisa melakukan validasi untuk mengecek apakah sebuah item ada di dalam sebuah set dengan menggunakan operator in yang kita juga bisa pakai dalam tipe data list.
numbers = {2,3,1,3}
if 3 in numbers:
  print("1 terdapat dalam set")
#output
# 1 terdapat dalam set

# Selain itu kita juga bisa menambahkan serta menghapus value yang ada di dalam set menggunakan fungsi add() serta remove(): Kita bisa menambahkan item baru menggunakan fungsi add():
numbers = {1,2,3}
numbers.add(4)
print(numbers)
#output
{1, 2, 3, 4}

#  Dan kita bisa menghapus item dalam set menggunakan fungsi remove():
numbers = {1,2,3,4}
numbers.remove(4)
print(numbers)
#output
{1, 2, 3}

"""Set - Union and Intersections"""
