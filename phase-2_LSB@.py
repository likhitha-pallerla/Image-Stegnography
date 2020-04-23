# Speech to text - 
def getTextFromMicrophone():
    import speech_recognition as sr

    rec = sr.Recognizer()

    with sr.Microphone() as mic:
        print('Please say the message that you want to hide...')
        audio = rec.listen(mic)
        print('Message recorded!')

    try:
        message = rec.recognize_google(audio)
        print('Message to be hidden:' + message)
        return message
    except:
        print('It just exploded!!!')

# resources
inImgPNG = 'dexterLab.png'
inImgJPG = 'dexterLab2.jpg'

outImgPNG = 'topSecret.png'
outImgJPG = 'topSecret2.jpg'

msg = 'This is likhitha.'

# 1) hide
from stegano import lsb

# we are hiding the text here
#lsb.hide(inImgPNG, message=msg).save(outImgPNG)

# # we are getting text from the image
message = lsb.reveal(outImgPNG)
print(f'Reveal message: {message}')


# 2) hide using generators
from stegano.lsbset import generators
from stegano import lsbset

# msg = getTextFromMicrophone()

# # hide message
# lsbset.hide(
#     inImgPNG,
#     msg,
#     generators.eratosthenes()
# ).save(outImgPNG)

# # reveal message
# message = lsbset.reveal(
#     outImgPNG, 
#     generators.eratosthenes()
# )
# print(F'Reveal message: {message}')


# 4) Hide in the specification
# wiki: exif = Exchangeable image file format
# only works for JP[E]G and TIFF
from stegano import exifHeader as spec

#spec.hide(inImgJPG, outImgJPG, msg)

#message = spec.reveal(outImgJPG)
#print(F'Reveal message: {message}')