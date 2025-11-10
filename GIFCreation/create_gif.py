import imageio.v3 as iio

filenames = []
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('created.gif')