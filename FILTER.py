import numpy as np
import PIL
from PIL import Image, ImageOps, ImageEnhance
from PIL import ImageFilter
from PIL.ImageFilter import CONTOUR
import urllib.request
import os
import uuid

def getUniqueID(new):
    curr = './photo/'+str(uuid.uuid1())+'.png'
    if len( os.listdir('./photo')) > 10:
        for file in os.listdir('./photo'):
            if file.endswith('.png'):
                os.remove('./photo/'+file) 
    new.save(curr)
    return curr

def getPath(URL):
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(URL, 'image.png')
    print('Valid image address!')

def getSize(URL):
    try:
        getPath(URL)
        image = Image.open('image.png')
        width, height = image.width, image.height
        return {'valid': True, 'width': width, 'height': height}
    except:
        print('Invalid Image address!')
        return {'valid':False}

'''
    Basic Filters
'''
def BlackAndWhite(URL): 
    getPath(URL)
    ARRAY = [[0.299,0.587,0.114],[0.299,0.587,0.114],[0.299,0.587,0.114]]
    image = np.asarray(Image.open('image.png').convert('RGB'))
    trans = np.array(ARRAY).transpose()
    new_image = np.dot(image,trans)
    img = Image.fromarray(np.array(new_image).astype('uint8'))
    return getUniqueID(img)

def Reverse(URL):
    getPath(URL)
    im = 255 - np.asarray(Image.open('image.png').convert('RGB'))
    image = Image.fromarray(np.array(im).astype('uint8'))  
    return getUniqueID(image)

def Contrast(URL, choice=1):
    getPath(URL)
    image = Image.open('image.png')
    choices = [
        0.5,
        0.8,
        1.2,
        1.5,
        1.7,
        2.0,
        2.4,
    ]
    contrast = ImageEnhance.Contrast(image)
    new_image = contrast.enhance(choices[choice - 1])
    return getUniqueID(new_image)

def Brightness(URL, choice=1):
    getPath(URL)
    image = Image.open('image.png')
    choices = [
        0.9,
        1.1,
        1.2,
        1.3,
        1.4,
        1.5,
    ]
    image = ImageEnhance.Brightness(image)
    new_image = image.enhance(choices[choice - 1])
    return getUniqueID(new_image)

def Sharpness(URL, choice=1):
    getPath(URL)
    image = Image.open('image.png')
    choices = [
        2,
        8,
        15, 
        24,
        30
    ]
    sharpness = ImageEnhance.Sharpness(image)
    new_image = sharpness.enhance(choices[choice - 1])
    return getUniqueID(new_image)
    
'''
    Blur Filters
'''
def Mean(URL):
    getPath(URL)
    [[i1, i2, i3], [i4, i5, i6], [i7, i8, i9]] = \
    [
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ]
    matrix = [[i1, i2, i3], [i4, i5, i6], [i7, i8, i9]]
    im = Image.open('image.png').convert('RGB')
    image = im.filter(ImageFilter.Kernel((3, 3),
    (i1, i2, i3, i4, i5, i6, i7, i8, i9), 1, 0))
    return getUniqueID(image)

def Gaussian1(URL):
    getPath(URL)
    [[i1, i2, i3], [i4, i5, i6], [i7, i8, i9]] = \
    [
        [1/16, 2/16, 1/16],
        [2/16, 4/16, 2/16],
        [1/16, 2/16, 1/16]
    ]
    matrix = [[i1, i2, i3], [i4, i5, i6], [i7, i8, i9]]
    im = Image.open('image.png').convert('RGB')
    image = im.filter(ImageFilter.Kernel((3, 3),
    (i1, i2, i3, i4, i5, i6, i7, i8, i9), 1, 0))
    return getUniqueID(image)

def Gaussian2(URL):
    getPath(URL)
    im = Image.open('image.png').convert('RGB')
    i1,i2,i3,i4,i5, i6= 1/256, 4/256, 6/256,16/256, 24/256, 36/256
    image = im.filter(ImageFilter.Kernel((5, 5),
    (i1,i2,i3,i2,i1, i2,i4,i5,i4,i2, i3,i5,i6,i5,i3, i2,i4,i5,i4,i2, i1,i2,i3,i2,i1), 1, 0))
    return getUniqueID(image)

'''
    Edge Filters
'''
def Contour(URL):
    getPath(URL)
    return getUniqueID(Image.open('image.png').filter(CONTOUR))

def EdgeDetection(URL):
    getPath(URL)
    [[i1, i2, i3], [i4, i5, i6], [i7, i8, i9]] = \
    [
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ]
    im = Image.open('image.png').convert('RGB')
    image = im.filter(ImageFilter.Kernel((3, 3),
    (i1, i2, i3, i4, i5, i6, i7, i8, i9), 1, 0))
    return getUniqueID(image)

