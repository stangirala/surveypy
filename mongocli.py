import pymongo
import json

# open pool connection
conn = pymongo.Connection()

# create db
db = conn.testdb

print conn.database_names()

# stub

# check and make sure that the date object does not break the thing
jsonstr = '{"SurveyName":"blah", "Description":"this is not a survey", "Questions": [ { "ID":"1", "Content":"question1"}, { "ID":"2", "Content": "question2"}], "Creator":"Name", "Created On":"7/22/2008 12:11:04 PM", "Updated On":"7/22/2008 12:11:04 PM"}'

obj = json.loads(jsonstr)

db.test.insert(obj)

itr = db.test.find_one({"SurveyName":"blah"})

#print itr

for i in list(db.test.find({"SurveyName":"blah"})):
  print i
  db.test.remove(i)

for i in list(db.test.find({"SurveyName":"blah"})):
  print i

