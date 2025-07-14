import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import Tool
from tools.tavily import get_profile_url
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)


class LookUp:
    def __init__(self, name: str):
        load_dotenv()
        self._name = name

    def linkedin_lookup(self) -> str:
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )
        template = """given the full name {name_of_person} I want you to provide me the linkedin profile page. Your answer should contain only the URL."""
        prompt_template = PromptTemplate(
            input_variables=["name_of_person"],
            template=template,
        )
        tool = Tool(
            name="LinkedIn Lookup",
            func=get_profile_url,
            description="Useful for getting LinkedIn URL page by name.",
        )
        react_prompt = hub.pull(
            "hwchase17/react"
        )  # React prompt template to send to LLM model
        agent = create_react_agent(
            llm=llm,
            tools=[tool],
            prompt=react_prompt,
        )
        agent_executor = AgentExecutor(
            agent=agent,
            tools=[tool],
            verbose=True,
        )
        result = agent_executor.invoke(
            input={"input": prompt_template.format(name_of_person=self._name)}
        )
        linkedin_url = result.get("output", "")
        print(f"LinkedIn URL for {self._name}: {linkedin_url}")
        return linkedin_url


if __name__ == "__main__":
    name = "ehsan tafehi"

    linkedin_url = LookUp(name).linkedin_lookup()
