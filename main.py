from fastapi import FastAPI, HTTPException
from models import EmailRequest, EmailResponse
from logic import enhance_email
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()

origins = ['https://code-switch-ui-git-main-gabe-lopezs-projects.vercel.app', 
           'https://code-switch-96e4t5pb0-gabe-lopezs-projects.vercel.app',
           'https://code-switch-ui.vercel.app']

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,  # Or set ["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/code_switch", response_model=EmailResponse)
async def enhance_email_endpoint(request: EmailRequest):
    if not request.user_input:
        raise HTTPException(status_code=400, detail="User input is required.")

    try:
        enhanced_email = await enhance_email(
            user_input=request.user_input,
            scenario=request.scenario,
            tone=request.tone,
            language=request.language
        )
        return {"enhanced_email": enhanced_email}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
