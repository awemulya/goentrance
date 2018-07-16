import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Course


class Command(BaseCommand):
    help = 'load courses data from institute.csv file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_csv(sys.argv[3])
        courses = [
            Course(
                id=df['id'][row],
                name=df['name'][row],
        ) for row in range(0, 9)
        ]
        courses = Course.objects.bulk_create(courses)
        if courses:
            self.stdout.write('Successfully loaded Courses..')
