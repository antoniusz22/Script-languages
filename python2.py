import os, glob

f = open('raport.html', 'w')
in_files = os.listdir("in/")
out_files = os.listdir("out/")
in_files_path = glob.glob("in/*.txt")
out_files_path = glob.glob("out/*.txt")

num_of_files = len(in_files_path)
data = ""

for i in range(num_of_files):
    outFile = open(f'{os.path.abspath(out_files_path[i])}', 'r')
    outContent = outFile.readline()
    outFile.close()
    inFile = open(f'{os.path.abspath(in_files_path[i])}', 'r')
    inContent = inFile.read().splitlines()
    inFile.close()
    data = data + f"""
      <tr>
        <td><a href="{os.path.abspath(in_files_path[i])}">{in_files[i]}</a></td>
        <td><a href="{os.path.abspath(out_files_path[i])}">{out_files[i]}</a></td>
      
        <td><div>liczba miast: {inContent[0]}</div><div>koszt transportu: {inContent[1], inContent[2], inContent[3]}</div></td>
        <td>{outContent}</td>
      </tr>
      """

style = '{padding: 0.4rem;border: 1px solid black;border-collapse: collapse;border-spacing:8px;text-align:center}'

raport = f"""<html>
<head><style>
table, th, td {style}
</style></head>
<body style="background-color:gainsboro">
<center>
<div><big style="font-size:42px;">GDZIE ZBUDOWAĆ BROWAR</big></div>
<div><big>Antoni Zuber</big></div>

<div style='height:5%'></div>
<center>
<table style='width:90%'>
  <tr>
    <th style='width:10%'>IN FILES</td>
    <th style='width:10%'>OUT FILES</td>
    <th style='width:50%'>DANE WEJŚCIOWE</td>
    <th style='width:20%'>ŁĄCZNY KOSZT, MIASTO</td>
  </tr>
  {data}
</table></center></body></html>"""


f.write(raport)
f.close()

print("Raport został zapisany w pliku raport.html\n")