# Berikut ini adalah proses membaca dan memeriksa informasi data pribadi tipe kamus dalam tipe data json. Data tipe json yang terdiri dari string dapat diubah menjadi tipe dictionary melalui fungsi loads() 
# import json
# data = '{"Nama" : "Andy","Age" : 18,"Hobby":["Renang"],\
#     "Family":{"Father" : "Bambang"},"marrie": true}'

# json_data = json.loads(data)

# print(type(json_data))
# print(json_data['Nama'])
# print(json_data['Family'])
# print(json_data['marrie'])

#  fungsi dumps() untuk merubah dictionary menjadi json-string. Fungsi dumps() untuk menghasilkan sebuah file tipe JSON dari data dictionary.
# import json
# Dictionary ={'Halo':123,'Semua':456}
 
# json_string = json.dumps(Dictionary)
 
# print('Result: ',json_string)
# print('Tipe: ',type(json_string))

# Exporting JSON data
import json
data = '{"title": "Superboi","ISBN" : "12345","Author" : "Andy"}'
json_data = json.loads(data)
with open('book.json','w') as f:
    json.dump(json_data,f,indent = '\t')