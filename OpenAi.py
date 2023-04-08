import openai
import os 
from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv('API_KEY')    # You have to put your api key here

# list engines
engines = openai.Engine.list()



# create a completion
choice = int(input("Voulez vous une réponse à une question (1) ou générer une image (2) ?   "))

while choice != 1 and choice !=2:
    print("Wront input , choose between 1 ( image generation) and 2 ( text prompt )")
    choice = input("Voulez vous une réponse à une question 1 ou générer une image 2 ?  ")
    
if choice==1:
    prompt = input()
    completion = openai.Completion.create(engine="text-davinci-003",
                                           prompt=prompt,
                                           temperature=0.4,
                                           max_tokens=180,
                                           top_p=1, 
                                           frequency_penalty=0,
                                           presence_penalty=0,
                                           echo=True)
elif choice == 2:
    prompt = input()
    ShowImage=openai.Image.create(
    prompt=prompt,
    n=2,
    size="1024x1024"
)



#Complex_Completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt,temperature=0,max_tokens=1,top_p=0,logprobs=10)


#
if choice ==1:
    print("Output :  "+completion.choices[0].text)
elif choice == 2:
    print(ShowImage)
#print(Complex_Completion["choices"][0]["text"])