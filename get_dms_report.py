import json
import csv
import boto3


# Get DMS Table Statistics Method
def get_table_statistics(client, replication_task_arns):
    """
    Get DMS Table Statistics
    :client: boto3 client
    :replication_task_arns: The Amazon Resource Name (ARN) of the replication task
    :return: returns request response
    """
    marker = ''
    table_statistics = []

    for replication_task_arn in replication_task_arns:
        while True:
            response = client.describe_table_statistics(
                ReplicationTaskArn=replication_task_arn,
                MaxRecords=500,
                Marker=marker
            )

            if isinstance(response.get('TableStatistics'), list):
                table_statistics += response.get('TableStatistics')

            if response.get('Marker'):
                marker = response.get('Marker')
            else:
                break

    return table_statistics


if __name__ == "__main__":
    # Reading Config file
    configs = json.loads(
        open(
          "config.json",
          "r").read()
          )

    # calling dms client
    client = boto3.client('dms', region_name=configs.get('region'))

    # Extracting Table statistics from given Database Migration Task ARNs
    with open("table_statistics.csv", "w", newline="") as table_statistics_file:
        title = "SchemaName,TableName,Inserts,Deletes,Updates,Ddls,FullLoadRows,FullLoadCondtnlChkFailedRows,FullLoadErrorRows,FullLoadStartTime,FullLoadEndTime,FullLoadReloaded,LastUpdateTime,TableState,ValidationPendingRecords,ValidationFailedRecords,ValidationSuspendedRecords,ValidationState,ValidationStateDetails".split(",")
        cw = csv.DictWriter(table_statistics_file, title, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        cw.writeheader()
        cw.writerows(get_table_statistics(client, configs.get('database_migraion_tasks_arns')))
