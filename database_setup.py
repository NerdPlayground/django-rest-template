from urllib.parse import quote

def get_postgres_url(USER,PASSWORD,HOST,PORT,NAME):
    return "postgres://{}:{}@{}:{}/{}".format(quote(USER),quote(PASSWORD),HOST,PORT,quote(NAME))

def main():
    labels=["USER","PASSWORD","HOST","PORT","NAME"]
    env_file="application/.env"
    with open(env_file) as read_file:
        postgres={}
        for line in read_file:
            line=line.strip()
            if not line: continue
            label,value=line.split("=")
            if label in labels: postgres[label.strip()]=value.strip()
    
    if postgres:
        with open(env_file,"a") as write_file:
            URL=get_postgres_url(
                postgres['USER'],postgres['PASSWORD'],
                postgres['HOST'],postgres['PORT'],postgres['NAME'],
            )
            write_file.write(f"\nDATABASE_URL={URL}")

if __name__=="__main__": main()
