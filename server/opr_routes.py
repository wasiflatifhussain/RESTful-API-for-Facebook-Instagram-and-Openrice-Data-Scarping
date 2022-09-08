from flask import render_template
# importing all the models(this is after db so that db can be recognized by models!)
from server import app
from server import db

from server import logmaker

from server.models.OPR_Queue import OPR_Queue
from server.models.OPR_Adds import OPR_Adds
from server.models.OPR_Users import OPR_Users

@app.route('/')
def index():  # initation webpage
    print(app.config)
    return render_template('first.html')


## OPENRICE PATH AND FUNCTIONS ##

@app.route('/OPR')  # to get all users at once
def get_OPRusers():  # get openrice users data
    users = OPR_Users.query.all()

    output = []

    for user in users:
        user_data = {'userid': user.name, 'level': user.level,
                     'following': user.followings, 'followers': user.followers}
        output.append(user_data)

    # print(output)
    logmaker.logger.info(f"Printing all OPR users by GET request.")
    return render_template('getOPRpage.html', outputs=output)


@app.route('/OPR/<id>')
def get_OPRuser(id):  # to get a single user at once  /////modification: can change path to something simpler for easier get requests(use something else instead of <id>)
    output = []
    user = OPR_Users.query.get_or_404(id)
    user_data = {'userid': user.name, 'level': user.level,
                 'following': user.followings, 'followers': user.followers}
    output.append(user_data)
    # need to use jsonify is return is not dictionary
    # print(user)
    logmaker.logger.info(f"Printing OPR user with database id {id}.")
    # return {'User ID': user.name, 'User Level': user.level, 'User Following': user.followings, 'User Followers': user.followers}
    return render_template('getOPRuser.html', outputs=output)


@app.route('/OPR', methods=['POST'])
def add_OPRuser(user_name, user_level, user_followings, user_followers):  # for adding new posts
    users = OPR_Users.query.all()
    for each in users:
        if (user_name == each.name):
            print("User exists in the database.")
            return {}
    user = OPR_Users(name=user_name,
                     level=user_level, followings=user_followings, followers=user_followers)
    db.session.add(user)
    db.session.commit()
    print("Successfully Added.")
    logmaker.logger.info(f"Openrice User with User ID: {user_name} has been added to DB.")
    return {'id': user.id}


@app.route('/OPR', methods=['DELETE'])  # for deleting posts
def delete_OPRuser(username):
    users = OPR_Users.query.all()
    for each in users:
        if (each.name == username):
            db.session.delete(each)
            db.session.commit()
            # print("Successfully Deleted.")
            logmaker.info(f"User with username: {username} has been deleted successfully.")
            return {"Message": "Delete Success"}

    # print("User does not exist.")
    logmaker.logger.info(f"User with username: {username} does not exist.")
    return {"Message": "User does not exist"}


