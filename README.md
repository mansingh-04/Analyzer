# Website Analyzer Tool

A powerful tool that analyzes websites and provides actionable suggestions for improvement. The tool uses OpenAI's GPT-4 to analyze website content and offer targeted recommendations.

## Features

- Analyze websites via URL or HTML input
- Automatically categorize website type
- Detailed analysis of:
  - Call-to-Action (CTA) effectiveness
  - Visual hierarchy
  - Copy effectiveness
  - Trust signals
- Prioritized improvement suggestions for each component
- Expandable detailed recommendations

## Project Structure

```
websiteAnalyzer/
├── backend/           # Flask backend
│   ├── app.py         # Main server file
│   └── requirements.txt
└── frontend/          # React frontend
    ├── src/
    ├── public/
    └── package.json
```

## Setup Instructions

### Prerequisites

- Python 3.7+ for the backend
- Node.js for the frontend
- OpenAI API Key

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the backend directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   PORT=5050
   ```

6. Start the backend server:
   ```
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

## Usage

1. Access the application at `http://localhost:3000`
2. Choose an input method (URL or HTML)
3. Enter a website URL or paste HTML code
4. Click "Analyze Website"
5. View the analysis results and recommendations
6. Use the "Show More Suggestions" buttons to see additional recommendations for each component

## API Endpoints

### POST /components

Analyzes a website from URL or HTML input.

#### Request Body

```json
{
  "url": "https://example.com"
}
```

OR

```json
{
  "html": "<html>...</html>"
}
```

#### Response

```json
{
  "source": "https://example.com",
  "category": "E-commerce",
  "analysis": {
    "cta": { "observations": [...] },
    "visual_hierarchy": { "observations": [...] },
    "copy_effectiveness": { "observations": [...] },
    "trust_signals": { "observations": [...] }
  },
  "suggestions": {
    "cta": {
      "high_priority": [...],
      "additional": [...]
    },
    "visual_hierarchy": {
      "high_priority": [...],
      "additional": [...]
    },
    "copy_effectiveness": {
      "high_priority": [...],
      "additional": [...]
    },
    "trust_signals": {
      "high_priority": [...],
      "additional": [...]
    }
  }
}
``` 