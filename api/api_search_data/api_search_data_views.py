from rest_framework.response import Response
from rest_framework.views import APIView
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from rest_framework import status

client = Elasticsearch(hosts="elasticsearch")


class SearchData(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        data = []
        try:
            s = Search().using(
                client
            ).query(
                "multi_match",
                query=query,
                fields=[
                    'Url',
                    'Regex_patterns',
                    'Headers',
                    'Div_Id',
                    'alink',
                    'Scrapped_Data'
                ]
            )
            response = s.execute()
            response_dict = response.to_dict()
            hits = response_dict['hits']['hits']
            for val in hits:
                data.append(val["_source"])
            data_to_send = {
                "msg": "smart search success",
                "data": data
            }
            return Response(data=data_to_send, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
