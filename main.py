import pymssql
import pandas

sqlserver = "20.87.42.95"
sqluser = "prtgmonitor"
sqlpass = "Monitor@dm1n"

batchName = input("Enter the batch name (exact name works better): ")
openBatchIDs = []
completeBatchIDs = []
#Added tag 103337 #2
#Added tag 103337 #1
#96000000006021FF 88821 #2
#96000000006021FF 88821 #1
#88867 - Pin Reactivation for failed machines at GLS PnP Eastport #1
try:
    connection = pymssql.connect(sqlserver, sqluser, sqlpass, "Qsmacker")
    cursor = connection.cursor(as_dict=True)
    cursor.execute(f"exec GetBatchStatus '{batchName}'")
    for row in cursor:
        print(row["batchStatusId"])
        if row["batchStatusId"] == 1:
            openBatchIDs.append(row["id"])
        elif row["batchStatusID"] == 3:
            completeBatchIDs.append({row["id"], row["refNo"]})
    print(openBatchIDs)
    print(completeBatchIDs)
except Exception as e:
    print("couldn't connect", e)