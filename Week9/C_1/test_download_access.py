import time
from download_access_pr import can_download

user = {"id": 1, "active": True}

file_record = {
    "id": 10,
    "deleted": False
}

token = {
    "revoked": False,
    "expires_at": time.time() + 100
}

print("Download allowed:", can_download(user, file_record, token))
