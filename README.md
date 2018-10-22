# email-alert-me
alert me if im losing digital "money" :'(

# Configuration

Modify `config.py` with the appropriate `SMTP` mail configuration.

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