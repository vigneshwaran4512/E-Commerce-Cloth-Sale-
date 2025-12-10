#!/bin/bash

echo "🔧 Starting E-Commerce T-Shirt Dashboard..."

# Activate virtual environment
if [ -f ".venv/bin/activate" ]; then
    echo "✔ Virtual environment found. Activating..."
    source .venv/bin/activate
else
    echo "❌ .venv not found! Creating new one..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
fi

# Run Streamlit with correct params
echo "🚀 Launching Streamlit at port 8501..."
streamlit run ecom_tshirt_project/app_streamlit.py --server.address=0.0.0.0 --server.port=8501