def Sobel1(URL):
    getPath(URL)
    [[i1, i2, i3], [i4, i5, i6], [i7, i8, i9]] = \
    [
        [-1/2, 0, 1/2],
        [-2/2, 0, 2/2],
        [-1/2, 0, 1/2]
    ]
    matrix = [[i1, i2, i3], [i4, i5, i6], [i7, i8, i9]]
    im = Image.open('image.png').convert('RGB')
    image = im.filter(ImageFilter.Kernel((3, 3),
    (i1, i2, i3, i4, i5, i6, i7, i8, i9), 1, 0))
    return getUniqueID(image)

def Sobel2(URL):
    getPath(URL)
    [[i1, i2, i3], [i4, i5, i6], [i7, i8, i9]] = \
    [
        [1/8, 2/8, 1/8],
        [0/8, 0/8, 0/8],
        [-1/8, -2/8, -1/8]
    ]
    matrix = [[i1, i2, i3], [i4, i5, i6], [i7, i8, i9]]
    im = Image.open('image.png').convert('RGB')
    image = im.filter(ImageFilter.Kernel((3, 3),
    (i1, i2, i3, i4, i5, i6, i7, i8, i9), 1, 0))
    return getUniqueID(image)

def Sharpen(URL):
    getPath(URL)
    [[i1, i2, i3], [i4, i5, i6], [i7, i8, i9]] = \
    [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]
    im = Image.open('image.png').convert('RGB')
    image = im.filter(ImageFilter.Kernel((3, 3),
    (i1, i2, i3, i4, i5, i6, i7, i8, i9), 1, 0))
    return getUniqueID(image)

'''
    Color Filters
'''
# 112, 276, 313, 322, 681, 108
def Vintage(URL, choice=1):
    getPath(URL)
    ARRAYs = [
        [   
            [0.71564319, 0.13257802, 0.58511742],
            [0.69484577, 0.32191478, 0.1063795 ],
            [0.19605009, 0.20891388, 0.32782248]
        ],[
            [0.94339585, 0.12088298, 0.68769125],
            [0.08463725, 0.20233426, 0.80945859],
            [0.30960484, 0.04931678, 0.35308348]
        ],[
            [0.14259632, 0.1554463,  0.24320735],
            [0.7289721,  0.14509162, 0.00808861],
            [0.47157715, 0.04619819, 0.59838045]
        ],[
            [0.76658624, 0.14813191, 0.12164835],
            [0.23017741, 0.1463261,  0.57230343],
            [0.10123897, 0.33601658, 0.2410023 ]
        ],[
            [0.42724101, 0.19953104, 0.42679979],
            [0.80287867, 0.06689895, 0.10171888],
            [0.36230923, 0.12505937, 0.18753308]
        ],[
            [0.393,0.769,0.189],
            [0.349,0.686,0.168],
            [0.272,0.534,0.131]
        ]
    ]
    image = np.asarray(Image.open('image.png').convert('RGB'))
    trans = np.array(ARRAYs[choice-1]).transpose()
    new_image = np.dot(image, trans).clip(max=255) 
    img = Image.fromarray(np.array(new_image).astype('uint8'))
    return getUniqueID(img)

# 286, 302, 336, 455, 673, 17
def Cold(URL, choice=1):
    getPath(URL)
    ARRAYs = \
    [[
        [0.71525279, 0.58845067, 0.02671351],
        [0.44119899, 0.79810486, 0.80466698],
        [0.90033505, 0.80586149, 0.87428593]
    ],[   
        [0.15058729, 0.19210636, 0.14965648],
        [0.22430212, 0.28041811, 0.6144532 ],
        [0.40669025, 0.80909544, 0.56682773]
    ],[
        [0.55614047, 0.11286346, 0.37683839],
        [0.53968608, 0.8223035,  0.19043917],
        [0.73169985, 0.77958601, 0.40939477]
    ],[
        [0.06206943, 0.08218212, 0.27545463],
        [0.09762172, 0.26514524, 0.32157921],
        [0.53043014, 0.10684297, 0.35319257]
    ],[
        [0.47782348, 0.23977846, 0.47332196],
        [0.24119175, 0.48072044, 0.42522163],
        [0.54210249, 0.44549714, 0.92409388]
    ],[
        [0.38193851, 0.22635271, 0.3352272 ],
        [0.28480674, 0.77615277, 0.56712389],
        [0.07810153, 0.54885068, 0.85964927]
    ]]
    image = np.asarray(Image.open('image.png').convert('RGB'))
    trans = np.array(ARRAYs[choice-1]).transpose()
    new_image = np.dot(image, trans).clip(max=255) 
    img = Image.fromarray(np.array(new_image).astype('uint8'))
    return getUniqueID(img)

