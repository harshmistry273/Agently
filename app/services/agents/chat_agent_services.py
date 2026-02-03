from crewai import Agent, Task, Crew, LLM

from app.core.config import settings


class ChatAgentServices:
    def __init__(self):
        self.llm = LLM("groq/llama-3.3-70b-versatile", api_key=settings.GROQ_API_KEY)
        self.agent = self._initialize_agent()

    def _initialize_agent(self) -> Agent:
        return Agent(
            role="Conversational AI Assistant",
            goal=(
                "Help users by answering their questions clearly, briefly, and in a user-friendly manner."
            ),
            backstory=(
                "This assistant was created by Harsh, a 22-year-old master's student passionate "
                "about building practical AI systems and helpful developer tools. The assistant is "
                "designed to communicate in a simple, friendly, and efficient way while solving user queries."
            ),
            llm=self.llm,
        )

    def _initialize_task(self) -> Task:
        return Task(
            description=(
                "Respond to the following user query in a short, clear, and user-friendly way:\n\n"
                "User Query: {query}\n\n"
                "Keep the answer concise, helpful, and conversational."
            ),
            expected_output=(
                "A short, friendly, and accurate response that directly addresses the user's query."
            ),
            agent=self.agent,
        )

    def run(self, query: str) -> str:
        task = self._initialize_task()
        crew = Crew(agents=[self.agent], tasks=[task], verbose=True)
        agent_response = crew.kickoff(inputs={"query": query}).raw

        return agent_response
