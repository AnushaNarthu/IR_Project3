import json
import urllib.request
import urllib
import string
import requests

if __name__ == "__main__":
    core = 'IRF21_project3_bm25'
    #outfn = 'test_output.txt'
    IRModel = 'bm25' 
    #outf = open(outfn, 'w+')
    file_count = 1
    with open('test-queries.txt', encoding="utf-8") as input_queries:
    #with open('queries.txt', encoding="utf-8") as input_queries:
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
            #print(docs)
            rank = 1
            outf = open('BM25/' + str(file_count)+'.txt', 'w+')
            for doc in docs:
                outf.write(str(qid) + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(
                    doc['score']) + ' ' + IRModel + '\n')
                rank += 1
            outf.close()
            file_count +=1
        input_queries.close()
