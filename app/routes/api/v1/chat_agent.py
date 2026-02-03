from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.models.agents.chat_agent_models import ChatRequest

from app.services.agents.chat_agent_services import ChatAgentServices

router = APIRouter()
services = ChatAgentServices()

@router.post("/chat-agent", status_code=status.HTTP_200_OK)
async def chat_agent(agent_input: ChatRequest) -> dict:
    try:
        response = services.run(query=agent_input.user_message)
        
        return JSONResponse(content={"data": response, "message": "Agent Message", "error": None, "status": True})

    except Exception as e:
            return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "data": None,
                "message": "Internal server error",
                "error": str(e),              
                "status": False,
            },
        )
