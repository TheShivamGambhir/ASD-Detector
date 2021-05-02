import pickle
import pandas as pd
model = pickle.load(open('model.pkl', 'rb'))

def predict(testcase):
    ip_df = pd.DataFrame(data=testcase)
    ans = model.predict_proba(ip_df)
    print(ans)



testcase = {'A1_Score': [1],
          'A2_Score': [1],
          'A3_Score': [1],
          'A4_Score': [1],
          'A5_Score': [1],
          'A6_Score': [1],
          'A7_Score': [1],
          'A8_Score': [1],
          'A9_Score': [1],
          'A10_Score': [1],
          'age': [21.0],
          'gender': [0],
          'ethnicity': [3],
          'juandice': [0],
          'relative_autism': [0],
          'country_of_res': [41]}
predict(testcase)
