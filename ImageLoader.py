from PIL import Image
from numpy import asarray
import requests
import shutil

def Update(image_url):
    r = requests.get(image_url, stream = True)

    if r.status_code == 200:
        r.raw.decode_content = True

        with open('image_cache.png','wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded')
    else:
        print('Failed')
        exit()

    size = 200, 120
    simage = Image.open("image_cache.png")
    srimage = simage.resize(size, Image.ANTIALIAS)
    srimage.save('image_cache.png')
    image = Image.open('image_cache.png')
    numpydata = asarray(image)
    file = open("Data.json", "w") # Replace Data.json with where you put Data.json in public_html

    count = 0
    nub2 = 0
    file.write('{ "data": [\n')
    for x in numpydata:
        file.write("[\n")
        nub2 = nub2+1
        nub = 0
        for y in x:
            nub = nub+1
            if nub >= len(x):
                file.write("[\n")
                file.write(str(y[0]) + ", " + str(y[1]) + ", " +  str(y[2]))
                count += 1
                file.write("\n]")
            else:
                file.write("[\n")
                file.write(str(y[0]) + ", " + str(y[1]) + ", " +  str(y[2]))
                count += 1
                file.write("\n],")
        if nub2 >= len(numpydata):
            file.write("\n]")
        else:
            file.write("\n],")
    file.write(']}')
    file.close()
    return True