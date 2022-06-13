import json
import random
from operator import attrgetter

from chartjs.views.lines import BaseLineChartView
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Forecast_Master

# import pandas as pd
BLOCK_CONSTANTS = [
    'block1', 'block2', 'block3', 'block4', 'block5', 'block6', 'block7', 'block8', 'block9', 'block10', 'block11',
    'block12', 'block13', 'block14', 'block15', 'block16', 'block17', 'block18', 'block19', 'block20', 'block21',
    'block22', 'block23', 'block24', 'block25', 'block26', 'block27', 'block28', 'block29', 'block30', 'block31',
    'block32', 'block33', 'block34', 'block35', 'block36', 'block37', 'block38', 'block39', 'block40', 'block41',
    'block42', 'block43', 'block44', 'block45', 'block46', 'block47', 'block48', 'block49', 'block50', 'block51',
    'block52', 'block53', 'block54', 'block55', 'block56', 'block57', 'block58', 'block59', 'block60', 'block61',
    'block62', 'block63', 'block64', 'block65', 'block66', 'block67', 'block68', 'block69', 'block70', 'block71',
    'block72', 'block73', 'block74', 'block75', 'block76', 'block77', 'block78', 'block79', 'block80', 'block81',
    'block82', 'block83', 'block84', 'block85', 'block86', 'block87', 'block88', 'block89', 'block90', 'block91',
    'block92', 'block93', 'block94', 'block95', 'block96'
]


class ForecastDashboardView(TemplateView):
    # template_name = 'dashboard/forecastDash.html'
    template_name = 'index.html'
    model = Forecast_Master

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = self.request.GET.get('date', None)
        state = self.request.GET.get('state', None)
        forecast_types = self.request.GET.getlist('ftype')

        print("forecast_type===>", forecast_types)

        state_choices = [
            'INDBH000000', 'INDMPCZ0000', 'INDMPEZ0000', 'INDMPMP0000', 'INDMPWZ0000', 'INDUP000000'
        ]
        forecast_type_choices = [
            'ITD', 'MCorrD', 'MCorrD_F', 'MCorrD_F_cz', 'MCorrD_F_ez', 'MCorrD_F_state', 'MCorrD_F_wz', 'MCorrD_cz',
            'MCorrD_ez', 'MCorrD_state', 'MCorrD_wz', 'Manual', 'TLB_Forecast', 'TLB_Forecast_CZ', 'TLB_Forecast_EZ',
            'TLB_Forecast_State', 'TLB_Forecast_WZ', 'TLB_Historical', 'TLB_Historical_CZ', 'TLB_Historical_EZ',
            'TLB_Historical_State', 'TLB_Historical_WZ', 'TLB_Nearby', 'TLB_Nearby_CZ', 'TLB_Nearby_EZ',
            'TLB_Nearby_State', 'TLB_Nearby_WZ', 'TLD_Forecast', 'TLD_Forecast_CZ', 'TLD_Forecast_EZ',
            'TLD_Forecast_State', 'TLD_Forecast_WZ', 'TLD_Historical', 'TLD_Historical_CZ', 'TLD_Historical_EZ',
            'TLD_Historical_State', 'TLD_Historical_WZ', 'TLD_Nearby', 'TLD_Nearby_CZ', 'TLD_Nearby_EZ',
            'TLD_Nearby_State', 'TLD_Nearby_WZ', 'pred_adaBoost', 'pred_adaBoost_cz', 'pred_adaBoost_ez',
            'pred_adaBoost_state', 'pred_adaBoost_wz', 'pred_bagging', 'pred_bagging_cz', 'pred_bagging_ez',
            'pred_bagging_state', 'pred_bagging_wz', 'pred_gradientBoosting', 'pred_gradientBoosting_cz',
            'pred_gradientBoosting_ez', 'pred_gradientBoosting_state', 'pred_gradientBoosting_wz', 'pred_lasso',
            'pred_lasso_cz', 'pred_lasso_ez', 'pred_lasso_state', 'pred_lasso_wz', 'pred_rf', 'pred_ridge',
            'pred_ridge_cz', 'pred_ridge_ez', 'pred_ridge_state', 'pred_ridge_wz', 'temp_diff_state', 'temp_diff_wz',
            'weather_forecast', 'weather_tempF_forecast', 'weather_temp_forecast'
        ]
        date_choices = Forecast_Master.objects.all().exclude(
            date__isnull=True
        ).values_list('date', flat=True).order_by('-date').distinct()
        datasets = []
        border_colors = [
            'indianred', 'salmon', 'darksalmon', 'crimson', 'red', 'darkred', 'pink', 'hotpink', 'deeppink',
            'palevioletred', 'coral', 'tomato', 'orangered', 'darkorange', 'orange', 'gold', 'palegoldenrod',
            'darkkhaki', 'thistle', 'plum', 'violet', 'orchid', 'fuchsia', 'magenta', 'rebeccapurple', 'blueviolet',
            'darkviolet', 'darkorchid', 'darkmagenta', 'purple', 'indigo', 'slateblue', 'darkslateblue', 'greenyellow',
            'lawngreen', 'limegreen', 'springgreen', 'seagreen', 'forestgreen', 'green', 'darkgreen', 'yellowgreen',
            'olivedrab', 'darkolivegreen', 'darkseagreen', 'darkcyan', 'teal', 'cyan', 'aquamarine', 'turquoise',
            'darkturquoise', 'cadetblue', 'steelblue', 'powderblue', 'skyblue', 'deepskyblue', 'dodgerblue',
            'cornflowerblue', 'royalblue', 'blue', 'darkblue', 'navy', 'midnightblue', 'burlywood', 'tan', 'rosybrown',
            'sandybrown', 'goldenrod', 'darkgoldenrod', 'peru', 'chocolate', 'saddlebrown', 'sienna', 'brown', 'maroon',
            'aliceblue', 'darkgray', 'darkslategray', 'black'
        ]
        for forecast in forecast_types:
            fc = self.model.objects.filter(
                forecast_type__iexact=forecast, date=date
            ).first()

            print("FC OBJECT===>", fc)
            block_values = attrgetter(*BLOCK_CONSTANTS)(fc)
            color = random.choice(border_colors)
            datasets.append({
                'label': fc.forecast_type,
                'backgroundColor': color,
                'borderColor': color,
                'borderWidth': 2,
                'data': block_values
            })

        context['datasets'] = json.dumps(datasets)
        context['labels'] = json.dumps([i for i in range(1, 97)])
        context['fcast_types'] = forecast_type_choices
        context['date_choices'] = date_choices

        context['f_type_selected'] = forecast_types

        return context


