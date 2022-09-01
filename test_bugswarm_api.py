from bugswarm.common.rest_api.database_api import DatabaseAPI

TOKEN = 'NEc6kALgl4Wid0LvtypQuGUuIiguytpAfctYabLQ5F8'
ROOT = '/Users/yumeng/Workspace/BugSwarm-master'

bugswarmapi = DatabaseAPI(token=TOKEN)
api_filter = '{"reproduce_successes":{"$gt":0, "$lt":10}, "lang":"Java"}'
bugswarmapi.filter_artifacts(api_filter)