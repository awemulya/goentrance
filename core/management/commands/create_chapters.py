import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Unit, Chapter


class Command(BaseCommand):
    help = 'load subject chapters data from chapter.csv file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_csv(sys.argv[3])
        chapters = [
            Chapter(
                id=df['id'][row],
                name=df['name'][row],
                unit=Unit.objects.get(id=df['unitid'][row]),

            ) for row in range(0, 632)
        ]
        chapters = Chapter.objects.bulk_create(chapters)
        if chapters:
            self.stdout.write('Successfully loaded subject-chapters..')
