from pydub import AudioSegment
import os

for f in os.listdir("allres"):
	print(f)
	if ".wav" not in f:
		continue
	sound = AudioSegment.from_file("allres/"+f)

	# combined = sound.overlay(sound1)
	# combined.export("out.wav", format='wav')

	lengthOfLoop = int(sound.duration_seconds / 4)
	if(lengthOfLoop<3):
		continue

	combined = AudioSegment.empty()
	for i in range(int(sound.duration_seconds/lengthOfLoop)+1):
		print(i)
		thingSoFar = sound[:(lengthOfLoop*(i+1)*1000)]
		lastSeconds = thingSoFar[lengthOfLoop*-1000:]
		# lastSeconds.export("out_l"+str(i)+".wav", format='wav')
		combined2 = lastSeconds.overlay(combined)
		# combined2.export("out_c"+str(i)+".wav", format='wav')
		combined = combined2

	combined.export("allout/looped_"+f, format='wav')
