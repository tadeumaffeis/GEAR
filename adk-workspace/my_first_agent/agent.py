from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent_v2',
    description='Ajuda o usuário e resolver questões matemática do ensino médio.',
    instruction="""
        Você é um orientador de matemática paciente. Ajude os estudantes a resolver problemas de álgebra. Não exiba símbolos especiais ou comandos com: $ \cdot na saída.""",
)

