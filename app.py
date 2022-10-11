from flask import Flask, render_template, request
import config
import blog
def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
      prompt= []
      prompt.append(request.form['nameofcandidate'])
      prompt.append(request.form['dateofbirth'])
      prompt.append(request.form['locationofcandidate'])
      prompt.append(request.form['numberofcandidate'])
      prompt.append(request.form['country'])
      prompt.append(request.form['nameofcollege'])
      prompt.append(request.form['nameofcourse'])
      prompt.append(request.form['score'])
      prompt.append(request.form['score2'])
      prompt.append(request.form['experience'])
      prompt.append(request.form['parentsinfo'])
      prompt.append(request.form['refusal'])
      prompt.append(request.form['academicinfo'])
      prompt.append(request.form['gapyear'])
      prompt.append(request.form['fees'])
      prompt.append(request.form['feestatus'])
      prompt.append(request.form['confirmation'])
      for i in prompt:
        print(i)
      blogT = blog.generatename(prompt)
      blogTopicIdeas = blogT.replace('\n','<br>')
    return render_template('index.html', **locals())



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
