 Setup

### 1. Create Virtual Environment

First, create and activate a virtual environment:

```sh
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### 2. Install Dependencies
```sh
pip install -r requirements.txt

### 3. create database
```sh
MONGO_URI=mongodb://localhost:27017/
DATABASE_NAME=mydatabase
UPLOAD_FOLDER=./uploads

### 4.Run the Application
```sh
uvicorn app.main:app --reload

swagger ui
http://127.0.0.1:8000/docs
