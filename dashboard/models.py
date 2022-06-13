from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import FloatField
from djongo import models


class Forecast_Master(models.Model):
    date_int = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    forecast_type = models.CharField(max_length=50, null=True)
    forecast_term = models.CharField(max_length=50, null=True)
    ID = models.CharField(max_length=50, null=True)
    block1 = models.FloatField(db_column='1', null=True)
    block2 = models.FloatField(db_column='2', null=True)
    block3 = models.FloatField(db_column='3', null=True)
    block4 = models.FloatField(db_column='4', null=True)
    block5 = models.FloatField(db_column='5', null=True)
    block6 = models.FloatField(db_column='6', null=True)
    block7 = models.FloatField(db_column='7', null=True)
    block8 = models.FloatField(db_column='8', null=True)
    block9 = models.FloatField(db_column='9', null=True)
    block10 = models.FloatField(db_column='10', null=True)
    block11 = models.FloatField(db_column='11', null=True)
    block12 = models.FloatField(db_column='12', null=True)
    block13 = models.FloatField(db_column='13', null=True)
    block14 = models.FloatField(db_column='14', null=True)
    block15 = models.FloatField(db_column='15', null=True)
    block16 = models.FloatField(db_column='16', null=True)
    block17 = models.FloatField(db_column='17', null=True)
    block18 = models.FloatField(db_column='18', null=True)
    block19 = models.FloatField(db_column='19', null=True)
    block20 = models.FloatField(db_column='20', null=True)
    block21 = models.FloatField(db_column='21', null=True)
    block22 = models.FloatField(db_column='22', null=True)
    block23 = models.FloatField(db_column='23', null=True)
    block24 = models.FloatField(db_column='24', null=True)
    block25 = models.FloatField(db_column='25', null=True)
    block26 = models.FloatField(db_column='26', null=True)
    block27 = models.FloatField(db_column='27', null=True)
    block28 = models.FloatField(db_column='28', null=True)
    block29 = models.FloatField(db_column='29', null=True)
    block30 = models.FloatField(db_column='30', null=True)
    block31 = models.FloatField(db_column='31', null=True)
    block32 = models.FloatField(db_column='32', null=True)
    block33 = models.FloatField(db_column='33', null=True)
    block34 = models.FloatField(db_column='34', null=True)
    block35 = models.FloatField(db_column='35', null=True)
    block36 = models.FloatField(db_column='36', null=True)
    block37 = models.FloatField(db_column='37', null=True)
    block38 = models.FloatField(db_column='38', null=True)
    block39 = models.FloatField(db_column='39', null=True)
    block40 = models.FloatField(db_column='40', null=True)
    block41 = models.FloatField(db_column='41', null=True)
    block42 = models.FloatField(db_column='42', null=True)
    block43 = models.FloatField(db_column='43', null=True)
    block44 = models.FloatField(db_column='44', null=True)
    block45 = models.FloatField(db_column='45', null=True)
    block46 = models.FloatField(db_column='46', null=True)
    block47 = models.FloatField(db_column='47', null=True)
    block48 = models.FloatField(db_column='48', null=True)
    block49 = models.FloatField(db_column='49', null=True)
    block50 = models.FloatField(db_column='50', null=True)
    block51 = models.FloatField(db_column='51', null=True)
    block52 = models.FloatField(db_column='52', null=True)
    block53 = models.FloatField(db_column='53', null=True)
    block54 = models.FloatField(db_column='54', null=True)
    block55 = models.FloatField(db_column='55', null=True)
    block56 = models.FloatField(db_column='56', null=True)
    block57 = models.FloatField(db_column='57', null=True)
    block58 = models.FloatField(db_column='58', null=True)
    block59 = models.FloatField(db_column='59', null=True)
    block60 = models.FloatField(db_column='60', null=True)
    block61 = models.FloatField(db_column='61', null=True)
    block62 = models.FloatField(db_column='62', null=True)
    block63 = models.FloatField(db_column='63', null=True)
    block64 = models.FloatField(db_column='64', null=True)
    block65 = models.FloatField(db_column='65', null=True)
    block66 = models.FloatField(db_column='66', null=True)
    block67 = models.FloatField(db_column='67', null=True)
    block68 = models.FloatField(db_column='68', null=True)
    block69 = models.FloatField(db_column='69', null=True)
    block70 = models.FloatField(db_column='70', null=True)
    block71 = models.FloatField(db_column='71', null=True)
    block72 = models.FloatField(db_column='72', null=True)
    block73 = models.FloatField(db_column='73', null=True)
    block74 = models.FloatField(db_column='74', null=True)
    block75 = models.FloatField(db_column='75', null=True)
    block76 = models.FloatField(db_column='76', null=True)
    block77 = models.FloatField(db_column='77', null=True)
    block78 = models.FloatField(db_column='78', null=True)
    block79 = models.FloatField(db_column='79', null=True)
    block80 = models.FloatField(db_column='80', null=True)
    block81 = models.FloatField(db_column='81', null=True)
    block82 = models.FloatField(db_column='82', null=True)
    block83 = models.FloatField(db_column='83', null=True)
    block84 = models.FloatField(db_column='84', null=True)
    block85 = models.FloatField(db_column='85', null=True)
    block86 = models.FloatField(db_column='86', null=True)
    block87 = models.FloatField(db_column='87', null=True)
    block88 = models.FloatField(db_column='88', null=True)
    block89 = models.FloatField(db_column='89', null=True)
    block90 = models.FloatField(db_column='90', null=True)
    block91 = models.FloatField(db_column='91', null=True)
    block92 = models.FloatField(db_column='92', null=True)
    block93 = models.FloatField(db_column='93', null=True)
    block94 = models.FloatField(db_column='94', null=True)
    block95 = models.FloatField(db_column='95', null=True)
    block96 = models.FloatField(db_column='96', null=True)

    class Meta:
        db_table = 'Forecast_Master'


