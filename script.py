import requests
import pytesseract
from PIL import Image
from io import BytesIO
for i in range(1,505):
    response = requests.get(f'https://www.kristheeyakeerthanangal.org/assets/songs/{i}.png')
    image = Image.open(BytesIO(response.content))
    text = pytesseract.image_to_string(image,lang='ml+eng')
    with open(f'kristheeya_keerthanagal/{i}.txt','w') as file:
        file.write(text)
        file.close()


