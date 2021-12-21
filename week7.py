#Week 7
# https://techiesanswer.com/python-solution/how-to-create-github-repository-in-python/

from github import Github
gclient = Github('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')

user = gclient.get_user()
repo_name = user.login+'-repoWeek7'
user.create_repo(repo_name)
