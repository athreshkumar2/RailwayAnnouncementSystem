import os
from typing import Generator
import pandas as pd
from pandas.core.reshape.merge import merge
from pandas.io.sql import execute
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text, filename):  #eg:text-I am good boy, filename-athresh.mp3 (It will read filename and say text presnt in text)
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=True)
    myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1.Generating kripaya Dhyan Dijiye
    start = 88500                                   #we should give values in milliseconds from the audio file present in the directory. 
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is from-city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 7 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 is platform number

    # 11 - Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():           #It will iterate through the rows of excel sheet taking index(0) we should mention index and iterrows() is a function in pandas.#Item is like heading in each row for example item of train_no with index 1 is 14315 and train_name item has index 2 with intercity name.
        # 2 - Generate from-city
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4 - Generate via-city
        textToSpeech(item['via'], '4_hindi.mp3')

        # 6 - Generate to-city
        textToSpeech(item['to'], '6_hindi.mp3')

        # 8 - Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')

        # 10 - Generate platform number
        textToSpeech(item['platform'], '10_hindi.mp3')     

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]            #Here we are iterating through mp3 files from 1 to 12 to merge audio                       

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton() 
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")



""" When executed first it will run skeleton function and will save it (i.e the common ones-1,3,5,7,9,11.mp3)
and then announcement function is executed it will read excel file and will make the mp3 files according to the data in the excel sheet and will use textToSpeech function to make these mp3 files. then we will run mergeAudios function and will iterate it and will save it and will export it. """