import pymongo
import json

def pushsurvey(jsonstr):

  # open pool connection
  conn = pymongo.Connection()

  # create db
  db = conn.testdb

  # check and make sure that the date object does not break the thing
  '''jsonstr = '{"SurveyName":"blah", "Description":"this is not a survey", "Questions": [ { "ID":"1", "Content":"question1"}, { "ID":"2", "Content": "question2"}], "Creator":"Name", "Created On":"7/22/2008 12:11:04 PM", "Updated On":"7/22/2008 12:11:04 PM"}'''

  obj = json.loads(jsonstr)

  for i in list(db.test.find({"SurveyName":"blah"})):
    db.test.remove(i)

  db.test.insert(obj)

  for i in list(db.test.find({"SurveyName":"blah"})):
    print "QUESTION HERE\n\n"
    print i['Description']
    print "DONE\n\n"
