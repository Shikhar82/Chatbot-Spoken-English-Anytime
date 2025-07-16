# Use a minimal Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the repo into the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port used by Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "chatbot_ui.py", "--server.port=8501", "--server.headless=true"]
