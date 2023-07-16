from demucs import separate
import torchaudio

data = separate.main(['latindb1.wav', "--out='songs'"])
if data:
    print(data)
    source, sr, encoding, bits_per_sample =  data['source'], data['sr'], data['encoding'], data['bits_per_sample']
    torchaudio.save('songs/latindb1.wav', source, sr, encoding, bits_per_sample)
else:
    print("No data returned")