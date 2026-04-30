from python.modules.oeModule.module import simpleInterest
from python.modules.oeModule.compoundInterest import cInterest

principal = float(input("Enter principal amount: "))
time = int(input("Enter Time: "))
rate = float(input("Enter rate: "))

si = simpleInterest.sInterest(principal, time, rate);
print(f"Simple interest = {si}")

ci = cInterest(principal, time, rate)
print(f"Compund Intrest = {ci}")