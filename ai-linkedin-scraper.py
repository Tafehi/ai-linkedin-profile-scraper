import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from utils.linkedin import LinkedInProfileScraper 
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Bedrock
import boto3
import streamlit as st


if __name__ == "__main__":
    
    print("Starting LinkedIn profile scraping...")
    scraper = LinkedInProfileScraper(
        linkedin_url="https://www.linkedin.com/in/ehsan-tafehi/", mock=True
    )
    linked_data = scraper.scrape_linkedin_profile()
    print(linked_data)

    # Simulate a request to the LinkedIn profile (this won't work without proper headers and authentication)

    print("Starting LinkedIn profile scraping...")

    llm = OllamaLLM(
        model="gemma:latest",
        temperature=0.4,
    )
    # Define a prompt template for generating summaries
    summary_template = """Give the linkedin profile information about a person {information} from I want you to create:
    1. A short summary of the person
    2. two interesting facts about the person
    3. the 3 top skills of the person which is highly on demand
    4. the last two company experiences of the person
    5. A list of the person's education
    6. A list of the person's languages
    """
    summary_prompt = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    chain = summary_prompt | llm | StrOutputParser()
    response = chain.invoke(input={"information": {linked_data}})
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
