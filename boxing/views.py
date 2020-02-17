
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PredictBout
import pickle
from django.templatetags.static import static
from xgboost import XGBClassifier
import pandas as pd
import category_encoders as ce
import boxing.django_boxrec as dbr

# Create your views here.

model_filename = 'boxing/static/xgboost_boxing_model_2.sav'
encoder_filename = 'boxing/static/encoder_pipeline (1).sav'
loaded_model = pickle.load(open(model_filename, 'rb'))
loaded_encoder = pickle.load(open(encoder_filename, 'rb'))

def boxing(request):
    if request.method == 'GET':
        form = PredictBoutURL(request.GET or None)
        if form.is_valid():
            date = form['date'].value()
            # blue = form['blue_name'].value()
            # red = form['red_name'].value()
            # red_br_id = form['red_br_id'].value()
            # blue_br_id = form['blue_br_id'].value()
            title_fight = form['title_fight'].value()
            # gender = form['gender'].value()
            venue = form['venue'].value()
            # red_born = form['red_born'].value()
            # red_debut = form['red_debut'].value()
            # red_division = form['red_division'].value()
            # red_height = form['red_height'].value()
            # red_nationality = form['red_nationality'].value()
            # red_reach = form['red_reach'].value()
            # red_stance = form['red_stance'].value()
            # red_age = form['red_age'].value()
            # red_age_at_fight_time = form['red_age_at_fight_time'].value()
            # red_years_actice = form['red_years_actice'].value()
            # blue_born = form['blue_born'].value()
            # blue_debut = form['blue_debut'].value()
            # blue_division = form['blue_division'].value()
            # blue_height = form['blue_height'].value()
            # blue_nationality = form['blue_nationality'].value()
            # blue_reach = form['blue_reach'].value()
            # blue_stance = form['blue_stance'].value()
            # blue_age = form['blue_age'].value()
            # blue_age_at_fight_time = form['blue_age_at_fight_time'].value()
            # blue_years_actice = form['blue_years_actice'].value()
            division = form['division'].value()
            red_url = form['red_url'].value()
            blue_url = form['blue_url'].value()
            gender = form['gender'].value()

            red = dbr.get_boxer_profile(red_url)
            blue = dbr.get_boxer_profile(blue_url)
            print(red.T)
            print(blue.T)
            red = dbr.clean(red, date)
            blue = dbr.clean(blue, date)

            df = pd.DataFrame({
                'date': date,
                'blue': blue['name'].iloc[0],
                'red': red['name'].iloc[0],
                'red_br_id': int(red['br_id'].iloc[0]),
                'blue_br_id': blue['br_id'].iloc[0],
                'title_fight': title_fight,
                'venue': venue,
                'red_born': red['born'].dt.strftime(date_format='%Y-%m-%d'),
                'red_debut': red['debut'].dt.strftime(date_format='%Y-%m-%d'),
                'red_division': division,
                'red_height': red['height'].iloc[0],
                'red_nationality': red['nationality'].iloc[0],
                'red_reach': red['reach'].iloc[0],
                'red_stance': red['stance'].iloc[0],
                'blue_born': blue['born'].dt.strftime(date_format='%Y-%m-%d'),
                'blue_debut': blue['debut'].dt.strftime(date_format='%Y-%m-%d'),
                'blue_division': division,
                'blue_height': blue['height'].iloc[0],
                'blue_nationality': blue['nationality'].iloc[0],
                'blue_reach': blue['reach'].iloc[0],
                'sex': gender,
                'blue_stance': blue['stance'].iloc[0],
                'red_age': red['age'].iloc[0],
                'blue_age': blue['age'].iloc[0],
                'red_age_at_fight_time': red['age_at_fight_time'].iloc[0],
                'red_years_active': red['years_active'].iloc[0],
                'blue_age_at_fight_time': blue['age_at_fight_time'].iloc[0],
                'blue_years_active': blue['years_active'].iloc[0]
                },
                index=[0])

            df_encoded = loaded_encoder.transform(df)

            print(df.T)
            print(df_encoded.T)

            prediction = loaded_model.predict_proba(df_encoded)

            draw_proba = prediction[0][0]
            loss_proba = prediction[0][1]
            win_proba = prediction[0][2]

            context= {
            'draw_proba': draw_proba,
            'win_proba': win_proba,
            'loss_proba': loss_proba,
            'dataframe': df.values.tolist(),
            'encoded_df': df_encoded.values.tolist(),
            'blue': blue
            }

            return render(request, 'boxing/prediction_results.html', context)

    else:
        form = PredictBout()
    return render(request, 'boxing/boxing.html', {'form': form})
