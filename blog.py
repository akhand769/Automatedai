import os
import openai
import config
openai.api_key = config.OPENAI_API_KEY
def generatename(prompt):
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt="Following data is provided by a candidate to apply for a college:\nName of the Candidate:\
  {}\nDate of Birth: 11-08-1996\nCurrent location: N/A\nContact Number: 994859503\nCountry for which candidate\
  has applied for Student Visa: Canada\nCollege candidate has applied for admission: Canadore college, Northbay, College Drive\nCourse\
  Name: Human Resources Management\nIELTS Academics Band Score: 6 \nIELTS Score in Listening: 6\nIELTS Score in Reading: 6\nIELTS \
  Score in Writing: 6\nIELTS Score in Speaking: 6\nEducation:\n| Class | Score | Education Board/University | Year of passing |Stream\
  |\n| Class 10 | 65% | PSEB | 2012 | N/A |\n| Class 12 | 44% | CBSE | 2014 | Commerce |\n| Bachelor of arts | 59.95% | \
  punjabi university patiala | 2020 | psychology,sociology,physical education,english,punjabi |\
  \nWork Experience: N/A\nHobbies/Extra Curricular activities: N/A\nFamily Background: my father is farmer as well as does farming. Mother housewife.\
  Grandmother getting pension by indian army as my grandfather was a army officer. my sister has done her graduation in b.com in 2020\nHas candidate received visa refusal in the past:\
  Yes\nDoes candidate have a gap year: No\nDetails about the gap year: N/A\nDetails of GIC paid and Fees amount deposited: my father and grandmother help me in my financials.\
  i have paid my full tution\nPaid the fees for the SOP services: Yes\nAmount paid for SOP services: N/A\n\nGenerate Statement of\
  Purpose on the basis of the data provided by the student:\n\n".format(prompt),
    temperature=0.7,
    max_tokens=1600,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  return response['choices'][0]['text']

