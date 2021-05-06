import base64

def DecodeFileToBase64(file, storage_location):
    audio = base64.b64decode(file)

    with open(storage_location, "wb") as f:
        f.write(audio)
        f.close()
