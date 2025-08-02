def fibonacci(range_val):
    a=0
    b=1
    for i in range(range_val):
        print(b)
        a,b = b, a+b
        
obj = fibonacci(8)
a = [5, 2, 4, 1]
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]

print(a)

a = {"pfdee": 100, "pafeeg": 1000, "ddsds": 999, "gfgfgh": 10}
arr = {i:a[i] for i in sorted(list(a.keys()), key=lambda e: -len(e))}
print(arr)

str_values = {
	    
    "AUTOMATIC_RESERVATION_DELETION_ENABLED_DE_WEBSITE": "Enabled",
    "AUTOMATIC_RESERVATION_DELETION_RUN_TIME_DE_WEBSITE": "60",
    "AUTOMATIC_RESERVATION_DELETION_ENABLED_FR_WEBSITE": "Enabled",
    "AUTOMATIC_RESERVATION_DELETION_RUN_TIME_FR_WEBSITE": "60"
}
market_channel = []
market_enabled = []
markets = []
mkt_chnl = ""
for str1, val in str_values.items():
    i = 0
    if "AUTOMATIC_RESERVATION_DELETION_ENABLED_" in str1:
        arr1 = str1.split("_")
        mkt= arr1[len(arr1)-2:-1:]
        # chnl = chnl.insert(arr1[len(arr1)-1])
        chnl = arr1[len(arr1)-1::]
        if val == 'Enabled':
            mkt_chnl = mkt[i]+"_"+chnl[i]
            mkt_enabled = mkt[i]+"_"+val
            market_channel.append(mkt_chnl)
            market_enabled.append(mkt_enabled)
            markets.append(mkt[i])
    # print(mkt_chnl) 
    if market_enabled[i] == markets[i]+"_Enabled" and "AUTOMATIC_RESERVATION_DELETION_RUN_TIME_"+mkt_chnl in str1:
        print("Run Val: {}"+str_values[str1])
        print(market_enabled)
    i = i + 1
# print(market_channel)
# for str2, val2 in str_values.items():
#     s = 0
#     if "AUTOMATIC_RESERVATION_DELETION_RUN_TIME_"+market_channel[s] in str2:
#             print("Run Val: {}"+str_values[str2])
#             s = s+1


print("\n\n")

print("========Read each element from list=======")

list_one = [{'DE-WEBSITE': 1}, {'AE-WEBSITE': 0}, {'CZ-WEBSITE': 0}, {'GB-WEBSITE': 0}, {'ID-WEBSITE': 0}, {'MX-WEBSITE': 2}, {'MX-DIRECTRETAIL': 5}, {'TN-WEBSITE': 0}, {'VN-WEBSITE': 0}, {'VU-WEBSITE': 0}, {'DE-DIRECTRETAIL': 0}, {'DE-INDIRECTRETAIL': 0}, {'DE-CEF': 0}, {'FR-DIRECTRETAIL': 0}, {'FR-INDIRECTRETAIL': 0}, {'FR-CEF': 0}, {'AE-DIRECTRETAIL': 0}, {'AE-INDIRECTRETAIL': 0}, {'AE-CEF': 0}, {'CZ-DIRECTRETAIL': 0}, {'CZ-INDIRECTRETAIL': 0}, {'CZ-CEF': 0}, {'GB-DIRECTRETAIL': 0}, {'GB-INDIRECTRETAIL': 0}, {'GB-CEF': 0}, {'ID-DIRECTRETAIL': 0}, {'ID-INDIRECTRETAIL': 0}, {'ID-CEF': 0}, {'MX-DIRECTRETAIL': 0}, {'MX-INDIRECTRETAIL': 0}, {'MX-CEF': 0}, {'TN-DIRECTRETAIL': 0}, {'TN-INDIRECTRETAIL': 0}, {'TN-CEF': 0}, {'VN-DIRECTRETAIL': 0}, {'VN-INDIRECTRETAIL': 0}, {'VN-CEF': 0}, {'VU-DIRECTRETAIL': 0}, {'VU-INDIRECTRETAIL': 0}, {'VU-CEF': 0}]
print("*****List Element****")
for i in range(len(list_one)):
    for key in list_one[i].keys():
        print("-----Key Value---")
        print("Key: "+key+" Value: "+str(list_one[i][key]))
        lst_str = key.split("-")
        print(lst_str[0]+"\r")
        print(lst_str[1]+"\r")