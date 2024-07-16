import imageio.v3 as iio

filenames = ['telali/hadikocumatarsin0.png','telali/hadikocumatarsin1.png','telali/hadikocumatarsin2.png','telali/hadikocumatarsin3.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("telalibasket.gif", images, duration=250, loop = 0)
