import random
import string
from django.utils import timezone


def generate_slug(max_length=8) -> str:
    first_pass = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=max_length)
    )

    timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
    return f"{first_pass}-{timestamp}"[:max_length]
