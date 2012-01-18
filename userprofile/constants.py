import os
import settings

USER_TYPES = (
    ('Admin', 'Admin'),
    ('Staff', 'Staff',),
    ('Member', 'Member',),
)

GENDER = (
    ('m','Male'),
    ('f','Female'),
)

UPLOAD_TO = os.path.join(settings.PROJECT_DIR, 'media/guest_data/')
