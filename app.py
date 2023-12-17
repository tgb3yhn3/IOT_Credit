from flask import Flask, request, jsonify,redirect
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from Credit import Credit
import os
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///credit_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 定義數據模型
class CreditData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String, nullable=False)  # 存儲 JSON 字符串

    def __repr__(self):
        return f'<CreditData {self.id}>'
    def to_dict(self):
        # 將 CreditData 物件轉換為字典
        return {
            'id': self.id,
            'data': self.data
        }
def create_database(app):
    with app.app_context():
        db.create_all()

# 在應用程式啟動時調用這個函數
create_database(app)
@app.route("/credit", methods=['POST'])
def index_get():
    data = request.get_json()
    credit = Credit(list(data.values()))
    response = credit.customer_rank_percentage()

    # 保存數據到數據庫
    new_credit_data = CreditData(data=str(json.dumps(data)))
    db.session.add(new_credit_data)
    db.session.commit()

    return jsonify(response)
@app.route("/history", methods=['GET'])
def get_history():
    last_record = CreditData.query.order_by(CreditData.id.desc()).all()
    data=[]
    for i in last_record:
        data.append(i.to_dict())
    if last_record:
        return jsonify( data)
    else:
        return jsonify({"message": "No records found"})
@app.route("/history/<id>", methods=['GET'])
def get_history_1(id):
    if(id=='last'):
        last_record = CreditData.query.order_by(CreditData.id.desc()).first()
    else:
        last_record = CreditData.query.filter_by(id=id)[0]
    print(last_record.data)
    data=Credit(list(json.loads(last_record.data).values()))
    response = data.customer_rank_percentage()
    return jsonify(response)
@app.route("/history/<id>", methods=['DELETE'])
def delete_history(id):
    
      
    last_record = db.session.query(CreditData).filter_by(id=id).delete()
    db.session.commit()
    return jsonify("success")
@app.route("/", methods=['GET'])
def index():
    return redirect('http://127.0.0.1:3000/')
if __name__=="__main__":
    app.run(port=5001,debug=True)
