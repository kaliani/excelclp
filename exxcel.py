import click
import sys
import pandas as pd
import clipboard


@click.command()
@click.argument('filename')
@click.argument('columnname')


def main(filename, columnname):

    df = pd.read_excel(filename)
    string = ''

    for i in df.index:
        if len(df.index)-1 > i:
            string += "'"+str(df[columnname][i])+"'"+","+'\n'
        else:
            string += "'"+str(df[columnname][i])+"'"

    clipboard.copy(string)


if __name__ == "__main__":
    main()
