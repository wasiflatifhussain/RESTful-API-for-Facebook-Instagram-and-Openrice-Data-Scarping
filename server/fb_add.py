from flask import request,render_template
from server.models.FB_Adds import FB_Adds # importing all the models(this is after db so that db can be recognized by models!)
from server import app
from server import db

from flask import request
from flask import render_template, url_for,flash, redirect

# importing all the models(this is after db so that db can be recognized by models!)
from server import app
from server import db
from server import logmaker
from server.models.form import FB_Link


# import logging
# import datetime

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# #to be used for naming the files for each day basis
# x = datetime.datetime.now()
# y1 = x.strftime("%d") 
# y2 = x.strftime("%b")
# y3 = x.strftime("%Y")
# # x.strftime("%x")


# file_handler = logging.FileHandler(f"logs/employees-{y1}-{y2}-{y3}.log")
# file_handler.setFormatter(formatter)

# logger.addHandler(file_handler)

@app.route('/FB/TQ/add/q')
def get_FBurls():
  links = FB_Adds.query.all()
  output = []
  
  for each in links:
    url_data = {'URL': each.url}
    output.append(url_data)
  
  return {"URLs: ": output}

@app.route('/FB/TQ/add',methods=['GET','POST'])
def add_FBurl():
  # #new = FB_Adds(url=link)
  # new = FB_Adds(url=request.json['url'])
  # db.session.add(new)
  # db.session.commit()
  # return {'id': new.id}
  form = FB_Link()
  if form.validate_on_submit():
    url = FB_Adds(url=form.link.data)
    db.session.add(url)
    db.session.commit()
    flash("URL Added Successfully.")
    return redirect(url_for('index'))
  # url = FB_Adds(url=form.link.data)
  # db.session.add(url)
  # db.session.commit()
  return render_template('url_taker.html', form=form)

@app.route('/FB/TQ/add',methods=['DELETE'])
def delete_FBurl(link):
  all_links = FB_Adds.query.all()
  for each in all_links:
    if (each.url == link):
      db.session.delete(each)
      db.session.commit()