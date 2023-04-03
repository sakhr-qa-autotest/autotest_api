from voluptuous import PREVENT_EXTRA, Schema

user = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str,
    },
    extra=PREVENT_EXTRA,
    required=False
)
