"""import os
import openai
import config
openai.api_key = config.OPENAI_API_KEY

def generatename(prompt):
  start_sequence = "To,"
  response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Following data is provided by a candidate to apply for a college:\nName of the Candidate: Pawani singh Mastana\nDate of Birth: 11-08-1996\nCurrent location: N/A\nContact Number: 994859503\nCountry for which candidate has applied for Student Visa: Canada\nCollege candidate has applied for admission: Canadore college, Northbay, College Drive\nCourse Name: Human Resources Management\nIELTS Academics Band Score: 6 \nIELTS Score in Listening: 6\nIELTS Score in Reading: 6\nIELTS Score in Writing: 6\nIELTS Score in Speaking: 6\nEducation:\n| Class | Score | Education Board/University | Year of passing |Stream |\n| Class 10 | 65% | PSEB | 2012 | N/A |\n| Class 12 | 44% | CBSE | 2014 | Commerce |\n| Bachelor of arts | 59.95% | punjabi university patiala | 2020 | psychology,sociology,physical education,english,punjabi |\nWork Experience: N/A\nHobbies/Extra Curricular activities: N/A\nFamily Background: my father is farmer as well as does farming. Mother housewife. Grandmother getting pension by indian army as my grandfather was a army officer. my sister has done her graduation in b.com in 2020\nHas candidate received visa refusal in the past: Yes\nDoes candidate have a gap year: No\nDetails about the gap year: N/A\nDetails of GIC paid and Fees amount deposited: my father and grandmother help me in my financials. i have paid my full tution\nPaid the fees for the SOP services: Yes\nAmount paid for SOP services: N/A\n\nWrite an application to visa officer by giving Generate Statement of Purpose with the reason of refusal of visa application on the basis of the data provided by the student:\n",
  temperature=0.7,
  max_tokens=1671,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )

  return response['choices'][0]['text']"""
import os
import openai
import config

openai.api_key = config.OPENAI_API_KEY


def generatename(prompt):
  start_sequence = "To,"
  response = openai.Completion.create(
  model="text-davinci-002",
  prompt="If {} is an url then search on google and use details in the SOP.\Generate a SOP for refusal of visa by explaining about purpose of visit to the country {} and importance of the course {} and the university {} in which candidate\
    is going to take admission and also explain about reason to return back to home country which should based on the family background and current background provided below - \
    The SOP should be in following format divided in 4 paragraphs- \
    To,\n\
    Visa Officer\n\
    {}\n\
    {}\n\
    Give subject of the sop as : SOP/Explanation regarding refusal of visa\
    Greet with respected Sir/Ma'am\
    Now write application with an experience generated from the experience given by the candidate\
    for refusal of visa and finally conclude the application by requesting to\
    reconsider the application and also give reasons for it.\
    Following data is provided by a candidate to apply for a college:\n\
    Name of the Candidate is {} .\
    Date of Birth is {} .\
    Contact Number of candidate is {} .\
    Country for which candidate has applied for Student Visa is {} .\n\
    Instruction - Explain in detail about purpose of visit to {} country\
    Name of college candidate has applied for admission is {} .\n\
    Instruction - Explain in detail why {} university is better ?\n\
    Instruction - Explain in details about {} course\n\
    IELTS Academics Band and score in Listening /Reading /Writing /Speaking are as : {} \n\
    Write a paragraph to give scores of the candidate as below -\
    Academics percentages for 10th ,12th ,graduation with the year of passing and stream choosen are as: {} \n\
    Instruction - Give 100 words detailed information of the above academic and IELTS scores of the candidate\n \
    Instruction - Write a 200 words paragraph to give reason to the officer that the candidate will be returning back to the country giving the reason as : {}. \
    Has candidate received visa refusal in the past status is {} .\n\
    Write any story about candidate to have experience as : {}.\n\
    Does candidate have a gap year  {} .\
    Details of GIC paid and Fees amount deposited are {} .\
    Paid the fees for the SOP services is {} .\
    Instruction - At last conclude the SOP with request to accept the visa. \
    ".format(prompt[5],prompt[5],prompt[6],prompt[7],prompt[4],prompt[2],prompt[0],prompt[1],prompt[3],prompt[4],prompt[5],prompt[6],prompt[6],prompt[7],prompt[7]\
      ,prompt[8],prompt[9],prompt[10],prompt[11],prompt[12],prompt[13],prompt[14],prompt[15]),
  temperature=0.7,
  max_tokens=3000,
  top_p=1,
  frequency_penalty=0.2,
  presence_penalty=0
  )
  return response['choices'][0]['text']
 



