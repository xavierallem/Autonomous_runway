# Autonomous_runway

## About 
Autonomous Runway Detection project was made to detect edge of runways 
or terrains by processing the edge detection at edge computing and then 
sending this data to TCP/IP server. 
This is the report of the project with explanation of how to use and 
implementation 

## Implementation

 The client will start processing and sending the images while server receives 
them and saves them in solution folder. This FreeRTOS project takes the image 
input, performs the edge detection then encrypts it using RSA then sends it to 
server. The server receives the image and performs decryption using private 
key and saves the image. Total three task are created, canny filter, RSA 
encryption and socket for sending data.  

## Edge Detection using Canny filter

Edge detection was implemented using canny filter  coded in c from [Link](https://rosettacode.org/wiki/Canny_edge_detector)

## RSA Encryption

The image we recive is encypted in RSA Algorithm with public key and decrypted at server side with private key 
RSA code in c [Link](https://d3c33hcgiwev3.cloudfront.net/_24f8f0f03c28125c673fd64ce47b253a_rsa.c?Expires=1598659200&Signature=BTH-bY0ZJNxs4wrlB-5IuXvUeTiRMJgUzO~mQJNvk8FOot61NYGVHWABfPWDBN6hqZ9Cqx8l-EsmXWfCtTBOcgjJmjkN~jrebZOSFz1qv8E6yWU1dhEB3KPU5m2yRfpXcLG7oWHk0ood8hQmc7JXPbmNT2RHtuSYASxiyxjlnIc_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

## How to use
- Copy the files from Add_to to FreeRTOS +/Demo/ (you have to download FreeRTOS+ and open through VS)
- Config the main.c to respected Ip and port address
- Run the Server program and wait until it,s up to recieve
