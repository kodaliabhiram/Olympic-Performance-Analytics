import streamlit as st
from helper import preprocess
import plotly.express as px

st.set_page_config(page_title="Olympic Analytics")

st.title("🏅 Olympic Performance Analytics")

df = preprocess()
st.sidebar.title("Filters")

selected_year = st.sidebar.selectbox(
    "Select Olympic Year",
    sorted(df['Year'].unique())
)

df = df[df['Year'] == selected_year]

# KPI Cards

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Athletes", df['Name'].nunique())

with col2:
    st.metric("Countries", df['region'].nunique())

with col3:
    st.metric("Sports", df['Sport'].nunique())

with col4:
    st.metric("Olympic Years", df['Year'].nunique())
    st.header("Top 10 Countries by Medal Count")

medals = df.dropna(subset=['Medal'])

country_medals = medals.groupby('region').size().reset_index(name='Medals')

country_medals = country_medals.sort_values(
    'Medals',
    ascending=False
).head(10)

fig = px.bar(
    country_medals,
    x='region',
    y='Medals',
    title='Top 10 Countries'
)

st.plotly_chart(fig, use_container_width=True)

st.write(df.head())

st.header("Medal Trend Over Years")

trend = preprocess()

trend = trend.dropna(subset=['Medal'])

trend = trend.groupby('Year').size().reset_index(name='Medals')

fig2 = px.line(
    trend,
    x='Year',
    y='Medals',
    markers=True,
    title='Olympic Medal Trend'
)

st.plotly_chart(fig2, use_container_width=True)


st.header("Top Athletes")

athletes = preprocess()

athletes = athletes.dropna(subset=['Medal'])

top_athletes = athletes.groupby(
    'Name'
).size().reset_index(name='Medals')

top_athletes = top_athletes.sort_values(
    'Medals',
    ascending=False
).head(10)

fig3 = px.bar(
    top_athletes,
    x='Name',
    y='Medals',
    title='Top 10 Athletes'
)

st.plotly_chart(fig3, use_container_width=True)

st.header("Top Sports")

sports = preprocess()

sports = sports.dropna(subset=['Medal'])

sports = sports.groupby(
    'Sport'
).size().reset_index(name='Medals')

sports = sports.sort_values(
    'Medals',
    ascending=False
).head(10)

fig4 = px.bar(
    sports,
    x='Sport',
    y='Medals',
    title='Top Sports by Medal Count'
)

st.plotly_chart(fig4, use_container_width=True)


st.header("Gender Participation")

gender = preprocess()

gender = gender.groupby(
    'Sex'
).size().reset_index(name='Count')

fig5 = px.pie(
    gender,
    names='Sex',
    values='Count',
    title='Male vs Female Participation'
)

st.plotly_chart(fig5, use_container_width=True)