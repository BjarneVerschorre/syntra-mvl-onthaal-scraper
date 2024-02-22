# Syntra MVL Onthaal Scraper
This is a simple scraper to get the database from the [Syntra MVL Onthaal website](https://onthaal.syntra-mvl.be/). It is written in Python 3.11 and uses the [HTTPX](https://www.python-httpx.org/) library to make requests.


## 🗒️ Quick Note
The "database" is publicly available in the source of the website. This scraper just makes it easier to get the data in a structured format.

## 🧰 Installation
1. Clone the repository
```bash
git clone https://github.com/BjarneVerschorre/syntra-mvl-onthaal-scraper.git
``` 

2. Create a virtual environment
```bash
python3.11 -m venv .venv
```

3. Activate the virtual environment **(Linux)**
```bash
source .venv/bin/activate
```

3. Activate the virtual environment **(Windows)**
```bash
.venv\Scripts\activate
```

4. Install the dependencies
```bash
pip3 install -r requirements.txt
```

## 💻 Usage
To use the scraper, run the following command:
```bash
python3 src/main.py
```
<hr>

To get get help, run the following command:
```bash
python3 src/main.py --help
```



