import requests  # for requesting data from crt.sh
import argparse  # for parsing the arguments
from rich import print  # Rich for styling and highlighting outputs
from rich.text import Text
from rich.panel import Panel
import json  # for parsing json data


def domain_banner():
    banner = Text("Found Subdomains - CRT.SH",
                  justify='center', style='green bold')
    print(Panel(banner))
    print()


def raw_data_banner():
    banner = Text("Raw Data - CRT.SH", justify='center', style='green bold')
    print(Panel(banner))
    print()


def crtsh(domain):
    host = "https://crt.sh/?q="
    # host url (https://crt.sh/?q=<domain>&output=json)
    req_url = host+domain+"&output=json"
    req = requests.get(req_url)  # requesting url
    found_data = req.text  # loading data as text
    # loading json data in python dictionary
    data_dict = json.loads(found_data)
    data = [data_dict, found_data]
    return data  # returning data


def Subdomains(data_dict):
    """function for extracting subdomains from output data"""
    subdomains = []
    for i in data_dict:
        if (i['common_name'] not in subdomains):
            subdomains.append(i['common_name'])
    domain_banner()
    return subdomains


def raw_output(found_data):
    """printing raw output data"""
    raw_data_banner()
    print(json.loads(found_data))


def output_data(outfile, data):
    with open(outfile, 'a') as outfile:
        for i in data:
            outfile.write(i+"\n")


def main():
    # Parsing Arguments
    parser = argparse.ArgumentParser(description="CRT SH Automation")
    parser.add_argument(
        '-d', "--domain", help="Specify Target Domain", type=str, required=True)
    parser.add_argument('-r', "--raw", help="Raw Output", action="store_true")
    parser.add_argument(
        '-o', "--output", help="Write output on a file", type=str)
    arg = parser.parse_args()

    data = crtsh(arg.domain)

    if (arg.raw):
        raw_output(data[1])
    elif (not arg.raw):
        subdomains = Subdomains(data[0])
        for i in subdomains:
            print("[[bold green]+[/bold green]] {}".format(i))
        if (arg.output):
            output_data(arg.output, subdomains)


if __name__ == "__main__":
    main()
