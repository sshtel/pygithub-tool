from github import Github
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


# repositories_search = g.search_repositories(query='language:python')
# for repo in repositories_search:
#    print(repo)



# Fetch pull requests by the committer

# pull_requests = repository.get_pulls(state="all", user=committer)
pull_requests = repository.get_pulls(state='open', sort='created', base='master')


# Initialize counters
pull_request_count = 0
lines_added_modified = 0
review_comment_count = 0

# Iterate through the pull requests
for pull_request in pull_requests:
    pull_request_count += 1

    # Fetch commits for the pull request
    commits = pull_request.get_commits()

    # Iterate through commits
    for commit in commits:
        lines_added_modified += commit.stats.additions + commit.stats.deletions

    # Fetch review comments for the pull request
    review_comments = pull_request.get_review_comments()
    review_comment_count += review_comments.totalCount

# Print the results
print(f"Pull Requests by {committer_username}: {pull_request_count}")
print(f"Lines Added/Modified by {committer_username}: {lines_added_modified}")
print(f"Review Comments by {committer_username}: {review_comment_count}")
