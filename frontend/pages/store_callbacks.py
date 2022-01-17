from dash.dependencies import Input, Output, State 
from datetime import datetime
from app import app, mqtt
import random

@app.callback(Output(component_id='battery-temp-store', component_property='data'), 
              [Input('batterytemp-interval', 'n_intervals')], 
              [State('battery-temp-store', 'data')],)
def battery_temp_store_data(self, data):
  #data=[]
  print("battery_store_data function")
  hms = datetime.now().strftime("%H:%M:%S")
  x = random.randint(0,100)
  data += [hms, x]
  #print(data)
  return data

@app.callback(Output(component_id='battery-voltage-store', component_property='data'), 
              [Input('batteryvoltage-interval', 'n_intervals')], 
              [State('battery-voltage-store', 'data')],)
def battery_voltage_store_data(self, data):
  #print(data)
  #data= []
  print("battery_voltage_data function")
  hms = datetime.now().strftime("%H:%M:%S")
  x = random.randint(0,10)
  data += [hms, x]
 # print(data)
  return data

