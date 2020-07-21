# New Flask to feed an endpoint
from flask import Flask,request 
from flask import jsonify
import pandas as pd
app = Flask("publishing_reccomender")
@app.route('/getweird')
def getweirdarticles():
    original_df=pd.read_pickle("./original_df.pkl") # Download pickle file that has the data frame with the score that shows the "worseness"
    date=request.args.get('Date') # Retrieve date to query the recent posts. 
    n=int(request.args.get('n')) # Number of posts to show. This should be passed as an argument. 
    # Combine both the published and updated dates to get a union of dataframes. 
    filtered_df=pd.concat([original_df[original_df["published_at"]==date], original_df[original_df["updated_at"]==date]],ignore_index=True)
    lis=list(filtered_df.sort_values(by=['score'])['headline'])[0:n] #Sort from least to highest of the similarity score. 
    return jsonify(lis) # Return the json version with the headline of the posts. 

if __name__ == '__main__':
    app.run(debug=True,port=5001,host='0.0.0.0')
