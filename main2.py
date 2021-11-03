import json
import urllib.request
import urllib
import string
import requests

if __name__ == "__main__":
    core = 'IRF21_p3_demo_vsm'
    outfn = 'test_output1.txt'
    IRModel = 'vsm' 
    outf = open(outfn, 'a+')
    with open('queries.txt', encoding="utf-8") as input_queries:
        for line in input_queries:
            query = line.replace(':', '')
            arr = query.split()
            join_query=""
            for i in range(1,len(arr)):
                join_query+=arr[i]+" "
            qid = arr[0]
            params={
            'q':'text_en:('+ join_query +')or text_de:('+join_query+') or text_ru:('+join_query+')',
            'fl':'id,score',
            'wt':'json',
            'indent':'true',
            'rows':'20'
            }

            query_response= requests.get(f'http://localhost:8983/solr/' + core + '/select', params=params)
            docs = query_response.json()['response']['docs']
            rank = 1
            for doc in docs:
                outf.write(str(qid) + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(
                    doc['score']) + ' ' + IRModel + '\n')
                rank += 1
        outf.close()
        input_queries.close()
