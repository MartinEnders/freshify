# Food_Freshness_Categorizer

# Quickstart

Setup our repository:
```
git clone https://github.com/Timbakimbo/Food_Freshness_Categorizer
cd Food_Freshness_Categorizer
```

Setup a virtual environment for development purposes:
```
python -m venv .venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

Install all dependencies:
```
pip install -r requirements.txt
```

# Structure

```
root/
│
├── data/
│   ├── raw/
│   │    ├── unsorted/
│   │    ├── dataset_cat1/
│   │    │      ├── <categories>/
│   │    │      │       ├── <files>
│   │    │      ├── .../
│   │    │      │       ├── ...
│   │    ├── dataset_cat2/
│   │    │      ├── <categories>/
│   │    │      │       ├── <files>
│   ├── processed/
│   ├── train/
│   │   ├── edible/
│   │   │    ├── <categories>/
│   │   │    │      ├── <files>
│   │   │    ├── .../
│   │   │    │      ├── ...
│   │   ├── non_edible/
│   │   │    ├── <categories>/
│   │   │    │      ├── <files>
│   │   │    ├── .../
│   │   │    │      ├── ...
│   ├── val/
│   │   ├── edible/
│   │   │    ├── <categories>/
│   │   │    │      ├── <files>
│   │   │    ├── .../
│   │   │    │      ├── ...
│   │   ├── non_edible/
│   │   │    ├── <categories>/
│   │   │    │      ├── <files>
│
├── logs/
│   ├── ...
│
├── doc/
│   ├── ...
│
├── models/
│   ├── pepper_classifier.keras
│   ├── ...
│
├── src/
│   ├── data_loader.py
│   ├── train.py
│   ├── predict.py
│   ├── ...
│
├── app/
│   ├── streamlit_app.py
│
├── config/
│   ├── config.yaml
│   ├── ...
│
├── main.py
├── requirements.txt
└── README.md
```
