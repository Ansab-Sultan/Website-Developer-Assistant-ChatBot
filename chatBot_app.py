import os
from getpass import getpass
from langchain_community.llms import HuggingFaceHub

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
import streamlit as st
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline
from langchain.prompts import ChatPromptTemplate, FewShotPromptTemplate
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0'

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens = 256
)


llm = HuggingFacePipeline(pipeline=pipe)
examples = [
    {"input": "how to create the body of webpage using html",
     "output": """
CODE:
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Webpage Title</title>
</head>
<body>

    <h1>Hello, World!</h1>

    <p>This is a simple webpage created using HTML.</p>

    <!-- Add more content and elements here -->

</body>
</html>

EXPLAINATION:
-The <html> element is the root element of the HTML document.
-The <head> section contains meta-information about the HTML document, such as the character set, viewport settings, and the title of the webpage.
-The <body> section contains the content of the webpage, including headings (<h1>, <h2>, etc.), paragraphs (<p>), and other HTML elements.
"""},



    {"input": "how to create a div using html",
     "output": """
CODE:
<div>
    <!-- Your content goes here -->
</div>

EXPLAINATION:
-<div> elements are used inside the BODY of the webpage
-Using <div> elements and applying CSS styles to them allows you to create flexible and responsive layouts for your webpage. You can use different <div> elements to structure your content and apply styles selectively.
"""},



    {"input": "how to apply style in a website using css",
     "output": """
CODE:
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Webpage Title</title>
    <!-- Internal CSS styles -->
    <style>
        /* Define styles for the body element */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
        }

        /* Define styles for the h1 element */
        h1 {
            color: #0066cc;
        }
    </style>
</head>
<body>
    <!-- Your content goes here -->
</body>
</html>

EXPLAINATION:
-You can include the CSS styles directly within the <style> tags in the <head> section of your HTML file.
"""},

]


from langchain.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("assistant", "{output}"),
    ]
)
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
    input_variables = ["input"]
)


final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert website developer that helps in developing websites using HTML and CSS"),
        few_shot_prompt,
        ("human", "{input}"),

    ]
)

from langchain.chains import ConversationChain

from langchain.chains.conversation.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(
    memory_key="history",
    input_key="input",
    k=2
)

conv_chain = LLMChain(
    llm = llm,
    prompt = final_prompt,
    verbose = True,
    memory = memory
)
template = """
You are an expert website developer that helps in developing websites using HTML and CSS. You check the Previous Conversation to check the pattern of output.

Previous Conversation:

{history}

Conversation:
Human: {input}

"""
prompt = PromptTemplate(
    input_variables=["history", "input"], template=template
)
conv_chain1 = ConversationChain(
    llm = llm,
    prompt = prompt,
    verbose = True,
    memory = memory
)
def main():
    st.title("Website Developer Assistant")

    with st.expander("Conversation"):
        history = st.empty()
        input_message = st.text_input("Human:")
        if input_message:
            response = conv_chain.run(input=input_message)
            history.write("Human: " + input_message + "\n")
            history.write("Assistant: " + response + "\n")
            while True:
                follow_up_message = st.text_input("Human (Follow-up):")
                if follow_up_message == 'exit' or not follow_up_message:
                    break
                response = conv_chain1.run(input=follow_up_message)
                history.write("Human: " + follow_up_message + "\n")
                history.write("Assistant: " + response + "\n")

if __name__ == "__main__":
    main()





