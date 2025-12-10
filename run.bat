@echo off
echo ============================================
echo    Starting Keyword Extraction Server
echo ============================================
echo.

cd backend
call venv\Scripts\activate

echo Starting Flask server...
echo Server will be available at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ============================================
echo.

python app.py
