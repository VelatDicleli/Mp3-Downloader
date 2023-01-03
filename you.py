from pytube import YouTube
import os
#C:\Users\User\Desktop\İndirilenler   dosya yolu
#https://www.youtube.com/watch?v=XXYlFuWEuKI&list=RDMMXXYlFuWEuKI&start_radio=1&ab_channel=TheWeekndVEVO   şarkı

def indir(link):

    try:
        yt = YouTube(link)
        muzik = yt.streams.filter(only_audio=True).first()
        print("Lutfen bekleyin...")
        destination = input("nereye kaydetmek istiyorsunuz ? : ")
        out_file = muzik.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print("muziginiz basarili bir sekilde indirildi")

    except:
        print("uzgunum bir hata olustu tekrar dene")



link = input("videonun urlsini giriniz:  ")
indir(link)
