import os
import rawpy
import imageio
import astroalign as aa # pip install scikit-image
from PIL import Image

dirname = "Orione/light/"

# lista foto
listafoto = os.listdir(dirname)
listafoto.sort()
numfoto = len(listafoto)

# mi sposto nella dir dove sono le immagini
os.chdir(dirname)

# le preprocesso per allinearle
listargb = []
for i in range(numfoto):
    print("Preprocessing '%s'..." %(listafoto[i]),flush=True)
    raw = rawpy.imread(listafoto[i])
    rgb = raw.postprocess()
    listargb.append(rgb)
    imageio.imsave('rgb_%d.tiff'%(i+1),listargb[i])

# le allineo
allineate = []
target = listargb[0]
for i in range(numfoto):
    print("Allineamento '%s'..." %(listafoto[i]),flush=True)
    ligned_image, footprint = aa.register(listargb[i],target,min_area=9)
    allineate.append(ligned_image)

# scrivo le immagini allineate per vederle
for i in range(len(allineate)):
    print("Salvataggio '%s'..." %(listafoto[i]),flush=True)
    #allineate[i] = Image.fromarray(allineate[i].astype("unit8"))
    imageio.imsave('allineata_%d.tiff'%(i+1),allineate[i])


