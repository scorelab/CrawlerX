from elasticsearch_dsl import Document, Date, Nested, token_filter, Boolean, \
    analyzer, InnerDoc, Completion, Keyword, Text, connections, Integer, Short, Float, Double, tokenizer, Long, analysis

data_analyzer = analyzer(
    'data_analyzer',
    tokenizer=tokenizer(
        'whitespace',
        'standard'
        'letter'
        'ngram',
        min_gram=1,
        max_gram=100,
    ),
    filter=[
        'lowercase',
        token_filter('asciifolding')
    ]
)


class ProjectIndex(Document):
    User_ID = Integer()
    Project_Id = Integer()
    Url = Text(analyzer=data_analyzer, fields={'keyword': Keyword()})
    Regex_patterns = Text(analyzer=data_analyzer, fields={'keyword': Keyword()})
    CreationDate = Date()
    Headers = Text(analyzer=data_analyzer, fields={'keyword': Keyword()})
    Div_Id = Text(analyzer=data_analyzer, fields={'keyword': Keyword()})
    alink = Text(analyzer=data_analyzer, fields={'keyword': Keyword()})
    Scrapped_Data = Text(analyzer=data_analyzer, fields={'keyword': Keyword()})

    class Index:
        name = "projects"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