"""
 "Date": "29-12-2021",
  "Block": 1,
  "Called_At": "28-12-2021 22:01:03",
  "GeoCode": "25.4303,81.7404",
  "cloudCover": 90,
  "dayOfWeek": "Wednesday",
  "dayOrNight": "N",
  "precipChance": 15,
  "precipType": "rain",
  "pressureMeanSeaLevel": 1015.9,
  "qpf": 0,
  "qpfSnow": 0,
  "relativeHumidity": 100,
  "temperature": 15.6,
  "temperatureDewPoint": 15.6,
  "temperatureFeelsLike": 15.6,
  "temperatureHeatIndex": 15.6,
  "temperatureWindChill": 15.6,
  "uvDescription": "Low",
  "uvIndex": 0,
  "validTimeLocal": "2021-12-29T00:30:00+0530",
  "visibility": 1.9,
  "windDirection": 100,
  "windDirectionCardinal": "E",
  "windGust": null,
  "windSpeed": 5,
  "wxPhraseLong": "Cloudy",
  "wxPhraseShort": "Cloudy",
  "wxSeverity": 1,
  "StateCode": "UP0"
"""


class Weather(models.Model):
    date = models.DateField(null=True, blank=True)
    Block = models.IntegerField(null=True, blank=True)
    Called_At = models.DateTimeField(null=True, blank=True)
    GeoCode = models.CharField(max_length=200, null=True, blank=True)
    cloudCover = models.FloatField(null=True, blank=True)
    dayOfWeek = models.CharField(max_length=200, null=True, blank=True)
    dayOrNight = models.CharField(max_length=200, null=True, blank=True)
    precipChance = models.FloatField(null=True, blank=True)
    precipType = models.CharField(max_length=200, null=True, blank=True)
    pressureMeanSeaLevel = models.FloatField(null=True, blank=True)
    qpf = models.FloatField(null=True, blank=True)
    qpfSnow = models.FloatField(null=True, blank=True)
    relativeHumidity = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    temperatureDewPoint = models.FloatField(null=True, blank=True)
    temperatureFeelsLike = models.FloatField(null=True, blank=True)
    temperatureHeatIndex = models.FloatField(null=True, blank=True)
    temperatureWindChill = models.FloatField(null=True, blank=True)
    uvDescription = models.CharField(max_length=200, null=True, blank=True)
    uvIndex = models.FloatField(null=True, blank=True)
    validTimeLocal = models.DateTimeField(null=True, blank=True)
    visibility = models.FloatField(null=True, blank=True)
    windDirection = models.FloatField(null=True, blank=True)
    windDirectionCardinal = models.CharField(max_length=200, null=True, blank=True)
    windGust = models.FloatField(null=True, blank=True)
    windSpeed = models.FloatField(null=True, blank=True)
    wxPhraseLong = models.CharField(max_length=200,null=True, blank=True)
    wxPhraseShort = models.CharField(max_length=200,null=True, blank=True)
    wxSeverity = models.IntegerField(null=True, blank=True)
    StateCode = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return f"{self.GeoCode}"
