import os
import pymssql
import pandas
from decouple import config

sqlserver = config('SQLSERVER')
sqluser = config('SQLUSER')
sqlpass = config('SQLPASS')

batchName = input("Enter the batch name (exact name works better): ")
openBatchIDs = []
completeBatchIDs = []
allBatchData = pandas.DataFrame()

#Added tag 103337 #2
#Added tag 103337 #1
#96000000006021FF 88821 #2
#96000000006021FF 88821 #1
#88867 - Pin Reactivation for failed machines at GLS PnP Eastport #1
try:
    connection = pymssql.connect(sqlserver, sqluser, sqlpass, "Qsmacker")
    cursor = connection.cursor(as_dict=True)
    cursor.execute(f"exec GetBatchStatus '{batchName}'")
    allBatchData = pandas.DataFrame(cursor.fetchall())
    print(allBatchData)
    for row in allBatchData.itertuples():
        if row.batchStatusId == 1:
            openBatchIDs.append(row.id)
            print(f"Batch is open for {row.refNo}")
        elif row.batchStatusId == 3:
            completeBatchIDs.append({row.refNo})
        elif row.batchStatusId == 4:
            print(f"Batch failed for {row.refNo}")
    for item in range(len(completeBatchIDs)):
        print(f"Batch is complete for {completeBatchIDs[item]}")
#TODO we can add some logic to check if open machines is less than the total machines in the batch, therefore seeing if the batch is still running
except Exception as e:
    print("couldn't connect", e)




    # if row['batchStatusId'] == 1:
    #     openBatchIDs.append(row["id"])
    # elif row['batchStatusId'] == 3:
    #     completeBatchIDs.append({row["id"], row["refNo"]})
    # elif row["batchStatusID"] == 4:
    #     print(f"Batch failed for {row['refNo']}")