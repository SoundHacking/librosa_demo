filename = "piano2.wav"

import librosa
audio, sample_rate = librosa.load(filename)
print(sample_rate)

import matplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(audio)
ax.set(xlabel='time (samples)', ylabel='Sound',
       title='Audio')
fig.set_size_inches(12,3)
plt.show()

#from playsound import playsound
#playsound(filename)

