
# Movie Recommender System using Content-Based Filtering

This project implements a movie recommender system based on content-based filtering using natural language processing techniques. It analyses movie descriptions, genres, keywords, cast, and crew information to recommend similar movies.

## Overview

The system uses the TMDB 5000 Movie Dataset, consisting of movie metadata and credits information. It preprocesses the data to extract relevant features and compute similarity scores between movies based on their content.

## Setup
To run this project locally, follow these steps:
1.  ### Clone the repository

    ```bash
    git clone https://github.com/YOGESH1504/movie-recommender-system.git
    cd movie-recommender-system
    ```

2.  ### Create and Activate a Virtual Environment 
	Using venv (for Python 3.x) 
	#### Create a virtual environment 
	```bash
	 # Create a virtual environment named 'venv'
	  python3 -m venv venv
	  ```
    ####  Activate the Virtual Environment 
    ##### On Windows 
    ```bash 
    .\env\Scripts\activate
    ```
    ##### on macOS
     ```bash
      source env/bin/activate
      ```
3. ### Install dependencies

    Ensure you have Python 3.x installed along with the necessary libraries. Install them using:

    ```bash
    pip install pandas nltk scikit-learn
    ```

    You also need to download NLTK data:

    ```bash
	python -m nltk.downloader wordnet
	```

4.  ### Download the dataset

    -   Download the TMDB 5000 Movie Dataset from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv).
    -   Place the `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` files in a directory accessible to your Python environment.
5.  ### Run the preprocessing script

    Execute the model builder script (`movie_recommendation.ipynb` or similar) in Google Colab or Jupyter notebook
    This script cleans the data, extracts relevant features, applies lemmatization, and computes TF-IDF vectors for movie tags.

6.  ### Run the recommender system:

    Start the Streamlit application:

    ```bash
	streamlit run mrs_interface.py
	```

    Open a web browser and navigate to `http://localhost:8501` to access the recommender system.

## Usage

-   **Select a Movie:** Choose a movie from the dropdown menu.
-   **Show Recommendations:** Click the button to view recommended movies based on similarity scores.
