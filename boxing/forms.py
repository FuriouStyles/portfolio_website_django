from django import forms

class PredictBout(forms.Form):
    MINIMUM = 'minimum'
    LIGHT_FLYWEIGHT = 'light fly'
    FLYWEIGHT = 'fly'
    SUPER_FLYWEIGHT = 'super fly'
    BANTAMWEIGHT = 'bantam'
    SUPER_BANTAM = 'super bantam'
    FEATHERWEIGHT = 'feather'
    SUPER_FEATHERWEIGHT = 'super feather'
    LIGHTWEIGHT = 'light'
    SUPER_LIGHTWEIGHT = 'super light'
    WELTERWEIGHT = 'welter'
    SUPER_WELTERWEIGHT = 'super welter'
    MIDDLEWEIGHT = 'middle'
    SUPER_MIDDLEWEIGHT = 'super middle'
    LIGHT_HEAVYWEIGHT = 'light heavy'
    CRUISERWEIGHT = 'cruiser'
    HEAVYWEIGHT = 'heavy'
    DIVISIONS = [
        (MINIMUM, 'Minimum Weight'),
        (LIGHT_FLYWEIGHT, 'Light Flyweight'),
        (FLYWEIGHT, 'Flyweight'),
        (SUPER_FLYWEIGHT, 'Super Flyweight'),
        (BANTAMWEIGHT, 'Bantamweight'),
        (SUPER_BANTAM, 'Super Bantamweight'),
        (FEATHERWEIGHT, 'Featherweight'),
        (SUPER_FEATHERWEIGHT, 'Super Featherweight'),
        (LIGHTWEIGHT, 'Lightweight'),
        (SUPER_LIGHTWEIGHT, 'Super Light'),
        (WELTERWEIGHT, 'Welterweight'),
        (SUPER_WELTERWEIGHT, 'Super Welterweight'),
        (MIDDLEWEIGHT, 'Middleweight'),
        (SUPER_MIDDLEWEIGHT, 'Super Middleweight'),
        (LIGHT_HEAVYWEIGHT, 'Light Heavyweight'),
        (CRUISERWEIGHT, 'Cruiserweight'),
        (HEAVYWEIGHT, 'Heavyweight')
    ]

    MALE = 'male'
    FEMALE = 'female'
    SEX = [
        (MALE, 'male'),
        (FEMALE, 'female')
    ]

    red_url = forms.CharField(label="Red Corner BoxRec URL")
    blue_url = forms.CharField(label="Blue Corner URL")
    date = forms.CharField(label="Fight Date as (format: 2019-01-22)")
    venue = forms.CharField(label="Venue")
    title_fight = forms.BooleanField(label="Title Fight", required=False)
    division = forms.ChoiceField(label='Division', choices=DIVISIONS)
    gender = forms.ChoiceField(label='Gender', choices=SEX)


# class PredictBout(forms.Form):
#     MINIMUM = 'minimum'
#     LIGHT_FLYWEIGHT = 'light fly'
#     FLYWEIGHT = 'fly'
#     SUPER_FLYWEIGHT = 'super fly'
#     BANTAMWEIGHT = 'bantam'
#     SUPER_BANTAM = 'super bantam'
#     FEATHERWEIGHT = 'feather'
#     SUPER_FEATHERWEIGHT = 'super feather'
#     LIGHTWEIGHT = 'light'
#     SUPER_LIGHTWEIGHT = 'super light'
#     WELTERWEIGHT = 'welter'
#     SUPER_WELTERWEIGHT = 'super welter'
#     MIDDLEWEIGHT = 'middle'
#     SUPER_MIDDLEWEIGHT = 'super middle'
#     LIGHT_HEAVYWEIGHT = 'light heavy'
#     CRUISERWEIGHT = 'cruiser'
#     HEAVYWEIGHT = 'heavy'
#     DIVISIONS = [
#         (MINIMUM, 'Minimum Weight'),
#         (LIGHT_FLYWEIGHT, 'Light Flyweight'),
#         (FLYWEIGHT, 'Flyweight'),
#         (SUPER_FLYWEIGHT, 'Super Flyweight'),
#         (BANTAMWEIGHT, 'Bantamweight'),
#         (SUPER_BANTAM, 'Super Bantamweight'),
#         (FEATHERWEIGHT, 'Featherweight'),
#         (SUPER_FEATHERWEIGHT, 'Super Featherweight'),
#         (LIGHTWEIGHT, 'Lightweight'),
#         (SUPER_LIGHTWEIGHT, 'Super Light'),
#         (WELTERWEIGHT, 'Welterweight'),
#         (SUPER_WELTERWEIGHT, 'Super Welterweight'),
#         (MIDDLEWEIGHT, 'Middleweight'),
#         (SUPER_MIDDLEWEIGHT, 'Super Middleweight'),
#         (LIGHT_HEAVYWEIGHT, 'Light Heavyweight'),
#         (CRUISERWEIGHT, 'Cruiserweight'),
#         (HEAVYWEIGHT, 'Heavyweight')
#     ]
#     ORTHODOX = 'orthodox'
#     SOUTHPAW = 'southpaw'
#     STANCES = [
#         (ORTHODOX, 'orthodox'),
#         (SOUTHPAW, 'southpaw')
#     ]
#     MALE = 'male'
#     FEMALE = 'female'
#     SEX = [
#         (MALE, 'male'),
#         (FEMALE, 'female')
#     ]
#
#     date = forms.CharField(label='Fight Date')
#     venue = forms.CharField(label='Venue')
#     title_fight = forms.BooleanField(label='Title Fight', required=False)
#     gender = forms.BooleanField(label='Female', required=False)
#
#     red_name = forms.CharField(label='Red Corner Name')
#     red_br_id = forms.FloatField(label='Red BoxRec ID')
#     red_born = forms.CharField(label='Red Born (format: 2019-01-22)')
#     red_debut = forms.CharField(label='Red Debut (format: 2019-01-22)')
#     red_division = forms.ChoiceField(label='Red Corner Division', choices=DIVISIONS)
#     red_height = forms.CharField(label='Red Corner Height (format: 185cm)')
#     red_reach = forms.CharField(label='Red Corner Reach (format: 74cm)')
#     red_years_actice = forms.CharField(label='Red Corner Years Active at Fight Time')
#     red_age = forms.FloatField(label='Red Corner Age at Fight Time')
#     red_age_at_fight_time = forms.CharField(label='Red Age at Fight Time')
#     red_nationality = forms.CharField(label='Red Corner Nationality')
#     red_stance = forms.ChoiceField(label='Red Stance', choices=STANCES)
#
#     blue_name = forms.CharField(label="Blue Corner Name")
#     blue_br_id = forms.CharField(label="Blue BoxRec ID")
#     blue_born = forms.CharField(label='Blue Born as (format: 2019-01-22)')
#     blue_debut = forms.CharField(label='Blue Debut (format: 2019-01-22)')
#     blue_division = forms.ChoiceField(label='Division', choices=DIVISIONS)
#     blue_height = forms.CharField(label='Blue Corner Height (format: 185cm)')
#     blue_reach = forms.CharField(label='Blue Corner Reach (format: 74cm)')
#     blue_years_actice = forms.CharField(label='Blue Corner Years Active At Fight Time')
#     blue_age = forms.FloatField(label='Blue Corner Age at Fight Time')
#     blue_age_at_fight_time = forms.CharField(label='Blue Age at Fight Time')
#     blue_nationality = forms.CharField(label='Blue Corner Nationality')
#     blue_stance = forms.ChoiceField(label='Blue Stance', choices=STANCES)
