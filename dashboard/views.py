from django.shortcuts import render
from typing import List
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Forecast_Master
from collections import defaultdict
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


import djongo
# import pandas as pd 
from collections import defaultdict
import json


def forecastDash(request):
    print("request.get",request.GET)
    if   request.GET.get('date') and  request.GET.get('state') and  request.GET.get('ftype'):
     print("inif")
     date= request.GET.get('date')
     state= request.GET.get('state')
     ftype=  request.GET.get('ftype')
    elif  request.GET.get('date') and  request.GET.get('state'):
        print("inelif1") 
        state= request.GET.get('state')
        date= request.GET.get('date')
    elif  request.GET.get('ftype') and  request.GET.get('state'):
        
        state= request.GET.get('ftype')
        date= request.GET.get('state')
    elif request.GET.get('date'):
        print("inelif2")
        
        date= request.GET.get('date') 
    elif  request.GET.get('ftype'):
        ftype=  request.GET.get('ftype')
    else:
        print("inelse")
        state = "INDUP000000" 
        date = "2021-12-21"
        ftype= "TLD_Forecast"
    tld_demands= Forecast_Master.objects.filter( forecast_type= ftype , ID= state, date= date )
    demands_second= list(Forecast_Master.objects.filter( forecast_type__iexact='pred_bagging' , ID= state, date= date )) 
    # all_demands = list(Forecast_Master.objects.values()) 
    # fcast_types= list(Forecast_Master.objects.values_list( 'forecast_type', flat= True ).distinct())
    common_demands = list(Forecast_Master.objects.filter(ID= state,date= date ))
    
    
    common_demands_ftypes = []
    for f in common_demands: 
        ftype= f.forecast_type
        common_demands_ftypes.append(ftype)
    

    print ("demands_second...",demands_second[0])
 
    print ("tld_demands",tld_demands)
   
    states = {'Uttar Pradesh' : 'INDUP000000', 'Madhya Pradesh':'INDMPMP0000', 'Madhya Pradesh East Zone':'INDMPEZ0000','Madhya Pradesh West Zone': 'INDMPWZ0000','Madhya Pradesh Central Zone':'INDMPCZ0000', 'Bihar': 'INDBH000000' }
    





    tld_values= []
    demands_sec=[] 
    blocks=list(range(1,97))
    print("tld_demands",tld_demands)  
    b="block"
    bNo= 1  
    while bNo <= 96 : 
        blockno=b + str(bNo)
        tldblockData=getattr(tld_demands[0], blockno)
        tld_values.append(tldblockData) 
        # print("blockno", blockno)
        scndblockData=getattr(demands_second[0],blockno) 
        demands_sec.append(scndblockData)
        bNo +=1  
    print("demands_second", demands_sec)
    # print("tld_values",tld_values)
    # print("all_demands ",all_demands)

 
 
    context={
        'tld_values': tld_values,
        'blocks': blocks,
        'states':states,
        'fcast_types': common_demands_ftypes,
       'demands_second':demands_second,
    }
    

    return render(request, 'dashboard/forecastDash.html', context)



class Forecast_view(BaseLineChartView, TemplateView):
    template_name='forecastDash.html'
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
   



