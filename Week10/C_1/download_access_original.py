import time


def is_user_active(user):
    if user is None:
        return False

    return user.get("active") is True


def file_exists(file_record):
    if file_record is None:
        return False

    if file_record.get("deleted") is True:
        return False

    return True


def is_token_expired(token):
    if token is None:
        return True

    return time.time() > token["expires_at"]


def is_token_valid(token):
    if token is None:
        return False

    if token.get("revoked") is True:
        return False

    if is_token_expired(token):
        return False

    return True


def can_download(user, file_record, token):
    if not is_user_active(user):
        return False

    if not file_exists(file_record):
        return False

    if not is_token_valid(token):
        return False

    return True
