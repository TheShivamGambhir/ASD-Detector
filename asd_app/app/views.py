from django.shortcuts import render
import keras
from keras.preprocessing import image
import pickle
import pandas as pd
model = pickle.load(open('./ml/model.pkl', 'rb'))
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
from tensorflow.keras.models import load_model

cvmodel = load_model('./ml/ann.h5')

from django.http import HttpResponse
# Create your views here.
from .forms import CHOICES
def getvalue(request):
    form = CHOICES(request.POST)
    selected = form.cleaned_data.get("NUMS")
    return selected
name = "John Doe !"
def home(request):
    return render(request, 'basic_info.html', {'name': name})
def questionnaire(request):
    na = request.POST["username"]
    return render(request, 'questionnaire.html', {'name': na})

list = []
reverse_map = {}
for i in range(1, 11):
    reverse_map[i] = 'A' + str(i) + '_Score'
    for j in range(1, 4):
        list.append("q" + str(i) + str(j))
def result(request):
    print(request.POST)
    for q in list:
        if q in request.POST:
            # print(q + " is present")
            val = request.POST[q]
            ans_number = int(q[1])
            question_number = reverse_map[ans_number]
            # print('--------------------------')
            # print(question_number)
            testcase[question_number][0] = float(val)
    # print(testcase)
    ip_df = pd.DataFrame(data=testcase)
    ans = model.predict_proba(ip_df)
    ans = ans[0][1]*100
    path = request.POST['image']
    path = './ml/' + path
    import numpy as np
    img_data = []
    myimg = image.load_img(path, target_size=(224, 224))
    img_array = image.img_to_array(myimg)
    img_data.append(img_array)
    X = np.array(img_data)
    print(X.shape)
    X /= 255.0
    # plt.imshow(X[0])
    # img.shape
    ans2 = 1
    ans2 = cvmodel.predict(X)
    ans2 = ans2[0][1]*100
    return render(request, 'result.html', {'name': name, 'ans': ans, 'ans2': ans2})
