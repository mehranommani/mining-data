import user_input
import github_apis
import pandas as pd
#User inputs
url = user_input.ask_user_for_repo()
response = github_apis.get_pull_requests(url) 
pull_requests = response.json()
#This is an empty list to store the data
data = []
#extract comment on pull request
for pull_request in pull_requests:
    number = pull_request['number']
    title = pull_request['title']
    # print(str(number))
    #extract review comment on pull request
    comment_response = github_apis.get_comments(url,number) 
    comment_requests = comment_response.json()
    for comment_request in comment_requests:
        comment = comment_request['body']
    review_response = github_apis.get_review(url,number)
    review_request = review_response.json()
    for review_request in review_request:
        review = review_request['body']
        
        data.append({'Number': number, 'Title': title, 'Comment': comment, 'Review': review})
        # print(f'Review comment on pull request #{number}:\n the subject is ========>>>>> {title} \n the comments is ===========>>>>>> {comment} \n the reviews are ==========>>>>> {review}')
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)
# print(response , end='              ')

