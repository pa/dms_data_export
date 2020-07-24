# DMS Report

This repo contains a python script while exports DMS reports

## Repository Structure

```bash
.
├── CHANGELOG.md
├── CONTRIBUTORS.txt
├── README.md
├── config.json
└── get_dms_report.py
```

## Pre-requisite

- Install [Python3](https://www.python.org/downloads/)
- Install [boto3](https://pypi.org/project/boto3/) package
- Update appropriate values in the [configuration](config.json) file
- Setup [AWS Credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) in your local machine

## Usage

Run [python](get_dms_report.py) script

```bash
python3 get_dms_report.py
```

## License

BSD
