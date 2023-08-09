import requests
import pandas as pd
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url)

# Create BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the movie rows in the table
movie_rows = soup.select('tbody.lister-list tr')

# Initialize lists to store movie details
titles = []
ratings = []

# Iterate over each movie row and extract the title and rating
for row in movie_rows:
    title = row.find('td', class_='titleColumn').find('a').text.strip()
    rating = row.find('td', class_='imdbRating').text.strip()
    titles.append(title)
    ratings.append(rating)

# Create a DataFrame from the extracted data
data = {'Title': titles, 'Rating': ratings}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('top_movies.xlsx', index=False)



