import json
from typing import Literal

from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.ServiceInfo import ServiceInfo
from volcengine.base.Service import Service


def translate(text: str, lang: Literal["en", "jp"] = "jp") -> str:
    k_access_key = "AKLTMzI4MWRhOGFhNWNiNDVjY2I3NTUzOTVkZjdjNDQxZTU"  # https://console.volcengine.com/iam/keymanage/
    k_secret_key = "WkRSa01EWTJZVGhtWkRaaE5ERXdZMkZoWVdNd1ptSmxOekl4WmpreE56UQ=="
    k_service_info = ServiceInfo(
        "open.volcengineapi.com",
        {"Content-Type": "application/json"},
        Credentials(k_access_key, k_secret_key, "translate", "cn-north-1"),
        5,
        5,
    )
    k_query = {"Action": "TranslateText", "Version": "2020-06-01"}
    k_api_info = {"translate": ApiInfo("POST", "/", k_query, {}, {})}
    service = Service(k_service_info, k_api_info)
    body = {"TargetLanguage": "zh", "TextList": [text], "SourceLanguage": lang}
    res = service.json("translate", {}, json.dumps(body))
    res_text = json.loads(res)["TranslationList"][0]["Translation"]
    print(res_text)
    return res_text


if __name__ == "__main__":
    translate("hello")
