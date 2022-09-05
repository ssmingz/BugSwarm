import os
import json
from bugswarm.common.rest_api.database_api import DatabaseAPI


TOKEN = 'NEc6kALgl4Wid0LvtypQuGUuIiguytpAfctYabLQ5F8'
ROOT = '/Users/yumeng/Workspace/BugSwarm-master'

bugswarm_path = os.path.join(ROOT, 'docs', 'bugswarm.json')
if os.path.exists(bugswarm_path):
    with open(bugswarm_path) as fd:
        bugswarm_jobs = json.load(fd)

target_bugid_list = []
for job in bugswarm_jobs:
    bugid = job['image_tag']
    #s1 = job['failed_job']['config']['language']
    #s2 = job['classification']['code']
    #print(f'{s1} {s2}')
    lang_is_java = job['failed_job']['config']['language'] == 'java'
    cl_is_test = (job['classification']['code'] == 'Yes' or job['classification']['code'] == 'Partial')
    if lang_is_java and cl_is_test:
        target_bugid_list.append(bugid)



count = 0
for bugid in os.listdir(f'{ROOT}/BugSwarm'):
    count += 1
    src_path = f'{ROOT}/BugSwarm/{bugid}'
    if os.path.isdir(src_path):
        if bugid in target_bugid_list:
            tgt_path = os.path.join(ROOT, 'BugSwarm_java_inCode', bugid)
            os.mkdir(tgt_path)
            os.system(f'cp {src_path}/failed.diff {tgt_path}/failed.diff')
            os.system(f'cp {src_path}/patch.diff {tgt_path}/patch.diff')
            os.system(f'cp {src_path}/failing.log {tgt_path}/failing.log')
            print(f'finish {count}/{len(target_bugid_list)}')