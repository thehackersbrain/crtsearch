# CRTSH
> crt.sh data scraping script in python

<br/>

Simple Python3 Script for scraping data from `crt.sh`.

<br/>

## Usage
- `python3 main.py -d 'gauravraj.tech'`
```bash
[elliot@archlinux]  crtsh python main.py -d 'gauravraj.tech'
╭───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                       Found Subdomains - CRT.SH                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────╯

[+] gauravraj.tech
[+] blog.gauravraj.tech
[+] *.gauravraj.tech
```

<br/>

- `python3 main.py -d 'gauravraj.tech' -r`
```bash
[elliot@archlinux]  crtsh python main.py -d 'gauravraj.tech' -r
╭───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                           Raw Data - CRT.SH                                           │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────╯

[
    {
        'issuer_ca_id': 183267,
        'issuer_name': "C=US, O=Let's Encrypt, CN=R3",
        'common_name': 'gauravraj.tech',
        'name_value': 'gauravraj.tech\nwww.gauravraj.tech',
        'id': 4875700034,
        'entry_timestamp': '2021-07-15T08:11:14.637',
        'not_before': '2021-07-15T07:11:14',
        'not_after': '2021-10-13T07:11:13',
        'serial_number': '0356c649bd123e7773333fb45324e776f294'
    },
    {
        'issuer_ca_id': 183267,
        'issuer_name': "C=US, O=Let's Encrypt, CN=R3",
        'common_name': 'gauravraj.tech',
        'name_value': 'gauravraj.tech\nwww.gauravraj.tech',
        'id': 4868425658,
        'entry_timestamp': '2021-07-15T08:11:14.235',
        'not_before': '2021-07-15T07:11:14',
        'not_after': '2021-10-13T07:11:13',
        'serial_number': '0356c649bd123e7773333fb45324e776f294'
    },
	...........
```

------

## Credits

- Creator: [Gaurav Raj](https://github.com/thehackersbrain/)
- Portfolio: [gauravraj.tech](https://gauravraj.tech/)
- Blog: [blog.gauravraj.tech](https://blog.gauravraj.tech/)
- TryHackMe: [hackersbrain](https://tryhackme.com/p/hackersbrain)
- HackTheBox: [hackersbrain](https://app.hackthebox.eu/profile/303514)
- Twitter: [thehackersbrain](https://twitter.com/thehackersbrain)
- Instagram: [thehackersbrain](https://instagram.com/thehackersbrain)
- Projects: [GitHub](https://github.com/thehackersbrain?tab=repositories)

--------