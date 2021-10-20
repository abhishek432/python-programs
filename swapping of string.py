# Python Program - Swap Two Strings

string1 = input("Enter First String to swap: ");

string2 = input("Enter Second String to swap: ");
print("\nBoth String before swap:");
print("First String =",string1);
print("Second String =",string2);
temp = string1;
string1 = string2;
string2 = temp;
print("\nBoth String after swap:");
print("First String =", string1);
print("Second String =", string2);