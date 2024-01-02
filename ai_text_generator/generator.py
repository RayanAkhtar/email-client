import os
import time
import text_menu.user_io as io
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()


def generate_text_chained(prompts):
    # Takes in multiple prompts and outputs the result, using the previous result to form the next result
    prompts = prompts.split(";")

    prev_results = ""
    final_result = ""
    prompt_number = 1
    for prompt in prompts:
        start_time = time.time()
        iteration = 1
        io.clear_screen()
        print(f"Chain size of {len(prompts)}")
        print(f"Currently processing prompt number {prompt_number}...")
        prompt_number += 1
        while True:
            io.clear_screen()
            print(f"Currently processing prompt number {prompt_number - 1}...")
            try:
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": prompt + prev_results}
                    ]
                )
                break
            except openai.RateLimitError:
                curr_time = int(time.time() - start_time)
                print("Currently waiting on rate limit to reset, may take up to 60 secs")
                print(f"Time elapsed: {curr_time} / 60")
                print("waiting" + get_dots(iteration))
                iteration += 1
                if iteration > 3:
                    iteration -= 3

                if curr_time > 60:
                    print("Reached max number of daily ai prompts (max 200 prompts per day)")
                    input("Press enter to return to the main menu")
                    io.clear_screen()
                    return "FAILED"  # not returning an error here as this will be a repetitive error
                time.sleep(1)

        final_result = completion.choices[0].message.content
        prev_results += final_result

    return "{" + final_result + "}"


def get_dots(number):
    to_return = ""
    for i in range(number):
        to_return += "."
    return to_return
