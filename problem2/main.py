def caesar(offset, input_str):
    ans = ""
    for i in range (len(input_str)):
        ch = input_str [i] 
        if (ch.isupper()):
            ans += chr((ord(ch)+offset-65)%26+65)
        # elif ch ==" ":
        #     ans += " "
        else :
            ans += chr((ord(ch)+offset-97)%26+97)
    return ans

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl