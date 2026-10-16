# try:
#     pass
# except Exception as e:
#     print("An error occurred:",e)
# else:
#     print("No errors occurred.")
# finally:
#     print("Execution completed.")




# try:
#     a = 100
#     b = 5
#     c = a/b
#     print(int(c))
# except Exception as e:
#     print("An error occurred:",e)
# else:
#     print("No errors occurred.")
# finally:
#     print("Execution completed.")

for i in range (1,11):
    try:
        if i == 3 or i == 5:
            raise Exception("number 3 and 5 are not allowed", {i})

        print(i)
    except Exception as e:
        print({"An error occurred:", e})
