import argparse
import os
import openai
#import wandb

#run = wandb.init(project='GPT-4 in Python')
#prediction_table = wandb.Table(columns=["prompt", "prompt tokens", "completion", "completion tokens", "model", "total tokens"])

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--apikey', type=str, required=True,
                        help="Open AI Api Key.")
    parser.add_argument('--chem_desc', type=str, required=True,
                         default="climate, climate_change, language, forest, biodiversity, archaeology, linguistic, ocean, ecological, heritage, child, land, cognitive, sea, marine",
                         help="Chemical description to use be labelled.")
    
    args = parser.parse_args()

    openai.api_key = args.apikey
    
    gpt_prompt = f"Give me a label for this set of words: {args.chem_desc}"
    #print(gpt_prompt)

    message=[{"role": "user", "content": gpt_prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = message,
        temperature=0.2,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    response = response["choices"][0]["message"]["content"]
    print(response)
    return response
    
if __name__ == '__main__':
    main()