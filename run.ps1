$venv_folder = ".nailavenv"

if (-Not (Test-Path $venv_folder)) {
  Write-Output "Virtual environment doesn't exist, creating it..."
  python -m venv $venv_folder
}

Write-Output "Initializing virtual environment..."
& "$venv_folder\Scripts\Activate.ps1"

Write-Output "Installing dependencies..."
pip install -r requirements.txt

# # Uncomment the code below if you do not have your
# # API keys as environment variables in your system:

# Write-Output "Setting API key variables"
# $env:HF_API_KEY="your_huggingface_key"
# $env:GROQ_API_KEY="your_groq_key"

Write-Output " -> Running App"
python app.py