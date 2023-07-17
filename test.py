from demucs import separate

data = separate.main(['latindb1.wav', "--out='songs'", '--stream=True'])
if data:
    print(data)
else:
    print("No data returned")