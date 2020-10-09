## DNS-App



#### Author: Mucheng Luo

#### CSCI 2262 CDN



## 1. Servers

#### 1. User Server(US)

1. function: 

   1. recieve GET request from browser and parse the url. 
   2. Send GET request to AS for the IP address of  FS
   3. Send GET request to FS for the Xth fibo number

2. possible result(status code)

   1. 400: wrong parameter
   2. 404: hostname not found
   3. 200: get fibo number 

3. paths

   1. '/': home page, shows welcome
   2. '/fabonacci': do the jobs above, return a fibo number or errors

4. input url format:

   ```HTML
   http://0.0.0.0:8080/fibonacci?hostname=fibo.com&fs_port=9090&number=10&as_ip=0.0.0.0&as_port=53533
   ```



#### 2. Fibonacci Server(FS)

1. function:

   1. Send POST request to register the hostname with ipaddress to the AS
   2. Recieve GET request from US and respond a fibo number or error

2. possible result(status code)

   1. 200: get fibo number

3. paths

   1. '/' : home page, shows welcome
   2.  '/register': do the function 1
   3.  '/fabonacci': do the function 2

4. input url format:

   ```
   http://0.0.0.0:9090/register?hostname=fibonacci.com
   ```



#### 3. Authorization Server(AS)

1. function:

   1. Recieve POST request to update the json file
   2. Recieve GET request for the ip address correspond to a host name

2. possible result(status code)

   1. 404: host name not found
   2. 200: saved host information/returned host information

3. paths

   1. '/': finish all the functions above

4. input url format:

   no need for input

   

## 2. Run the App

#### 1. process 1-3(register FS)

1. start the AS

   ![image-20201009122631898](https://s1.ax1x.com/2020/10/10/0s9aTI.png)

2. start the FS, go to path register, the hostname and the ip address will be registered automatically

   my input:(hostname is fibonacci.com, ip address is0.0.0.0, port9090)

   ```http
   http://0.0.0.0:9090/register?hostname=fibonacci.com
   ```

   we can see we get a response status code 200

   ![image-20201009122631898](https://s1.ax1x.com/2020/10/10/0s9XA1.png)

   AS will automatically set up a json file named: address_map.json if it does not exist. Open the Json file we can see the recode:

   ![image-20201009122631898](https://s1.ax1x.com/2020/10/10/0sCQBj.png)

#### 2. Process 4-9(US ask for Xth fibo number)

1. start the US, enter the url with specific parameter

   my input:

   hostname: fibonacci.com, FS port:9090, X: 10, AS ip address:0.0.0.0, AS port: 53533

   ```HTML
   http://0.0.0.0:8080/fibonacci?hostname=fibo.com&fs_port=9090&number=10&as_ip=0.0.0.0&as_port=53533
   ```

2. it will first send request to AS, get the IP address of the hostname, we can see the request and response here:

   in US server:

   ![image-20201009122631898](https://s1.ax1x.com/2020/10/10/0sC7PP.png)

   in AS server:

   ![image-20201009122631898](https://s1.ax1x.com/2020/10/10/0sCOKg.png)

3. if the status code is 200, it shows AS has found the host name and returned the IP address. If not, it will response status code 404, like this:

   please pay attention to the URL I entered, instead of using fibonacci.com as hostname, I use fibo.com this time. So there will not be a fit in AS

   ![image-20201009122631898](https://s1.ax1x.com/2020/10/10/0sPQxO.png)

   the response sent in AS:

   ![image-20201009122631898](https://s1.ax1x.com/2020/10/10/0sP3se.png)

4. If we get the IP address, US server will then send a GET request to the FS server using the IP address just recieved. Then we will get the response from FS and get the fibo number

   ![image-20201009122631898](https://s1.ax1x.com/2020/10/10/0sPfzT.png)

