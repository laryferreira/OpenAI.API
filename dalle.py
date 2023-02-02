import openai 
import datetime 
from openai.error import InvalidRequestError
import webbrowser
from base64 import b64decode


def image_gen(prompt, n=1, size = '512x512', output_format = 'url'):
    try:
        images = []
        response = openai.Image.create(
            prompt = prompt,
            n = n,
            size = size,
            response_format = output_format
        )
        if output_format == 'url':
            for image in response['data']:
                images.append(image.url)

        elif output_format == 'b64_json':
            for image in response['data']:
                images.append(image.b64_json)

        return {'created': datetime.datetime.fromtimestamp(response['created']), 'images': images}

    except InvalidRequestError as e:
        print(e)


API_KEY = # your api
openai.api_key = API_KEY

SIZES = ('1024x1024', '512x512', '256x256')
prompt = str(input("What do you wanna do today? "))
choice = int(input("Enter 0 to URL and 1 to save as JPG"))
if choice == 0:
    # generate url image
    response = image_gen(prompt, n=2, size= SIZES[1])
    time_stamp = response['created']
    print(time_stamp)
    for image in response['images']:
        webbrowser.open(image)

elif choice == 1:
    # generate jpg image
    response = image_gen(prompt, n=2, size=SIZES[1], output_format='b64_json')
    prefix = 'openai_gen'
    for index, image in enumerate(response['images']):
        with open(f"{prefix}_{index}.jpg","wb") as f:
            f.write(b64decode(image))
