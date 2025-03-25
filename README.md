# ml-end-to-end

End to End Machine Learning Project, from model train and test to the UI to AWS Deployment - Demo Proj: Wine Quality Prediction

ml-end-to-end/
│
├── data/ # Store datasets
│ ├── raw/ # Raw, unprocessed data
│ ├── processed/ # Processed data ready for training
│ └── external/ # External data (e.g., third-party datasets)
│
├── src/ # Main source code
│ ├── **init**.py
│ ├── data/ # Data ingestion and preprocessing
│ │ ├── **init**.py
│ │ └── data_loader.py
│ ├── features/ # Feature engineering
│ │ ├── **init**.py
│ │ └── build_features.py
│ ├── models/ # Model training and evaluation
│ │ ├── **init**.py
│ │ ├── train.py
│ │ └── predict.py
│ ├── utils/ # Utility functions
│ │ ├── **init**.py
│ │ └── common.py
│ └── pipeline/ # End-to-end pipeline
│ ├── **init**.py
│ └── run_pipeline.py
│
├── config/ # Configuration files
│ ├── config.yaml # General configurations
│ ├── params.yaml # Model parameters
│ └── schema.yaml # Data schema
│
├── notebooks/ # Research and experimentation
│ └── eda.ipynb # Exploratory data analysis
│
├── tests/ # Unit tests
│ ├── **init**.py
│ ├── test_data.py
│ └── test_model.py
│
├── app/ # Deployment (e.g., Flask app)
│ ├── templates/ # HTML templates for web app
│ ├── app.py # Flask/FastAPI app
│ └── main.py # Entry point for deployment
│
├── models/ # Store trained models
│ └── model_v1.pkl # Serialized model
│
├── .gitignore # Git ignore file
├── README.md # Project documentation
├── requirements.txt # Dependencies
├── setup.py # Package setup
└── Dockerfile # For containerization
