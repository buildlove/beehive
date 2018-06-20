import requests

url = "https://api.github.com/repos/buildlove/test/contents/test1/demo10.txt"

payload = "{\n  \"message\": \"my commit message\",\n  \"committer\": {\n    \"name\": \"buildlove\",\n    \"email\": " \
          "\"564845354@qq.com\"\n  },\n  \"content\": \"bXkgdXBkYXRlZCBmaWxlIGNvbnRlbnRz\",\n  \"sha\": " \
          "\"329688480d39049927147c162b9d2deaf885005f\"\n} "
headers = {
    'authorization': "token f80de53a6bda9046e494a07f4d56d0e7797eea67",
    }
print(payload)
print('')
print(headers)
response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)