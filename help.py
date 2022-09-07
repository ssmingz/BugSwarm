import requests
import os
import json

ROOT = 'D:\\expdata\\bugswarm\\BugSwarm-master'

travis_jobs_path = os.path.join(ROOT, 'docs', 'travis_data.json')
if os.path.exists(travis_jobs_path):
    with open(travis_jobs_path) as fd:
        travis_jobs = json.load(fd)

bugswarm_jobs_path = os.path.join(ROOT, 'docs', 'bugswarm.json')
if os.path.exists(bugswarm_jobs_path):
    with open(bugswarm_jobs_path) as fd:
        bugswarm_jobs = json.load(fd)

target_bugid_list = []
with open('targetlist.txt', 'r') as file:
    for l in file:
        target_bugid_list.append(l.strip())

count = 0
for job in bugswarm_jobs:
    tag = job['tag']
    if tag not in target_bugid_list:
        continue
    count += 1
    failed_commit = job['failed_job']['trigger_sha']
    passed_commit = job['passed_job']['trigger_sha']
    repo = job['repo']
    failed_url = f'https://github.com/{repo}/commit/{failed_commit}'
    passed_url = f'https://github.com/{repo}/commit/{passed_commit}'
    print(f'{count}\t{tag}\t{failed_url}\t{passed_url}')
