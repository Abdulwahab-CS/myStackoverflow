from django.core.validators import RegexValidator


tag_validator = RegexValidator(
            regex='^[a-zA-Z$][a-zA-Z0-9.@#+-_]*$',
            message='Invalid tag name')