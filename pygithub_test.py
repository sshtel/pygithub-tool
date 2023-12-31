# github Repository
# ==> by PRs
# ======> by commit
# ==========> commit addition/deletion LoC

from github import Github
from datetime import datetime
import os

tokenFile = open('./accesstoken', 'r')
token = tokenFile.read()
print(token)

# Authenticate with your personal access token
g = Github(token)

user = g.get_user()
print(user.login)
print(user.name)


# Define the repository and committer
repository_name = "sshtel/pygithub-tool"
committer_username = "sshtel"

repository = g.get_repo(repository_name)
committer = g.get_user(committer_username)

print(f"commiter info of {committer_username}")
print(committer)
print("-------------------------------")

# Fetch pull requests by the committer

### Reference: https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html
pull_requests = repository.get_pulls(state='all', sort='created', base='main')
# pull_requests = repository.get_pulls(state='open', sort='created')


print(f"PRs to main branch of {repository}")
for pr in pull_requests:
    print(pr)
print("-------------------------------")


### Reference: https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html
sinceDateTime = datetime.fromisoformat('2023-11-05T00:00:00')
print(f"PR comments of {repository} since {sinceDateTime}")
pr_comments = repository.get_pulls_comments(sort='created', since=sinceDateTime)

### Reference: https://pygithub.readthedocs.io/en/latest/github_objects/PullRequestComment.html
for pr_comment in pr_comments:
    print(pr_comment)
    # reactions = pr_comment.get_reactions()
    # ### Reference: https://pygithub.readthedocs.io/en/latest/github_objects/Reaction.html
    # for reaction in reactions:
    #     print(reaction)
print("-------------------------------")

print(f"PR Review Comments of {repository} since {sinceDateTime}")
get_pulls_review_comments = repository.get_pulls_review_comments(sort='created', since=sinceDateTime)

### Reference: https://pygithub.readthedocs.io/en/latest/github_objects/PullRequestComment.html
for pr_review_comment in get_pulls_review_comments:
    print(pr_review_comment)
    # reactions = pr_review_comment.get_reactions()
    # for reaction in reactions:
    #     print(reaction)
print("-------------------------------")

# get_pulls_comments(sort: Opt[str] = NotSet, direction: Opt[str] = NotSet, since: Opt[datetime] = NotSet) → PaginatedList[PullRequestComment]¶


# Initialize counters
pull_request_count = 0
lines_added_modified = 0
comment_count = 0
review_comment_count = 0
review_count = 0


# Iterate through the pull requests
for pull_request in pull_requests:
    print("-------------------------------")
    pull_request_count += 1

    print(f"==> commit infos of PR {pull_request}")
    # Fetch commits for the pull request
    commits = pull_request.get_commits()

    # Iterate through commits
    for commit in commits:
        print(f"==> ==> commit: {commit}")
        print(f"==> ==> committer: {commit.commit.committer}")
        print(f"==> ==> committer.date: {commit.commit.committer.date}")
        print(f"==> ==> author: {commit.commit.author}")
        print(f"==> ==> author.date: {commit.commit.author.date}")
        lines_added_modified += commit.stats.additions + commit.stats.deletions


    # Fetch comments for the pr
    comments = pull_request.get_comments()
    print(f"==> comments: {comments}")
    for comment in comments:
        print(comment)
        reactions = comment.get_reactions()
        for reaction in reactions:
            print(reaction)

    comment_count += comments.totalCount

    # Fetch review comments for the pull request
    review_comments = pull_request.get_review_comments()
    print(f"==> review_comments: {review_comments}")
    for review_comment in review_comments:
        print(review_comment)
        reactions = review_comment.get_reactions()
        for reaction in reactions:
            print(reaction)

    review_comment_count += review_comments.totalCount


    # Fetch review 
    reviews = pull_request.get_reviews()
    print(f"==> reviews: {reviews}")
    for review in reviews:
        print(f"===> ===> {review}")
        # print(f"===> ===> review.id: {review.id}")
        # print(pull_request.get_review(review.id))
        
    review_count += reviews.totalCount

# Print the results

print("=====================================")
print(f"Total Pull Requests: {pull_request_count}")
print(f"Lines Added/Modified: {lines_added_modified}")
print(f"Comments: {comment_count}")
print(f"Review Comments: {review_comment_count}")
print(f"Reviews: {review_count}")
print("=====================================")