# Video Management API

A RESTful API for managing videos using FastAPI. This API allows users to upload, search, update, and delete videos.

## Features

- **Upload Video**: Upload video files.
- **Search Video**: Find videos by title.
- **Update Video**: Modify video details by ID.
- **Delete Video**: Remove videos by ID.

## Getting Started

### Prerequisites

- Python 3.7+

### Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd video_management
   
2. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: `venv\Scripts\activate`

3. **Install Dependencies:**
    ```bash
    pip install fastapi uvicorn sqlalchemy python-multipart
    
4. **Run the Application**
    ```bash
    uvicorn main:app --reload
      
5. **Access the API**
    ```bash
    Visit http://127.0.0.1:8000/docs for API documentation.
