# DMS Report

This repo contains a python script which exports DMS report.

## Repository Structure

```bash
.
├── CHANGELOG.md
├── CONTRIBUTORS.txt
├── README.md
└── extract_table_statistics.py
```

## Pre-requisite

- Install [Python3](https://www.python.org/downloads/)
- Install [boto3](https://pypi.org/project/boto3/) package
- Setup [AWS Credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) in your local machine

## Usage

- Run [python](extract_table_statistics.py) script

  ```bash
  ✗ python3 get_dms_report.py
      Region: us-west-2
      Migration Task Arns (or Enter to quit):
      arn:aws:dms:us-west-2:xxxxxxx:task:xxxxxxx
      arn:aws:dms:us-west-2:xxxxxxx:task:xxxxxxx
      arn:aws:dms:us-west-2:xxxxxxx:task:xxxxxxx

      Extracting Table Statistics...

      Tasks: 3 of 3

      Created DMS Table Statistics Report!!!
  ```

- Report File will be in the root directory

## License

BSD
