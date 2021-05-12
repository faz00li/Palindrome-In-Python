def isPalindrome(strng: str):
  print("\nParsing Input")
  # print("Input:           ", strng)
  strng = strng.upper()
  # print("Input to upper:  ", strng)
  l_strng = strng.split()
  l_strng.insert(0, "*")
  # print("Input as list:   ", l_strng)
  strng = "".join(l_strng)
  print("Input as string: ", strng + "\n")

    
  print("Comparing")
  for i in range(int(len(strng) / 2)):
    i += 1
    print(" i: ", strng[i], end=" <---> ")
    print("-i: ", strng[-i])
    if strng[i] != strng[-i]:
      print(strng[i] + " does not match " + strng[-i])
      return False

  return True

  

print(isPalindrome("bob"))
print(isPalindrome("boob"))
print(isPalindrome("boook"))
print(isPalindrome("bobby"))
print(isPalindrome("I did did I"))
print(isPalindrome("My gym"))



