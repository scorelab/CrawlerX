from django.core.management.base import BaseCommand, CommandError
from elasticsearch_dsl import Search, Index, connections
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from create_project.models import ProjectModel
from DisplayData.document import ProjectIndex
from elasticsearch_dsl import connections


print("I am alive!!")
ES_HOST = os.environ.get('ES_HOST')
ES_PORT = os.environ.get('ES_PORT')

connections.create_connection(
    hosts=[{'host': ES_HOST, 'port': ES_PORT}])


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(ES_HOST)
        print(ES_PORT)
        es = Elasticsearch(
            [{'host': ES_HOST, 'port': ES_PORT}],
            index="projects"
        )
        project_index = Index('projects')
        project_index.document(ProjectIndex)
        result = bulk(
            client=es,
            actions=(que.indexing() for que in ProjectModel.objects.all())
        )

        print('Indexed Scrapped Data')

        print("indexed entries:" + str(result[0]))
