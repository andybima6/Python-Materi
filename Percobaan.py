"""Function - Call a Function"""
def anjay():
    print('andy ganteng sekali didunia')

anjay()

"""Function - Arguments and Parameters"""
def yoi_wow(start,end):#parameter
    s = 0
    for i in range(start,end+1):# argument
        s += 1
    return s

"""Function - Arbitrary Arguments"""
# Arbitrary Argument digunakan ketika Jumlah argumen belum bisa atau tidak ditentukan
def greet(*names):
    for name1 in names:
        print('hello',name1,'!')

greet('A','B','C')
greet('Andy','Bagus')

"""Function - Default Parameters"""
# Contoh 1
def andy_star(n = 2):
    for _ in range(n):
        print('ppppppppppp')
andy_star()

# Contoh 2
def andy_star(n = 2):
    for _ in range(n):
        print('sssssssssss')
andy_star(4)

# Contoh 3
# Default Parameters in Multiple Parameters
"""def div(a = 2,b):
    return a/b"""
# Output
# SysntaxError

"""Function - Keyword Parameter"""
# Contoh 1
def get_root(a,b,c):
  r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  return r1,r2

result1, result2 = get_root(a=1,c=-8,b=2)
print('Hasil akar-akarnya adalah', result1, 'atau', result2)

# Contoh 2
def test(a = 2, b = 3):
    print(a,b)

test(4)

"""Function - Return Statement"""
def get_sum(a,b): # fungsi yang akan mengembalikan total dari 2 angka
  result = a + b
  return result # mengembalikan hasil penjumlahan menggunakan return

n1 = get_sum(10,20)
print("hasil penjumlahan dari 10 dan 20 adalah",n1)

"""Apa itu Recursive Function"""
# Contoh 1
def factorial(n): # membuat function untuk factorial
  if n <= 1: # untuk melakukan termination/pemutusan recursive function
    return 1
  else:
    return n * factorial(n-1) # implementasi dari recursive function 

n = 5
print(f"factorial dari {n} adalah {factorial(n)}")

#output
# factorial dari 5 adalah 120

# Contoh 2
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

str1 = "GaG"
if is_palindrome(str1):
    print("Palindrome")
else:
    print("Not a palindrome")
#Hasilnya adalah Not a palindrome.
#Fungsi is_palindrome() memeriksa apakah string yang dimasukkan merupakan palindrome atau bukan. Palindrome adalah sebuah kata yang dibaca sama dari depan atau dari belakang.
#Fungsi is_palindrome() memeriksa panjang string. Jika panjangnya kurang dari atau sama dengan 1, maka akan mereturn True. Jika panjang lebih dari 1, akan memeriksa karakter pertama dan terakhir. Jika sama, akan memanggil fungsi is_palindrome() lagi dengan parameter string tanpa karakter pertama dan terakhir. Proses ini akan terus berulang sampai panjang stringnya kurang dari atau sama dengan 1.
#Pada contoh ini, string yang dimasukkan adalah "Hello", sehingga panjangnya adalah 5. Karena panjangnya lebih dari 1, maka akan memeriksa karakter pertama dan terakhir. Karakter pertama adalah "H" dan terakhir adalah "o". Karena karakter pertama dan terakhir berbeda, maka akan mereturn False. Akhirnya, hasilnya adalah Not a palindrome.

"""Lambda - Expression and Syntax"""
# Dengan def keyword
def add(x,y):
    return x + y
print("total dari 100 dan 200 adalah:",add(100,200))
#output
# total dari 100 dan 200 adalah: 300
    
# Dengan lambda function
add = lambda x, y : x + y
print("total dari 100 dan 200 adalah:",add(100,200))
#output
# total dari 100 dan 200 adalah: 300

"""Lambda - Filter"""
list_umur = [20,25,30,85,19,17,15]# list
print("Umur Yang Dewasa : ")
for a in filter(lambda x : x >= 19,list_umur): # tuple
     print(a,end = ' ')

# Contoh dari iterable object adalah list atau tuple.

