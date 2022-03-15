# Assignment

LabelA backend assignment. Develop an API according to some user stories within 8 hours. User stories include:

- As a company, I want all my products in a database, so I can offer them via our new platform to customers
- As a client, I want to add a product to my shopping cart, so I can order it at a later stage
- As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need
- As a client, I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car
- As a client, I want to select a delivery date and time, so I will be there to receive the order
- As a client, I want to see an overview of all the products, so I can choose which product I want
- As a client, I want to view the details of a product, so I can see if the product satisfies my needs

**Project setup**

- `docker-compose up`
- `docker exec -it *id from the app container* python manage.py createsuperuser` then create your account

**Api endpoints**

- /api/carparts/
- /api/carparts/id
- /api/shoppingcart/
- /api/order/

**Usage**

- Go to http://localhost:8000/admin/ and log in using your account. Add some car parts from the admin menu, then go to the carparts API endpoint to see them.
- Go to the carparts/id endpoint to see the details about a specific item.
- To add items to your shopping cart, go to the shopping cart items section in the admin menu and add the desired amount of items. Then go to the shoppingcart API endpoint to see all the items in the shopping cart
- To place an order, go to the Orders section in the admin menu and select all the items you want to order and select the datetime for delivery. Then go to the shoppingcart API endpoint to see your order.
