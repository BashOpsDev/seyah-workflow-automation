# Seyah Space - Smart Workflow Automation API

Production-ready AI-powered workflow automation system built for **Seyah Space**. Demonstrates expertise in FastAPI, async Python, LLM integration, and scalable backend architecture.

🟢 **Live API:** https://seyah-workflow-automation.onrender.com/docs  
🔑 **API Key:** `seyah-demo-key-2026`  
👨‍ **Built by:** Bashir (BashOps)

---

## 🚀 Quick Start

**Try the live API right now:**

1. Go to https://seyah-workflow-automation.onrender.com/docs
2. Click **Authorize** (top right)
3. Enter API Key: `seyah-demo-key-2026`
4. Try any endpoint!

**Example: Automate a task**
```bash
curl -X POST "https://seyah-workflow-automation.onrender.com/api/v1/automate/task" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: seyah-demo-key-2026" \
  -d '{
    "description": "Summarize the benefits of FastAPI for building modern APIs"
  }'
```

---

## ✨ Features

### **1. Workflow Creation & Management**
- Create multi-step automation workflows
- Store workflow definitions in PostgreSQL
- Execute workflows on-demand

### **2. AI-Powered Task Automation**
- Natural language task execution
- Groq LLM integration (Mixtral-8x7b)
- Sub-200ms response times
- Structured JSON output

### **3. Intelligent Document Processing**
- Extract entities from text
- Auto-summarization
- Categorization & tagging
- Key information extraction
### **4. Workflow Execution Engine**
- Sequential step execution
- Progress tracking
- Status monitoring
- Error handling

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Framework** | FastAPI 0.109.0 |
| **Language** | Python 3.11+ |
| **Database** | PostgreSQL / SQLite (Async SQLAlchemy) |
| **AI/LLM** | Groq API (Mixtral-8x7b-32768) |
| **Validation** | Pydantic V2 |
| **Deployment** | Render |
| **API Docs** | OpenAPI 3.1 / Swagger UI |

---

## 📡 API Endpoints

### **Workflows**
- `POST /api/v1/workflows/create` - Create new workflow
- `POST /api/v1/workflows/{id}/execute` - Execute workflow

### **Automation**
- `POST /api/v1/automate/task` - AI-powered task execution
- `POST /api/v1/process/document` - Intelligent document processing

### **Health**
- `GET /` - Root health check

---

## 🏗️ Architecture

### **Database Strategy**
The app uses SQLAlchemy async engine with a flexible configuration:
- **Development/Demo:** SQLite + aiosqlite (zero setup)
- **Production:** PostgreSQL + asyncpg (one-line toggle)

This allows instant testing without Docker while maintaining production readiness.

### **LLM Integration**
**Why Groq?**
- 10-50x faster than traditional LLM APIs
- Critical for real-time workflow automation- Cost-effective for high-volume tasks
- Mixtral-8x7b provides excellent reasoning capabilities

### **Async Architecture**
- All endpoints use `async/await`
- Non-blocking database queries
- High concurrency support
- Optimized for I/O-bound operations

---

## 📦 Installation (Local Setup)

### **1. Clone the Repository**
```bash
git clone https://github.com/BashOpsDev/seyah-workflow-automation.git
cd seyah-workflow-automation
```

### **2. Create Virtual Environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure Environment**
```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your Groq API key
# Get yours at: https://console.groq.com
```

**.env file:**
```env
DATABASE_URL=sqlite+aiosqlite:///./seyah_demo.db
GROQ_API_KEY=your_groq_api_key_here
API_KEY=seyah-demo-key-2026
SECRET_KEY=your_secret_key_here```

### **5. Run the Application**
```bash
python run.py
```

**Server starts at:** http://localhost:8000  
**API Docs:** http://localhost:8000/docs

---

## 🧪 Testing

### **Test Workflow Creation**
```bash
curl -X POST "http://localhost:8000/api/v1/workflows/create" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: seyah-demo-key-2026" \
  -d '{
    "name": "Daily News Summary",
    "description": "Summarize top AI news daily",
    "steps": [
      {"step_id": "fetch", "action": "scrape", "parameters": {"url": "https://news.ycombinator.com"}},
      {"step_id": "summarize", "action": "llm", "parameters": {"max_length": 500}},
      {"step_id": "email", "action": "send", "parameters": {"to": "user@example.com"}}
    ]
  }'
```

### **Test AI Task Automation**
```bash
curl -X POST "http://localhost:8000/api/v1/automate/task" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: seyah-demo-key-2026" \
  -d '{
    "description": "Explain the benefits of async Python for web development"
  }'
```

### **Test Document Processing**
```bash
curl -X POST "http://localhost:8000/api/v1/process/document" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: seyah-demo-key-2026" \
  -d '{
    "content": "Seyah Space is building AI-powered automation tools using Python and FastAPI to help businesses streamline workflows and increase productivity."
  }'
```
---

## 🚢 Deployment (Render)

### **1. Push to GitHub**
```bash
git add .
git commit -m "Production-ready workflow automation API"
git push origin main
```

### **2. Deploy on Render**
1. Go to https://render.com
2. Click **New** → **Web Service**
3. Connect your GitHub repo
4. Configure:
   - **Name:** seyah-workflow-automation
   - **Region:** Choose closest to you
   - **Branch:** main
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### **3. Add Environment Variables**
In Render dashboard, add:
- `DATABASE_URL` (Render auto-creates PostgreSQL)
- `GROQ_API_KEY=your_key_here`
- `API_KEY=seyah-demo-key-2026`
- `SECRET_KEY=your_random_secret`

### **4. Deploy**
Click **Create Web Service** → Wait 3-5 minutes → Done!

---

## 📁 Project Structure
## 🛠️ Tech Stack
- **Framework:** FastAPI, Python 3.10+
- **Database:** PostgreSQL / SQLite (via SQLAlchemy Async)
- **AI Integration:** Groq API
- **Validation:** Pydantic V2

## 📦 Installation & Immediate Run

1. **Clone & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