"""Lambda - Map"""
a = [1,2,3,4,5,6,7]
a_kuadrat = list(map(lambda x: x **2, a))
print(a_kuadrat)
#output
[1, 4, 9, 16, 25, 36, 49]

"""Lambda - Reduce"""
# Mengembalikan sebuah nilai dengan menjalankan operasi dari function yang diberikan terhadap iterable items
# Contoh 1
from functools import reduce
# Returns the sum of two elements
def sumTwo(a,b):
    return a-b
result = reduce(sumTwo, [1, 2, 3, 4,12])
print(result)

# Contoh 2
from functools import reduce # mengimport fungsi reduce

a = [1,2,3]
n = reduce(lambda x,b : x + b, a)
print(n)

# Contoh 3
from functools import reduce 

a = [1,2,3,4]
n = reduce(lambda x,y : x + (x*y), a)
print(n)
# Output
60
# 1. Ambil angka pertama dari list a, yaitu 1.
# 2. Selanjutnya, lakukan perhitungan 1 + (1*2) = 3.
# 3. Ambil angka ketiga dari list a, yaitu 3.
# 4. Selanjutnya, lakukan perhitungan 3 + (3*3) = 12.
# 5. Ambil angka keempat dari list a, yaitu 4.
# 6. Selanjutnya, lakukan perhitungan 12 + (12*4) = 60.

"""Nested Function Concept"""
# Contoh 1
def decorate(style = 'italic'):
  def italic(s):
    return '<i>' + s + '<i>'
  def bold(s):
    return '<b>' + s + '<b>'
  if style == 'italic':
    return italic
  else:
    return bold

dec = decorate('italic')
print(dec('hello'))
dec2 = decorate('bold')
print(dec2('hello'))

#output
# <i>hello<i>
# <b>hello<b>

# COntoh 2
def another_func():
  print('hello')
  
def outer_func():
  return another_func()
  
outer_func()
#output
# hello

"""Non-local Variable - Local Variable vs Global Variable"""
# Local
def print_counter():
  counter = 200
  print('counter didalam fungsi =',counter) # nilai counter didalam fungsi

# Global    
counter2 = 100
print_counter()
print('counter diluar fungsi = ',counter2) # nilai counter diluar fungsi

"""Closure - Concept"""
def closure_calc():
  a = 2
  def mult(x):
    return a * x
  return mult
  
c = closure_calc()
print(c(1),c(2),c(3))

"""Class - Instances vs Class"""

# Class : Sebuah konsep abstrak yang menunjukkan satu set atribut dan tindakan yang digunakan dalam sebuah program.
# Instances : Sebuah objek individu yang dibuat dari class. Instances memiliki nilai atribut tertentu yang spesifik.

"""Class - Declaring and Self Parameters"""
class anjing: # membuat class Cat
  def guuukk(wow): # fungsi meow didalam class Cat
   print('gukgakguk') 

nobi = anjing() # membuat sebuah instance dari Cat
nobi.guuukk() # setelah membuat object dari Cat, kita bisa memanggil method meow 

#output
# guukgakguk

"""Class - Constructor __init__ Method"""
class Cat:
  def __init__(self,name,color): # menginisialisasi instance dengan constructor
    self.name = name
    self.color = color

nobi= Cat('nobi','black') # membuat instance dari kelas Cat dengan nama nabi dan warna hitam
nero = Cat('nero','white')
#Nobi,Neri Termasuk dalam Self
print(nobi.name)
print(nobi.color)
print(nero.name)
print(nero.color)

#output
# nobi
# black
# nero
# white

"""Class - Instance vs Class Variables"""
# Intance Variable
class Circle:
  def __init__(self,name,radius,PI):
    self.__name = name # instance variable
    self.__radius = radius # instance variable
    self.__PI = PI
  
  # menghitung area sebuah lingkaran dengan pi * r kuadrat
  def area(self):
    return self.__PI * self.__radius ** 2

c1 = Circle("C1",4,3.14)
print("Area dari c1:",c1.area())
c2 = Circle("C2",6,3.141)
print("Area dari c2:",c2.area())
c3 = Circle("C3",6,3.1415)
print("Area dari c3:",c3.area())
#output
# Area dari c1: 50.24
# Area dari c2: 113.076
# Area dari c3: 113.09400000000001

