from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv
from flask_cors import CORS
import google.generativeai as genai
import base64
from components.scoringModel import predict_score, train_from_user_data, train_dummy_model


# Check if .env file exists and load it
if os.path.exists(".env"):
    load_dotenv()

# Get API key from environment variable
api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    print("WARNING: No GEMINI_API_KEY found in environment variables")

# Skip model training in Vercel environment as it's read-only filesystem
is_vercel = os.environ.get('VERCEL') == '1'

if not is_vercel:
    print("Initializing scoring model...")
    try:
        if os.path.exists("components/score_model.pkl"):
            os.remove("components/score_model.pkl")
        train_dummy_model()
        print("Scoring model created successfully")
    except Exception as e:
        print(f"Error creating scoring model: {str(e)}")
else:
    print("Running in Vercel environment - using simplified scoring")

app = Flask(__name__)
# Configure CORS to allow requests from any origin
CORS(app, resources={r"/*": {"origins": "*"}})

# ... existing code ... 