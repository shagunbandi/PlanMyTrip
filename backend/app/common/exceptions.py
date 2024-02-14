from rest_framework.exceptions import APIException, ValidationError


class ValidationException(Exception):
    status_code = 400
    detail = "Invalid input."

    def __init__(self, detail=None, status_code=None):
        if detail is not None:
            self.detail = detail
        if status_code is not None:
            self.status_code = status_code
        raise ValidationError({"detail": detail, "status_code": status_code})
