# importing Image class from PIL package
from PIL import Image

# creating a object
image = Image.open("/images/universe.jpg")
image.load()

# Splitting the image into individual
# bands
r, g, b, = image.split()

# merge function used
im1 = Image.merge('RGB', (g, b, r))
im1.show()