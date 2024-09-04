<h1><center>Pipeline HCM AI CHALLENGE <br> Event Retrieval from Visual Data</center></h1>

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

URL: http://0.0.0.0:5001/home?index=0


