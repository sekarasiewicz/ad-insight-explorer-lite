from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for startup and shutdown events"""
    # Startup
    logger.info("Starting FastAPI React Kit API")
    logger.info("Server is ready to serve requests")

    yield

    # Shutdown
    logger.info("Shutting down FastAPI React Kit API")


# Create FastAPI app with lifespan
app = FastAPI(
    title="FastAPI React Kit API",
    description="A simple API template for FastAPI and React projects",
    version="1.0.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "FastAPI React Kit API", "version": "1.0.0", "docs": "/docs"}


@app.get("/api/hello")
async def hello_world():
    """Hello World endpoint"""
    return {"message": "Hello, World!"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
