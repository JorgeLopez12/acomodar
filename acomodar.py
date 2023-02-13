#from PIL import Image
import shutil
import os

descargas = "/Users/lopez/Downloads"
mis_documentos = "/Users/lopez/Documents/Instaladores"

#take the documents to download file and put on filenames
#toma los documentos de descargas y las guarda en filenames
file_names = os.listdir(descargas)
#move the files to my files
#reccorre los documentos y los mueve a la carpete dentro de mis documentos
for file_name in file_names:
    #move only the specific files
    #mueve solo los archivos con extencion especifica
    #if file_name.endswith('.png'):
    shutil.move(os.path.join(descargas, file_name), mis_documentos)