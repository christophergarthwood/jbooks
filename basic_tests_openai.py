import os
import openai

try:
    openai_api_key=os.getenv("OPENAI_API_KEY");
except Exception as e:
    print("ERROR: OPENAI_API_KEY environment variable not set, you cannot use OpenAI API functions without this key.")
    print("...check with your administrator for assistance procuring or registering the key.")
    exit(1) 

########################################
#Model Parameters
########################################
engine_name="CGW-LLM-GPT35TUBRO16K-SummaryTest"
model_temperature=0.7
#model_max_tokens=int(800)
model_max_tokens=8000
model_top_p=0.95
model_frequency_penalty=0
model_presence_penalty=0

########################################
#API Parameters
########################################
openai.api_type = "azure"
openai.api_base = "https://oai-nonprd-openai-poc.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
#openai.api_key=os.getenv("OPENAI_USFS_API_KEY")
openai.api_key=openai_api_key

openai.api_key = openai_api_key
#print(openai.Model.list())


print(f"Initiating simple ChatCompletion with information about the unix terminal.")
try:
#    completion = openai.ChatCompletion.create(model=engine_name,
#                                              messages=[{"role": "user", "content": "Hello world"}])
    message_text = [
                    {"role":"system", "content": "You are an AI assistant." },
                    {"role":"user",   "content": "Tell me about the unix terminal." }
                   ]

    completion_message = openai.ChatCompletion.create(
      engine=engine_name,
      messages = message_text,
      temperature=model_temperature,
      max_tokens=model_max_tokens,
      top_p=model_top_p,
      frequency_penalty=model_frequency_penalty,
      presence_penalty=model_presence_penalty,
      stop=None
    )
    resultant = completion_message["choices"][0]["message"]

except Exception as e:
    print("ERROR: openai.ChatCompletion failed.")
    print("...the following error resulted from the API call:")
    print(f"......{str(e)}")
    exit(1) 



print("Response:")
print("##################################################################")
print(resultant)
print("##################################################################")
