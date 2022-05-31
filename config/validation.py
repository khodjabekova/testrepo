def validate_audio(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".mp3", ".wav", ".ogg"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Faqat audio fayl kiritish mumkin.")