def forecastDash(request):
    print("request.get", request.GET)
    if request.GET.get('date') and request.GET.get('state') and request.GET.get('ftype'):
        print("inif")
        date = request.GET.get('date')
        state = request.GET.get('state')
        ftype = request.GET.get('ftype')
    elif request.GET.get('date') and request.GET.get('state'):
        print("inelif1")
        state = request.GET.get('state')
        date = request.GET.get('date')
    elif request.GET.get('ftype') and request.GET.get('state'):

        state = request.GET.get('ftype')
        date = request.GET.get('state')
    elif request.GET.get('date'):
        print("inelif2")

        date = request.GET.get('date')
    elif request.GET.get('ftype'):
        ftype = request.GET.get('ftype')
    else:
        print("inelse")
        state = "INDUP000000"
        date = "2021-12-21"
        ftype = "TLD_Forecast"
    tld_demands = Forecast_Master.objects.filter(forecast_type=ftype, ID=state, date=date)
    demands_second = list(Forecast_Master.objects.filter(forecast_type__iexact='pred_bagging', ID=state, date=date))
    # all_demands = list(Forecast_Master.objects.values()) 
    # fcast_types= list(Forecast_Master.objects.values_list( 'forecast_type', flat= True ).distinct())
    common_demands = list(Forecast_Master.objects.filter(ID=state, date=date))

    common_demands_ftypes = []
    for f in common_demands:
        ftype = f.forecast_type
        common_demands_ftypes.append(ftype)

    print("demands_second...", demands_second[0])

    print("tld_demands", tld_demands)

    states = {'Uttar Pradesh': 'INDUP000000', 'Madhya Pradesh': 'INDMPMP0000',
              'Madhya Pradesh East Zone': 'INDMPEZ0000', 'Madhya Pradesh West Zone': 'INDMPWZ0000',
              'Madhya Pradesh Central Zone': 'INDMPCZ0000', 'Bihar': 'INDBH000000'}

    tld_values = []
    demands_sec = []
    blocks = list(range(1, 97))
    print("tld_demands", tld_demands)
    b = "block"
    bNo = 1
    while bNo <= 96:
        blockno = b + str(bNo)
        tldblockData = getattr(tld_demands[0], blockno)
        tld_values.append(tldblockData)
        # print("blockno", blockno)
        scndblockData = getattr(demands_second[0], blockno)
        demands_sec.append(scndblockData)
        bNo += 1
    print("demands_second", demands_sec)
    # print("tld_values",tld_values)
    # print("all_demands ",all_demands)

    context = {
        'tld_values': tld_values,
        'blocks': blocks,
        'states': states,
        'fcast_types': common_demands_ftypes,
        'demands_second': demands_second,
    }

    return render(request, 'dashboard/forecastDash.html', context)


class ForecastView(BaseLineChartView, TemplateView):
    template_name = 'forecastDash.html'

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='forecastDash.html')
