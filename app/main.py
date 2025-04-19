from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routes import router as api_v1_router
import uvicorn
app = FastAPI(
    title="Mietkautionstool API",
    description="API for managing rental deposits",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Mietkautionstool API"} 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)