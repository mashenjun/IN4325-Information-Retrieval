__author__ = 'alienware'

from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, Http404
from django.template import *
import os



def viewCSV(request):
    return  render_to_response('viewCSV.html')

def viewTotal(request):
    return  render_to_response('viewTotal.html')

def index(request):
    return  render_to_response('index.html')

def JavaRead(request):
    t = get_template('JavaRead.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def Result(request):
    t = get_template('Result.html')
    html = t.render(Context({}))
    return HttpResponse(html)


def selecttweets(Num):
    import csv
    tweetscontent=''
    i=1
    uncertaintweets=open('./static/uncertaintweets.csv','w',newline='')
    writer=csv.writer(uncertaintweets)

    with open('./static/uncertain.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            tweet=row[0]
            writer.writerow([tweet])
            i=i+1
            if i>Num:
                 break

        writer=csv.writer(f)

    uncertaintweets.close()

def postdata(Num):
    import csv
    import requests

    API_KEY = "NUbs14x8-jenQy1tnSJ5"
    job_id = "707980"
    #Num = request.GET['Num']
    selecttweets(Num)

    file_path = "./static/uncertaintweets.csv"
    csv_file = open(file_path, 'rb')

    request_url = "https://api.crowdflower.com/v1/jobs/{}/upload".format(job_id)
    headers = {'content-type': 'text/csv'}
    payload = { 'key': API_KEY }
    print(os.getcwd())
    requests.put(request_url, data=csv_file, params=payload, headers=headers)

def main(request):
    import csv
    import requests
    Num= int(request.GET['Num'])

    API_KEY = "NUbs14x8-jenQy1tnSJ5"
    job_id = "707980"
    #Num = request.GET['Num']
    tweetscontent=''
    i=1
    uncertaintweets=open(os.path.join(os.path.dirname(__file__),'static/uncertaintweets.csv'),'w',newline='')
    #'E:/programming/Python/IR/mysite/mysite/static/uncertaintweets.csv'
    writer=csv.writer(uncertaintweets)

    with open(os.path.join(os.path.dirname(__file__),'static/uncertain.csv')) as f:
        #'E:/programming/Python/IR/mysite/mysite/static/uncertain.csv'
        reader = csv.reader(f)
        for row in reader:
            tweet=row[0]
            writer.writerow([tweet])
            i=i+1
            if i>Num:
                 break

        writer=csv.writer(f)

    uncertaintweets.close()

    file_path = os.path.join(os.path.dirname(__file__),'static/uncertaintweets.csv')
        #"E:/programming/Python/IR/mysite/mysite/static/uncertaintweets.csv"
    csv_file = open(file_path, 'rb')

    request_url = "https://api.crowdflower.com/v1/jobs/{}/upload".format(job_id)
    headers = {'content-type': 'text/csv'}
    payload = { 'key': API_KEY }

    requests.put(request_url, data=csv_file, params=payload, headers=headers)
    return HttpResponse("Success!!!")

