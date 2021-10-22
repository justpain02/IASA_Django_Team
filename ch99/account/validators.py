from django.core.exceptions import ValidationError

def validate_email(email):
    # 이메일이 유효한지 검사
    if not '@' in email or not '.' in email:
        raise ValidationError(("Invalid email"), code='invalid')
    

def validate_password(password):
    # 비밀번호 길이가 8자 이상인지 검사
    if len(password) < 8:
        raise ValidationError(("The length of password should be more than 8"), code='invalid')
    