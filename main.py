import os
import chainlit as cl
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

# Set up model and config
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    tracing_disabled=True
)

# Agents with strict short instructions
career_agent = Agent(
    name="Career Roadmap Agent",
    instructions="In 1-2 short sentences, describe a suitable career path in simple language.",
    model=model,
)

skill_agent = Agent(
    name="Skill Development Agent",
    instructions="List only 3 important skills for this field. Keep the response short and direct.",
    model=model,
)

job_agent = Agent(
    name="Job Search Agent",
    instructions="Provide 2 simple job search tips for this field. No long explanation.",
    model=model,
)

# Chat start
@cl.on_chat_start
async def start_chat():
    await cl.Message(
        content="### 👨‍💼 Career Mentor by **Aqeel Ahmed Baloch**\n\nWelcome! Type your field of interest (e.g., `software development`, `data science`) to get started."
    ).send()

# Message handler
@cl.on_message
async def on_message(message: cl.Message):
    user_interest = message.content.strip()

    await cl.Message(content="Finding the best career path for you...").send()

    result1 = await Runner.run(career_agent, user_interest, run_config=config)
    await cl.Message(content=f"**Suggested Career**: {result1.final_output}").send()

    result2 = await Runner.run(skill_agent, user_interest, run_config=config)
    await cl.Message(content=f"**Important Skills**:\n{result2.final_output}").send()

    result3 = await Runner.run(job_agent, user_interest, run_config=config)
    await cl.Message(content=f"**Job Search Advice**:\n{result3.final_output}").send()
