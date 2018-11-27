# email-alert-me

![License](https://img.shields.io/github/license/mashape/apistatus.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

email-alert-me is a command-line interface that alerts you regarding the price change of cryptocurrency.

Dependencies include [schedule](https://github.com/dbader/schedule) to do job-scheduling and [requests](http://docs.python-requests.org/en/master/) to handle API requests to Binance.

# Configuration

Modify `config.py` with the appropriate `SMTP` mail configuration (SSL is enabled by default, so your configuration must target port 465).

The `alerts.json` file can be used to configure the conditions of when to alert the destination e-mail address(es) of the value of a pairing having satisfied the new condition(s).

A separate e-mail is sent for each condition. Once an e-mail alert is sent, the condition is removed from the `conditions` array and `alerts.json` is updated.

```
{
    "alerts": [
        {
            "to": "example@example.com",
            "conditions": [
                "BTCUSDT < 300", "XRPUSDT < 0.5"
            ]
        },
        {
            "to": "foo@bar.com",
            "conditions": [
                "BTCUSDT >= 1000"
            ]
        }
    ]
}
```

will alert `example@example.com` when the value of `XRPUSDT` goes below 0.5, or `BTCUSDT` is below 300, and `foo@bar.com` when the value of `BTCUSDT` is greater than or equal to 1000.

# Installation

Using `virtualenv`

```
virtualenv -p python3 env
. env/bin/activate
pip install -r requirements.txt
```

# Usage

After installation, in the virtual environment run `python run.py`.

# Deployment

Using `pm2` deployment is as simple as

```
pm2 start run.py --interpreter=evn/bin/python
```

The interpreter flag is **necessary** since it forces the Python installation used to be the associated with the virtual environment created during the installation step.
