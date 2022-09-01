import requests
import os
import json

token = 'NEc6kALgl4Wid0LvtypQuGUuIiguytpAfctYabLQ5F8'
ROOT = '/Users/yumeng/Workspace/BugSwarm-master'

travis_jobs_path = os.path.join(ROOT, 'docs', 'travis_data.json')
if os.path.exists(travis_jobs_path):
    with open(travis_jobs_path) as fd:
        travis_jobs = json.load(fd)

images = []
with open(os.path.join(ROOT, 'docs', 'commits.txt')) as fd:
    lines = fd.read().splitlines()
    for l in lines:
        (commit, branch) = l.split('\t')
        if branch == 'HEAD' or branch == 'master':
            continue
        images.append({
            'branch': branch,
            'commit': commit
        })

count = 0
for image in images:
    bug_id = image['branch']

    bug_path = os.path.join(ROOT, 'BugSwarm', bug_id)
    diff_path = os.path.join(bug_path, 'failed.diff')

    if os.path.exists(diff_path):
        continue

    branch_id = bug_id.split('-')[-1]
    travis_job_info = travis_jobs[branch_id]
    repo_slug = travis_job_info['repository_slug']
    failed_commit = travis_job_info['commit']['sha']

    url = "https://github.com/%s/commit/%s.diff" % (repo_slug, failed_commit)
    r = requests.get(url)
    if r.status_code != 200:
        if os.path.exists(diff_path):
            os.remove(diff_path)
            continue
    count += 1
    content = r.content
    print(count, int(count * 100 / 3091), bug_id, url, r.status_code)

    if not os.path.exists(bug_path):
        os.makedirs(bug_path)

    with open(diff_path, 'wb') as fd:
        fd.write(content)

print(count)