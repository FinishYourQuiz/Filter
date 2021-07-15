import numpy as np
from PIL import Image
from PIL import ImageFilter
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
import urllib.request
import os
import uuid

def getUniqueID(new):
    curr = './photo/'+str(uuid.uuid1())+'.png'
    if len( os.listdir('./photo')) > 15:
        for file in os.listdir('./photo'):
            if file.endswith('.png'):
                os.remove('./photo/'+file) 
    new.save(curr)
    return curr

def getPath(URL):
    urllib.request.urlretrieve(URL, 'image.png')

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

def OldFilm(URL):
    getPath(URL)
    im = np.asarray(Image.open('image.png').convert('RGB'))
    trans = np.array([[0.393,0.769,0.189],[0.349,0.686,0.168],[0.272,0.534,0.131]]).transpose()
    im = np.dot(im,trans).clip(max=255)              
    image = Image.fromarray(np.array(im).astype('uint8')) 
    return getUniqueID(image)


def RedEnhance(URL, params=12): 
    getPath(URL)
    image = np.asarray(Image.open('image.png').convert('RGB'))
    im1 = np.sqrt(image*[1.0,0.0,0.0])*params
    im2 = image*[0.0,1.0,1.0]
    im = im1+im2
    img = Image.fromarray(np.array(im).astype('uint8'))
    return getUniqueID(img)

def BlueEnhance(URL, params=12): 
    getPath(URL)
    image = np.asarray(Image.open('image.png').convert('RGB'))
    im1 = np.sqrt(image*[0.0,0.0,1.0])*params
    im2 = image*[1.0,1.0,0.0]
    im = im1+im2
    img = Image.fromarray(np.array(im).astype('uint8'))
    return getUniqueID(img)

def GreenEnhance(URL, params=12): 
    getPath(URL)
    image = np.asarray(Image.open('image.png').convert('RGB'))
    im1 = np.sqrt(image*[0.0,1.0,0.0])*params
    im2 = image*[1.0,0.0,1.0]
    im = im1+im2
    img = Image.fromarray(np.array(im).astype('uint8'))
    return getUniqueID(img)

def Blur(URL):
    getPath(URL)
    return getUniqueID(Image.open('image.png').filter(BLUR))
    
def Contour(URL):
    getPath(URL)
    return getUniqueID(Image.open('image.png').filter(CONTOUR))
    
def Detail(URL):
    getPath(URL)
    return getUniqueID(Image.open('image.png').filter(DETAIL))
    
def EdgeEnhance(URL):
    getPath(URL)
    return getUniqueID(Image.open('image.png').filter(EDGE_ENHANCE))
    
def EdgeEnhanceMore(URL):
    getPath(URL)
    return getUniqueID(Image.open('image.png').filter(EDGE_ENHANCE_MORE))

def Emboss(URL):
    getPath(URL)
    return getUniqueID(Image.open('image.png').filter(EMBOSS))
    
def FindEdges(URL):
    getPath(URL)
    return getUniqueID(Image.open('image.png').filter(FIND_EDGES))
    
def Smooth(URL):
    getPath(URL)
    return getUniqueID(Image.open('image.png').filter(SMOOTH))
    
def SmoothMore(URL):
    getPath(URL)
    return getUniqueID(Image.open('image.png').filter(SMOOTH_MORE))
    
def Sharpen(URL):
    getPath(URL)
    return getUniqueID(Image.open('image.png').filter(SHARPEN))