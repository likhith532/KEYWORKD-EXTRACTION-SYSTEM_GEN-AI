@echo off
echo ============================================
echo    Keyword Extraction System - Setup
echo    (Lightweight Version - YAKE only)
echo ============================================
echo.

cd backend

echo [1/2] Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

echo.
echo [2/2] Installing dependencies (only ~5MB)...
pip install -r requirements.txt

echo.
echo ============================================
echo    Setup Complete!
echo ============================================
echo.
echo To start the server, run:
echo    Double-click run.bat
echo    OR
echo    cd backend
echo    venv\Scripts\activate
echo    python app.py
echo.
echo Then open http://localhost:5000 in your browser
echo ============================================
pause
