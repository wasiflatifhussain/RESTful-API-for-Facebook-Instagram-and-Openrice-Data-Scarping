from server import app
from server import db
from flask import render_template
from server.models.IG_Users import IG_Users  # importing all the models(this is after db so that db can be recognized by models!)
from server.models.IG_Queue import IG_Queue
from server.models.IG_Adds import IG_Adds

from server import logmaker 

## FACEBOOK PATHS AND FUNCTIONS ##

@app.route('/IG')  # to get all drinks at once
def get_IGusers():
    users = IG_Users.query.all()

    output = []

    for user in users:
        user_data = {'username': user.username, 'followers': user.followers,
                     'followings': user.followings}
        output.append(user_data)

    # print(output)
    logmaker.logger.info(f"Printing all IG users by GET request.")
    return render_template('getIGpage.html', outputs=output)


@app.route('/IG/<id>')  # to get a single drink at once
def get_IGuser(id):  # each db entry is named as id=1, id=2 and so on
    output = []
    user = IG_Users.query.get_or_404(id)
    user_data = {'username': user.username, 'followers': user.followers,
                  'followings': user.followings}
    output.append(user_data)
    # need to use jsonify is return is not dictionary
    # print(user)
    logmaker.logger.info(f"Printing IG user with database id {id}.")
    # return {'User ID': user.name, 'User Level': user.level, 'User Following': user.followings, 'User Followers': user.followers}
    return render_template('getIGuser.html', outputs=output)


@app.route('/IG', methods=['POST'])  # to post a drink to db using postman
def add_IGuser(user_name, user_followers, user_followings):
    users = IG_Users.query.all()
    for each in users:
        if (user_name == each.username):
            print("User exists in database.")
            return {}
    user = IG_Users(username=user_name, followers=user_followers,
                    followings=user_followings)
    db.session.add(user)
    db.session.commit()
    # print("Successfully Added.")
    logmaker.logger.info(f"Instagram User with username: {user_name} has been added to DB.")
    return {'id': user.id}


@app.route('/IG', methods=['DELETE'])
def delete_IGuser(user_name):
    users = IG_Users.query.all()
    for each in users:
        if (each.username == user_name):
            db.session.delete(each)
            db.session.commit()
            # print("Successfully Deleted.")
            logmaker.info(f"User with username: {user_name} has been deleted successfully.")
            return {"Message": "Delete Success"}
    # print("User does not exist.")
    logmaker.logger.info(f"User with username: {user_name} does not exist.")
    return {"Message": "User does not exist"}


