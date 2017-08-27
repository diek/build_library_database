import json
import pywikibot
# set .env PYWIKIBOT2_NO_USER_CONFIG = 1


def get_wiki_entryID(author):
    try:
        author = "{} {}".format(author[1], author[0])
        site = pywikibot.Site("en", "wikipedia")
        page = pywikibot.Page(site, author)
        item = pywikibot.ItemPage.fromPage(page)
        return item.getID()
    except:
        return 'No Entry'


def get_authors_wiki(authors):
    authors_wiki = []
    for i, author in enumerate(authors):
        author_name = parse_author(author)
        author_ent = get_wiki_entryID(author_name)
        author_name.append(author_ent)
        authors_wiki.append(author_name)

    return authors_wiki


def parse_author(name):
    """Some names are malformatted, so 2 methods needed
    """
    if name.find(',') < 0:
        f_name, *m_name, l_name = name.split(' ')
        if m_name:
            m_name = " ".join([str(x) for x in m_name])
            f_name = f_name.strip() + " " + m_name.strip()

        return [l_name.strip(), f_name.strip()]
    else:
        name = name.split(',')
        if len(name) == 1:
            return [name[0], "Anon"]
        else:
            return [name[0].strip(), name[1].strip()]


def retrieve_authors():
    authors = []
    with open('espionage_books.json') as json_file:
        data = json.load(json_file)

    for i in range(len(data['data'])):
        for idx, author in enumerate(data['data'][i][0]['author_data']):
            author = data['data'][i][0]['author_data'][idx]['name']
            authors.append(author.strip())

    return get_authors_wiki(set(authors))


def write_authors(authors):
    authors.sort(key=lambda x: x[0])
    with open('authors.csv', 'w') as file_handler:
            for idx, author in enumerate(authors):
                l_name, f_name, wiki_ent = author
                file_handler.write("{}, {}, {}, {}\n".format(idx + 1, l_name, f_name, wiki_ent))


def main():
    authors = retrieve_authors()
    write_authors(authors)

if __name__ == '__main__':
    main()
