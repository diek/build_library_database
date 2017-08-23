import json
import requests
import os


BASE_URL = 'http://isbndb.com/api/v2/json/' + os.environ["ISBN_KEY"]

def get_subject_titles(subject):
    url = BASE_URL + '/subjects?q=' + subject
    resp = requests.get(url=url)


def get_book_detail():
    book_titles = []

    with open('espionage_titles.json') as json_file:
        data = json.load(json_file)
        for book in data['data'][0]['book_ids']:
            book_titles.append(book)

    for idx, book in enumerate(book_titles):
        url = BASE_URL + '/book/'
        url += book
        resp = requests.get(url=url)
        book_data = json.loads(resp.text)
        book_data['data'].append(book_data['data'])

    return book_data


def write_json(data, f_name):
    f_name += '.json'
    json_data = json.dumps(data, indent=4, sort_keys=True)
    with open(f_name, 'w') as outfile:
        outfile.write(json_data)


def main():
    subject = 'espionage'
    get_subject_titles(subject)
    write_json(book_data, 'espionage_titles')
    book_data = get_book_detail()
    write_json(book_data, 'espionage_books')

if __name__ == '__main__':
    main()
