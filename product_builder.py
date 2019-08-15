import codecs
sfilename = "pdf_unido_txt.txt"
#sfilename = "txt_3_primeros.txt"
dfilename = "result.txt"
f = open(sfilename, "r", encoding="latin-1")
data = f.read()
data = data.replace("Avda. de las canteras 23-25 Nave 5, Políg. Industrial Valmor.","")
data = data.replace("Avda. de las canteras 23-25 Nave 5, Políg. Industrial Valmor","")
#data = data.replace("PICTOGRAMAS","")
data = data.replace("28340 VALDEMORO  MADRID (SPAIN)","")
data = data.replace("E-mail: tecnico@kleer-kim.com Web site: kleer-kim.com","NEWPRODUCT")
data = data.replace("Tel. 91 895 65 10 Fax. 91 895 66 08","")
products=data.split("NEWPRODUCT")
len(products)
result = open(dfilename,"w+", encoding="latin-1")
for x in range(len(products)-1):
  print ("Processing Line: " + str(x) +"\n")
  #descripcion
  p_name = products[x].split("PICTOGRAMAS\n")[0].split("\n")[3]
  p_name = p_name.replace(" - ","-")
  p_name = p_name.replace("- ","-")
  p_name = p_name.replace(" -","-")
  p_name = p_name.replace(" – ","-")
  p_name = p_name.replace("– ","-")
  p_name = p_name.replace(" –","-")
  p_name = p_name.replace(" – "," ")

  prod_desc = products[x].split("DESCRIPCION\n")[1].split("APLICACIONES\n")[0]
  prod_desc = prod_desc.replace("\n"," ")
  #descripcion corta
  brief_desc = prod_desc.split(".")[0]
  slug = p_name.replace(" ","-")
  post_title = p_name
  p_id = str(1521 + x)
  line = p_id + " | " + p_name + " | " + post_title + " | " + slug + " | " + brief_desc + " | " + prod_desc + "\n"
  result.write(line)

result.close()
