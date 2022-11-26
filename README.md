<div id="home" align="left">

# Yahoo Finance Scraper

<img src="https://user-images.githubusercontent.com/72005563/204069209-5e364554-511a-45b7-8199-8a0bdbe490e7.png" width="325">


![made-with-Python](https://img.shields.io/badge/Python-blue?&logo=python&logoColor=yellow&label=Built%20with&style=flat&labelColor=black)
[![License](https://img.shields.io/github/license/seraph776/seraph776?logo=github&color=green&labelColor=black)](https://github.com/seraph776/yahoo-finance-scraper/blob/main/contributing.md) [![Contribute](https://img.shields.io/badge/Contribute-black?&logo=github&logoColor=black&label=&flat&labelColor=yellow)](https://github.com/seraph776/yahoo-finance-scraper/blob/main/contributing.md) [![Report Bugs](https://img.shields.io/badge/Report%20Bugz-black?&logo=github&logoColor=black&label=&flat&labelColor=red)](https://github.com/seraph776/yahoo-finance-scraper/issues/new/choose)

_Show your support and give this repo a_ ⭐


  
</div>


## Intro

[Yahoo! Finance](https://finance.yahoo.com/) is a media property that is part of the Yahoo! network. It provides financial news, data and commentary including stock quotes, press releases, financial reports, and original content.

## Objective

The objective of this project is to download the financial history of the following stocks, and save the data to csv in
the [downloads](#) directory. 

- `Amazon`
- `Apple`
- `Google`
- `Netflix`
- `FaceBook (Meta)`
- `Tesla`
- `Bitcoin`
- `Ethereum`


## Requirements

This project was built using the `Python 3.10.1` and the following modules: 

| Required         | Version | Purpose                                                    |
|------------------|:-------:|------------------------------------------------------------|
| `requests`       |  2.7.0  | A simple, yet elegant, HTTP library.                       | 
| `beautifulsoup4` |  4.9 3  | HTML/XMl processing library.                               | 
| `fake-useragent` | 1.0. 1  | Up-to-date simple useragent faker with real world database | 
| `csv`            |    _    | Reads and writes tabular data in CSV format.               | 
| `json`           |    _    | Simple JSON decoder.                                       | 



## Setup Instructions 
Instructions on how to create a pipenv virtual environment.

<details>
<summary>🎯 Click to View </summary>

1. Download [zip file](https://github.com/seraph776/yahoo-finance-scraper/archive/refs/heads/main.zip) 
2. Extract zip files
3. Change directory into projectFolder:

```
$ cd projectFolder
```

4. Install from Pipfile:

```
$ pipenv install  
```

5. Run the application from within virtual environment:

```
$ pipenv run python app/main.py
```

</details>




## Usage


This scraper is highly adaptable. The stocks that are downloaded are controlled in the `config.py` file. Simply add the ticker symbols of teh company's 
that you want from the `SYMBOLS` list.  

For more information read [documentation](https://github.com/seraph776/yahoo-finance-scraper).


## Contact me

If you have any questions or wish to collaborate please contact me please feel free to contact me:  
- **Email** : [seraph776@gmail.com](mailto:seraph776@gmail.com)


## License 

[MIT](https://github.com/seraph776/seraph776/blob/main/LICENSE) © [Seraph★776](https://github.com/seraph776) 


<div align="right">

[[↑] Back to top](#home)

</div>  
