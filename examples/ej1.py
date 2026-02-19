from GetPicture import GetPicture

with open("salida.txt", "r") as file:
    lines = file.readlines()

results = []

for line in lines:
    key, value = line.split('\t')    
    nada, id = key.split('=')
    nada, faceurl = value.split('=')
    print (f'ID ={id}= faceURL ={faceurl}=')
    foto_path = rf'F:\Clientes\florida\tarjado\fotos\{id}.jpg'
    GetPicture(faceurl,'admin','Admin2023$',foto_path)