from flask import request
from flask import render_template, url_for,flash, redirect

# importing all the models(this is after db so that db can be recognized by models!)
from server import app
from server import db
from server.models.form import FB_Link, IG_Link, OPR_Link
from server.models.FB_Adds import FB_Adds
from server import logmaker

from server.models.OPR_Queue import OPR_Queue
from server.models.OPR_Adds import OPR_Adds
from server.models.OPR_Users import OPR_Users
from server.models.FB_Queue import FB_Queue
from server.models.FB_Adds import FB_Adds
from server.models.FB_Users import FB_Users
from server.models.IG_Queue import IG_Queue
from server.models.IG_Adds import IG_Adds
from server.models.IG_Users import IG_Users


# @app.route('/FB/TQ/add', methods=['GET','POST'])
# def register():
#   form = FB_Link()
#   # url = FB_Adds(url=form.link.data)
#   # db.session.add(url)
#   # db.session.commit()
#   return render_template('url_taker.html', form=form)

# @app.route('/FB/TQ/add', methods=['GET','POST'])
# def register():
#   form = FB_Link()
#   if request.method == "POST":
#     user = request.form['link']
#     url = FB_Adds(url=user)
#     db.session.add(url)
#     db.session.commit()
#     flash("URL Added Successfully.")
#   # url = FB_Adds(url=form.link.data)
#   # db.session.add(url)
#   # db.session.commit()
#   return render_template('tryFB.html',form=form)

@app.route('/FB/TQ/add', methods=['GET','POST'])
def register():
  form = FB_Link()
  if form.validate_on_submit():
    flash("URL Added Successfully.")
    return redirect(url_for('index'))
  # url = FB_Adds(url=form.link.data)
  # db.session.add(url)
  # db.session.commit()
  return render_template('url_taker.html', form=form)