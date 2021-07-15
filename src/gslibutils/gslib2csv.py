'@author Exequiel Sepulveda https://github.com/exepulveda'
import sys
import os.path
import typer

from gslibutils.parser import parse_input

app = typer.Typer()

@app.command()
def convert(input: str, output: str = sys.stdout, output_format: str = 'csv'):
    # check input exists
    if not os.path.exists(input):
        msg = f"The input file {input} " + typer.style("does not exist", fg=typer.colors.RED, bold=True)
        typer.echo(msg, err=True)
        raise typer.Exit()

    # open the file
    with open(input) as fd_gslib:
        title, var_names, rows = parse_input(fd_gslib)

if __name__ == '__main__':
    app()