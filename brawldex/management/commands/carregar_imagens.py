import json
from pathlib import Path

from django.core.management.base import BaseCommand

from brawldex.models import Brawler


# Caminho do JSON baixado do Brawlify (fica do lado deste comando)
JSON_PATH = Path(__file__).resolve().parent / 'brawlers.json'


class Command(BaseCommand):
    help = (
        'Popula o campo imagem_url dos Brawlers a partir do arquivo '
        'brawlers.json (baixado da API do Brawlify).'
    )

    def handle(self, *args, **options):

        # 1) Verifica se o JSON existe
        if not JSON_PATH.exists():
            self.stdout.write(self.style.ERROR(
                f'Arquivo não encontrado: {JSON_PATH}'
            ))
            self.stdout.write(
                'Baixe o JSON em https://api.brawlify.com/v1/brawlers '
                'e salve como brawldex/management/commands/brawlers.json'
            )
            return

        # 2) Carrega o JSON
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)

        brawlers_json = data.get('list', [])
        if not brawlers_json:
            self.stdout.write(self.style.WARNING(
                'O JSON não contém a chave "list" ou está vazio.'
            ))
            return

        self.stdout.write(
            f'{len(brawlers_json)} Brawlers encontrados no JSON.'
        )

        atualizados = 0
        sem_imagem_no_json = 0
        nao_encontrados = []

        # 3) Itera e atualiza
        for item in brawlers_json:
            nome = item.get('name')
            imagem_url = item.get('imageUrl2')  # sem moldura

            if not nome:
                continue

            if not imagem_url:
                sem_imagem_no_json += 1
                continue

            brawler = Brawler.objects.filter(nome=nome).first()

            if not brawler:
                nao_encontrados.append(nome)
                continue

            brawler.imagem_url = imagem_url
            brawler.save(update_fields=['imagem_url'])
            atualizados += 1

        # 4) Relatório
        self.stdout.write(self.style.SUCCESS(
            f'{atualizados} Brawler(s) atualizado(s) com URL de imagem.'
        ))

        if sem_imagem_no_json:
            self.stdout.write(self.style.WARNING(
                f'{sem_imagem_no_json} Brawler(s) do JSON estavam sem imageUrl2.'
            ))

        if nao_encontrados:
            self.stdout.write(self.style.WARNING(
                f'{len(nao_encontrados)} Brawler(s) do JSON não existem no seu banco:'
            ))
            for nome in nao_encontrados:
                self.stdout.write(f'  - {nome}')
        else:
            self.stdout.write(self.style.SUCCESS(
                'Todos os Brawlers do JSON foram encontrados no banco.'
            ))