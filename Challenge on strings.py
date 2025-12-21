"""Convert the messy phno into clean num format with digitos only
+49 (176) 123-4567 ------ 00491761234567"""
phonenum="+49 (176) 123-4567"
print(phonenum.replace("+","00").replace(" ","").replace("(","").replace(")","").replace("-",""))