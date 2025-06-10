## pillow ALSO A TYPE OF LIBRARY THAT IS USED TO AD MULTI MEDIA IN THE CODE AND ITS MANAGEMENT
import sys
from PIL import Image
images=[]
for arg in sys.argv[1:]:
    image=Image.open(arg)
    images.append(image)

images[0].save("costumes.jpg",save_all=True,append_images=[images[1]],duration=200,loop=0)

## THE CODE IS STILL INCOMPLETE
