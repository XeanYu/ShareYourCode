from . import main
from flask import render_template,request,redirect,url_for,jsonify
from models import Share
from random import randint
from exts import db

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/<string:url>/')
def share_code(url):
    find = Share.query.filter_by(code_id=url).first()
    if not find:
        code = False
        title = False
        return render_template('read.html',code=code,title=title)
    code = find.code
    title = find.title
    find.req_num = find.req_num + 1
    req_num = find.req_num
    return render_template('read.html',code=code,title=title,req_num=req_num)

@main.route('/submit_code/',methods=['POST'])
def submit_code():
    if request.method == 'POST':
        title = request.form.get('title')
        code = request.form.get('code')
        code_id = randint(100000,99999999)
        find = Share.query.filter_by(code_id=str(code_id)).first()

        while find:
            code_id = randint(100000, 999999)
            find = Share.query.filter_by(code_id=str(code_id)).first()

        new_code = Share(title=title,code=code,code_id=code_id)
        db.session.add(new_code)
        db.session.commit()
        return jsonify(msg=True,code_id=code_id)
    else:
        return redirect(url_for('index'))