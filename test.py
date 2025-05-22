import numpy as np
import pyaudio

FREQUENCY = 440  # Frequency of the sine wave in Hz (A4 note)
SAMPLE_RATE = 60000  # Standard sample rate in Hz
DURATION = 1  # Duration of the sine wave in seconds
VOLUME = 0.3  # Volume of the sine wave (0.0 to 1.0)

time = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), False)

sine_wave = np.cos(((2*np.pi)/3) * FREQUENCY * time)

audio_data = VOLUME * sine_wave

audio_data = audio_data.astype(np.float32)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=SAMPLE_RATE,
                output=True)

stream.write(audio_data.tobytes())

stream.stop_stream()
stream.close()

sine_wave = np.cos(((4*np.pi)/3) * FREQUENCY * time)

audio_data = VOLUME * sine_wave

audio_data = audio_data.astype(np.float32)

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=SAMPLE_RATE,
                output=True)

stream.write(audio_data.tobytes())

stream.stop_stream()
stream.close()

p.terminate()
