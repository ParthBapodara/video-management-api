from fastapi import FastAPI, Depends, UploadFile, File
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from services import VideoService

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/videos/")
async def upload_video(title: str, description: str, url: str, db: Session = Depends(get_db)):
    video_service = VideoService(db)
    return video_service.create_video(title, description, url)

@app.get("/videos/search/")
async def search_video(title: str, db: Session = Depends(get_db)):
    video_service = VideoService(db)
    video = video_service.get_video_by_title(title)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video

@app.put("/videos/{video_id}")
async def update_video(video_id: int, title: str, description: str, url: str, db: Session = Depends(get_db)):
    video_service = VideoService(db)
    return video_service.update_video(video_id, title, description, url)

@app.delete("/videos/{video_id}")
async def delete_video(video_id: int, db: Session = Depends(get_db)):
    video_service = VideoService(db)
    return video_service.delete_video(video_id)
