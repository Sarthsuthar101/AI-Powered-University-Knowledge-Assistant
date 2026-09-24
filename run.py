"""Launch the University Knowledge Assistant.
Usage:  python run.py   ->  open http://localhost:5000
"""
from backend.app import app

if __name__ == "__main__":
    print("=" * 55)
    print("  Greenfield University - AI Knowledge Assistant")
    print("  Backend API : http://localhost:5000/api/health")
    print("  Frontend    : http://localhost:5000")
    print("=" * 55)
    app.run(host="0.0.0.0", port=5000, debug=True)
