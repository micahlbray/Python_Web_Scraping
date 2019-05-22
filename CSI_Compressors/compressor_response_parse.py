import xmltodict
import pandas as pd
import compressor_requests as compressor


#####################################################################################
### All compressors
#####################################################################################
xml = xmltodict.parse(r.text)
data_Compressors = xml['XML']['OVERVIEWDATA']['OVERVIEW']
df_Compressors = pd.DataFrame.from_dict(data_Compressors, orient='columns')

df_Compressors.to_csv("compressors.csv")

#####################################################################################
#####################################################################################
#####################################################################################
### Individual Compressor Field Data
#####################################################################################
xml = xmltodict.parse(r.text)
data = xml['M2M']
data_SystemStatus = xml['M2M']['SystemStatus']['Row_SS']
data_FieldDataSample = xml['M2M']['FieldDataSampleTime']['Row_FDS']
data_FieldData = xml['M2M']['FieldData']['Row_FD']
df_SS = pd.DataFrame.from_dict(data_SystemStatus, orient='columns')
df_FD = pd.DataFrame.from_dict(data_FieldData, orient='columns')
df_FDS = pd.DataFrame.from_dict(data_FieldDataSample, orient='columns')

df_SS.to_csv("compressor_SystemStatus.csv")
df_FD.to_csv("compressor_FieldData.csv")
df_FDS.to_csv("compressor_FieldDataSampleTime.csv")

#####################################################################################
### Historical data
#####################################################################################
xml = xmltodict.parse(r.text)
f = open("compressors_historical_dict.txt", "r")
f.close()
data_DP = xml['M2M']['DP']
for dp in data_DP:
    name = dp['@Nm']
    if name == 'Latitude':
        data_Lat = dp['P']
        df_Lat = pd.DataFrame.from_dict(data_Lat, orient='columns')
        df_Lat.to_csv("compressor_FieldData_latitude.csv")
    elif name == 'Longitude':
        data_Long = dp['P']
        df_Long = pd.DataFrame.from_dict(data_Long, orient='columns')
        df_Long.to_csv("compressor_FieldData_longitude.csv")
    elif name == 'Altitude':
        data_Alt = dp['P']
        df_Alt = pd.DataFrame.from_dict(data_Alt, orient='columns')
        df_Alt.to_csv("compressor_FieldData_altitude.csv")
    elif name == 'Signal Quality':
        data_Signal = dp['P']
        df_Signal = pd.DataFrame.from_dict(data_Signal, orient='columns')
        df_Signal.to_csv("compressor_FieldData_signal.csv")
    elif name == 'Firmware Version':
        data_Firmware = dp['P']
        df_Firmware = pd.DataFrame.from_dict(data_Firmware, orient='columns')
        df_Firmware.to_csv("compressor_FieldData_firmware.csv")
    elif name == 'Fault Code':
        data_Code = dp['P']
        df_Code = pd.DataFrame.from_dict(data_Code, orient='columns')
        df_Code.to_csv("compressor_FieldData_faultcode.csv")
    elif name == 'Engine Hour Meter':
        data_Meter = dp['P']
        df_Meter = pd.DataFrame.from_dict(data_Meter, orient='columns')
        df_Meter.to_csv("compressor_FieldData_meter.csv")
    elif name == 'Field Pressure':
        data_Press = dp['P']
        df_Press = pd.DataFrame.from_dict(data_Press, orient='columns')
        df_Press.to_csv("compressor_FieldData_pressure.csv")
    elif name == 'Password':
        data_Pwd = dp['P']
        df_Pwd = pd.DataFrame.from_dict(data_Pwd, orient='columns')
        df_Pwd.to_csv("compressor_FieldData_password.csv")
    elif name == 'Unit Battery Voltage':
        data_Volt = dp['P']
        df_Volt = pd.DataFrame.from_dict(data_Volt, orient='columns')
        df_Volt.to_csv("compressor_FieldData_voltage.csv")

data_REF = xml['M2M']['REF']['D']
df_REF = pd.DataFrame.from_dict(data_REF, orient='columns')
df_REF.to_csv("compressor_historical_xref.csv")

#####################################################################################
### Individual Compressor Runtime Report
#####################################################################################
# not worth the trouble
xml = xmltodict.parse(r.text)

#####################################################################################
### XML approach instead of converting to JSON
#####################################################################################
import xml.etree.ElementTree as ET
root = ET.parse("compressors.txt").getroot()

for type_tag in root.findall('OVERVIEWDATA/OVERVIEW'):
    value = type_tag.get('ASSETID')
    print(value)