import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel


TARGET_SAMPLE_RATE = 16000

CHUNK_DURATION = 0.1
CHUNK_SIZE = int(TARGET_SAMPLE_RATE * CHUNK_DURATION)

SILENCE_DURATION = 1.0

START_MULTIPLIER = 1.5
STOP_MULTIPLIER = 1.2


model = WhisperModel("tiny", device="cpu", compute_type="float32")


def listen_and_transcribe():

    print("Calibrating silence... Do not speak.")

    silence_volumes = []

    with sd.InputStream(
        samplerate=TARGET_SAMPLE_RATE,
        channels=1,
        blocksize=CHUNK_SIZE,
        dtype="float32"
    ) as stream:


        # CALIBRATION
        # CALIBRATION
        print("Calibrating... wait 1 second")
        for i in range(30): # Increased to 30
            chunk, _ = stream.read(CHUNK_SIZE)
            if i < 10: continue # Skip the first 10 chunks (initialization noise)
            volume = np.sqrt(np.mean(chunk**2))
            silence_volumes.append(volume)

        silence_mean = np.mean(silence_volumes)

        START_THRESHOLD = silence_mean * START_MULTIPLIER
        STOP_THRESHOLD = silence_mean * STOP_MULTIPLIER


        print(f"Silence level: {silence_mean:.4f}")
        print(f"Start threshold: {START_THRESHOLD:.4f}")
        print(f"Stop threshold: {STOP_THRESHOLD:.4f}")


        frames = []
        recording = False
        silent_time = 0


        print("\nListening... Speak now")


        while True:

            chunk, _ = stream.read(CHUNK_SIZE)

            volume = np.sqrt(np.mean(chunk**2))

            print(f"Volume: {volume:.4f} Recording: {recording}")


            # START
            if not recording:

                if volume > START_THRESHOLD:

                    print("Recording started")

                    recording = True
                    frames.append(chunk)

                continue


            # RECORD
            frames.append(chunk)


            # STOP
            if volume < STOP_THRESHOLD:

                silent_time += CHUNK_DURATION

                if silent_time >= SILENCE_DURATION:

                    print("Recording stopped")

                    break

            else:

                silent_time = 0


    # SAFETY CHECK
    if len(frames) == 0:

        print("No speech detected")

        return ""


    audio = np.concatenate(frames).flatten()


    # normalize safely
    max_val = np.max(np.abs(audio))

    if max_val > 0:

        audio = audio / max_val


    print("Transcribing...")


    segments, info = model.transcribe(

        audio,

        language="en",

        vad_filter=False

    )


    text = ""

    for segment in segments:

        text += segment.text


    return text



result = listen_and_transcribe()


print("\nRESULT:")

print(result)