import codecs
import csv
import json
csvFilePath = "wc_product-buena.csv"
jsonFilePath = "result.csv"
#sfilename = "txt_3_primeros.txt"
data ={}
url_1 = "[su_members message=\"Contenido adicional disponible solo para usuarios autorizados. Por favor \%login\%.\"]<a class=\"btn btn-primary btn-warning, fa fa-file-pdf-o\" href=\"/FichasTecnicas/K-7040.pdf">
url_2 = "\"> Ficha de Datos de Seguridad</a>"

with open(csvFilePath, "rU", encoding="latin-1") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['ID']
        data[id] = rows


with open (jsonFilePath,'w+', encoding="latin-1" ) as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

result = open('urls_ft_files.csv',"w+", encoding="latin-1")

nombre =''

for id in data:
    if len(data[id]['Nombre'].split(" ")) > 1:
        if len(data[id]['Nombre'].split(" ")[1]) == 1:
            nombre = data[id]['Nombre'].split(" ")[0] + " " + data[id]['Nombre'].split(" ")[1] + ".pdf"
            nombre = nombre.lstrip()
            nombre = nombre.rstrip()
        else:
            nombre = data[id]['Nombre'].split(" ")[0] + ".pdf"
            nombre = nombre.replace(" ",'')
            nombre = nombre.lstrip()
            nombre = nombre.rstrip()
    else:
        nombre = data[id]['Nombre'].split(" ")[0] + ".pdf"
        nombre = nombre.lstrip()
        nombre = nombre.rstrip()
    print('---')
    print(data[id]['Nombre'])
    print('---')
    print(nombre)
    print('---')
    description = data[id]['DescripciÃ³n']
    print(description)
    url = url_1 + nombre + url_2
    data[id]['DescripciÃ³n'] =  "\"" + description + "\n" + "\n"  + url + "\"" + "\n"
    result.write(data[id]['DescripciÃ³n'])

result.close()
