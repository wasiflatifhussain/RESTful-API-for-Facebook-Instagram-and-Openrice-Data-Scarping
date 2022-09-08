from flask import render_template
# importing all the models(this is after db so that db can be recognized by models!)
from server import app
from server import db
from server import logmaker

from server.models.OPR_Queue import OPR_Queue
from server.models.OPR_Adds import OPR_Adds
from server.models.OPR_Users import OPR_Users

@app.route('/OPR/TQ', methods=['POST'])  # for adding new task queues
def add_OPRqueue(task):
    queues = OPR_Queue.query.all()
    for each in queues:
        if (each.url == task):
            print("URL already in queue. Please wait.")
            return {}
    new = OPR_Queue(url=task, status="Pending")
    db.session.add(new)
    db.session.commit()
    # print("Added to queue.")
    logmaker.logger.info(f"Openrice URL {task} has been added to queue.")
    return {'URL: ', new.url}


@app.route('/OPR/TQ', methods=['DELETE'])  # for deleting completed tasks
def delete_OPRqueue(task):
    queues = OPR_Queue.query.all()
    for each in queues:
        if (each.url == task):
            db.session.delete(each)
            db.session.commit()
            new = OPR_Queue(url=task,status="Complete")
            db.session.add(new)
            db.session.commit()
            logmaker.logger.info(f"Openrice URL {task} has been deleted from queue.")
            return {"Message": "Delete Successful"}


@app.route('/OPR/TQ')  # for geting task queues
def get_OPRqueues():
    queues = OPR_Queue.query.all()
    all_queues = []

    for each in queues:
        queue_data = {'URL': each.url,'status': each.status}
        all_queues.append(queue_data)
    # print(all_queues)
    logmaker.logger.info(f"Printing all OPR queues by GET request.")
    return render_template('getOPRqueues.html', outputs=all_queues)