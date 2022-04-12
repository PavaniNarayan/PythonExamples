#  list to store multi line input
#  press enter two times to exit
data = []
print("Tell me about yourself")
while True:
    line = raw_input()
    if line:
        data.append(line)
    else:
        break
finaltext = '\n'.join(data)
print("\n")
print("Final Text is :")
print(finaltext)

