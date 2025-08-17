venv_folder=".nailavenv"

if [ ! -d "$venv_folder" ]; then
  echo "Virtual environment doesn't exist, creating it..."
  python3 -m venv "$venv_folder"
fi

echo "Initializing virtual environment..."
source "./$venv_folder/bin/activate"

echo "Installing dependencies..."
pip install -r requirements.txt

# # Uncomment the code below if you do not have your
# # API keys as environment variables in your system:

# echo "Setting API key variables"
# export HF_API_KEY="your_huggingface_key"
# export GROQ_API_KEY="your_groq_key"

echo " -> Running App"
python3 app.py