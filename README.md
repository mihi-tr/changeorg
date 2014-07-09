# changeorg a python module to interact with the [change.org](https://change.org) API

[Change.org](https://change.org) is a plattform allowing everyone to create
petitions and collect signatures for support. The site offers an API that
allows to do most things with dedicated clients. This is a python
implementation of basic functionality.

## Installing

`pip install git+https://....`

## Usage

```
import changeorg
change_client = changeorg.Client(api_key='MYKey',api_secret='MySecret')
change.get_petition_id('http://www.change.org/petitions/tell-congress-build-the-enterprise')
```

## Contributing

So far only a subset of functionality is supported - code and documentation
contributions are highly welcome. If you miss functionality or discovered a
Bug: Please submit an issue on [github](https://github.com/mihi-tr/changeorg)

## License

Licensed with a 2-Clause BSD License
