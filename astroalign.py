import rawpy
import imageio
import astroalign

paths = ['1.dng','2.dng','3.dng']
#bad_pixels = rawpy.enhance.find_bad_pixels(paths)

#for path in paths:
#    with rawpy.imread(path) as raw:
#        rawpy.enhance.repair_bad_pixels(raw,bad_pixels,method='median') # for dark image
#        rgb = raw.postprocess()
#    imageio.imsave(path + '.tiff',rgb)

allineate = []
for i in range(1,len(paths)):
    ligned_image, footprint = astroalign.register(paths[i],paths[0])
    allineate.append(ligned_image)

for i in range(len(allineate)):
    with rawpy.imread(allineate[i]) as raw:
        rgb = raw.postprocess()
        #rgb = raw.postprocess(gamma=(1,1), no_auto_bright=True, output_bps=16) # 16 bit linear image
    imageio.imsave('%d.tiff'%(i+1),rgb)
