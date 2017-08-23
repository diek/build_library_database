# Build Library Database

This project was created out of my love of data, as a Django programmer a project needs data. Without data,   
Django is boring. The crew @ Mozilla created one of the best Django tutorials out there, [Django Web Framework (Python)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django). And they finally created a detailed Django tutorial that uses something other than a blog, a great concept a [local library](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)!  One issue, there was no data, I was somewhat amazed that I could not find a single source of books with titles, isbn, with author detail. So a project was born.


## Getting Started/Prerequisites
You will need an api key, [ISBNdb](http://isbndb.com/) they have a good policy of 500 free requests per day. 
Most of the data comes from ISBNdb. Author details comes from [Wikidata](https://www.wikidata.org/wiki/Wikidata:Data_access)

There is some manual work needed but this project draws data from 2 sources. For this project I used the subject of espionage, there are many others to choose from, and ISBNdb gives you access to search for subjects.


### Installing

Navigate to your working folder.
```
git clone git@github.com:diek/build_library_database.git   
cd build_library_database  
# Remove git info from repo 
rm -rf dir_name/.git    
python3 -m venv _env    
source _env/bin/activate  
pip install --upgrade pip  
pip install -r requirements.txt  
```


## Built With

* [Python 3.6](https://www.python.org/downloads/release/python-362/)  
* [Requests](http://docs.python-requests.org/en/master/) - Retrieving requests for data
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Parsing the Wikidata

## Comments

Please read leave comments and constructive criticism.


## Authors

* **Derrick Kearney**  - [diek](https://github.com/diek)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Justin who keeps me motivated, when I need a push
* The crew @ RealPython, Dan Bader, and Adrian Rosebrock, who keep me informed and on track
