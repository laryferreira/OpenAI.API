import openai

API_KEY = # your api
openai.api_key = API_KEY

model = 'text-davinci-003' # id of the model that we're using
continuar=True #used this as a counter, did not use 'continue' as it is an reserved word

while continuar:
    sentence = input("Chat: ") #where the user will put the request
    if sentence=='': #stop point
        continuar=False
    else:
        full_response = openai.Completion.create(
            prompt=sentence,
            model=model, #model receives the parameter model
            max_tokens=800, #lenght of your response
            temperature=0.4 #risks and creativity of the response
        )

        for result in full_response.choices: 
            text_response = result.text #this output prints only the response, if you want to, you can print full response

        print(text_response)

