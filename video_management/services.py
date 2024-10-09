from sqlalchemy.orm import Session
from models import Video
from fastapi import HTTPException

class VideoService:
    def __init__(self, db: Session):
        self.db = db

    def create_video(self, title: str, description: str, url: str):
        video = Video(title=title, description=description, url=url)
        self.db.add(video)
        self.db.commit()
        self.db.refresh(video)
        return video

    def get_video_by_title(self, title: str):
        return self.db.query(Video).filter(Video.title == title).first()

    def update_video(self, video_id: int, title: str, description: str, url: str):
        video = self.db.query(Video).filter(Video.id == video_id).first()
        if not video:
            raise HTTPException(status_code=404, detail="Video not found")
        video.title = title
        video.description = description
        video.url = url
        self.db.commit()
        return video

    def delete_video(self, video_id: int):
        video = self.db.query(Video).filter(Video.id == video_id).first()
        if not video:
            raise HTTPException(status_code=404, detail="Video not found")
        self.db.delete(video)
        self.db.commit()
        return {"message": "Video deleted successfully"}
