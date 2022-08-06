"""
The code below was written by @author: https://github.com/DianaNtz and is an 
example on how to create an animated gif with the library imageio.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import imageio
n=100       #gifs worth in units of 10**3 words :)
t=np.linspace(-1,1,n-1)
filenames = []
for i in range(0,n):
    #plot the curve
    fig, ax = plt.subplots(figsize=(7,7))
    ax.plot(t[:i],np.sqrt((t[:i])**2)+np.sqrt(1-(t[:i])**2),"-",
    linewidth=3.0,color='deeppink',label='$(\:t,|t|+\sqrt{1-t^2}\:)$')
    ax.plot(-t[:i],np.sqrt((t[:i])**2)-np.sqrt(1-(t[:i])**2), "-m",
    linewidth=3.0,label='$(\:t,|t|-\sqrt{1-t^2}\:)$')
    ax.set_xlim(-1.5,1.5)
    ax.set_ylim(-1.5,2.5)
    plt.xticks(fontsize= 16) 
    plt.yticks(fontsize= 16)
    plt.legend(loc=1,fontsize= 16)
    #create file name for index i 
    filename ='bla{0:.0f}.png'.format(i)
    #append file name to the list filename
    filenames.append(filename)
    #save the plot
    plt.savefig(filename,dpi=100)
    plt.close()
#build the gif
with imageio.get_writer('Herz.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image) 
#remove saved figures 
for filename in set(filenames):
    os.remove(filename)        