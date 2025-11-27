import secrets
from urllib.parse import quote

def main():
    # Add secret key, admin site url and debug
    BASE="SECRET_KEY={0}\nADMIN_SITE_URL={1}\nDEBUG=True\n".format(secrets.token_urlsafe(),secrets.token_urlsafe())

    # Add database URL
    URL="DATABASE_URL=postgres://{}:{}@{}:{}/{}".format(quote(USER),quote(PASSWORD),HOST,PORT,quote(NAME))

    # Populate env file
    with open("application/.env","a",encoding='utf-8') as write_file:
        write_file.write(BASE+URL)

if __name__=="__main__":
    NAME=""
    USER=""
    HOST=""
    PORT=0
    PASSWORD=""
    if NAME and USER and HOST and PORT and PASSWORD: main()
    else: print("MISSING CREDENTIALS")
