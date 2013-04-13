import pymongo

# open pool connection
conn = pymongo.Connection()

# create db
db = conn.testdb

# stub
db.test.insert({
  "SurveyName":"blah",
  "Description":"this is not a survey",
  "Questions":
  [
    {
      "ID":"1",
      "Content":"question1"
    },
    {
      "ID":"2",
      "Content": "question2"
    }
  ],

  "Creator":"Name",
  "Created On":"'7/22/2008 12:11:04 PM'",
  "Updated On":"'7/22/2008 12:11:04 PM'"
})


db.test.insert({
    "SurveyName":"blah",
      "Description":"this is not a survey",
        "Questions":
          [
              {
                      "ID":"1",
                            "Content":"question1"
                                },  
                                    {   
                                            "ID":"2",
                                                  "Content": "question2"
                                                      }   
                                                        ],  

                                                          "Creator":"Name",
                                                            "Created On":"'7/22/2008 12:11:04 PM'",
                                                              "Updated On":"'7/22/2008 12:11:04 PM'"
})



for i in list(db.test.find()):
  print i


