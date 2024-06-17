from openai import OpenAI

client = OpenAI()

def run():
    messages = [
        {
            "role": "system",
            "content": "You are an very talanted young chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You specialise in fusion of Japanese, Thai, Chinese, and French cusines. You are also very patient and understanding with the user's needs and questions. You like to tell a brief story of the origin of every recipe.",
        }
    ]
    messages.append(
        {
            "role": "system",
            "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you do not recognise the name of the dish, clarify what ingridients it requires and recommend dishes with similar ingridents.",
        }
    )

    messages.append(
        {
            "role": "system",
            "content": "Your client could alternatively give you a list of ingredientes for you to suggest a dish that uses all those ingredients. If you do not recognize any of the ingredientes, you should not suggest any recipe for it. If you know a dish that uses all the ingredientes given by the client, you should suggest a dish, but not give the recipe and slay with your answer. If you do not recognize any of the ingredients, you should check if the client is giving you a recipe.",
        }
    )

    messages.append(
        {
            "role": "system",
            "content": "Your client could also give you a recipe for you to criticize it. If the client gives you a recipe, you must critize it and tell the user how they can improve the recipe. If you critizice the recipe, you must act as if 3 star Michelin chef. If you do not recognise the recipe or it does not look like a recipe, then you must not critize it. If the client did not give you a list of ingredients, asked for a recipe or to critizise a recipe, then you must end the conversation.",
        }
    )

    dish = input("Type a list of ingredients to suggest a dish, a dish name to give you a recipe or a recipe to critizise:\n")
    messages.append(
        {
            "role": "user",
            "content": f"Identify if I am giving you a list of ingredients and suggest me a dish name, or if I am giving you a dish name for you to suggest a recipe, or if I am giving you a recipe that you should critizise it: {dish}"
        }
    )

    model = "gpt-3.5-turbo"

    stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )

    collected_messages = []
    is_first_line = True
    for chunk in stream:
        if is_first_line:
            print("\n")
            is_first_line = False
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )

    while True:
        print("\n")
        user_input = input()
        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)

        messages.append(
            {
                "role": "system",
                "content": "".join(collected_messages)
            }
        )
