from app import app
import os  # Import os module

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's dynamic port
    app.run(host="0.0.0.0", port=port)  # Bind to 0.0.0.0
