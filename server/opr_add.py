from flask import render_template
from flask import request
from server.models import OPR_Queue, OPR_Users, OPR_Adds # importing all the models(this is after db so that db can be recognized by models!)
from server import app
from server import db

from server.models.OPR_Queue import OPR_Queue
from server.models.OPR_Adds import OPR_Adds
from server.models.OPR_Users import OPR_Users

from flask import request
from flask import render_template, url_for,flash, redirect
from server.models.form import OPR_Link

@app.route('/OPR/TQ/add/q')
def get_OPRurls():
  links = OPR_Adds.query.all()
  output = []
  
  for each in links:
    url_data = {'URL': each.url}
    output.append(url_data)
  
  return {"URLs: ": output}

@app.route('/OPR/TQ/add',methods=['GET','POST'])
def add_OPRurl():
  # new = OPR_Adds(url=request.json['url'])
  # db.session.add(new)
  # db.session.commit()
  # return {'ID': new.id}
  form = OPR_Link()
  if form.validate_on_submit():
    url = OPR_Adds(url=form.link.data)
    db.session.add(url)
    db.session.commit()
    flash("URL Added Successfully.")
    return redirect(url_for('index'))
  # url = FB_Adds(url=form.link.data)
  # db.session.add(url)
  # db.session.commit()
  return render_template('url_taker.html', form=form)

@app.route('/OPR/TQ/add',methods=['DELETE'])
def delete_OPRurl(link):
  all_links = OPR_Adds.query.all()
  for each in all_links:
    if (each.url == link):
      db.session.delete(each)
      db.session.commit()
      return {"Delete":"Successful"}