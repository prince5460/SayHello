'''
Created by ZhouSp 18-10-29.
'''
from flask import flash, redirect, url_for, render_template, jsonify, request

from sayhello import app, db
from sayhello.models import Message
from sayhello.forms import HeloForm

__author__ = 'zhou'


@app.route('/', methods=['GET', 'POST'])
def index():
    # 加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HeloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)  # 实例化模型类，创建记录
        db.session.add(message)  # 添加记录到数据库会话
        db.session.commit()  # 提交会话
        flash('消息发布成功！')
        return redirect(url_for('index'))  # 重定向到index视图

    return render_template('index.html', form=form, messages=messages)


@app.route('/api')
def api():
    count = Message.query.count()
    page_size = 5  # 每页显示的数量
    page = int(request.args.get('page', 0))
    if page:
        page_start = (page - 1) * page_size
        page_end = page * page_size
    else:
        page_start = 0
        page_end = count

    id = request.args.get('id', None)
    if id:
        messages = Message.query.filter_by(id=id)
    else:
        messages = Message.query.order_by(Message.timestamp.desc()).all()

    messages_list = []
    for message in messages[page_start: page_end]:
        data = {}
        data['name'] = message.name
        data['body'] = message.body
        data['time'] = message.timestamp
        data['id'] = message.id

        messages_list.append(data)

    return jsonify({"count": count, "messages": messages_list})
