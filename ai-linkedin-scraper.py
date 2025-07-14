import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM

# from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Bedrock
import boto3
import streamlit as st

PersonName = "Elon Musk"

if __name__ == "__main__":
    print("Hello LangChain!")

    # Load environment variables from .env file
    # load_dotenv()

    # # Fetch credentials from environment
    # aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    # aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    # aws_session_token = os.getenv("AWS_SESSION_TOKEN")  # Optional
    # aws_region = os.getenv("AWS_REGION", "eu-west-1")  # Default to 'eu-west-1' if not set

    # Optional: Set up a boto3 client for Bedrock
    # Create a boto3 client using the loaded credentials
    # bedrock_client = boto3.client(
    #     "bedrock-runtime",
    #     region_name=aws_region,
    #     aws_access_key_id=aws_access_key,
    #     aws_secret_access_key=aws_secret_key,
    #     aws_session_token=aws_session_token  # Only include if not None
    # )

    # Initialize the Bedrock LLM with Titan Text G1 - Lite
    # llm = Bedrock(
    #     model_id="amazon.titan-text-lite-v1",
    #     client=bedrock_client,
    #     model_kwargs={
    #         "temperature": 0.2,
    #         "maxTokenCount": 512,
    #         "topP": 0.9,
    #         "stopSequences": [],
    #     },
    # )
    llm = OllamaLLM(
        model="gemma:latest",
        temperature=0.2,
    )
    # Define a prompt template for generating summaries
    summary_template = """given the infomation about a person {person} from I want you to create:
    1. A short summary of the person
    2. intresting facts about the person
    """
    summary_prompt = PromptTemplate(
        input_variables=["person"],
        template=summary_template,
    )

    chain = summary_prompt | llm | StrOutputParser()
    response = chain.invoke(input={"person": {PersonName}})
    print(response)

# # Streamlit UI
# st.title("🔍 LinkedIn Profile Explorer USing AI")
# name = st.text_input("Enter a person's name", placeholder="e.g., Elon Musk")

# if name:
#     with st.spinner("Generating summary..."):
#         result = chain.invoke({"person": name})
#         st.subheader("📝 Summary & Facts")
#         st.write(result)

#     # Display image (example for Elon Musk)
#     if name.lower() == "elon musk":
#         st.subheader("📸 Photo")
#         st.image("https://media.gettyimages.com/photos/elon-musk-attends-the-10th-annual-breakthrough-prize-ceremony-picture-id1492022342", caption="Elon Musk", use_column_width=True)