# Class Variables
class Circle:
  PI = 3.1415
  def __init__(self,name,radius):
    self.__name = name # instance variable
    self.__radius = radius # instance variable
  
  # menghitung area sebuah lingkaran dengan pi * r kuadrat
  # method dari class Circle dan instance akan mengambil value PI dari class variable melalui Circle.PI
  def area(self):
    return Circle.PI * self.__radius ** 2

c1 = Circle("C1",4)
print("Area dari c1:",c1.area())
c2 = Circle("C2",6,)
print("Area dari c2:",c2.area())
c3 = Circle("C3",5)
print("Area dari c3:",c3.area())

#output
# Area dari c1: 50.264
# Area dari c2: 113.09400000000001
# Area dari c3: 78.53750000000001

"""Class - Inheritence"""
class Person: # Parent class
  nama = 'test'

class Employee(Person): # child class
  gaji = 1000
  
person1 = Person()
employee1 = Employee()

print('nama dari person', person1.nama)
print('nama dari employee', employee1.nama)
print('gaji dari employee',employee1.gaji)
# print('gaji dari person',person1.gaji)

#output
# nama dari person test
# nama dari employee test
# gaji dari employee 1000
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Person' object has no attribute 'gaji'

"""Class - Polymorphism""" 
# Contoh 1
class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()
# output
# There are different types of birds
# Most of the birds can fly but some cannot
# There are different types of bird
# Parrots can fly
# There are many types of birds
# Penguins do not fly

# Contoh 2
# Kita dapat membuat loop yang berulang melalui objek tuple seperti berikut ini:
class Hewan():
    def suara(self):
      print("Suara hewan")

class Kucing(): 
    def suara(self):
       print("Meow")

    def harapan_hidup(self): 
      print("Harapan hidup kucing adalah 10 tahun.") 
   
    def warna_tubuh(self): 
      print("Warna tubuh kucing pada umumnya adalah kuning") 
   
class Anjing(): 
    def suara(self):
      print("Woof")

    def harapan_hidup(self): 
      print("Harapan hidup anjing adalah 15 tahun.") 
   
    def warna_tubuh(self): 
      print("Warna tubuh anjing pada umumnya adalah hitam") 
   
obj1 = Kucing() 
obj2 = Anjing() 
for type in (obj1, obj2): # creating a loop to iterate through the obj1, obj2
    type.harapan_hidup() 
    type.warna_tubuh() 

  
# output
# Harapan hidup kucing adalah 10 tahun.
# Warna tubuh kucing pada umumnya adalah kuning
# Harapan hidup anjing adalah 15 tahun.
# Warna tubuh anjing pada umumnya adalah hitam

"""Class - Encapsulation"""
# Single Underscore
class Orang:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age
 
    def tampilkan(self):
        print(self.name)
        print(self._age)
 
orang_obj = Orang('Budi', 30)

#mengakses melalui metode
orang_obj.tampilkan()

#mengakses langsung variable
print(orang_obj.name)
print(orang_obj._age)

# Double Underscore
"""Jika kita ingin menjadikan anggota class yaitu method dan attribute menjadi private, maka kita harus mengawalinya 
dengan garis bawah ganda atau double underscore __."""
# Contoh 2
""""class Orang:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
 
    def tampilkan(self):
        print(self.name)
        print(self.__age)
 
orang_obj = Orang('Budi', 30)

#mengakses melalui metode
orang_obj.tampilkan()

#mengakses langsung variable
print(orang_obj.name)
print(orang_obj.__age)

#output
Budi
30
Budi
Traceback (most recent call last):
  File "test.py", line 17, in <module>
    print(orang_obj.__age)
AttributeError: 'Orang' object has no attribute '__age'
"""


# Contoh 2
# Untuk mengubah data, kita juga perlu membuat setter karena tidak bisa mengubah data secara langsung.
class Orang:
  def __init__(self, name, age=0):
    self.name = name
    self.__age = age

  def setAge(self, age):
    self.__age = age
 
  def tampilkan(self):
    print(self.name)
    print(self.__age)
    print("----------")
 
