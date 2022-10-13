from flask import Blueprint, render_template, request, flash, jsonify,Response
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import cv2
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

def gen():
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    while(cap.isOpened()):
        success, frame = cap.read()
        if success == True:
            img_BGR = frame
            frame = cv2.imencode('.jpg', img_BGR)[1].tobytes()
            result1=b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            yield(result1)
 
        else:
            break
        # print(result1)


@views.route('/video',methods=['GET', 'POST'])
@login_required

def video():
    
   
    return Response(gen(),
                            mimetype='multipart/x-mixed-replace; boundary=frame')
    #return "Lütfen Giriş Yapın"







@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
