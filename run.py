from source.main import app
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "DEBUG":
        app.run(debug=True)
    else:
        app.run()
