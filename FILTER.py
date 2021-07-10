import numpy as np
from PIL import Image
import urllib.request

def getPath(URL):
    urllib.request.urlretrieve(URL, 'image.png')

def BlackAndWhite(URL): 
    getPath(URL)
    ARRAY = [[0.299,0.587,0.114],[0.299,0.587,0.114],[0.299,0.587,0.114]]
    image = np.asarray(Image.open('image.png').convert('RGB'))
    trans = np.array(ARRAY).transpose()
    new_image = np.dot(image,trans)
    img = Image.fromarray(np.array(new_image).astype('uint8'))
    img.save('BlackAndWhite.png')
    return 'BlackAndWhite.png'

def RedEnhance(URL, params=12): 
    getPath(URL)
    image = np.asarray(Image.open('image.png').convert('RGB'))
    im1 = np.sqrt(image*[1.0,0.0,0.0])*params
    im2 = image*[0.0,1.0,1.0]
    im = im1+im2
    img = Image.fromarray(np.array(im).astype('uint8'))
    img.save('RedEnhance.png')
    return 'RedEnhance.png'

def BlueEnhance(URL, params=12): 
    getPath(URL)
    image = np.asarray(Image.open('image.png').convert('RGB'))
    im1 = np.sqrt(image*[0.0,0.0,1.0])*params
    im2 = image*[1.0,1.0,0.0]
    im = im1+im2
    img = Image.fromarray(np.array(im).astype('uint8'))
    img.save('BlueEnhance.png')
    return 'BlueEnhance.png'

def GreenEnhance(URL, params=12): 
    getPath(URL)
    image = np.asarray(Image.open('image.png').convert('RGB'))
    im1 = np.sqrt(image*[0.0,1.0,0.0])*params
    im2 = image*[1.0,0.0,1.0]
    im = im1+im2
    img = Image.fromarray(np.array(im).astype('uint8'))
    img.save('GreenEnhance.png')
    return 'GreenEnhance.png'

def Reverse(URL):
    getPath(URL)
    im = 255 - np.asarray(Image.open('image.png').convert('RGB'))
    image = Image.fromarray(np.array(im).astype('uint8'))  
    image.save('Reverse.png')
    return 'Reverse.png'

def OldFilm(URL):
    getPath(URL)
    im = np.asarray(Image.open('image.png').convert('RGB'))
    trans = np.array([[0.393,0.769,0.189],[0.349,0.686,0.168],[0.272,0.534,0.131]]).transpose()
    im = np.dot(im,trans).clip(max=255)              
    image = Image.fromarray(np.array(im).astype('uint8')) 
    image.save('OldFilm.png') 
    return 'OldFilm.png'
