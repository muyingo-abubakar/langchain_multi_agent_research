from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import web_search, scrape_url
from dotenv import load_dotenv

load_dotenv()

# model initialization
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# 1st Agent : Search Agent


def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],

    )

# 2nd Sgent : Reader Agent


def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url],

    )


# writer chain

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. write clear, structured and insightful repors"),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
-Introduction
_Key Findings (minimum 3 well-explained points)
-conclusion
-Sources (list all URLs found in the research)

Be detailed, fuctual and professional.""")
])

writer_chain = writer_prompt | llm | StrOutputParser()


# critic_chain

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific"),
    ("human", """Review the research report below and evaluate it strictly.

    Report:
    {report}

    Respond in this exact format:

    Score:x/10

    Strengths:
    - ...
    - ...

    Areas to improve:
    - ...
    - ...

    One line verdict:
    ..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()
