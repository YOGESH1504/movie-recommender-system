import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch poster URL from TMDb API
def fetch_poster(movie_id):
    base_url = "https://api.themoviedb.org/3/movie/"
    url = f"{base_url}{movie_id}?language=en-US"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZTk5OWRkZDIxMzU3YWJlMThlYzY1ZDY1YTg3ZWFmMSIsIm5iZiI6MTcxOTc1NTE2OC4xNzEzNzQsInN1YiI6IjY2ODEzOTU4MjE5NGIzMjEzZmFjMzBkZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Sk6ydzEbjwUWCw6etRvlAir_TUitamXWGTeo8GA398k"  # Replace with your TMDb API key
    }

    retries = 3
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            poster_path = data['poster_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                continue
            else:
                st.error(f"Error fetching poster for movie ID {movie_id}: {e}")
                return None

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']  # Ensure correct access to movie_id
        poster_url = fetch_poster(movie_id)
        if poster_url:
            recommended_movie_posters.append(poster_url)
            recommended_movie_names.append(movies.iloc[i[0]]['title'])

    return recommended_movie_names, recommended_movie_posters

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies)

# Streamlit UI with enhanced frontend design
st.set_page_config(layout="wide")  # Wide layout for better display

# Header
st.title('Movie Recommender System')
st.markdown("---")

# Sidebar for movie selection
st.sidebar.header('Select a movie')
selected_movie = st.sidebar.selectbox('Choose a movie', movies['title'].values)

# Button to trigger recommendation
if st.sidebar.button('Show Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    # Display recommendations in a grid layout
    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(len(recommended_movie_names)):
        with locals()[f"col{i % 5 + 1}"]:
            st.subheader(recommended_movie_names[i])
            st.image(recommended_movie_posters[i], use_column_width=True)
            st.markdown("---")

# Footer or additional information section
st.sidebar.markdown("---")
st.sidebar.info(
    "This app recommends movies based on similarity scores computed from a dataset. "
    "Select a movie from the sidebar and click 'Show Recommendations' to see suggestions."
)