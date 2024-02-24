import re
import json
import httpx
from pprint import pprint

from utils.parse_args import args


BASE_URL = 'https://onthaal.syntra-mvl.be/'


def get_onthaal_database() -> dict:
    ''' Get the database from the website's HTML and return it as a dictionary'''
    res = httpx.get(BASE_URL)
    res.raise_for_status()

    html = res.text
    onthaal_db = re.search(r'var onthaalDB = (.*?);', html)

    if not onthaal_db or not onthaal_db.group(1):
        raise ValueError('Database not found in HTML')

    onthaal_db = json.loads(onthaal_db.group(1))
    return onthaal_db


def filter_database(db: dict, location: str = '', cursus: str = '') -> dict:
    db = db.copy()

    if location:
        db = [x for x in db if re.match(f'.*{location}.*', x['locatie'], re.IGNORECASE)]

    if cursus:
        db = [x for x in db if re.match(f'.*{cursus}.*', x['Cursus'], re.IGNORECASE)]

    return db


def main(locatie: str, cursus: str, output:str) -> None:
    db = get_onthaal_database()
    filtered_db = filter_database(db, locatie, cursus)

    for entry in filtered_db:
        if entry.get('registed') == 'false':
            continue
        print(entry.get('Cursus'))
        print(f'Datum: {entry.get("date")}')
        print(f'Uur: {entry.get("start")}')
        print(f'Online: {entry.get("onlineles") != "0"}')
        
        if entry.get("Lokaal") != "":
            print(f'Locatie: {entry.get("locatie")}, {entry.get("Lokaal")}')
        
        print()
    
    if output:
        with open(output, 'w') as f:
            json.dump(filtered_db, f, indent=4)


if __name__ == '__main__':
    locatie = args.locatie
    cursus = args.cursus
    output = args.output

    main(locatie=locatie, cursus=cursus, output=output)
