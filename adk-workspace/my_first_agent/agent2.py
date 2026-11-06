"""
Exemplo completo: executar um agente do ADK de modo programático
Copie este bloco de código inteiro para executá-lo em um script ou notebook Python.
"""
# Etapa 1: instalar o ADK (faça a execução no terminal ou na célula do notebook)
# pip install google-adk
# Etapa 2: definir a chave de API
# Opção A: definir como variável de ambiente antes da execução
# export GOOGLE_API_KEY=your-api-key-here
# Opção B: remover a marca de comentário e usar este código:
import os
if not os.environ.get("GOOGLE_API_KEY"):
    raise RuntimeError("Defina GOOGLE_API_KEY no terminal antes de executar.")
os.environ['GOOGLE_GENAI_USE_VERTEXAI'] = 'FALSE'
# Etapa 3: importar as bibliotecas necessárias
import asyncio
from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

# Etapa 4: definir o agente
agent = Agent(
    model="gemini-3.5-flash",
    name="math_tutor",
    instruction="""Você é um orientador de matemática paciente.
    Ajude os estudantes nas etapas de resolução dos problemas.
    Dê as respostas de uma vez e ajude-os a encontrar as soluções.
    Elimine simbolos com $** ou $ da resposta."""
)

# Etapa 5: configurar a sessão e o Runner
APP_NAME = "math_tutor_app"
USER_ID = "student_1"
SESSION_ID = "session_001"
session_service = InMemorySessionService()
runner = Runner(
    agent=agent,
    app_name=APP_NAME,
    session_service=session_service
)
# Etapa 6: definir a função assíncrona para executar o agente
async def run_agent():
    # Criar a sessão
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    print(f"Session created: {SESSION_ID}\n")
    # Preparar a mensagem do usuário
    user_message = Content(
        role="user",
        parts=[Part(text="Como eu resolvo 2x + 5 = 13?")]
    )
    # Executar o agente e coletar a resposta
    print("Usuário: Como eu resolvo 2x + 5 = 13?\n")
    print("Agente: ", end="")
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_message
    ):
        # Mostrar a resposta final
        if event.is_final_response() and event.content and event.content.parts:
            print(event.content.parts[0].text)
            print('\n')
# Etapa 7: executar o agente
# Para Jupyter/Colab: usar await diretamente
# await run_agent()
# Para scripts Python: usar asyncio.run()

asyncio.run(run_agent())
