import requests
import json
import os
import base64


def upload(data):
    """upload to github by api

    :param data: from plugin
    :return:
    """
    config_path = os.getcwd() + '/config/config.json'
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
            # don't be fool
            if config['repo'] != 'beehive':
                print('Be careful, cowboy!')
                return
            url = "https://api.github.com/repos/{user}/{repo}/contents/{path}/{filename}".format(
                user=config['user'],
                repo=config['repo'],
                path='data/'+data['type'],
                filename=data['type'] + '_' + data['date'] + '.json'
            )

            print(url)

            message = 'doc({}):import '.format(data['type']) + data['type'] + '_' + data['date'] + '.json'
            content = base64.b64encode(json.dumps(data['content']).encode('utf-8'))
            payload = "{\n  \"message\": \""+message+"\",\n" \
                      "  \"committer\": {\n" \
                      "    \"name\": \""+config['user']+"\",\n" \
                      "    \"email\": \""+config['email']+"\"\n  },\n" \
                      "  \"content\": \""+str(content, 'utf-8')+"\",\n" \
                      "  \"sha\": \"329688480d39049927147c162b9d2deaf885005f\"\n} "
            headers = {
                'authorization': "token " + config['token']
            }
            response = requests.request("PUT", url, data=str(payload), headers=headers)
            print(response,'111')
    else:
        print('no such config file : ' + config_path)
