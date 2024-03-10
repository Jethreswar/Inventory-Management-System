**Products and Inventory Management System**

*Intrduction:*
Created an user-enhanced Inventory Management System using Django for managing product inventory. Primarily, the Django application includes two entities: User (Inventory Manager) and Product.

*Scope/Features:*
- Inventory Manager (user) should be able to register himself with first name, last name and username.
- Inventory Manager should be able to (perform CRUD operations):
  1. Create a product
  2. Read products
  3. Update product details
  4. Delete a product
  5. To execute the above actions, the Django application provides a dashboard that was built using HTML templates with CSS styling.

*Functionalities of the inventory system:*
- Product entities must have fields like product name, description, stock quantity, price, user etc.
- Inventory Manager, upon registering will receive a user id that must be auto-generated.
- Product should have user id (referring to the id of inventory manager, that last modified the state of the product or created it)
- User id attribute would bind the association between inventory product and the user who creates/modifies. Hence it must be taken as an input while creating/updating/deleting products through REST API.
- Inventory Manager should be able to see all the products in the inventory in the latest state, i.e., it should be consistent if multiple users add or modify the inventory.
- When viewing the entire inventory, we must be able to see all the attributes of the products as mentioned above. For the product’s user attribute, the least you need to display is the user's username.
- Make sure you identify the requirements of primary and foreign keys to design schemas based on them.
- Maintained an audit table, to allow users to show history of the product’s modifications, using versioning and its modified states.
