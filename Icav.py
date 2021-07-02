#Importing libraries required
from flask import Flask
from flask_restful import Api,Resource
import csv

#creating a flask app object
app = Flask(__name__)

#creating an Api object
api=Api(app)

class Readbooks(Resource):
    def get(self,myrows):
        try:
            data_csv=[]
            #reading data from csv file 
            with open('books-2.csv','r') as f:
                #data = csv.reader(f)
                datalines=list(csv.reader(f))
                #creating a list of columns
                columns = [datalines[0][x] for x in range(0,10)]
                
                for row in range(1,myrows+1):
                    data_csv.append({columns[0]:datalines[row][0],
                    columns[1]:datalines[row][1],
                    columns[2]:datalines[row][2],
                    columns[3]:datalines[row][3],
                    columns[4]:datalines[row][4],
                    columns[5]:datalines[row][5],
                    columns[6]:datalines[row][6],
                    columns[7]:datalines[row][7],
                    columns[8]:datalines[row][8],
                    columns[9]:datalines[row][9]}
                    )

            return {"books":data_csv}
        
        except Exception as e:
            return {"Message":'Something went Wrong!'}

api.add_resource(Readbooks,"/<int:myrows>")

app.run(debug=True, host='0.0.0.0')
