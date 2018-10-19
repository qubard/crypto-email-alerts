# email-alert-me
alert me if im losing digital "money" :'(

# Configuration

The `alerts.json` file can be used to configure the conditions of when to alert the destination e-mail address(es) of the value of a pairing having satisfied the new condition.

```
{
    "alerts": [
        {
            "to": "example@example.com",
            "condition": "XRPUSDT < 0.5"
        },
        {
            "to": "foo@bar.com",
            "condition": "BTCUSDT >= 1000"
        }
    ]
}
```

will alert `example@example.com` when `XRPUSDT` goes below 0.5 and `foo@bar.com` when the price of `BTCUSDT` goes is greater than or equal to 1000.

# Installation

Using `virtualenv`

```
virtualenv env
env/Scripts/activate
pip install -r requirements.txt
```