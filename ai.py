import requests
import json
client_id = ''
client_secret = ''
def get_access_token():
    '''
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    '''
    url = f'''https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'''
    payload = json.dumps('')
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json' }
    response = requests.request('POST', url, headers = headers, data = payload)
    return response.json().get('access_token')


def ai(msage):
    url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token=' + get_access_token()
    payload = json.dumps({
        'messages': [
            {
                'role': 'user',
                'content': msage }] })
    headers = {
        'Content-Type': 'application/json' }
    response = requests.request('POST', url, headers = headers, data = payload)
    result = json.loads(response.text)
    return result

