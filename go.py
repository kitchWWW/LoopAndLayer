from pydub import AudioSegment

# sound1 = AudioSegment.from_file("res/a.wav")
sound = AudioSegment.from_file("res/4_1.wav")

# combined = sound.overlay(sound1)

# combined.export("out.wav", format='wav')

lengthOfLoop = 35

combined = AudioSegment.empty()
for i in range(int(sound.duration_seconds/lengthOfLoop)+1):
	print(i)
	thingSoFar = sound[:(lengthOfLoop*(i+1)*1000)]
	lastSeconds = thingSoFar[lengthOfLoop*-1000:]
	# lastSeconds.export("out_l"+str(i)+".wav", format='wav')
	combined2 = lastSeconds.overlay(combined)
	# combined2.export("out_c"+str(i)+".wav", format='wav')
	combined = combined2

combined.export("outz.wav", format='wav')
