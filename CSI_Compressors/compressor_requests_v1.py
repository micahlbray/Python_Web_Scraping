import compressor_requests_v1
import json

url = 'https://csi.m2mops.com/'
r = compressor_requests_v1.get(url)
for cookie in r.cookies:
    if 'ASPSESSIONID' in cookie.name:
        sessionName = cookie.name
        sessionId = cookie.value
    else:
        sessionName = ''
        sessionId = ''

#####################################################################################
#####################################################################################
url = 'https://csi.m2mops.com/Components/Security/UserLogin.asp'
headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'csi.m2mops.com',
            'Referer': 'https://csi.m2mops.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
}
cookies = {
    sessionName: sessionId,
    'strTest2': 'Test',
}
r = compressor_requests_v1.get(url, headers=headers, cookies=cookies)

#####################################################################################
#####################################################################################
user = 'PDCWESTREG'
pwd = 'PDCenergy!!8'
url = 'https://csi.m2mops.com/Components/Security/UserLoginProcessSysReqs.asp'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'csi.m2mops.com',
    'Origin': 'https://csi.m2mops.com',
    'Referer': 'https://csi.m2mops.com/Components/Security/UserLogin.asp',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
}
cookies = {
    sessionName: sessionId,
    'intTZOffsetHours': '6',
    'strBrowserReq': 'True',
    'strColorDepthReq': 'True',
    'strCookiesReq': 'True',
    'strDetectSystemReq': 'True',
    'strJavaScriptReq': 'True',
    'strTest2': 'Test',
}
data = {
        'strUser_UserName': user,
        'strUser_Password': pwd
}
r = compressor_requests_v1.post(url, headers=headers, data=data, cookies=cookies)
fixation = r.cookies['ASPFIXATION']

#####################################################################################
#####################################################################################
url = 'https://csi.m2mops.com/Components/Security/UserLoginProcessSiteMap.asp'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'csi.m2mops.com',
    'Origin': 'https://csi.m2mops.com',
    'Referer': 'https://csi.m2mops.com/Components/Security/UserLoginProcessSysReqs.asp',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
}
cookies = {
    'ASPFIXATION': fixation,
    sessionName: sessionId,
    'intTZOffsetHours': '6',
    'strBrowserReq': 'True',
    'strColorDepthReq': 'True',
    'strCookiesReq': 'True',
    'strDetectSystemReq': 'True',
    'strJavaScriptReq': 'True',
    'strTest2': 'Test',
}
data = {'intBandwidth': '8713'}
r = compressor_requests_v1.get(url, headers=headers, cookies=cookies, data=data)

# Get homepage cookie and add to cookies variable
homepage = r.cookies['strUserHomePage']
cookies = {
    'ASPFIXATION': fixation,
    sessionName: sessionId,
    'intTZOffsetHours': '6',
    'strBrowserReq': 'True',
    'strColorDepthReq': 'True',
    'strCookiesReq': 'True',
    'strDetectSystemReq': 'True',
    'strJavaScriptReq': 'True',
    'strTest2': 'Test',
    'strUserHomePage': homepage,
}

#####################################################################################
#####################################################################################
url = 'https://csi.m2mops.com/Components/Modules/Custom/CSI/Overview/SuperOverview.asp'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'csi.m2mops.com',
    'Origin': 'https://csi.m2mops.com',
    'Referer': 'https://csi.m2mops.com/Components/Security/UserLoginProcessSiteMap.asp',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
}
cookies = {
    'ASPFIXATION': fixation,
    sessionName: sessionId,
    'intTZOffsetHours': '6',
    'strBrowserReq': 'True',
    'strColorDepthReq': 'True',
    'strCookiesReq': 'True',
    'strDetectSystemReq': 'True',
    'strJavaScriptReq': 'True',
    'strTest2': 'Test',
    'strUserHomePage': homepage,
}
data = {
        'AId': '471',
        'ANm': '414 GasJack',
        'MId': '6',
        'MNm': 'Overview',
        'SMR': '1',
        'ATId': '5',
        }
r = compressor_requests_v1.get(url, headers=headers, cookies=cookies, data=data)

#####################################################################################
### All compressors
#####################################################################################
url = 'https://csi.m2mops.com/Components/Modules/Custom/CSI/Overview/SuperOverview_Data2.asp?'
cookies = {
    'ASPFIXATION': fixation,
    sessionName: sessionId,
    'strTest2': 'Test',
    #'strUserHomePage': homepage,
}
params = {
        'Assetid': '471',
        'TimeZoneOffset': '6',
}
r = compressor_requests_v1.post(url, cookies=cookies, params=params)


