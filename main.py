from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

movie = soup.find_all("img", class_="jsx-952983560")
movie_list = []
for tag in movie:
    movie_list.append(tag.get("alt"))

movie_list = movie_list[::-1]

with open("movies.txt",mode="w") as file:
    for movie in range(len(movie_list)-1):
        file.write(f"{movie+1} {movie_list[movie]}\n")

# response = requests.get(url="https://news.ycombinator.com")
# response.raise_for_status()
# data = response.text
#
# soup = BeautifulSoup(data, "html.parser")
# head = soup.find_all(class_="titlelink")
# score = soup.find_all(class_="score")
#
# text = []
# link = []
#
# for tag in head:
#     link.append(tag.get("href"))
#     text.append(tag.getText())
#
# upvote = [int(tag.getText().split(sep=" ", maxsplit=-1)[0]) for tag in score]
#
# most_upvote = max(upvote)
# largest_index = upvote.index(most_upvote)
# print(upvote[largest_index], text[largest_index])

# for i in range(len(text)):
#     if upvote[i] == most_upvote:
#         print(upvote[i], text[i])
#         break

# for tag in head:
#     print(tag.getText())

# for tag in score:
#      print(tag.getText())

# with open("website.html", encoding="utf-8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# data = soup.find_all(name="a")
#
# # for tag in data:
# #     print(tag.get("href"))
#
# name = soup.find(name="h1",id="name")
# print(name.name)
#
