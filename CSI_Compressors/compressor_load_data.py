import compressor_requests as cr
import compressor_response_parse as crp

cookies = cr.get_cookies()
a = cr.get_compressors(cookies)
b = cr.get_compressor_field_data(cookies)
c = cr.get_compressor_field_data_historical(cookies)