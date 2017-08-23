import json
# set .env PYWIKIBOT2_NO_USER_CONFIG = 1
import pywikibot


def get_wiki_item(author):
    try:
        site = pywikibot.Site("en", "wikipedia")
        page = pywikibot.Page(site, author)
        item = pywikibot.ItemPage.fromPage(page)
        return item.getID()
    except:
        return 'No Entry'


def get_author_Q(authors):
    authors_wiki = []
    for author in authors:
        author = author.split(',')
        if len(author) < 2:
            author.append('Anon')  # Mr. X
        author_name = "{} {}".format(author[1].strip(), author[0].strip())
        author_ent = get_wiki_item(author_name)
        authors_wiki.append([author[0], author[1], author_ent])

    return authors_wiki


def create_authors_csv():
    authors = []
    with open('espionage_books.json') as json_file:
        data = json.load(json_file)
        for idx in range(1, 111):
            for item in data['data'][idx]:
                if len(item['author_data']) > 1:
                    for idx in range(len(item['author_data'])):
                        authors.append(item['author_data'][idx]['name'])
                else:
                    authors.append(item['author_data'][0]['name'])

    authors_list = get_author_Q(sorted(set(authors)))

    with open('authors.csv', 'w') as file_handler:
            for idx, author in enumerate(authors_list):
                l_name, f_name, wiki_ent = author
                file_handler.write("{}, {}, {}, {}\n".format(idx + 1, l_name.strip(), f_name.strip(), wiki_ent))


def main():
    create_authors_csv()

if __name__ == '__main__':
    main()
