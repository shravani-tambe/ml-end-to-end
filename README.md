# ml-end-to-end

End-to-End Machine Learning Project: From model training and testing to UI and AWS deployment.  
**Demo Project:** Wine Quality Prediction  

## Project Structure  

```bash
ml-end-to-end/
│
├── data/                   # Store datasets
│   ├── raw/                # Raw, unprocessed data
│   ├── processed/          # Processed data ready for training
│   └── external/           # External data (e.g., third-party datasets)
│
├── src/                    # Main source code
│   ├── __init__.py
│   ├── data/               # Data ingestion and preprocessing
│   │   ├── __init__.py
│   │   └── data_loader.py
│   ├── features/           # Feature engineering
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models/             # Model training and evaluation
│   │   ├── __init__.py
│   │   ├── train.py
│   │   └── predict.py
│   ├── utils/              # Utility functions
│   │   ├── __init__.py
│   │   └── common.py
│   └── pipeline/           # End-to-end pipeline
│       ├── __init__.py
│       └── run_pipeline.py
│
├── config/                 # Configuration files
│   ├── config.yaml         # General configurations
│   ├── params.yaml         # Model parameters
│   └── schema.yaml         # Data schema
│
├── notebooks/              # Research and experimentation
│   └── eda.ipynb           # Exploratory Data Analysis (EDA)
│
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_data.py
│   └── test_model.py
│
├── app/                    # Deployment (e.g., Flask app)
│   ├── templates/          # HTML templates for web app
│   ├── app.py              # Flask/FastAPI app
│   └── main.py             # Entry point for deployment
│
├── models/                 # Store trained models
│   └── model_v1.pkl        # Serialized model
│
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
├── requirements.txt        # Dependencies
├── setup.py                # Package setup
└── Dockerfile              # For containerization
