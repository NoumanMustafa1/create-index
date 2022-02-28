from elasticsearch import Elasticsearch

def generateIndex(es,query_body,index_name):
    try:
        es.index(index=index_name, body=query_body)
    except Exception as e:
        print(f"Exception occured:{e}")
            
if __name__ == '__main__':
    ELASTIC_HOST=''
    ELASTIC_USERNAME=''
    ELASTIC_PASSWORD=''

    es = Elasticsearch(hosts=[
            {
                'host': ELASTIC_HOST,
                'port': 9243,
                'use_ssl': True
            }
        ],
        timeout=30,
        http_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD),
        http_compress=True
    )
    
    query={  "settings": {  "number_of_shards": 1,"number_of_replica":1},"mappings": {"properties": {
        "collection_id": { "type": "Numbers" },
        "author_id": { "type": "Numbers" }, 
        "vol_no": { "type": "Numbers" },
        "vno_for_search": { "type": "text" },
        "lang": { "type": "text" },
        "text": { "type": "text" },
        "collection": { "type": "text" },
        "author": { "type": "text" },
        "author_priority": { "type": "text" },
        "page_no": { "type": "Numbers" },
        "pdf_pno": { "type": "Numbers" },
        "url":{ "type": "text" },
        "ref_text": { "type": "text" }
        
        }}}