from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.utils.logger import logger

# Import API routes
from app.api.routes import posts, anomalies, summary


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for startup and shutdown events"""
    # Startup
    logger.info("Starting Ad Insights Explorer API")
    logger.info("Server is ready to serve requests")

    yield

    # Shutdown
    logger.info("Shutting down Ad Insights Explorer API")


# Create FastAPI app with lifespan
app = FastAPI(
    title="Ad Insights Explorer API",
    description="API for analyzing ad content and detecting anomalies",
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

# Include API routes
app.include_router(posts.router, prefix="/api")
app.include_router(anomalies.router, prefix="/api")
app.include_router(summary.router, prefix="/api")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Ad Insights Explorer API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "posts": "/api/posts",
            "anomalies": "/api/anomalies",
            "summary": "/api/summary",
        },
    }


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
