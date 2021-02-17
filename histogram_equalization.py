# importando o pacote de plotagem gráfica matplotlib
from matplotlib import pyplot as plt
# importando o pacote de plotagem gráfica seaborn 
import seaborn as sns
# importando o pacote de vetorização numpy 
import numpy as np

def histogram(image, bins = 255):
    '''função que cria um histograma baseado em uma imagem'''
    
    # criando um array zerado para armazenar a distribuição de píxels por valor 
    histogram = np.zeros(bins)
    
    # intera sobre os píxels da imagem o os separa por intensidade  
    for pixel in image:
        histogram[int(pixel)] += 1
    
    return histogram

def cumulative_sum(a):
    '''função que computa a soma cumulativa do histograma''' 
    
    # definindo um iterador sobre a quantidade de píxels em cada intensidade 
    a = iter(a)
    # define b como receptor do próxumo item do iterador 
    b = [next(a)]
    
    # itera sobre a quantidade de píxels em cada intensidade 
    for i in a:
        # computa a soma cumulativo do histograma 
        b.append(b[-1] + i)
        
    return np.array(b)

def cs_equalization(cs):
    '''normalizando a soma cumulativo do histograma''' 

    # numerador e denominador da etapa de normalização 
    nj = (cs - cs.min()) * 255
    N = cs.max() - cs.min()

    # normalizando a soma cumulativo do histograma
    cs = nj / N
    
    # modificando o tipo de dado para visualização da imagem 
    cs = cs.astype('uint8')
    
    return cs 

def histogram_equalization(image_file):
    '''preprocessando a imagem com equalização de histograma'''
    
    if type(image_file) == str:
        # carregando a imagem como um array numpy  
        image = plt.imread(image_file)
    else:
        # considera que image_file já é um array
        image = image_file 
    # convertendo a imagem em um numpy array
    image = np.asarray(image)
    # colocando as imagens em um array 1-dimensional
    flatten = image.flatten()
    # obtendo a quantidade de píxels por intensidade
    hist = histogram(flatten, 256)
    # calculando a soma cumulativa do histograma  
    cs = cumulative_sum(hist)
    # aplicando a normalização na soma cumulativa do histograma
    cs = cs_equalization(cs)  
    flatten = flatten.astype('uint8')
    # aplicando as transformações em cada umas das intensidades de píxel do vetor 1-dimensional
    img_new = cs[flatten] 
    # redimensionando o vetor 1-dimensional para as dimensões da imagem original
    img_new = np.reshape(img_new, image.shape)
    
    return img_new.astype('float64')

