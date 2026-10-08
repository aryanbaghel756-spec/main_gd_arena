"""
GD Arena - One-Command Launcher
Runs the FastAPI server which serves both the REST API and the pre-built Next.js frontend on http://localhost:8000.
"""
import os
import sys
import webbrowser
import uvicorn

def main():
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    print("=" * 65)
    print(f"  🎙️ GD ARENA - Voice-First AI Group Discussion Platform")
    print(f"  Server URL: http://localhost:{port}")
    print(f"  Interactive Pipeline: http://localhost:{port}/")
    print("=" * 65)
    print("Opening browser...")
    try:
        webbrowser.open(f"http://localhost:{port}")
    except Exception:
        pass

    uvicorn.run("backend.main:app", host=host, port=port, reload=False)

if __name__ == "__main__":
    main()
