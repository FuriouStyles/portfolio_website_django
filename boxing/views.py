
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PredictBout
import pickle
from django.templatetags.static import static
from xgboost import XGBClassifier
import pandas as pd
import category_encoders as ce

# Create your views here.

model_filename = 'boxing/static/xgboost_boxing_model.sav'
loaded_model = pickle.load(open(model_filename, 'rb'))

def boxing(request):
    if request.method == 'GET':
        form = PredictBout(request.GET or None)
        if form.is_valid():
            date = form['date'].value()
            blue = form['blue_name'].value()
            red = form['red_name'].value()
            red_br_id = form['red_br_id'].value()
            blue_br_id = form['blue_br_id'].value()
            title_fight = form['title_fight'].value()
            gender = form['gender'].value()
            venue = form['venue'].value()
            red_born = form['red_born'].value()
            red_debut = form['red_debut'].value()
            red_division = form['red_division'].value()
            red_height = form['red_height'].value()
            red_nationality = form['red_nationality'].value()
            red_reach = form['red_reach'].value()
            red_stance = form['red_stance'].value()
            red_age = form['red_age'].value()
            red_age_at_fight_time = form['red_age_at_fight_time'].value()
            red_years_actice = form['red_years_actice'].value()
            blue_born = form['blue_born'].value()
            blue_debut = form['blue_debut'].value()
            blue_division = form['blue_division'].value()
            blue_height = form['blue_height'].value()
            blue_nationality = form['blue_nationality'].value()
            blue_reach = form['blue_reach'].value()
            blue_stance = form['blue_stance'].value()
            blue_age = form['blue_age'].value()
            blue_age_at_fight_time = form['blue_age_at_fight_time'].value()
            blue_years_actice = form['blue_years_actice'].value()

            df = pd.DataFrame({
            'date': date,
            'blue': blue,
            'red': red,
            'red_br_id': red_br_id,
            'blue_br_id': blue_br_id,
            'title_fight': title_fight,
            'venue': venue,
            'red_born': red_born,
            'red_debut': red_debut,
            'red_division': red_division,
            'red_height': red_height,
            'red_nationality': red_nationality,
            'red_reach': red_reach,
            'red_stance': red_stance,
            'blue_born': blue_born,
            'blue_debut': blue_debut,
            'blue_division': blue_division,
            'blue_height': blue_height,
            'blue_nationality': blue_nationality,
            'blue_reach': blue_reach,
            'sex': gender,
            'blue_stance': blue_stance,
            'blue_stance': blue_stance,
            'red_age': red_age,
            'blue_age': blue_age,
            'red_age_at_fight_time': red_age_at_fight_time,
            'red_years_active': red_years_actice,
            'blue_age_at_fight_time': blue_age_at_fight_time,
            'blue_years_active': blue_years_actice,
            },
            index=[0])

            encoder = ce.OrdinalEncoder()

            df_encoded = encoder.fit_transform(df)

            prediction = loaded_model.predict_proba(df_encoded)

            draw_proba = prediction[0][0]
            win_proba = prediction[0][1]
            loss_proba = prediction[0][2]

            context= {
            'draw_proba': draw_proba,
            'win_proba': win_proba,
            'loss_proba': loss_proba
            }

            return render(request, 'boxing/prediction_results.html', context)

    else:
        form = PredictBout()
    return render(request, 'boxing/boxing.html', {'form': form})
