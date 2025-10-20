# Amazon Lowest Price Finder

A web app that automatically searches Amazon for products and finds the lowest price using playwright automation.

## Quick Start

### Prerequisites
- Node.js (v16+)
- Python (v3.8+)

### Installation
```bash
# Clone and setup
git clone <your-repo-url>
cd autoTasker

# Backend
cd backend
pip install -r requirements.txt
cp env.example .env

# Frontend  
cd ../frontend
npm install
cp env.example .env
```

### Run
```bash
#How to run backend
cd backend
python app.py

#How to run frontend
cd frontend
npm run dev
```

Visit `http://localhost:5173` and search for products like `blue_shirt` or `gaming_laptop`.

## Tech Stack

**Backend:** Flask + Playwright + Python  
**Frontend:** React + Vite + TypeScript

## How It Works

1. User enters product name
2. Playwright opens Amazon, searches, sorts by price
3. Extracts lowest price and product URL
4. Displays results with direct Amazon link