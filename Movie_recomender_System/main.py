import streamlit as st
import pickle
import json
import requests

similarity_matrix = pickle.load(open('similarity.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Movie Recomendation")

movie = st.selectbox('Movie_Name',df['title_x'].unique())

def recomend(Movie):
    movie_name_list=[]
    poster_list=[]
    index=df[df["title_x"]==Movie].index[0]
    movie_list=sorted(enumerate(similarity_matrix[index]), key=lambda x: x[1],reverse=True)[1:6]
    for i in movie_list:
        movie_id=df["id"][i[0]]
        api_key = "bf74a9c5c6c9050dc2a573d20dee6f25"
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        poster_path = data["poster_path"]
        poster_url = f"https://image.tmdb.org/t/p/original{poster_path}"
     
        #st.image(poster_url, use_column_width=True)
        movie_name_list.append(df["title_x"][i[0]])
        poster_list.append(poster_url)
    return movie_name_list, poster_list

if st.button('Predict movie'):
    movie_list, poster=recomend(movie)
    # for i in range(len(movie_list)):
    #     st.title(movie_list[i])
    #     row=st.empty()
    #     row.image(poster[i], use_column_width=True)
    col1, col2, col3, col4, col5 =st.columns(5)
    with col1:
        st.text(movie_list[0])
        st.image(poster[0])
    with col2:
        st.text(movie_list[1])
        st.image(poster[1])
    with col3:
        st.text(movie_list[2])
        st.image(poster[2])
    with col4:
        st.text(movie_list[3])
        st.image(poster[3])
    with col5:
        st.text(movie_list[4])
        st.image(poster[4])
    




