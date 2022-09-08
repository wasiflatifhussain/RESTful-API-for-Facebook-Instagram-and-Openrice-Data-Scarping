from server import app
from server import db
from flask import render_template
from server.models.FB_Users import FB_Users  # importing all the models(this is after db so that db can be recognized by models!)
from server.models.FB_Queue import FB_Queue
from server.models.FB_Adds import FB_Adds

from server import logmaker 

## FACEBOOK PATHS AND FUNCTIONS ##

@app.route('/FB')  # to get all drinks at once
def get_FBusers():
    users = FB_Users.query.all()

    output = []

    for user in users:
        user_data = {'userid': user.userid, 'name': user.name,
                     'friends': user.friends}
        output.append(user_data)

    # print(output)
    logmaker.logger.info(f"Printing all FB users by GET request.")
    return render_template('getFBpage.html', outputs=output)


@app.route('/FB/<id>')  # to get a single drink at once
def get_FBuser(id):  # each db entry is named as id=1, id=2 and so on
    output = []
    user = FB_Users.query.get_or_404(id)
    user_data = {'userid': user.userid,
                 'name': user.name, 'friends': user.friends}
    output.append(user_data)
    # need to use jsonify is return is not dictionary
    # print(user)
    logmaker.logger.info(f"Printing FB user with database id {id}.")
    # return {'User ID': user.name, 'User Level': user.level, 'User Following': user.followings, 'User Followers': user.followers}
    return render_template('getFBuser.html', outputs=output)


@app.route('/FB', methods=['POST'])  # to post a drink to db using postman
def add_FBuser(user_id, user_name, user_friends):
    users = FB_Users.query.all()
    for each in users:
        if (user_name == each.name):
            print("User exists in database.")
            return {}
    user = FB_Users(userid=user_id, name=user_name,
                    friends=user_friends)
    db.session.add(user)
    db.session.commit()
    # print("Successfully Added.")
    logmaker.logger.info(f"Faceook User with User ID: {user_id} has been added to DB.")
    return {'id': user.id}


@app.route('/FB', methods=['DELETE'])
def delete_FBuser(username):
    users = FB_Users.query.all()
    for each in users:
        if (each.userid == username):
            db.session.delete(each)
            db.session.commit()
            # print("Successfully Deleted.")
            logmaker.info(f"User with username: {username} has been deleted successfully.")
            return {"Message": "Delete Success"}
    # print("User does not exist.")
    logmaker.logger.info(f"User with username: {username} does not exist.")
    return {"Message": "User does not exist"}


