import requests

def get_cookies():
    user = 'PDCWESTREG'
    pwd = 'PDCenergy!!8'
    sessionName, sessionId = get_cookie_session()
    fixation = get_cookie_fixation(sessionName, sessionId, user, pwd)
    cookies = get_cookie_homepage(sessionName, sessionId, fixation)
    return cookies

def get_cookie_session():
    url = 'https://csi.m2mops.com/'
    req = requests.get(url)

    # Get session information from cookies
    for cookie in req.cookies:
        if 'ASPSESSIONID' in cookie.name:
            sessionName = cookie.name
            sessionId = cookie.value
        else:
            sessionName = ''
            sessionId = ''

    return sessionName, sessionId

#####################################################################################
#####################################################################################
def get_cookie_fixation(sessionName, sessionId, user, pwd):
    url = 'https://csi.m2mops.com/Components/Security/UserLoginProcessSysReqs.asp'
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
    req = requests.post(url, cookies=cookies, data=data)

    # Get Fixation code from cookies
    fixation = req.cookies['ASPFIXATION']

    return fixation

#####################################################################################
#####################################################################################
def get_cookie_homepage(sessionName, sessionId, fixation):
    url = 'https://csi.m2mops.com/Components/Security/UserLoginProcessSiteMap.asp'
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
    req = requests.get(url, cookies=cookies, data=data)

    # Get homepage cookie and add to cookies variable
    homepage = req.cookies['strUserHomePage']
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

    return cookies

#####################################################################################
#####################################################################################
### All compressors
#####################################################################################
def get_compressors_gas_jack(cookies):
    url = 'https://csi.m2mops.com/Components/Modules/Custom/CSI/Overview/SuperOverview_Data2.asp?'
    params = {
            'Assetid': '471', # this is the variance in request
            'TimeZoneOffset': '6',
    }
    req = requests.post(url, cookies=cookies, params=params)

    return req

#####################################################################################
def get_compressors_recip_gas(cookies):
    url = 'https://csi.m2mops.com/Components/Modules/Custom/CSI/Overview/SuperOverview_Data2.asp?'
    params = {
            'Assetid': '467', # this is the variance in request
            'TimeZoneOffset': '6',
    }
    req = requests.post(url, cookies=cookies, params=params)

    return req

#####################################################################################
#####################################################################################
### Individual Compressor Field Data
#####################################################################################
def get_compressor_gas_jack_field_data(cookies, AssetId):
    url = 'https://csi.m2mops.com/Components/Modules/Custom/CSI/FieldData/FieldData_Data.asp?'
    params = {
            'returnType': 'INITIAL_LOAD',
            'blnAnalyze': '0',
            'blnControl': '0',
            'blnSystemStatus': '1',
            'StartDate': '1/1/2016 12:00 AM',
            'EndDate': '5/16/2019 11:59 PM',
            'intAssetId': str(AssetId), # this is the variable
            'intAssetTypeId': '57', # this is the variance in request
            'blnExtendedData': '0',
    }
    req = requests.post(url, cookies=cookies, params=params)

    return req

#####################################################################################
def get_compressor_recip_gas_field_data(cookies, AssetId):
    url = 'https://csi.m2mops.com/Components/Modules/Custom/CSI/FieldData/FieldData_Data.asp?'
    AssetId = 5
    params = {
            'returnType': 'INITIAL_LOAD',
            'blnAnalyze': '0',
            'blnControl': '0',
            'blnSystemStatus': '1',
            'StartDate': '1/1/2016 12:00 AM',
            'EndDate': '5/16/2019 11:59 PM',
            'intAssetId': str(AssetId), # this is the variable
            'intAssetTypeId': '35', # this is the variance in request
            'blnExtendedData': '0',
    }
    req = requests.post(url, cookies=cookies, params=params)

    return req

#####################################################################################
#####################################################################################
### Individual Compressor Historical Field Data
#####################################################################################
def get_compressor_gas_jack_field_data_historical(cookies, AssetId):
    url = 'https://csi.m2mops.com/Components/Modules/Custom/CSI/FieldData/HistoricalData_DataNew.asp?'
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
            'strDataPointList': '''101339996,101339997,101339995,101331039,101331040,101331358,101331351,101331019,
                                101331700,101331017''',
            'strFilter': '',
            'MId': '33',
            'AId': str(AssetId), # this is the variable
            'blnShowUnitInfo': 'true',
    }
    req = requests.post(url, cookies=cookies, params=params)

    return req

#####################################################################################
def get_compressor_recip_gas_field_data_historical(cookies, AssetId):
    url = 'https://csi.m2mops.com/Components/Modules/Custom/CSI/FieldData/HistoricalData_DataNew.asp?'
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
            'strDataPointList': '''17231901,17231900,17231902,17231913,17231400,17231401,17231358,17235358,17231344,
                                17235344,17231351,17232351,17233351,17234351,17235351,17231319,17232319,17233319,
                                17234319,17235319,17231308,17232308,17233308,17234308,17235308,17231322,17232322,
                                17233322,17234322,17235322,17231314,17232314,17233314,17234314,17235314,17231363,
                                17232363,17233363,17234363,17235363''',
            'strFilter': '',
            'MId': '33',
            'AId': str(AssetId), # this is the variable
            'blnShowUnitInfo': 'true',
    }
    req = requests.post(url, cookies=cookies, params=params)

    return req

#####################################################################################
#####################################################################################
### Individual Compressor Historical Field Data
#####################################################################################