# 15, 61, 430, 190, 7, 347
def Warm(URL, choice=1):
    getPath(URL)
    ARRAYs = \
    [[
        [0.73302002, 0.8657471,  0.76066115],
        [0.19178657, 0.49701718, 0.20011635],
        [0.05054674, 0.27755555, 0.55146847]
    ],[
        [0.95381291, 0.96484441, 0.80912918],
        [0.38774878, 0.37731055, 0.13886695],
        [0.10995287, 0.76658571, 0.61554332]
    ],[   
        [0.55185642, 0.75345351, 0.58057232],
        [0.2655882,  0.58665387, 0.11101858],
        [0.68955672, 0.15595031, 0.21210792]
    ],[
        [0.74851567, 0.8782813,  0.43081502],
        [0.20451746, 0.45071595, 0.62426952],
        [0.49934697, 0.04697661, 0.44451852]
    ],[
        [0.06208895, 0.85048433, 0.77432106],
        [0.41864727, 0.01442545, 0.58043095],
        [0.03787402, 0.11351098, 0.15288306]
    ],[
        [0.81322676, 0.43284302, 0.24718028],
        [0.36435556, 0.46779954, 0.26242307],
        [0.29020248, 0.06838452, 0.25252334]
    ]]
    image = np.asarray(Image.open('image.png').convert('RGB'))
    trans = np.array(ARRAYs[choice-1]).transpose()
    new_image = np.dot(image, trans).clip(max=255) 
    img = Image.fromarray(np.array(new_image).astype('uint8'))
    return getUniqueID(img)

# 486, 420, 241, 325, 622, 388
def Winter(URL, choice=1):
    getPath(URL)
    ARRAYs = \
    [[
        [0.17931314, 0.95632556, 0.14101994],
        [0.53937675, 0.31329902, 0.42552083],
        [0.91966325, 0.04851659, 0.6402483 ]
    ],[
        [0.72354157, 0.89907424, 0.14845877],
        [0.66530785, 0.79249235, 0.75364234],
        [0.75363003, 0.79476985, 0.87207629]
    ],[
        [0.99710737, 0.75587682, 0.01223553],
        [0.8426471,  0.7617246,  0.15105083],
        [0.43800786, 0.51654517, 0.47684648]
    ],[
        [0.79892828, 0.47025739, 0.18855481],
        [0.9298952,  0.28973347, 0.24356313],
        [0.49872504, 0.77596701, 0.15302938]
    ],[   
        [0.72728702, 0.45555004, 0.03896127],
        [0.16165173, 0.97336631, 0.28916085],
        [0.34594485, 0.26944104, 0.86048052]
    ],[
        [0.57048048, 0.4324023,  0.85882328],
        [0.50628007, 0.62217282, 0.76231663],
        [0.51607027, 0.67198515, 0.71895522]
    ]]
    image = np.asarray(Image.open('image.png').convert('RGB'))
    trans = np.array(ARRAYs[choice-1]).transpose()
    new_image = np.dot(image, trans).clip(max=255) 
    img = Image.fromarray(np.array(new_image).astype('uint8'))
    return getUniqueID(img)

'''
    Frames
'''
def Eq_Border(URL, choice=1):
    getPath(URL)
    img = Image.open('image.png')
    color_choices = [
        'black',
        (86, 86, 86),   # grey
        'indianred',
        (142, 84, 55),  # brown
        (230, 204, 177),    # antique white
        'white'
    ]
    size = max(img.width, img.height) // 15
    image = ImageOps.expand(img, border=size, fill=color_choices[choice-1])
    if choice == 6:
        image = ImageOps.expand(image, border=5, fill='black')
    return getUniqueID(image)

def Un_Eq_Border(URL, choice=1):
    getPath(URL)
    color_choices = [
        'black',
        (86, 86, 86),   # grey
        'indianred',
        (142, 84, 55),  # brown
        (230, 204, 177),    # antique white
        'white'
    ]
    img = Image.open('image.png')
    width, height = img.size
    border = (height // 10, width // 10, height // 10, width // 10)
    image = ImageOps.expand(img, border=border, fill=color_choices[choice-1])
    if choice == 6:
        image = ImageOps.expand(image, border=5, fill='black')
    return getUniqueID(image)

def Border(URL, data):
    print(data)
    R, G, B, left, top, right, bottom = int(data['red']), int(data['green']), int(data['blue']), int(data['left']), int(data['top']), int(data['right']), int(data['bottom'])
    getPath(URL)
    img = Image.open('image.png')
    image = ImageOps.expand(img, border=(left, top, right, bottom), fill=(R, G, B))
    return getUniqueID(image)
    
'''
    Operations
'''
def Resize(URL, width, height):
    getPath(URL)
    image = Image.open('image.png')
    print(width, height)
    new_image = image.resize((width, height))
    return getUniqueID(new_image)

def Crop(URL, left, top, right, bottom):
    getPath(URL)
    image = Image.open('image.png')
    box = (left, top, right, bottom)
    new_image = image.crop(box)
    return getUniqueID(new_image)

def Rotate(URL, degree):
    getPath(URL)
    image = Image.open('image.png')
    new_image = image.rotate(degree)
    return getUniqueID(new_image)

def Flip(URL, choice=1):
    getPath(URL)
    choices = [
        PIL.Image.FLIP_LEFT_RIGHT,
        PIL.Image.FLIP_TOP_BOTTOM,
        PIL.Image.ROTATE_90,
        PIL.Image.ROTATE_180,
        PIL.Image.TRANSPOSE,
    ]
    image = Image.open('image.png')
    new_img = image.transpose(choices[choice - 1])
    return getUniqueID(new_img)

