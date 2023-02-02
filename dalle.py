import openai # main library
import datetime # these libraries will be required as the code expands. do it step by step
from openai.error import InvalidRequestError # except
import webbrowser # generating the image in a new web browser
from base64 import b64decode # jpg 


def image_gen(prompt, n=1, size = '512x512', output_format = 'url'): # function that takes the user's prompt, number of images, size of images and web output
    try:
        images = [] #empty list
        response = openai.Image.create(
            prompt = prompt, #required variables. see documentation
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

        return {'created': datetime.datetime.fromtimestamp(response['created']), 'images': images} # return datetime of creation and image

    except InvalidRequestError as e: # new variable
        print(e)


API_KEY = # your api
openai.api_key = API_KEY

SIZES = ('1024x1024', '512x512', '256x256')
prompt = str(input("What do you wanna do today? ")) # use your imagination
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
        with open(f"{prefix}_{index}.jpg","wb") as f: #this is preparing the browser for jpg
            f.write(b64decode(image))
