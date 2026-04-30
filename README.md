# 🛸 UFO Sighting Predictor Web App

This is a Machine Learning web application that predicts which country a UFO sighting likely occurred in based on the duration (seconds), latitude, and longitude.

## 🚀 Project Overview
- **Model:** Logistic Regression trained on global UFO sighting data.
- **Backend:** Flask web framework.
- **Frontend:** HTML/CSS.
- **Dataset:** Scraped UFO sighting reports filtered for sightings between 1-60 seconds.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/victoroh22/ufo-web-app.git
   cd ufo-web-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Access the app:**
   Open your browser and navigate to `http://127.0.0.1:5000`.

## 📂 File Structure
- `app.py`: Flask server and prediction logic.
- `ufo-model.pkl`: The trained Scikit-learn model.
- `templates/`: HTML user interface.
- `static/`: CSS styling.