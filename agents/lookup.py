import os
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
class LookUp:
    def __init__(self, name: str):
        load_dotenv()
        self._name = name
        self.__openapi_key = os.getenv("OPENAI_API_KEY")

    def _lookup_func(self, name_of_person: str) -> str:
        """Function to be used by the Tool to generate LinkedIn URL."""
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            openai_api_key=self.__openapi_key,
        )
        prompt = PromptTemplate(
            input_variables=["name_of_person"],
            template="Given the full name {name_of_person}, provide only the LinkedIn profile URL.",
        )
        chain = prompt | llm | StrOutputParser()
        return chain.invoke({"name_of_person": name_of_person})

    def linkedin_lookup(self) -> str:
        tool = Tool(
            name="LinkedIn Lookup",
            func=self._lookup_func,
            description="Useful for getting LinkedIn URL page by name.",
        )

        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            openai_api_key=self.__openapi_key,
        )

        react_prompt = hub.pull("hwchase17/react")
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

        result = agent_executor.invoke({"input": self._name})
        linkedin_url = result.get("output", "")
        print(f"LinkedIn URL for {self._name}: {linkedin_url}")
        return linkedin_url

if __name__ == "__main__":
    name = "ehsan tafehi"
    linkedin_url = LookUp(name).linkedin_lookup()
