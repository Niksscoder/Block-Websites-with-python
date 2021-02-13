from datetime import datetime

end_time = datetime(2021, 2, 12, 20)

sites_to_block = ['www.facebook.com', 'facebook.com']

hosts_path = "/etc/hosts"

redirect = "127.0.0.1"

def block_sites():
    if datetime.now() < end_time:
        print("block sites")
        # write all web-sites from our list to hostsfile
        with open(hosts_path, 'r+') as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")

    else:
        print("unblock sites")
        with open(hosts_path, 'r+') as hostsfile:
            lines = hostsfile.readline()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostsfile.write(line)
                hostsfile.truncate()

if __name__ == "__main__":
    # 1. run manually
    block_sites()