orang_obj1 = Orang('Budi', 97)

#mengakses melalui metode
orang_obj1.tampilkan()

#mengubah data tanpa setter tidak memungkinkan
orang_obj1.__age = 50
orang_obj1.tampilkan()

#mengubah data harus memalui setter
orang_obj1.setAge(27)
orang_obj1.tampilkan()

#output
# Budi
# 97
# ----------
# Budi
# 97
# ----------
# Budi
# 27  
# ----------

"""Class - Abstraction"""
from abc import ABC

class MobilMewah(ABC):  
    def harga(self):   
        pass  

class Tesla(MobilMewah):   
    def harga(self):   
        print("Harga mobil ini 2 Milliar Rupiah")   
class Lexus(MobilMewah):   
    def harga(self):   
        print("Harga mobil ini 3 Milliar Rupiah")  
class Ferrari(MobilMewah):   
    def harga(self):   
        print("Harga mobil ini 10 Milliar Rupiah")  

tesla_obj = Tesla()
tesla_obj.harga()

ferrari_obj = Ferrari()
ferrari_obj.harga()

"""Threading"""
# Thread adalah entitas dalam proses yang dapat dijadwalkan untuk dieksekusi.
# thread adalah urutan instruksi semacam itu di dalam program yang dapat dieksekusi secara independen dari kode lain
  # Multithreading didefinisikan sebagai kemampuan prosesor untuk mengeksekusi beberapa thread secara bersamaan.
  # import threading # import library threading
  # import time # import library time

# def print_with_dynamic_sleep(total_iteration):
#     """
#     fungsi berikut akan melakukan print command
#     dengan interval yang berbeda-beda
#     """
#     for w in range(total_iteration):
#         print("Hello from dynamic-sleep interval, pengulangan ke-{}".format(w))
#         time.sleep(w) # fungsi akan berhenti selama w second, akan berubah2 secara dinamis

# def print_with_static_sleep(total_iteration):
#     """
# 	fungsi berikut akan melakukan print command
# 	dengan interval yang statis/sama
#     """
#     for y in range(total_iteration):
#         print("Hello from static-sleep interval, pengulangan ke-{}".format(y))
#         time.sleep(2) # fungsi akan berhenti selama 2 second

# if __name__ == "__main__":
# 	# creating thread
# 	t1 = threading.Thread(target=print_with_dynamic_sleep, args=(5,))
# 	t2 = threading.Thread(target=print_with_static_sleep, args=(5,))

# 	# memulai thread pertama
# 	t1.start()
# 	# memulai thread kedua
# 	t2.start()

# 	# tunggu sampai thread 1 selesai dilaksanakan
# 	t1.join()
# 	# tunggu sampai thread 2 selesai dilaksanakan
# 	t2.join()

# 	# both threads completely executed  
# 	print("Selesai!")

"""Multiprocessing"""
import multiprocessing # import library multiprocessing
import time # import library time

def print_with_dynamic_sleep(total_iteration):
    """
    fungsi berikut akan melakukan print command
    dengan interval yang berbeda-beda
    """
    for x in range(total_iteration):
        print("Hello from dynamic-sleep interval, pengulangan ke-{}".format(x))
        time.sleep(x) # fungsi akan berhenti selama x second, akan berubah2 secara dinamis

def print_with_static_sleep(total_iteration):
    """
	fungsi berikut akan melakukan print command
	dengan interval yang statis/sama
    """
    for x in range(total_iteration):
        print("Hello from static-sleep interval, pengulangan ke-{}".format(x))
        time.sleep(2) # fungsi akan berhenti selama 2 second

if __name__ == "__main__":
	# creating thread
	p1 = multiprocessing.Process(target=print_with_dynamic_sleep, args=(5,))
	p2 = multiprocessing.Process(target=print_with_static_sleep, args=(5,))

	# memulai process pertama
	p1.start()
	# memulai process kedua
	p2.start()

	# tunggu sampai process 1 selesai dilaksanakan
	p1.join()
	# tunggu sampai process 2 selesai dilaksanakan
	p2.join()

	# both threads completely executed
	print("Selesai!")
	