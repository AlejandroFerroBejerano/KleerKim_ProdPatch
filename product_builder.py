import codecs
sfilename = "txt_3_primeros.txt"
dfilename = "result.txt"
f = open(filename, "r", encoding="latin-1")
data = f.read()
data = data.replace("Avda. de las canteras 23-25 Nave 5, Políg. Industrial Valmor.","")
data = data.replace("Avda. de las canteras 23-25 Nave 5, Políg. Industrial Valmor","")
data = data.replace("PICTOGRAMAS","")
data = data.replace("28340 VALDEMORO  MADRID (SPAIN)","")
data = data.replace("E-mail: tecnico@kleer-kim.com Web site: kleer-kim.com","NEWPRODUCT")
data = data.replace("Tel. 91 895 65 10 Fax. 91 895 66 08","")
products=data.split("NEWPRODUCT")
len(products)
result = open(dfilename,"w",encoding="latin-1")
for product in products:
  prod_desc = product[1].split("DESCRIPCION\n")[1].split("APLICACIONES\n")[0]
  prod_desc = prod_desc.replace("\n","")
  result.write(prod_desc)
