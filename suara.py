import speech_recognition as sr

# r = sr.Recognizer()
# r.energy_threshold=1000
#
# with sr.Microphone() as source:
#     while True:
#         print('Bilang sesuatu : ')
#         audio = r.listen(source)
#         try:
#             suara = format(r.recognize_google(audio))
#             print(suara)
#             try:
#                 if suara == 'hey':
#                     print('Ada yang bisa saya bantu')
#                     audio = r.listen(source)
#                     print('You said : {}'.format(r.recognize_google(audio)))
#             except:
#                 print('Saya tidak dengar')
#         except:
#             print('Saya tidak dengar')

r = sr.Recognizer()

with sr.Microphone() as sourc:
    print("Bilang Sesuatu")
    audio = r.listen(sourc)

try:
    print("TEXT : "+ r.recognize_google(audio, language='ENG'))
except:
    pass