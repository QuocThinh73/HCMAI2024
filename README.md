<h1><center>HCM AI CHALLENGE 2024<br> Event Retrieval from Visual Data</center></h1>

## Development environment
Python 3.10.1 64 bit

## Setup 
```
pip install git+https://github.com/openai/CLIP.git
pip install -r requirements.txt
```

## Download dataset to local
```
python download_dataset.py
```

***Notice:*** You can customize the download data by selecting the specific link in the links

## Run model
You run all the cells in create_faiss_index.ipynb to create database for webapp.

***Notice:*** You can choose the path to run model by setting the variable *list_image* in fourth cell.

## Run webapp
```
python app.py
```


