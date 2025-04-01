def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
if __name__ =='__main__':
    print(http_error(418))