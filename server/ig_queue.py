from server import app
from server import db
from flask import render_template  # importing all the models(this is after db so that db can be recognized by models!)
from server.models.IG_Queue import IG_Queue
from server.models.IG_Adds import IG_Adds
from server import logmaker
# import logging

from server import logmaker

@app.route('/IG/TQ', methods=['POST'])  # for adding new task queues
def add_IGqueue(task):
    queues = IG_Queue.query.all()
    for each in queues:
        if (each.url == task):
            print("URL already in queue. Please wait.")
            return {}
    new = IG_Queue(url=task,status="Pending")
    db.session.add(new)
    db.session.commit()
    logmaker.logger.info(f"Instagram URL {task} has been added to queue.")
    # print("Added to queue.")
    return {'URL: ', new.url}


@app.route('/IG/TQ', methods=['DELETE'])  # for deleting completed tasks
def delete_IGqueue(task):
    queues = IG_Queue.query.all()
    for each in queues:
        if (each.url == task):
            db.session.delete(each)
            db.session.commit()
            new = IG_Queue(url=task,status="Complete")
            db.session.add(new)
            db.session.commit()
            logmaker.logger.info(f"Instagram URL {task} has been deleted from queue.")
            return {"Message": "Delete Successful"}


@app.route('/IG/TQ')  # for geting task queues
def get_IGqueues():
    queues = IG_Queue.query.all()
    all_queues = []

    for each in queues:
        queue_data = {'URL': each.url, 'status': each.status}
        all_queues.append(queue_data)
    logmaker.logger.info(f"Printing all IG queues by GET request.")
    return render_template('getIGqueues.html', outputs=all_queues)