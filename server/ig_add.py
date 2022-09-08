from flask import request,render_template
from server.models.IG_Adds import IG_Adds # importing all the models(this is after db so that db can be recognized by models!)
from server import app
from server import db
from flask import request
from flask import render_template, url_for,flash, redirect
from server.models.form import IG_Link



@app.route('/IG/TQ/add/q')
def get_IGurls():
  links = IG_Adds.query.all()
  output = []
  
  for each in links:
    url_data = {'URL': each.url}
    output.append(url_data)
  
  return {"URLs: ": output}

@app.route('/IG/TQ/add',methods=['GET','POST'])
def add_IGurl():
  # #new = IG_Adds(url=link)
  # new = IG_Adds(url=request.json['url'])
  # db.session.add(new)
  # db.session.commit()
  # return {'id': new.id}
  form = IG_Link()
  if form.validate_on_submit():
    url = IG_Adds(url=form.link.data)
    db.session.add(url)
    db.session.commit()
    flash("URL Added Successfully.")
    return redirect(url_for('index'))
  # url = FB_Adds(url=form.link.data)
  # db.session.add(url)
  # db.session.commit()
  return render_template('url_taker.html', form=form)

@app.route('/IG/TQ/add',methods=['DELETE'])
def delete_IGurl(link):
  all_links = IG_Adds.query.all()
  for each in all_links:
    if (each.url == link):
      db.session.delete(each)
      db.session.commit()