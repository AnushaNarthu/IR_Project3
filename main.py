import json
import urllib.request
import urllib
import string
import requests

if __name__ == "__main__":
    core = 'IRF21_p3_demo_bm25'
    outfn = 'test_output.txt'
    IRModel = 'bm25' 
    outf = open(outfn, 'a+')
    with open('queries.txt', encoding="utf-8") as input_queries:
        for line in input_queries:
            query = line.replace(':', '')
            arr = query.split()
            join_query=""
            for i in range(1,len(arr)):
                join_query+=arr[i]+" "
            qid = arr[0]
            query_response = requests.get(f'http://localhost:8983/solr/' + core + '/select?fl=id%2Cscore&q=text_en%3A(' \
                            + join_query + ')%20or%20text_de%3A(' + join_query + ')%20or%20text_ru%3A(' \
                            + join_query + ')' + '&rows=20&wt=json')
            docs = query_response.json()['response']['docs']
            rank = 1
            for doc in docs:
                outf.write(str(qid) + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(
                    doc['score']) + ' ' + IRModel + '\n')
                rank += 1
        outf.close()
        input_queries.close()
