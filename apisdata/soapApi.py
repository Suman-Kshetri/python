# SOAP -> Simple Object Access Protocol
# Uses XML for requests and responses.
# Requires a WSDL (Web Services Description Language) URL

from zeep import Client # type: ignore

# WSDL url
wsdl = "http://www.dneonline.com/calculator.asmx?WSDL"

# Create a client
client = Client(wsdl=wsdl)

# Call the Add method
result = client.service.Add(5, 3)
print(result)
