from exts import db

class Share(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True) # 主键
    code_id = db.Column(db.String(64),index=True,unique=True,nullable=False) # 短URL
    title = db.Column(db.String(1024)) # 代码标题
    code = db.Column(db.Text) # 代码
    req_num = db.Column(db.Integer,default=0)

