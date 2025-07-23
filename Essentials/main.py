import json
import os
from dotenv import load_dotenv
import requests
import pandas as pd
from ETL import *
load_dotenv()


# Data = """Bill To
# Gatorade Global
# 8060 State Road 33 
# North
# Lakeland FL 33809
# Invoice
# Date I nvoice #
# 10/28/2022 21696
# Service Location
# Gatorade Global
# 8060 State Road 33 North
# Lakeland, FL 33809
# Net 60 12/27/2022 10/24/2022 315-22-009
# BOL Amount
# Bibs
# 10/24/2022
# Transportation Costs 731.00 731.00
# Fuel Surcharge 731 336.26
# Disposal Services of 5 gallon Bibs 691 2.35 1067187547 1,623.85 Disposal Services of 3 gallon Bibs 173 1.95 1067187547
# 337.35
# Subtotal $3,028.46
# Sales Tax (0.0%) $0.00
# Total $3,028.46
# Accounts Payable Payments/Credits $0.00 Attn: 
# There will be a additional 3.33% charge on total Invoice for Credit
# Balance Due $3,028.46
# Due Date Service I Ship 
# Date
# Purchase 
# Order Disposal Location
# Description Qty/Hours Ticket No. Rate Manifest 1 
# Fax: 281-867-4773
# Card 
# Payments
# CERTIFICATE OF DESTRUCTION
# ACOR
# American Complete Organics Recycling
# ISSUED TO: LEL ENVIRONMENTAL, LTD.
# ADDRESS: 4040-GAT LAKELAND SC 
# 8060 STATE ROAD 33 N LAKELAND, 
# FL 33809 DATE RECEIVED: 
# 10/24/2022
# DATE PROCESSED: 10/26/2022
# DESCRIPTION OF WASTE: 864 Total Cases: 691 - 5 gallon Pepsi Bibs, 173 - 3 gallon Pepsi 
# Bibs
# Bill of lading#: 40403906932.4040390605.40403906880 PO # 315-22-009 Invoice # 100606
# ACOR certifies acceptance of the material referenced on this document. ACOR certifies 
# that all materials listed above have been processed and destroyed pursuant to all 
# applicable laws including environmental and waste management regulations. The 
# destruction process will ensure that all material is destroyed and recycled.
# I certify that the information contained in or accompanying this document is true, accurate and complete as to the 
# identification of the materials received from the generator and the processing of the waste in accordance with the TCEO
# approvals and requirements.
# NAME: Les Kemp TITLE: Operations Manager
# Si Date: 10/28/22
# Date: 10/21/2022 17:24:34 BILL OF LADING Page 1
# CARRIER INFORMATION
# HANDLING 
# UNIT
# PACKAGE
# WEIGHT(LB)
# (X)
# COMMODITY DESCRIPTION LTL ONLY
# Commodities requiring specie' or additiona' a'tgnt'on in harx"ino or stowing must be SO 
# marked and packaged as to ensurg sate transportation with ordinar. care
# NMFC # CLASS QTY TYPE See Section 2(e) ot NMFC Item
# 1 6 CHEP pauets 437 CS- case 23237 BEV PREP DRY OR LIQ 721 60 60
# SHIP FROM Document Number: 40403906905
# Appt: 10/21/22 12:00 PM
# Checkin: 10/19/22 4:06 PM
# Loaded: 10/21/22 5:23 PM (402) 
# 40403906905
# Dispatch: 10/21122 5:24 PM
# Name: 4040-GAT LAEKLAND SC
# Address: 8060 STATE ROAD 33 N
# City/State/Zip: LAKELAND, FL 33809-1704
# SID/BOL#: 1067187547 FOB:
# SHIP TO 
# Name: ACOR
# Address: 1121 DIGIORGIO RD.
# City/State/Zip: FORT PIERCE, FL 34982
# ID: CWE8303410844 FOB..
# Carrier Name: 
# CUSTOMER PICK UP
# MOS: p
# Trailer Number:
# Seal number(s): no seal
# SCAC: CPU CAR MOVE: 1067187547
# Pro Number: 8303410844 LOAD SEQ: 1
# unless marked
# THIRD PARTY FREIGHT CHARGES BILL TO:
# Name: One—time Customer
# Address: One—time customer
# Freight Charge (freight charges are prepaid 
# otherwise)
# Prepaid Collect 3rd Party
# Master Bill Of Lading: with attached underlying Bills 
# (check box) of Lading
# SPECIAL INSTRUCTIONS: arranged by D. Joosten LEL
# CUSTOMER ORDER INFORMATION
# CUSTOMER ORDER NUMBER # PKGS WEIGHT(LB)
# Pallet'S"
# ADDITIONAL SHIPPER INFO rcle ne)
# PCNA BIB DISPOSAL 7 24360 Y
# N RAD-10/21/22 0-8303410845 S-125054641
# Y N
# Y N
# Y N
# Y N
# GRAND TOTAL 24360
# I 
# Wood 
# Pallets
# 20 cs-case 1 123 BEV PREP DRY OR 721 60 60
# 1 7 457 24360 25482 GROSS WGT GRAND TOTA
# Where the rate is dependent on vatue. shippers are required to State specifically in writing the 
# agreed or declared value of the property as foilows:
# •The agreed or declared value 0t the property IS specifically stated by the shipper to be not 
# exceeding 
# COD Amount: $
# Fee Terms: Collect: a Prepaid: Customer check acce 
# table:
# NOTE Liabilit Limitation for loss or damage in this shipment may be applicable. See 49 IJ.S.C. — and (B)
# RECEIVED, subject to individual'y determined rates or contracts that have been agreed upon in writing between 
# the carrier and shipper. if applicable. otherwise to the rates. classifications and rules thal have been established 
# by the carrier and are avaiiable to the shipper, on request, and to atl applicable state and federal regulations.
# The carrier shall not make delivery of this shipment 
# without payment of freight and all other lawful charges.
# Shipper
# Signature
# SHIPPER SIGNATURE/OATE
# TN'S is to certify that the above named materials are 
# property classified, described, packaged. marked and labeled. 
# and are in proper conditton for transportation according to 
# the applicable regulations Of lhO Otpartmonl o' 
# Transportation
# Trailer Loaded: Freight Counted:
# By ShipperBy Shipper
# By Driver/pallets said 
# Driverto
# By Driver/Pieces
# CARRIER SIGNATURE'PICKUP DATE
# Camor acknowledges receipt at packages and requited placards. Carrier 
# cert"ies emergency response tntcvmateon was madc available and,'or 
# carne' has the DOT emergency resptmse guidebook or aquyvaignt 
# documentation in the vehicle"""
Data = result
prompt = f"""You are an AI Model, with expertise in the finance so make sure you extract the given information
            in the perfect key value pairs {Data}, and list down all the invoice details with prper key value pairs along with, what is the source and destination (Usually Bill from and Bill to) of this invoice along with the final Taxcode
            and Tax Percentage if applies"""

def get_resp_from_api(prompt: str,
                      model: str = "gemma3:4b-it-qat",
                      ctx: int = 4000) -> None:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_ctx": ctx
            }
        }
    )
    
    # Get the response JSON
    resp_json = response.json()
    
    # Clean unicode escapes in the 'response' field if needed
    if 'response' in resp_json:
        resp_json['response'] = resp_json['response'].encode().decode('unicode_escape')
    
    # Print each key and value in a neat format
    print("\n--- API Response (Key: Value) ---\n")
    for key, value in resp_json.items():
        print(f"{key}:\n{value}\n")

get_resp_from_api(prompt)

