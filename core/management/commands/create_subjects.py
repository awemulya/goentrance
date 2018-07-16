import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Subject, Course


class Command(BaseCommand):
    help = 'load subjects data from subject.csv file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_csv(sys.argv[3])
        subjects = [
            Subject(
                id=df['id'][row],
                name=df['name'][row],
                course=Course.objects.get(id=df['instituteid'][row]),

            ) for row in range(0, 41)
        ]
        subjects = Subject.objects.bulk_create(subjects)
        if subjects:
            self.stdout.write('Successfully loaded course-subjects..')
