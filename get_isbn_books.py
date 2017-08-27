import simplejson as json
import requests
import os


BASE_URL = 'http://isbndb.com/api/v2/json/' + os.environ["ISBN_KEY"]


def get_subject_titles(subject):
    url = BASE_URL + '/subjects?q=' + subject
    resp = requests.get(url=url)
    return json.loads(resp.text)


def get_book_detail():
    book_data = {}
    book_data['data'] = []
    with open('espionage_titles2.json') as json_file:
        data = json.load(json_file)
    book_lists = [books['book_ids'] for books in data['data']]
    book_titles = [book for books in book_lists for book in books]

    for book in set(book_titles):
        url = BASE_URL + '/book/'
        url += book
        resp = requests.get(url=url)
        data = json.loads(resp.text)
        book_data['data'].append(data['data'])
    return book_data


def write_json(in_data, f_name):
    f_name += '.json'
    json_data = json.dumps(in_data, indent=4, sort_keys=True)
    with open(f_name, 'w') as outfile:
        outfile.write(json_data)


def main():
    subject = 'espionage'
    book_titles = get_subject_titles(subject)
    write_json(book_titles, 'espionage_titles')
    json_book_detail = get_book_detail()
    write_json(json_book_detail, 'espionage_books')

if __name__ == '__main__':
    main()
