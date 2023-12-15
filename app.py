from  flask   import Flask,render_template,request
from flask_cors import CORS
app=Flask(__name__)
CORS(app,supports_credentials=True)
# from Credit import get_advise
@app.route("/credit",methods=['POST'])
def index_get():
    data=request.get_json()
    print(request)

    return_data={credit_ratio: res.data.credit_ratio,
              income_ratio: res.data.income_ratio,
              income: res.data.income,
              same_age_credit_ratio: res.data.same_age_credit_ratio,
              same_age_income_ratio: res.data.same_age_income_ratio,
              same_age_income: res.data.same_age_income,}
    return "Hello World"

if __name__=='__main__':
    app.run(port="5001",debug=True)