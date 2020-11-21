import librosa

filename = librosa.example('nutcracker')
audio, sample_rate = librosa.load(filename)
print(sample_rate)

tempo, beat_frames = librosa.beat.beat_track(y=audio, sr=sample_rate)
beat_times = librosa.frames_to_time(beat_frames, sr=sample_rate)

print('tempo: {:.1f} beats per minute'.format(tempo))
print(beat_times)

y_harm, y_perc = librosa.effects.hpss(audio)

import librosa.display
librosa.display.waveplot(audio, sr=sample_rate)

y_harm, y_perc = librosa.effects.hpss(audio)
librosa.display.waveplot(y_harm, sr=sample_rate, alpha=0.25)
librosa.display.waveplot(y_perc, sr=sample_rate, color='r', alpha=0.5)

import matplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(audio)
ax.set(xlabel='time (samples)', ylabel='Sound',
       title='Audio')
fig.set_size_inches(12,3)
plt.show()
