import sys
from os import path
from pydub import AudioSegment

filePath = sys.argv[1]
filePathArr = filePath.split("/")
fileName = filePathArr[len(filePathArr) - 1]

# files                                                                         
src = filePath
dst = "./audio/{}.wav".format(fileName.split(".")[0])

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")