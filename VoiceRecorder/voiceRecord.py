import  sounddevice as sd#Ses kayıt ve oynatma için kullanılıyor
from scipy.io.wavfile import write#WAV dosyalarını okumak ve yazmak icin kullanılıyor
import wavio as wv#Yine bu da WAV dosyalarını yazmak icin kullanılan baska bir kütüphane


class voiceRecord():
    def __init__(self):
        try:
            freq = 44100#örnekleme frekansı
            duration = int(input("Audio duration: "))#kayıt süresi
            recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
            #kayıt işlemi burada oluyor
            sd.wait()#kayıt işlemi bittiği satır
            path = str(input("Pls, enter audio name: "))#kaydedilecek ses dosyası ismi ayarlanıyor
            write(f"{path}.wav", freq, recording)
        except:
            print("Error, Voice Recorded coouldn't recorded  ")