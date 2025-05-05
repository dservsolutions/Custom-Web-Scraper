import requests
import csv
import pandas as pd

from bs4 import BeautifulSoup

URL= "https://books.toscrape.com/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

product_pods = soup.find_all('article', class_='product_pod')

# Empty List
book_data = []

bookss = []
#Book Titles
for pod in product_pods:
    #Withing each product_pod, find the h3 tag
    #Extracting book titles
    title_element = pod.find('h3')
    titles = title_element.get_text(strip=True) if title_element else 'N/A'

    # Extracting book prices
    price_element = pod.find('p', class_='price_color')
    price = price_element.get_text(strip=True) if price_element else 'N/A'

    book_data = [{'Title': titles, 'Price': price}]
    for books in book_data:
        bookss.append(books)
        # Creating a DataFrame with Pandas

df = pd.DataFrame(bookss)

# Specify the CSV file name
csv_file = 'books_data.csv'

#Export the DataFrame to a CSV file
try:
    df.to_csv(csv_file, index=False, encoding='utf-8')
    print(f"Data successfully exported to {csv_file} using Pandas.")
except Exception as e:
    print(f"An error occurred while exporting to CSV using Pandas: {e}")

# Write data to the CSV
# try:
#     with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
#         fieldnames = ['Title', 'Price']
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#         writer.writeheader()# Write the header row
#         writer.writerows(book_data)# Write the book data rows
#
#     print(f"Data successfully exported to {csv_file}")
# except Exception as e:
#     print(f"An error ocurred while exporting to CSV: {e}")

