from django.shortcuts import render
import random
from django.core.files.storage import FileSystemStorage
from python_scripts.getJSON import getJSON,samples_to_midi

#import model

# Create your views here.
""" 
from keras.models import load_model,Model
from mido import MidiFile,MidiTrack,Message
from keras import backend as K
from tensorflow import Graph,Session
import numpy as np
y_orig=np.load('y_orig.npy')
model_graph=Graph()

print('hello start')
model_graph=Graph()
with model_graph.as_default():
    tf_session=Session()
    with tf_session.as_default():
        model=load_model('model.h5',compile=False)

"""

def home(request):
    return render(request,'aicomposer/home.html')

def about(request):
    return render(request,'aicomposer/about.html')


 
def music_composer(request):
  
    # randsong=np.zeros((16,96,96))
    # for i in range(16):
    #     randsong[i]=y_orig.reshape(-1,96,96)[random.randint(0,y_orig.shape[0]*16-1)]
    
    # with model_graph.as_default():
    #     with tf_session.as_default():

    #         song=model.predict(randsong.reshape((1,16,96,96)))
    # samples_to_midi(song[0],'hello.mid',20,0.5)

    data=getJSON('media/sessiontune0.mid')
    context={'data':(data)}
    return render(request,'aicomposer/app.html',context)



