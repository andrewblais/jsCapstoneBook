import requests

url = "https://openlibrary.org/search.json?q=clans+of+the+alphane+moon"

response = requests.get(url)

data = response.json()
first_result = data.get("docs")[0]

book_title = first_result.get("title")

author_name = first_result.get("author_name")[0]

isbn_string = ""
isbn_results = first_result.get("isbn")
for i in isbn_results:
    if len(i) == 10:
        isbn_string = i
        break

print(book_title, author_name, isbn_string, sep='\n')
