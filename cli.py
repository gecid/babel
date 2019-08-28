import click
import rows
from cprint import cprint

from babel.use_cases import chain_translate_text


TEXT = """
Para ele, cada leitura de qualquer texto sempre proporcionará um novo redimensionamento e entendimento desse texto. Metaforicamente falando, ele se posiciona diante dos textos como o banhista do rio de Heráclito, no qual é impossível entrar duas vezes devido a seu curso estar em constante mutação.
""".strip()


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def from_idh_csv(filename):
    entries = rows.import_from_csv(filename)
    languages = [e.code for e in entries]

    text, result = chain_translate_text(TEXT, 'pt', languages)


    cprint.info("\n##### RESULTADO ######\n")
    cprint.info(text)
    print()
    cprint.info(result)


if __name__ == '__main__':
    from_idh_csv()
