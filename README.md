# Shopify-Dev-Challenge-2019-Winter

Store Restful API
==============================
```
username: Shopify
password: CanadaorBust!
AuthToken: 7761bef4f133a557fb5236e5fb0f13dc93b71c3b
```

This API is a REST-style API designed for the Shopify Dev internship challenge. The "Test-Server" for this is deployed on a GKE cluster which is hosting one api-server pod for API micro-service and one RDBMS(MySQL) pod for Database micro-service. The API server is deployed at [http://35.190.190.186/admin/], please use the endpoints mentioned in this documentation to interact with the API The Docker image for the same would uploaded to Docker hub soon. All the CRUD functionalities have not been implemented yet due to the lack of time. Would be adding more CRUD features soon.
# Deployment
I've reused some of my deployment code from [https://github.com/nschhina/Shopify-Infrastructure_Engineering-Challenge-SPRING-2018] which was the Production Engineering challenge for Fall 2018, which I did for fun :P
I have deployed only one replica for both mysql pod and api pod as I don't expect a lot of traffic/requests. Both services are deployed on the same GKE cluster. I have not used secrets in my YAML as I was not too worried about securing those for this challenge, however it is a really bad practice to have sensitive passwords in cleartext in kubefiles. Both the deployments are exposed behind a LoadBalancer with appropriate targetPort.

![Alt text](static/deployment.png?raw=true "deployment")

# Table of Contents
- [Setup](#setup)
- [Model](#model)
    - [Endpoints](#endpoints)
- [Authentication](#authentication)
- [AdminPanel](#admin-panel)
- [API](#api)
    - [Product](#products)
        - [GET](#get-request-product)
        - [POST](#post-request-product)
        - [PUT](#put-request-product)
        - [DELETE](#delete-request-product)
    - [OrderListView](#orders-list-view)
        - [GET](#get-request-order-list-view)
        - [POST](#post-request-order-list-view)
    - [OrderDetailedView](#order-detailed-view)
        - [GET](#get-request-order-detailed-view)
        - [DELETE](#delete-request-order-detailed-view)
    - [LineItem](#line-items)
        - [GET](#get-request-line-items)

# Setup
-----
This API is written in Python3.7 using Django2.1.1 and DjangoRestFramework3.8.2.
This is my first attempt at designing a REST api using DjangoRestFramework, would advise not to follow the same design pattern.

# Model
-----
* Shops have many Products
* Shops have many Orders
* Products have many Line Items
* Orders have many Line Items

## Endpoints:  

* /api/shop/
* /api/shop/products/
* /api/shop/orders/
* /api/shop/lineitem/
* /api/shop/login/
* /admin

![Alt text](static/404home.png?raw=true "endpoints")


In Django, I'm using one Django app each for Shop, Product, Order and line item. Currently there's only one Shop, but it is very easy to scale up the model to include multiple shops. This API supports multiple Orders, Products and Line Items. Line Item model draws structural relationship from both Order and Product model (ForeignKey fields for each). I've avoided using ManytoManyField relationship in this model to keep everything simple and intuitive.

# Authentication
--------------

In the interest of time, I have only implemented token based authentication for this API. It is not recommended to use this API over HTTP connection. To generate your Auth token, the login endpoint is `35.190.190.186/api/shop/login/`. To create a token for access, make a POST FORM Request at this endpoint with the login credentials -

```
curl --header "Content-Type: application/json" --request POST --data '{"username":"Shopify","password":"CanadaorBust!"}' http://35.190.190.186/api/shop/login/
```

![Alt text](static/login.png?raw=true "login")
Make sure you include this token in your JSON POST/GET requests to be authenticated in order to use this API. For example -

```
{"Authorization": "Token 7761bef4f133a557fb5236e5fb0f13dc93b71c3b"}
```
![Alt text](static/token.png?raw=true "token")

For POSTMAN do the following-  
![Alt text](static/postmanlogin.png?raw=true "postmanlogin")

Another way to get your Auth token is to directly go to `http://35.190.190.186/api/shop/login/` and make a post request using Django's panel.

# Admin panel
Django provides an admin panel for access/manipulation of your models. You can easily use the UI panel at /admin/ once you login with your credentials. This is a pretty cool feature and Django does all the work for you. So in case you don't wish to manually make API requests from POSTMAN or using CURL, this would save you a lot of work.

![Alt text](static/adminlogin.png?raw=true "adminlogin")

![Alt text](static/adminlineitem.png?raw=true "adminlineitem")

![Alt text](static/adminorder.png?raw=true "adminorder")

![Alt text](static/adminview.png?raw=true "adminview")

# API
---------------

In curl, a simple request for the product list would look like this:

## Products

### GET request Product
For information about Current products in store, we make a get request at   /api/shop/products/

```
curl --header "Content-Type: application/json" --request GET -H 'Authorization:Token 7761bef4f133a557fb5236e5fb0f13dc93b71c3b' http://35.190.190.186/api/shop/products/
```

![Alt text](static/getproducts.png?raw=true "getproducts")

### POST request Product

To insert a new product in our shop, we'll be using Post request at   /api/shop/products/

```
curl --header "Content-Type: application/json" --request POST -H 'Authorization:Token 7761bef4f133a557fb5236e5fb0f13dc93b71c3b' --data '{"product_name":"ProdD", "product_price" :"45.54"}' http://35.190.190.186/api/shop/products/
```

![Alt text](static/postproduct.png?raw=true "postproduct")

### PUT request Product
Majorly used to modify the price of current item, this will not create a new object! Make sure you include product_name and product_price in your request
/api/shop/products/

```
curl --header "Content-Type: application/json" --request PUT -H 'Authorization:Token 7761bef4f133a557fb5236e5fb0f13dc93b71c3b' --data '{"product_name": "ProdB","product_price": "58.95"}' http://35.190.190.186/api/shop/products/
```

![Alt text](static/postproduct.png?raw=true "postproduct")

### DELETE request Product
Feel like you don't like product in the shop? JUST DELETE IT! :P Make sure you include product_name in your request  
/api/shop/products/

```
curl --header "Content-Type: application/json" --request DELETE -H 'Authorization:Token 7761bef4f133a557fb5236e5fb0f13dc93b71c3b' --data '{"product_name": "ProdD"}' http://35.190.190.186/api/shop/products/
```


Make sure you include both product_name and product_price fields in your POST request. By design you can't change product_price of an existing product. This will be handled in PUT request

## Orders List View

### GET request Order List View

For information about current orders in store, we make a get request at, you can here check individual price for line items and your total cart price.   /api/shop/orders/

```
curl --header "Content-Type: application/json" --request GET -H 'Authorization:Token 7761bef4f133a557fb5236e5fb0f13dc93b71c3b' http://35.190.190.186/api/shop/orders/
```
![Alt text](static/getorders.png?raw=true "getorders")

### POST requests Order List View
To start a new order, we will make a POST request with order_name field in the list view.    
/api/shop/orders/  

```
curl --header "Content-Type: application/json" --request POST -H 'Authorization:Token 7761bef4f133a557fb5236e5fb0f13dc93b71c3b' --data '{"order_name":"[order_name]"}' http://35.190.190.186/api/shop/orders/
```

## Order Detailed View

### GET request Order Detailed View
To get detailed view of a particular order you can use this detailed view GET method.    
/api/shop/orders/[order_name]/  
NOTE: I did not create slug field or methods, so your Request object must be case sensitive for example "OrderA", "OrderB"..

```
curl --header "Content-Type: application/json" --request GET -H 'Authorization:Token 7761bef4f133a557fb5236e5fb0f13dc93b71c3b' http://35.190.190.186/api/shop/orders/[order_name]/
```

![Alt text](static/orderviewlist.png?raw=true "orderviewlist")

## DELETE request Order Detailed View
Send a delete request with the order_name to get rid of an order. Make sure you include correct order_name. There's no going back

```
curl --header "Content-Type: application/json" --request DELETE -H 'Authorization:Token 7761bef4f133a557fb5236e5fb0f13dc93b71c3b' http://35.190.190.186/api/shop/orders/OrderA/
```

## Line Items

### GET request Line Items
To get detailed view of all the items in queue to be processed(bought), we will use this endpoint.  
/api/shop/lineitem/  

```
curl --header "Content-Type: application/json" --request GET -H 'Authorization:Token 7761bef4f133a557fb5236e5fb0f13dc93b71c3b' http://35.190.190.186/api/shop/lineitem/
```

![Alt text](static/getitem.png?raw=true "getitemlist")
