##This file communicates and calls API end points 
import requests
import json
# function that prepers the heading, since it is needed in every api. 

#Function that calls the api you want. this, uses, the header methods

def get_pull_requests(url):
    # define the GitHub token
    TOKEN = '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'

    url = url+"/pulls"
    headers = {'Authorization': f'token {TOKEN}'}
    print(url)
    params = {'per_page': 100}
    response = requests.get(url, headers=headers, params=params)
    print(response)
    return response


def get_comments(url,pr_number):
    # define the GitHub token
    TOKEN = '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'
    url = url +"/pulls" + "/comments" 
    print (url)
    # url = url+"/pulls/comments"
    headers = {'Authorization': f'token {TOKEN}'}
    params = {'per_page': 100}
    comment_response = requests.get(url, headers=headers, params=params)
    print(comment_response)
    return comment_response

def get_review(url,pr_number):
    # define the GitHub token
    TOKEN = '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'
    url = url +"/pulls/" + str(pr_number) + "/comments" 
    print (url)
    # url = url+"/pulls/comments"
    headers = {'Authorization': f'token {TOKEN}'}
    params = {'per_page': 100}
    review_response = requests.get(url, headers=headers, params=params)
    print(review_response)
    return review_response