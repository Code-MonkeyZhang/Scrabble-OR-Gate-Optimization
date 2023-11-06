import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://scrabble.merriam.com/browse'


def get_words_from_page(url):
    response = requests.get(url)  # get html
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract words
    words = []
    for a in soup.select('li > a[href^="/finder/"]'):
        word = a.text.upper()
        if len(word) == 6:
            print(word)  # 打印单词
            words.append(word)

    # Find the link to the next page
    next_page_link = soup.select_one('.pagination .button.next')
    if next_page_link:
        href_value = next_page_link['href']
        next_page_suffix = href_value.split("/browse")[-1]
        next_page_url = BASE_URL + next_page_suffix
    else:
        next_page_url = None

    return words, next_page_url


def get_next_letter_url(soup):
    next_letter_link = soup.select_one('li.unselected > a[href^="browse/"]')
    if next_letter_link:
        return next_letter_link['href']
    return None


def main():
    current_letter = 'a'
    current_page_url = BASE_URL + '/' + current_letter + '/1'  # Starting page for 'A' letter
    all_words = []

    while True:
        words, next_page_url = get_words_from_page(current_page_url)
        all_words.extend(words)

        if not next_page_url:  # If no next page, meaning End of the current letter
            if current_letter == 'z':
                break
            current_letter = chr(ord(current_letter) + 1)
            current_page_url = BASE_URL + '/' + current_letter + '/1'  # Start with the first page of the next letter

        else:
            current_page_url = next_page_url

    # Save words to a txt file
    with open('scrabble_words.txt', 'w') as file:
        for word in all_words:
            file.write(word + '\n')
    print(f"Total words extracted: {len(all_words)}")


if __name__ == '__main__':
    main()
