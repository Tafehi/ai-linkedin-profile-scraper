import os
from dotenv import load_dotenv

from utils.linkedin import LinkedInProfileScraper
from agents.lookup import LookUp
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

mock = True  # Set to True to use mock data, False to scrape live data
#name = "Ehsan Tafehi"  # Example name, can be replaced with user input

class Application:
    def __init__(self, name: str, mock: bool):
        load_dotenv()
        self._name = name
        self._mock = mock
        self._model = os.getenv("LLM_MODEL")

    def run(self):
        if self._mock:
            scraper = LinkedInProfileScraper(
                linkedin_url="https://www.linkedin.com/in/ehsan-tafehi/",
                mock=self._mock,
            )
            linked_data = scraper.scrape_linkedin_profile()
            linkedin_url = "https://www.linkedin.com/in/ehsan-tafehi/"
        else:
            linkedin_url = LookUp(self._name).linkedin_lookup()
        return {"url": linkedin_url}

    def run_model(self, linkedin_url: str):
        print(f"Running model with LinkedIn URL: {linkedin_url}")
        llm = ChatOpenAI(
            model=self._model,
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )
        summary_template = """
        Given the LinkedIn information {information} about a person, provide a:
        1. short summary.
        2. two interesting facts about the person.
        3. top 5 list of skills.
        4. a list of experiences.
        5. his or her education.
        Your answer should be in a JSON format with the following keys: summary, facts, skills, experiences, education.
        """
        prompt_template = PromptTemplate(
            input_variables=["information"],
            template=summary_template,
        )
        output_parser = StrOutputParser()

        # Scrape LinkedIn profile data
        scraper = LinkedInProfileScraper(linkedin_url=linkedin_url["url"], mock=self._mock)
        profile_data = scraper.scrape_linkedin_profile()

        # Generate response
        chain = prompt_template | llm | output_parser
        result = chain.invoke({"information": profile_data})
        return result

# if __name__ == "__main__":
#     app = Application(name, mock)
#     linkedin_url = app.run()
#     app.run_model(linkedin_url)

## Streamlit UI
st.set_page_config(page_title="🔍 LinkedIn Profile Explorer", layout="centered")
st.title("🔍 LinkedIn Profile Explorer Using AI")

name = st.text_input("Enter a person's name", placeholder="e.g., Ehsan Tafehi")

if name:
    with st.spinner("🔎 Looking up profile and generating summary..."):
        app = Application(name, mock)
        linkedin_url = app.run()
        result = app.run_model(linkedin_url)

        try:
            import json
            parsed = json.loads(result)

            # Display profile picture (placeholder or based on name)
            st.image("https://via.placeholder.com/150", caption=name.title(), use_column_width=False)

            st.subheader("📝 Summary")
            st.write(parsed.get("summary", "No summary available."))

            st.subheader("✨ Interesting Facts")
            for fact in parsed.get("facts", []):
                st.markdown(f"- {fact}")

            st.subheader("💼 Top 5 Skills")
            for skill in parsed.get("skills", []):
                st.markdown(f"- {skill}")

            st.subheader("📊 Experiences")
            for exp in parsed.get("experiences", []):
                st.markdown(f"- {exp}")

            st.subheader("🎓 Education")
            for edu in parsed.get("education", []):
                st.markdown(f"- {edu}")

        except Exception as e:
            st.error("⚠️ Failed to parse the model output. Please check the format.")
            st.text(result)
