from django.core.management.base import BaseCommand
from brawldex.models import Brawler


class Command(BaseCommand):

    help = 'Cadastra os 108 Brawlers do Brawl Stars automaticamente'

    def handle(self, *args, **kwargs):

        brawlers = [

            # =========================
            # 108 BRAWLERS
            # =========================

            ('8-Bit', 'Super-raro', 'Dano', 5200, 340),
            ('Bo', 'Épico', 'Controle', 3800, 700),
            ('Brock', 'Raro', 'Atirador', 3000, 1160),
            ('Lumi', 'Mítico', 'Dano', 3500, 600),
            ('Max', 'Mítico', 'Suporte', 3500, 320),
            ('Meg', 'Lendário', 'Tanque', 2400, 300),
            ('Nori', 'Lendário', 'Assassino', 3500, 1000),
            ('Rico', 'Super-raro', 'Dano', 3000, 300),
            ('Starr Nova', 'Mítico', 'Assassino', 3700, 480),
            ('Stu', 'Épico', 'Assassino', 3500, 540),
            ('Surge', 'Lendário', 'Dano', 3300, 1180),
            ('Wendy', 'Mítico', 'Suporte', 2000, 1000),

            ('Angelo', 'Épico', 'Atirador', 3100, 2000),
            ('Ash', 'Épico', 'Tanque', 5900, 800),
            ('Bolt', 'Épico', 'Tanque', 5000, 0),
            ('Byron', 'Mítico', 'Suporte', 2600, 0),
            ('Carl', 'Super-raro', 'Dano', 4200, 820),
            ('Colt', 'Raro', 'Dano', 3100, 360),
            ('Cordelius', 'Lendário', 'Assassino', 3500, 800),
            ('Crow', 'Lendário', 'Assassino', 2800, 320),
            ('Damian', 'Mítico', 'Tanque', 5600, 700),
            ('Edgar', 'Épico', 'Assassino', 3700, 540),
            ('Emz', 'Épico', 'Controle', 3900, 560),
            ('Gene', 'Mítico', 'Controle', 3800, 1000),
            ('Gray', 'Mítico', 'Suporte', 3400, 1280),
            ('Griff', 'Épico', 'Controle', 3700, 280),
            ('Leon', 'Lendário', 'Assassino', 3300, 480),
            ('Lou', 'Mítico', 'Controle', 3500, 440),
            ('Meeple', 'Épico', 'Controle', 3300, 1260),
            ('Mina', 'Mítico', 'Dano', 3600, 800),
            ('Mortis', 'Mítico', 'Assassino', 4000, 1000),
            ('Otis', 'Mítico', 'Controle', 3600, 500),
            ('Pearl', 'Épico', 'Dano', 4300, 280),
            ('Pierce', 'Lendário', 'Atirador', 3000, 950),
            ('Piper', 'Épico', 'Atirador', 2800, 1800),
            ('Ruffs', 'Mítico', 'Suporte', 3000, 600),
            ('Shade', 'Épico', 'Assassino', 3700, 800),

            ('Alli', 'Mítico', 'Assassino', 3900, 1300),
            ('Belle', 'Épico', 'Atirador', 2900, 1040),
            ('Bibi', 'Épico', 'Tanque', 5000, 1400),
            ('Bull', 'Raro', 'Tanque', 5000, 440),
            ('Charlie', 'Mítico', 'Controle', 3700, 800),
            ('Chester', 'Lendário', 'Dano', 3800, 670),
            ('Fang', 'Mítico', 'Assassino', 4800, 1360),
            ('Finx', 'Mítico', 'Controle', 3700, 900),
            ('Gus', 'Super-raro', 'Suporte', 3300, 1080),
            ('Kaze', 'Ultralendário', 'Assassino', 4100, 750),
            ('Kenji', 'Lendário', 'Assassino', 4000, 750),
            ('Kit', 'Lendário', 'Suporte', 3100, 1000),
            ('Lily', 'Mítico', 'Assassino', 4200, 1060),
            ('Mandy', 'Épico', 'Atirador', 3000, 1400),
            ('Moe', 'Mítico', 'Dano', 3600, 500),
            ('Najia', 'Mítico', 'Dano', 3400, 300),
            ('Nani', 'Épico', 'Atirador', 2500, 800),
            ('Nita', 'Raro', 'Dano', 4200, 960),
            ('Penny', 'Super-raro', 'Controle', 3500, 980),
            ('Poco', 'Raro', 'Suporte', 4000, 760),
            ('Sirius', 'Ultralendário', 'Controle', 3400, 600),
            ('Spike', 'Lendário', 'Dano', 3000, 540),
            ('Sprout', 'Mítico', 'Artilharia', 3200, 1100),
            ('Tara', 'Mítico', 'Dano', 3300, 480),

            ('Amber', 'Lendário', 'Controle', 3400, 210),
            ('Barley', 'Raro', 'Artilharia', 2700, 800),
            ('Buster', 'Mítico', 'Tanque', 5000, 1380),
            ('Buzz', 'Mítico', 'Assassino', 5000, 420),
            ('Colette', 'Épico', 'Dano', 3600, 1100),
            ('Darryl', 'Super-raro', 'Tanque', 5500, 240),
            ('Draco', 'Lendário', 'Tanque', 5600, 700),
            ('Frank', 'Épico', 'Tanque', 6800, 1160),
            ('Gale', 'Épico', 'Controle', 4000, 300),
            ('Gigi', 'Mítico', 'Assassino', 4100, 600),
            ('Glowy', 'Mítico', 'Suporte', 3900, 280),
            ('Jae-Yong', 'Mítico', 'Suporte', 3700, 750),
            ('Juju', 'Mítico', 'Artilharia', 3100, 1000),
            ('Lola', 'Épico', 'Dano', 4000, 280),
            ('Melodie', 'Mítico', 'Assassino', 4000, 460),
            ('R-T', 'Mítico', 'Dano', 4100, 700),
            ('Trunk', 'Épico', 'Tanque', 5200, 1400),

            ('Bea', 'Épico', 'Atirador', 2800, 800),
            ('Berry', 'Épico', 'Suporte', 2600, 660),
            ('Bonnie', 'Épico', 'Atirador', 5000, 1220),
            ('Doug', 'Mítico', 'Suporte', 5200, 1200),
            ('Dynamike', 'Super-raro', 'Artilharia', 3000, 800),
            ('Eve', 'Mítico', 'Dano', 3100, 400),
            ('Hank', 'Épico', 'Tanque', 5500, 0),
            ('Janet', 'Mítico', 'Atirador', 3400, 1100),
            ('Jessie', 'Super-raro', 'Controle', 3300, 1060),
            ('Larry & Lawrie', 'Épico', 'Artilharia', 3000, 700),
            ('Maisie', 'Épico', 'Atirador', 4000, 1500),
            ('Mico', 'Mítico', 'Assassino', 3500, 1140),
            ('Ollie', 'Mítico', 'Tanque', 5400, 900),
            ('Rosa', 'Raro', 'Tanque', 5400, 500),
            ('Sandy', 'Lendário', 'Controle', 4100, 900),
            ('Shelly', 'Comum', 'Dano', 3900, 300),
            ('Squeak', 'Mítico', 'Controle', 3800, 1160),
            ('Willow', 'Mítico', 'Controle', 3300, 0),
            ('Ziggy', 'Mítico', 'Controle', 3200, 950),

            ('Chuck', 'Mítico', 'Controle', 4400, 540),
            ('Clancy', 'Mítico', 'Dano', 3800, 700),
            ('El Primo', 'Raro', 'Tanque', 6500, 380),
            ('Grom', 'Épico', 'Artilharia', 3000, 1040),
            ('Jacky', 'Super-raro', 'Tanque', 5200, 0),
            ('Mr. P', 'Mítico', 'Controle', 3700, 760),
            ('Pam', 'Épico', 'Suporte', 5000, 300),
            ('Sam', 'Épico', 'Assassino', 5700, 800),
            ('Tick', 'Super-raro', 'Artilharia', 2400, 680),

            ('Cosmo', 'Mítico', 'Controle', 3400, 0),
            ('Vince', 'Mítico', 'Dano', 3400, 1100),
        ]

        descricoes = {
            'Dano': (
                'Brawler especializado em causar grande quantidade '
                'de dano aos inimigos.'
            ),

            'Tanque': (
                'Brawler resistente, especializado em absorver dano '
                'e lutar em curta distância.'
            ),

            'Atirador': (
                'Brawler especializado em ataques precisos '
                'de longa distância.'
            ),

            'Controle': (
                'Brawler especializado em controlar áreas '
                'e limitar os movimentos dos inimigos.'
            ),

            'Suporte': (
                'Brawler especializado em ajudar aliados '
                'e melhorar a sobrevivência da equipe.'
            ),

            'Assassino': (
                'Brawler especializado em eliminar inimigos '
                'rapidamente e se movimentar pelo campo.'
            ),

            'Artilharia': (
                'Brawler especializado em atacar por cima '
                'de obstáculos e controlar áreas.'
            ),
        }

        quantidade = 0

        for nome, raridade, classe, vida, dano in brawlers:

            brawler, criado = Brawler.objects.get_or_create(
                nome=nome,
                defaults={
                    'nome': nome,
                    'raridade': raridade,
                    'classe': classe,
                    'vida': vida,
                    'dano': dano,
                    'descricao': descricoes.get(
                        classe,
                        'Brawler do Brawl Stars.'
                    ),
                }
            )

            if criado:

                quantidade += 1

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Criado: {brawler.nome}'
                    )
                )

            else:

                self.stdout.write(
                    self.style.WARNING(
                        f'Já existe: {brawler.nome}'
                    )
                )

        self.stdout.write('')

        self.stdout.write(
            self.style.SUCCESS(
                f'{quantidade} Brawlers novos cadastrados!'
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'Total na lista: {len(brawlers)} Brawlers.'
            )
        )