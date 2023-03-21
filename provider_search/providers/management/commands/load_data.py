import pandas as pd
from django.core.management.base import BaseCommand
import json
# from ....models import Provider
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = 'Loads json data'

    def handle(self, *args, **options):
        json_file = '/Users/josephblackwell/code/uplift-provider-search/providers.json'
        print('trying')
        df = pd.read_json(json_file)
        
        df = df.set_index('id')
        # /Users/josephblackwell/code/uplift-provider-search/provider_search/
        engine = create_engine('sqlite:///db.sqlite3')
        # df.to_sql(Provider._meta.db_table, if_exists='replace', con=engine, index=True)