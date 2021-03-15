import os
import click
import requests
import inspect
from pathlib import Path

@click.command()
@click.option('--year', default=2020)
@click.argument('day')
def cli(year, day):
    # required because the cli compiles this ondemand
    __file__ = inspect.getfile(inspect.currentframe())

    sessionFile = Path(os.path.join(os.path.dirname(__file__), '..', '..', '.session'))

    if not sessionFile.is_file():
        click.echo('Not logged in to AoC')
        return 1

    session = ''

    with sessionFile.open() as f:
        session = f.readline()

    headers = { "cookie": f"session={session}"}
    request = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers=headers)

    folder = Path(os.path.join(os.path.dirname(__file__), '..', '..', 'inputs', str(year)))

    if not folder.is_dir():
        folder.mkdir()
    
    inputFile = Path(os.path.join(folder, f"{day:0>2}"))

    with inputFile.open('w') as f:
        f.write(request.text)

    return 0