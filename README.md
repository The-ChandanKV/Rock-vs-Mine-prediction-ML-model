# 🌊 Rock vs Mine Sonar Detection

An advanced machine learning application that uses sonar signals to distinguish between rocks and underwater mines with **99.06% accuracy**.

![Rock vs Mine Detection](https://img.shields.io/badge/Accuracy-99.06%25-success)
![Next.js](https://img.shields.io/badge/Next.js-16.0-black)
![Flask](https://img.shields.io/badge/Flask-3.0-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)

## ✨ Features

- **🎯 High Accuracy**: 99.06% classification accuracy using logistic regression
- **🎨 Beautiful UI**: Modern, animated interface with WebGL shader backgrounds
- **⚡ Real-time**: Instant predictions with millisecond response times
- **📊 60 Feature Analysis**: Comprehensive sonar frequency band analysis
- **🔄 Sample Data**: Pre-loaded rock and mine samples for testing
- **📱 Responsive**: Works seamlessly on desktop and mobile devices

## 🏗️ Architecture

### Frontend (Next.js + TypeScript)
- **Framework**: Next.js 16 with App Router
- **Styling**: Tailwind CSS v4
- **UI Components**: shadcn/ui
- **Icons**: Lucide React
- **Animations**: Custom WebGL shaders + CSS animations

### Backend (Flask + Python)
- **Framework**: Flask 3.0
- **ML Model**: Scikit-learn Logistic Regression
- **API**: RESTful JSON endpoints with CORS support
- **Data Processing**: NumPy for efficient array operations

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18+ and npm
- **Python** 3.8+
- **pip** package manager

### Installation

#### 1. Clone the repository

```bash
git clone <your-repo-url>
cd "Rock vs Mine prediction model"
```

#### 2. Set up the Backend (Flask)

```bash
# Install Python dependencies
pip install -r requirements.txt

# Start the Flask server
python app.py
```

The Flask API will run on `http://localhost:5000`

#### 3. Set up the Frontend (Next.js)

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The Next.js app will run on `http://localhost:3000`

## 📖 Usage

### Using the Web Interface

1. **Open your browser** to `http://localhost:3000`
2. **Scroll down** to the "Test the Model" section
3. **Choose an option**:
   - Click "Load Sample Rock" or "Load Sample Mine" for pre-filled data
   - Or manually enter 60 comma-separated sonar values
4. **Click "Predict Object Type"** to get the classification
5. **View the result** with visual feedback

### Using the API Directly

#### JSON API Endpoint

```bash
POST http://localhost:5000/api/predict
Content-Type: application/json

{
  "features": [0.0200, 0.0371, 0.0428, ..., 0.0032]  // 60 values
}
```

**Response:**

```json
{
  "prediction": "Rock",
  "success": true,
  "confidence": {
    "rock": 0.95,
    "mine": 0.05
  }
}
```

#### Form Data Endpoint (Legacy)

```bash
POST http://localhost:5000/predict
Content-Type: application/x-www-form-urlencoded

features=0.0200,0.0371,0.0428,...,0.0032
```

## 📊 About the Model

### Dataset
- **Source**: Sonar returns bounced off metal cylinders vs rocks
- **Features**: 60 frequency bands (0-1 normalized energy values)
- **Classes**: Rock (R) or Mine (M)
- **Training Accuracy**: 99.06%

### Model Details
- **Algorithm**: Logistic Regression
- **Input**: 60 numerical features representing sonar frequencies
- **Output**: Binary classification (Rock or Mine)
- **Preprocessing**: Feature normalization and standardization

### How It Works

1. **Sonar Signal**: A sonar pulse is sent toward an object
2. **Frequency Analysis**: The return signal is analyzed across 60 frequency bands
3. **Feature Extraction**: Energy values at each frequency are measured (0-1 scale)
4. **Classification**: The ML model analyzes the pattern to classify the object
5. **Result**: Determines if the object is a rock (natural) or mine (metallic)

## 🎨 UI Components

### Hero Section
- Animated WebGL shader background
- Gradient text with smooth animations
- Call-to-action buttons with smooth scrolling

### Features Section
- Three-column grid showcasing key capabilities
- Icon-based visual hierarchy
- Hover effects and transitions

### Prediction Form
- Real-time input validation
- Character counter (60 values required)
- Sample data loading buttons
- Loading states and error handling

### Results Display
- Color-coded results (green for Rock, red for Mine)
- Animated entrance effects
- Clear visual feedback with icons
- Safety status messages

## 🛠️ Development

### Frontend Development

```bash
cd frontend

# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Lint code
npm run lint
```

### Backend Development

```bash
# Run Flask in debug mode
python app.py

# The server auto-reloads on file changes
```

## 📁 Project Structure

```
Rock vs Mine prediction model/
├── frontend/                 # Next.js frontend
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx     # Main application page
│   │   │   ├── layout.tsx   # Root layout
│   │   │   └── globals.css  # Global styles
│   │   └── components/
│   │       └── ui/
│   │           └── animated-shader-hero.tsx
│   ├── package.json
│   └── tsconfig.json
├── templates/                # Flask HTML templates
│   └── index.html
├── static/                   # Static assets
│   └── styles.css
├── model/                    # ML model files
│   └── sonar_model.pkl
├── app.py                    # Flask backend
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env.local` file in the `frontend` directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:5000
```

### CORS Configuration

The Flask backend is configured to accept requests from any origin. For production, update `app.py`:

```python
CORS(app, origins=["https://your-production-domain.com"])
```

## 🚢 Deployment

### Frontend (Vercel)

```bash
cd frontend
npm run build
# Deploy to Vercel
```

### Backend (Heroku/Railway)

```bash
# Ensure requirements.txt is up to date
pip freeze > requirements.txt

# Deploy using your preferred platform
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Sonar dataset from UCI Machine Learning Repository
- WebGL shader by Matthias Hurrle (@atzedent)
- shadcn/ui for beautiful component primitives
- Next.js team for the amazing framework

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

**Built with ❤️ using Next.js, TypeScript, Flask, and Machine Learning**