#####################################################################################
#####################################################################################
#####################################################################################
### Individual Compressor Field Data
#####################################################################################
url = 'https://csi.m2mops.com/Components/Modules/Custom/CSI/FieldData/FieldData_Data.asp?'
cookies = {
    'ASPFIXATION': fixation,
    sessionName: sessionId,
    'strTest2': 'Test',
    'strUserHomePage': homepage,
}
params = {
        'returnType': 'INITIAL_LOAD',
        'blnAnalyze': '0',
        'blnControl': '0',
        'blnSystemStatus': '1',
        'StartDate': '1/1/2016 12:00 AM',
        'EndDate': '5/16/2019 11:59 PM',
        'intAssetId': '10133',
        'intAssetTypeId': '57',
        'blnExtendedData': '0',
}
r = compressor_requests_v1.post(url, cookies=cookies, params=params)


#####################################################################################
### Individual Compressor Historical Field Data
#####################################################################################
url = 'https://csi.m2mops.com/Components/Modules/Custom/CSI/FieldData/HistoricalData_DataNew.asp?'
cookies = {
    'ASPFIXATION': fixation,
    sessionName: sessionId,
    'strTest2': 'Test',
    'strUserHomePage': homepage,
}
params = {
        'strStartDate': '1/1/2016 12:00 AM', ## earliest date
        'strEndDate': '5/16/2019 11:59 PM',
        'strStartDateValue': '1/1/2016',
        'strStartTimeValue': '12:00 AM',
        'strEndDateValue': '5/16/2019',
        'strEndTimeValue': '11:59 PM',
        'blnInvalid': 'true',
        'StoredInGMT': 'TRUE',
        'returnType': 'Data',
        'strCurrSort': 'SampleTime',
        'strDataPointList': '101339996,101339997,101339995,101331039,101331040,101331358,101331351,101331019,101331700,101331017',
        'strFilter': '',
        'MId': '33',
        'AId': '10133',
        'blnShowUnitInfo': 'true',
}
r = compressor_requests_v1.post(url, cookies=cookies, params=params)

#signal quality (5=Acceptable, 10=Poort, 59=No Signal)

#####################################################################################
### Individual Compressor Runtime Report - Page Load
#####################################################################################
url = 'https://csi.m2mops.com/Components/Modules/RuntimeReportTabs/RuntimeReport.asp?'
cookies = {
    'ASPFIXATION': fixation,
    sessionName: sessionId,
    'strTest2': 'Test',
    'strUserHomePage': homepage,
}
params = {
        'MId': '16',
        'MTId': '12',
        'TId': '12',
        'AId': '10133',
        'ATId': '57',
        'ANm': 'MP-002',
}
r = compressor_requests_v1.post(url, cookies=cookies, params=params)

#####################################################################################
### Individual Compressor Runtime Report
#####################################################################################
url = 'https://csi.m2mops.com/Components/Modules/RuntimeReportTabs/RuntimeReportTabs_Data.asp?'
cookies = {
    'ASPFIXATION': fixation,
    sessionName: sessionId,
    'strTest2': 'Test',
    'strUserHomePage': homepage,
}
params = {
        'returnType': 'INITIAL_ASSETLOAD',
        'MId': '16',
        'ran': 'Thu May 16 2019 19:57:03 GMT-0600 (Mountain Daylight Time)',
        'strStartDate': '1/1/2016',
        'strEndDate': '5/16/2019',
        'strSort': 'ASC',
}
r = compressor_requests_v1.post(url, cookies=cookies, params=params)

#####################################################################################
### Individual Compressor Historical Runtime Report
#####################################################################################
url = 'https://csi.m2mops.com/Components/Modules/RuntimeReportTabs/RuntimeReportTabs_Data.asp?'
headers = {'Content-Type': 'application/x-www-form-urlencoded',}
cookies = {
    'ASPFIXATION': fixation,
    sessionName: sessionId,
    'strTest2': 'Test',
    'strUserHomePage': homepage,
}
params = {
        'returnType': 'BUILD_ASSETRUNTIME',
        'ran': 'Thu May 16 2019 19:57:03 GMT-0600 (Mountain Daylight Time)',
}
payload = {
        'strStartDate': '1/1/2016 12:00 AM',
        'strEndDate': '5/16/2019 11:59 PM',
        'AssetId': '10133',
        'ShowRunning': 'true',
        'ShowUnitInfo': 'true',
        'TimeZoneId': '6', #MST
        'strSort': 'ASC',
        'MId': '16',
}
r = compressor_requests_v1.post(url, headers=headers, data=json.dumps(payload)), cookies= cookies, params= params, json=payload)

