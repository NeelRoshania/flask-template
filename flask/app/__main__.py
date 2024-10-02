from app import create_app
from pathlib import Path

if __name__ == "__main__":
    print("- starting flask app")
    print(Path(__file__).stem)
    app = create_app()
    # app.run(8000)
    # app.run(f"{Path(__file__).stem}:app")
    app.run(f"app:app")
