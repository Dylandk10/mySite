import re
#class to handle sub routine for member request
class MemberRequestHandler:

    #return true or false for validation
    def validate_name_and_email_message(name, email, message):
        value = True
        if name and email and message:
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if(not re.search(regex,email)):
                value = False
        else:
            value = False
        return value

    #pull client ip
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
