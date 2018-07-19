import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Subject, Unit


class Command(BaseCommand):
    help = 'load subject unit data from unit.csv file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_csv(sys.argv[3])
        unit = [
            Unit(
                id=df['id'][row],
                name=df['name'][row],
                subject=Subject.objects.get(id=df['subjectid'][row]),

            ) for row in range(0, 114)
        ]
        unit = Unit.objects.bulk_create(unit)
        if unit:
            self.stdout.write('Successfully loaded subject-unit..')
