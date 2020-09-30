# cli.py
from SnowLang import app
import click


@click.command()
@click.argument('file_name')
def main(file_name):
    # click.echo(f"running {file_name}...")
    app.run(file_name)


if __name__ == "__main__":
    main()
