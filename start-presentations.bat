@echo off
cd /d "%~dp0"
echo Starting presentation server on http://localhost:3456
echo.
echo Serving presentations from: presentations\
echo.
echo Open any presentation at:
echo   http://localhost:3456/A%%20New%%20Era%%20for%%20Cyber.html
echo   http://localhost:3456/agentic-risk-pov.html
echo.
echo Press Ctrl+C to stop the server.
echo.
start http://localhost:3456
python presentation-server.py
