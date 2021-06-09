from app.models import db, Item


def seed_items():
    # Panda Express

    # Popular Items
    item1 = Item(name='Plate', description="Any 1 Side & 2 Entrees", price=10.45, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/c7705748-8e07-46c8-a153-1b7ff0355b75-retina-large-jpeg")
    db.session.add(item1)

    item2 = Item(name='Bigger Plate', description="Any 1 Side & 3 Entrees", price=12.25, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/1c55af2e-adeb-4d4a-8025-0a498eb70a0e-retina-large-jpeg")
    db.session.add(item2)

    item3 = Item(name='Bowl', description="Any 1 Side & 1 Entree", price=8.65, restaurant_id=1, 
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/7eaaa60a-bee5-4216-b192-c306066750c5-retina-large-jpeg")
    db.session.add(item3)

    item4 = Item(name='Kid\'s Meal', description="Any 1 Side & 1 Entree", price=7.70, restaurant_id=1)
    db.session.add(item4)

    item5 = Item(name="Family Meal", description="Any 2 Large Sides & 3 Large Entrees", price=34.80, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/6e737e50-8081-43d1-afe7-15997338bf51-retina-large-jpeg")
    db.session.add(item5)

    # A La Carte
    item6 = Item(name="Wok Seared Steak & Shrimp", price=12.50, restaurant_id=1, 
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/d09f8f91-4411-4ae7-b16d-dab4b02eaaf4-retina-large-jpeg")
    db.session.add(item6)

    item7 = Item(name="Black Pepper Angus Steak", price=12.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/905b2a5c-bf3a-414c-b0e7-f541dc781bcf-retina-large-jpeg")
    db.session.add(item7)

    item8 = Item(name="The Original Orange Chicken", price=12.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/79213bf5-59f5-48a3-8eed-e91ffaf3a81a-retina-large-jpeg")
    db.session.add(item8)

    item9 = Item(name="Grilled Teriyaki Chicken", price=12.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/07c22acc-3036-4030-b003-0000e3e0f53c-retina-large-jpeg")
    db.session.add(item9)

    item10 = Item(name="Honey Walnut Shrimp", price=12.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/a3b14174-a398-4aec-8b76-55124467324e-retina-large.jpg")
    db.session.add(item10)

    # Appetizers
    item11 = Item(name="Chicken Egg Roll", price=6.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/49d374aa-1718-4741-8ccd-afb8095a45cd-retina-large-jpeg")
    db.session.add(item11)

    item12 = Item(name="Veggie Spring Roll", price=5.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/896291aa-ee01-42dd-b8b4-aae584d96ca8-retina-large-jpeg")
    db.session.add(item12)

    # Drinks
    item13 = Item(name="Coca Cola", price=3.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/7fd1126b-54e9-4a69-8a7f-a08b8cc50e64-retina-large-jpeg")
    db.session.add(item13)

    item14 = Item(name="Diet Coke", price=3.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/4a3dd119-acf6-4d02-bb49-c858d920cee2-retina-large-jpeg")
    db.session.add(item14)

    item15 = Item(name="Sprite", price=3.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/aa366484-f518-4edc-a281-7699e0a08043-retina-large-jpeg")
    db.session.add(item15)

    item16 = Item(name="Diet Coke", description="16oz Bottle", price=3.00, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/4174683f-112d-40da-97af-7c54df019999-retina-large-jpeg")
    db.session.add(item16)

    # McDonald's

    # Most Popular
    item17 = Item(name="The BTS Meal", description="10 Piece McNugget, Medium Fry, Medium Drink (740 - 980 Cal.)", price=11.43, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/390a4bc8-3630-4ddd-a0a0-1a099851a7aa-retina-large-jpeg")
    db.session.add(item17)

    item18 = Item(name="Big Mac Meal", description="(870 - 1110 Cal.)", price=12.23, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/79ffceed-52b7-45e1-9606-36cd173572ae-retina-large.jpg")
    db.session.add(item18)

    item19 = Item(name="10 Piece McNuggets Meal", description="(740 - 980 Cal.)", price=11.43, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/0a37a43f-4320-419a-a72c-1138e35a73b5-retina-large-jpeg")
    db.session.add(item19)

    item20 = Item(name="40 McNuggets", description="(1660 Cal.)", price=11.59, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/8614e107-dabd-4218-be57-6df8fd619a3e-retina-large-jpeg")
    db.session.add(item20)

    item21 = Item(name="French Fries", description="(220 Cal.)", price=2.79, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/d0d5bdfb-a107-4050-8323-5bc4ad603adf-retina-large.jpg")
    db.session.add(item21)

    item22 = Item(name="Oreo McFlurry", description="(340 Cal.)", price=3.49, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/e7bb4627-110a-45f4-ba67-96e78a54959c-retina-large.jpg")
    db.session.add(item22)

    # Combo Meals
    item23 = Item(name="Spicy Chicken Sandwich Meal", description="(850 - 1090 Cal.)", price=11.43, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/1ee067c2-e907-4516-bbec-b555b11d3ffe-retina-large-jpeg")
    db.session.add(item23)

    item24 = Item(name="Quarter Pounder with Cheese Meal", description="(840 - 1080 Cal.)", price=12.53, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/804feda6-e466-4c58-b8b4-aab1718979c7-retina-large.jpg")
    db.session.add(item24)

    item25 = Item(name="2 Cheeseburger Meal", description="(920 - 1160 Cal.)", price=9.62, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/7015a61f-6179-4349-9087-82bb1d641a2b-retina-large-jpeg")
    db.session.add(item25)

    item26 = Item(name="Filet O Fish Meal", description="(700 - 940 Cal.)", price=11.43, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/4f6307a5-9392-4da1-9861-96686d136529-retina-large-jpeg")
    db.session.add(item26)

    # Happy Meals
    item27 = Item(name="Hamburger - Happy Meal", description="(375 Cal.)", price=4.69, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/45699277-6544-4ffc-8931-f86de29d8ff6-retina-large-jpeg")
    db.session.add(item27)

    item28 = Item(name="Cheese Burger - Happy Meal", description="(430 - 590 Cal.)", price=4.99, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/f33ae198-98e2-4e73-b7f8-a64ca856e377-retina-large.jpg")
    db.session.add(item28)

    item29 = Item(name="6pc Chicken McNuggets Happy Meal", description="(430 - 530 Cal.)", price=6.09, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/b912085a-31bf-4bf1-9e42-e4897acda5f2-retina-large-jpeg")
    db.session.add(item29)

    # McCafe
    item30 = Item(name="Premium Roast Coffee", description="(0 Cal.)", price=1, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/a7e0c926-9110-427c-8662-13ba8e86459e-retina-large.jpg")
    db.session.add(item30)
    
    item31 = Item(name="Decaf Coffee", description="(0 Cal.)", price=1, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/a7e0c926-9110-427c-8662-13ba8e86459e-retina-large.jpg")
    db.session.add(item31)
    
    item32 = Item(name="Hot Tea", description="(10 Cal.)", price=1.59, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/c2d0fc5c-7ce1-4157-9267-6f630b09e9bb-retina-large.jpg")
    db.session.add(item32)
    
    item33 = Item(name="Iced Coffee", description="(140 Cal.)", price=2.33, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/0a59dc23-88bd-4fff-8f2c-8b7f00b7b713-retina-large.jpg")
    db.session.add(item33)
    
    item34 = Item(name="Premium Hot Chocolate", description="(380 Cal.)", price=2.50, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/41adc628-bd31-4385-b44a-42a3b4a779de-retina-large.jpg")
    db.session.add(item34)
    
    item35 = Item(name="Mocha Frappé", description="(420 Cal.)", price=2.63, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/78476d12-1e2a-41fc-a0d4-4dccca626bd9-retina-large.jpg")
    db.session.add(item35)
    
    item36 = Item(name="Caramel Macchiato", description="(270 Cal.)", price=2.50, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/7f3df6f7-53d1-4413-a9a1-d02dd854c160-retina-large-jpeg")
    db.session.add(item36)
    
    item37 = Item(name="Americano", description="(5 Cal.)", price=2.50, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/6dcdd42a-a4e1-457f-a665-e66eae424b1e-retina-large-jpeg")
    db.session.add(item37)
    
    # Fries, Sides, and More
    item38 = Item(name="Apple Slices", description="(15 Cal.)", price=1.09, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/11616027-10b3-4d12-aab9-ea9f86666240-retina-large-jpeg")
    db.session.add(item38)

    # Sweets & Treats
    item39 = Item(name="Chocolate Shake", description="(520 Cal.)", price=3.09, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/95cbd3c9-6656-4fd2-af8c-8a5562ebb207-retina-large-jpeg")
    db.session.add(item39)
    
    item40 = Item(name="Strawberry Shake", description="(530 Cal.)", price=3.09, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/96ee505d-8f1b-4bc7-b9ad-aefc5fb151c1-retina-large-jpeg")
    db.session.add(item40)
    
    item41 = Item(name="M&M McFlurry", description="(420 Cal.)", price=3.49, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/09bb4bc1-c5fc-4a99-b3b4-445a7c1d33b5-retina-large-jpeg")
    db.session.add(item41)
    
    item42 = Item(name="Apple Pie", description="(230 Cal.)", price=1.79, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/58dc5072-93cd-42aa-8221-0d65c7f6d019-retina-large-jpeg")
    db.session.add(item42)
    
    # Beverages
    item43 = Item(name="Coke®", description="(150 Cal.)", price=1.39, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/150c813d-ea57-48cc-a6eb-e11d76dc8e57-retina-large.jpg")
    db.session.add(item43)
    
    item44 = Item(name="Diet Coke®", description="(0 Cal.)", price=1.25, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/4ed2e4b1-1b34-48db-b545-a9d1aa9d1764-retina-large.jpg")
    db.session.add(item44)
    
    item45 = Item(name="Dr Pepper®", description="(140 Cal.)", price=1.39, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/8de9f60f-2c6c-42cb-b169-2a07970a82a4-retina-large.jpg")
    db.session.add(item45)
    
    item46 = Item(name="Minute Maid® Orange Juice", description="(150 Cal.)", price=3.39, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/b2377684-b570-4b46-864a-4dab1b13be42-retina-large-jpeg")
    db.session.add(item46)
    
    item47 = Item(name="Dasani® Bottled Water", description="(0 Cal.)", price=2.59, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/31ba6fe2-51f9-4b66-aeef-4a86a21c7b00-retina-large-jpeg")
    db.session.add(item47)
    
    item48 = Item(name="Milk", description="(120 Cal.)", price=2.09, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/88c5903e-10d7-4d26-864c-008384fae497-retina-large-jpeg")
    db.session.add(item48)
    
    item49 = Item(name="Sweet Iced Tea", description="(170 Cal.)", price=1.25, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/ff74f476-f8a4-4e0f-a9f4-9a635b4c156f-retina-large-jpeg")
    db.session.add(item49)
    

    # Poki Time

    # Most Popular
    item50 = Item(name="Spicy Combo Poki Bowl", description="Half ahi tuna and half salmon marinated in our spicy mayo sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/bb85dbf9-fea4-4cac-82d4-642e54169ce6-retina-large.jpg")
    db.session.add(item50)

    item51 = Item(name="Original Combo Poki Bowl", description="Half ahi tuna and half salmon marinated in our original house sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/f4a6bdf0-d61f-496e-b2d1-4fdae17874bc-retina-large.jpg")
    db.session.add(item51)

    item52 = Item(name="Original Salmon Poki Bowl", description="Salmon marinated in our original house sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/e51a0e17-a2a2-423c-afb4-99eddabe8f86-retina-large.jpg")
    db.session.add(item52)

    item53 = Item(name="Spicy Salmon Poki Bowl", description="Salmon marinated in our spicy mayo sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/c493b7a6-c4c9-43a6-b12a-e439111dd5c3-retina-large.jpg")
    db.session.add(item53)

    item54 = Item(name="Poki Bowl and Drink Combo", description="Your choice of poki bowl with your choice of drink! We cannot make substitutions.", price=17.75, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/6c7f429f-5610-4ead-ad42-7c064a4e7112-retina-large.jpg")
    db.session.add(item54)

    item55 = Item(name="Poki Meal Combo", description="Make it a full meal with your choice of poki bowl, drink, and ice cream pint! We cannot make substitutions.", price=26.49, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/6914cd0a-50a2-4e4e-8a60-3e236293333b-retina-large.jpg")
    db.session.add(item55)

    # Poki Bowls
    item56 = Item(name="Original Ahi Tuna Poki Bowl", description="Ahi tuna marinated in our original house sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/60d3d15b-47e6-4e08-982f-62047c3f8cd1-retina-large.jpg")
    db.session.add(item56)

    item57 = Item(name="Spicy Ahi Tuna Poki Bowl", description="Ahi tuna marinated in our spicy mayo sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/70723679-bcfa-45c5-93d5-e2984d9a3dc6-retina-large.jpg")
    db.session.add(item57)

    # Humphry Slocombe Ice Cream
    item58 = Item(name="Black Sesame", description="Toasted black sesame seeds with sesame oil added for extra oomph. There’s no going back. Gluten-free. Contains dairy, eggs, and sesame seeds. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/7ae0bf79-add6-490e-b3de-84f15a75d198-retina-large.jpg")
    db.session.add(item58)

    item59 = Item(name="Hong Kong Milk Tea", description="Black tea ice cream made with housemade almond cookies. Made in partnership with Chef Melissa King. Contains gluten, eggs, dairy, and almonds. We cannot make substitutions.", price=10, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/1b75894c-15f7-4f2d-92ed-02a93b3c6e6a-retina-large.jpg")
    db.session.add(item59)

    item60 = Item(name="Matchadoodle", description="Housemade snickerdoodle cookies and the best green tea from Kyoto come together for an incredible flavor combination. Contains gluten, eggs, and dairy. We cannot make substitutions.", price=10, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/43293ab4-0a42-4e44-8128-babbadc9909a-retina-large.jpg")
    db.session.add(item60)

    item61 = Item(name="Secret Breakfast", description="Bourbon ice cream with housemade Cornflake cookies. Contains more than 0.5% of alcohol, as well as gluten, dairy, and eggs. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/e1b61246-31dd-4147-bc96-9cbe35ca74b0-retina-large.jpg")
    db.session.add(item61)

    item62 = Item(name="Honey Graham", description="Raw blackberry honey ice cream with house-made graham crackers folded in. Contains gluten, dairy, and eggs. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/ee883cc6-08cf-4080-a010-7fdc4fec8e79-retina-large.jpg")
    db.session.add(item62)

    # Van Leeuwen Ice Cream
    item63 = Item(name="Honeycomb", description="Nothing makes us happier than this Honeycomb Ice Cream. Despite being called honeycomb, it's not made from any honey at all. It’s made with housemade caramel candy. That all might seem confusing until you realize that ice cream is also made without ice. Your whole life has been a lie. Contains tree nuts, dairy, and eggs. We cannot make substitutions.", price=10, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/e5125ff8-9a89-41f1-859d-ab2af1b97939-retina-large.jpg")
    db.session.add(item63)

    item64 = Item(name="Mint Chip", description="Nothing makes us happier than this Mint Chip Ice Cream. We use single origin chocolate chips, so you can taste their true flavor profile. We add in a little pure peppermint extract and <chef’s kiss>. Contains dairy and eggs. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/9be10c05-a416-458f-9e92-9f64282efcc6-retina-large.jpg")
    db.session.add(item64)

    item65 = Item(name="Strawberry", description="Nothing makes us happier than this Strawberry Ice Cream. Oregon-grown strawberries. Delicately picked at peak ripeness. Then shoved in to a dark alley where fresh cream, egg yolks, and pure cane sugar get to work initiating strawberries in to the ice cream gang. Contains dairy and eggs. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/23a4583d-35c1-4132-853f-c3a8c41ea989-retina-large.jpg")
    db.session.add(item65)

    item66 = Item(name="Cookies and Cream", description="Nothing makes us happier than this Cookies & Cream Ice Cream. Nothing. Not children. Not dogs. Not rainbows. Nothing. Dark chocolate chip cookies + a rich cream filling + cold-ground vanilla bean ice cream = non-child, non-dog, non-rainbow happiness. Contains gluten, tree nuts, dairy, and eggs. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/e287bb57-28d4-471f-a5ba-c2278685404a-retina-large.jpg")
    db.session.add(item66)

    # Drinks
    item67 = Item(name="Topo Chico Mineral Water", description="12 oz glass bottle of sparkling mineral water. Bottled at the source in Monterrey, Mexico since 1895 with a natural mineral composition perfect for quenching thirst!", price=3.99, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/d1908724-cbea-4171-b31d-f776f3accb9d-retina-large.jpg")
    db.session.add(item67)

    item68 = Item(name="Mexican Coke", description="12 oz glass bottle of Coke, sweetened with real cane sugar.", price=3.99, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/84726d84-d3a1-484c-bd86-3ffb67997a3a-retina-large.jpg")
    db.session.add(item68)

    item69 = Item(name="La Colombe Coffee Draft Latte", description="9 oz can. Experience the full taste and texture of a true cold latte, complete with a frothy layer of silky foam. Made with real ingredients like nutrient-rich and lactose-free milk and two shots of espresso.", price=5.99, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/4a3b903e-1ba7-4801-95b1-a3659192dc24-retina-large.jpg")
    db.session.add(item69)

    item70 = Item(name="Dasani", description="16.9 oz bottle of Dasani's premium tasting, pure, and delicious water.", price=2.99, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/34407095-a71c-4780-8dd2-556cd4711fc4-retina-large.jpg")
    db.session.add(item70)


    # Tony's Pizza Napoletana

    # Popular
    item71 = Item(name="New Yorker", description="Mozzarella, hand crushed tomato sauce. Natural casing pepperoni, sliced Italian fennel sausage calabrese sausage, ricotta, chopped garlic, and oregano. (Gold Metal Winner Las Vegas 2013).", price=37, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/88d7768c-c906-4bcb-bf6d-ebce6d51fb0f-retina-large.jpg")
    db.session.add(item71)

    item72 = Item(name="Classic Pepperoni", description="", price=26, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/f7192f50-9521-4d6c-80f0-f34fbba193cc-retina-large-jpeg")
    db.session.add(item72)

    item73 = Item(name="Cheese", description="Vegetarian", price=35, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/c67c6f9a-5761-44c6-87bb-1e6679a67150-retina-large-jpeg")
    db.session.add(item73)

    item74 = Item(name="Caesar Salad", description="Caesar dressing with romaine, house croutons, Parmigiano, and white anchovies", price=15, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/172ae69e-cc6f-4f88-9b59-825012a588ea-retina-large-jpeg")
    db.session.add(item74)

    item75 = Item(name="Garlic Bread", description="", price=8, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/7b7ca99f-1b30-41a6-86a7-fa9e734b949c-retina-large-jpeg")
    db.session.add(item75)

    item76 = Item(name="Meatballs", description="Pecorino and parsley.", price=10.5, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/94c8b4e3-9852-4d02-ab96-7c1628d00b42-retina-large-jpeg")
    db.session.add(item76)

    # Sides
    item77 = Item(name="Gluten-Free Breadsticks", description="", price=7, restaurant_id=4,
        image_url="")
    db.session.add(item77)

    # Housemade Pasta
    item78 = Item(name="Pasta Genovese", description="Vegetarian. Linguini, pesto cream, goat cheese, sun-dried tomatoes and artichoke hearts.", price=27, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/bf2d4cff-9683-4383-a518-f379cb222912-retina-large-jpeg")
    db.session.add(item78)

    item79 = Item(name="Spaghetti & Meatballs", description="Pecorino and parsley.", price=28, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/3c3c1740-f875-4b37-bf62-c082e170ec6a-retina-large-jpeg")
    db.session.add(item79)

    # Classic American
    item80 = Item(name="Classic Cheese", description="Vegetarian", price=24, restaurant_id=4,
        image_url="")
    db.session.add(item80)

    item81 = Item(name="Classic Pepperoni", description="", price=26, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/f7192f50-9521-4d6c-80f0-f34fbba193cc-retina-large-jpeg")
    db.session.add(item81)

    item82 = Item(name="Jersey's Treton Tomato Pie", description="Vegetarian. Sliced mozzarella cheese, hand crushed tomato sauce, oregano, garlic, Parmigiana, and olive oil.", price=25.5, restaurant_id=4,
        image_url="")
    db.session.add(item82)

    item83 = Item(name="Picante", description="Mozzarella, garlic, pepperoni, linguica, calabrese peppers, serrano, and banana peppers, pork chorizo, green onions, cholula, and ricotta cheese.", price=30, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/10065f24-e2b1-4927-a002-506a61d93184-retina-large.jpg")
    db.session.add(item83)

    # Classic Italian
    item84 = Item(name="Cal Italia", description="Asiago, mozzarella, Italian Gorgonzola, croatian sweet fig preserve, prosciutto di parma, balsamic reduction, and no sauce. (gold medal winner food network pizza champions challenge).", price=31, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/c881a5ac-f6d6-470e-9f8b-f20af25a100a-retina-large.jpg")
    db.session.add(item84)

    item85 = Item(name="Prosciutto E Pomodorini", description="Mozzarella, prosciutto di parma, arugula, cherry tomatoes, and Parmesan cheese.", price=30, restaurant_id=4,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/d75a9c1d-6bd4-4963-bef8-9d43ad09ebd5-retina-large-jpeg")
    db.session.add(item85)

    # 20" NY
    item86 = Item(name="The Big Kahuna", description="Freshly sliced pineapple rings, bacon and ham.", price=39, restaurant_id=4,
        image_url="")
    db.session.add(item86)

    item87 = Item(name="Piccante", description="Chorizo, ￼garlic, green onions, cholula, ricotta, linguica, serrano, banana peppers, and pepperoni.", price=39, restaurant_id=4,
        image_url="")
    db.session.add(item87)

    # Wines
    item88 = Item(name="Alexander Valley Merlot", description="Aromas of black cherry compote and ripe plum are accentuated with hints of vanilla and cardamom.", price=22, restaurant_id=4,
        image_url="")
    db.session.add(item88)

    item89 = Item(name="Falanghina Iovine", description="This is the Italian varietal for all Chardonnay drinkers that want to try something new. Tropical fruit flavors, full bodied with a nice mineral finish", price=17, restaurant_id=4,
        image_url="")
    db.session.add(item89)

    item90 = Item(name="Nebbiolo Renato Ratti", description="With scents of strawberry and raspberry, this wine is pleasantly bitterish, velvety, at once, elegant and full.", price=26, restaurant_id=4,
        image_url="")
    db.session.add(item90)

    item91 = Item(name="Pinot Grigio Ketmeir", description="A dry, well-structured wine with ripe apple fruit flavors and good acidity.", price=19, restaurant_id=4,
        image_url="")
    db.session.add(item91)

    # KFC
    item92 = Item(name="4 pc. Chicken Combo", description="A Breast, Thigh, drum, & wing available in Original Recipe or Extra Crispy, 1 side of your choice, biscuit, and a medium drink. (1180-1890 cal.)", price=15.23, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/c57f97e3-5c41-4aac-875d-ace6915bc5b2-retina-large-jpeg")
    db.session.add(item92)

    item93 = Item(name="Famous Bowl", description="Creamy mashed potatoes, sweet corn and bite-sized chunks of crispy chicken are layered together then drizzled with home-style gravy and topped with a perfect blend of three shredded cheeses. (840-1120 cal.)", price=7.43, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/be55cd7b-cc00-4890-a70d-9e5b7fcea151-retina-large-png")
    db.session.add(item93)

    item94 = Item(name="Large Popcorn Nuggets", description="All white meat Popcorn Nuggets.(620-750 cal.)", price=7.43, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/6843f3bf-9ca8-4238-9378-640ad0d28735-retina-large-jpeg")
    db.session.add(item94)

    item95 = Item(name="Large Beverage", description="Select an ice-cold beverage. (0-430 cal.)", price=3.35, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/aaa41ffa-4dae-41a7-a830-7f1dd33a67d8-retina-large.jpg")
    db.session.add(item95)

    item96 = Item(name="8 Piece Meal", description="8 pieces of our freshly prepared chicken, available in Original Recipe or Extra Crispy, 2 large sides of your choice, and 4 biscuits. (2620-4980 cal.)", price=35.27, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/6fa8d90c-8d9d-4473-a832-d656fe2bc5c3-retina-large-jpeg")
    db.session.add(item96)

    item97 = Item(name="12 Piece Meal", description="12 pieces of our freshly prepared chicken, available in Original Recipe or Extra Crispy, 6 biscuits, and 3 large sides of your choice. (5090-9200 cal.)", price=46.31, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/3bc27f63-b139-4652-ae6a-4329a63da8f0-retina-large-png")
    db.session.add(item97)

    item98 = Item(name="16 Piece Meal", description="16 pieces of our freshly prepared chicken, available in Original Recipe or Extra Crispy, 8 biscuits, and 4 large sides of your choice. (6840-11880 cal.)", price=60.83, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/0438dbdf-763f-4464-9926-c40c7f7f1299-retina-large-png")
    db.session.add(item98)

    item99 = Item(name="6 Kentucky Fried Wings", description="6 Wings available in Honey BBQ, Buffalo, Nashville Hot or unsauced. Includes 1 Ranch dipping sauce. (500-880 cal.)", price=7.43, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/bae51586-d396-4b16-8d5b-db18727d79dc-retina-large.jpg")
    db.session.add(item99)

    item100 = Item(name="12 Kentucky Fried Wings", description="12 Wings available in Honey BBQ, Buffalo, Nashville Hot or unsauced. Includes 2 Ranch dipping sauces.(1000-1760 cal.)", price=14.75, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/40733e62-111d-4a55-8e39-712b71faf27f-retina-large-jpeg")
    db.session.add(item100)

    item101 = Item(name="24 Kentucky Fried Wings", description="24 Wings available in Honey BBQ, Buffalo, Nashville Hot or unsauced. Includes 4 Ranch dipping sauces. (2000-3250 cal.)", price=27.11, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/bae51586-d396-4b16-8d5b-db18727d79dc-retina-large.jpg")
    db.session.add(item101)

    item102 = Item(name="Fries", description="Crispier than your average fry and seasoned with our Secret Recipe. (230-930 cal.)", price=7.19, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/be72bdc5-75e8-4c81-8385-fe883aa285ea-retina-large-jpeg")
    db.session.add(item102)

    item103 = Item(name="Mashed Potatoes & Gravy", description="Creamy mashed potatoes and our signature brown gravy. (130-590 cal.)", price=7.19, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/df611672-ffef-4913-9eb2-4f818fcf5d77-retina-large-jpeg")
    db.session.add(item103)

    item104 = Item(name="Cole Slaw", description="Freshly prepared in restaurant with cabbage, carrots, onion, and our signature dressing. (170-640 cal.)", price=7.19, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/6cacb88e-154f-457e-b9ea-36ebca741134-retina-large-jpeg")
    db.session.add(item104)

    item105 = Item(name="Whole Kernel Corn", description="Sweet yellow corn.(70-280 cal.)", price=3.95, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/790da73f-4ed4-4614-8d8b-ea92e2aef809-retina-large-jpeg")
    db.session.add(item105)

    item106 = Item(name="Mac & Cheese", description="Elbow macaroni covered in a rich, creamy cheddar cheese sauce.", price=3.95, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/7760500d-200a-4de0-b527-ae0ac2a9983a-retina-large-jpeg")
    db.session.add(item106)

    item107 = Item(name="A La Carte Breast", description="1 Breast piece of our freshly prepared chicken, available in Original Recipe or Extra Crispy. (390-530 cal.)", price=4.86, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/f7c6becf-cccb-417d-8ad2-e6243d6ca75e-retina-large-jpeg")
    db.session.add(item107)

    item108 = Item(name="A La Carte Drum", description="1 Drum piece of our freshly prepared chicken, available in Original Recipe or Extra Crispy. (130-170 cal.)", price=3.06, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/4d671f99-2bbb-4c84-9ca3-9ad59e38a099-retina-large-jpeg")
    db.session.add(item108)

    item109 = Item(name="A La Carte Thigh", description="1 Thigh piece of our freshly prepared chicken, available in Original Recipe or Extra Crispy. (280-330 cal.)", price=3.66, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/bf19d137-0332-4134-a4d0-018fbb2956ee-retina-large-jpeg")
    db.session.add(item109)

    item110 = Item(name="A La Carte Wing", description="1 Wing piece of our freshly prepared chicken, available in Original Recipe or Extra Crispy. (130-170 cal.)", price=2.82, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/4e1b6f23-eeab-4f7c-9c65-55f30935c940-retina-large-jpeg")
    db.session.add(item110)

    item111 = Item(name="1/2 Gallon Beverage Bucket", description="Perfect for a group. Select a beverage. (0-880 cal.)", price=4.79, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/f9b32b4e-dd60-4007-9c42-658ac9da1584-retina-large.png")
    db.session.add(item111)

    item112 = Item(name="Medium Beverage", description="Select an ice-cold beverage. (0-280 cal.)", price=2.75, restaurant_id=5,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/bb85591c-05e6-4dc9-a514-9632680bad2d-retina-large-jpeg")
    db.session.add(item112)

    # Honey Honey
    item113 = Item(name="Two , Two and Two", description="Two eggs, two buttermilk, pancakes, and your choice of protein.", price=12.5, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/e0810ab2-9dcd-49fc-9817-cf4276b830c8-retina-large.jpg")
    db.session.add(item113)

    item114 = Item(name="Croissant Sandwich Breakfast", description="2 eggs scrambled with ham and Cheddar cheese in a warm croissant. Served with potatoes.", price=12.75, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/ea0b83a0-4a5a-449f-9bfd-7b13f064dc72-retina-large.jpg")
    db.session.add(item114)

    item115 = Item(name="French Toast Breakfast", description="3 thick slices of challah bread and served with fresh strawberries.", price=10.95, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/29621100-c1dd-49dd-9326-e0edbcfc8fe1-retina-large-jpeg")
    db.session.add(item115)

    item116 = Item(name="Eggs Benedict", description="2 poached eggs, Canadian bacon on an English muffin, topped with hollandaise sauce, and served with potatoes or fruit or salad.", price=13.95, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/19eef8f4-aaae-4a74-9890-498cc0150026-retina-large.jpg")
    db.session.add(item116)

    item117 = Item(name="Crab Cake Florentine", description="2 poached eggs, spinach, crab cake on an English muffin, topped with hollandaise sauce, and served with potatoes or fruit or salad.", price=14.95, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/e76ff93f-f741-432a-9d86-3dab50fd848b-retina-large.jpg")
    db.session.add(item117)

    item118 = Item(name="Salmon Benedict Breakfast", description="2 poached eggs, salmon, tomato, served on an English muffin, topped with hollandaise sauce, and served with potatoes or salad or fruit.", price=14.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/2b97e18c-1486-4c7a-a5cc-d80efd0ac6a6-retina-large-jpeg")
    db.session.add(item118)

    item119 = Item(name="Sunrise Burrito Breakfast", description="Flour tortoise, chorizo, onion, eggs, and Cheddar cheese. Served on bed of black beans with sour cream and cilantro topping.", price=12.95, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/cc5b9100-7752-405f-ba6d-cbd7d381aee4-retina-large.jpg")
    db.session.add(item119)

    item120 = Item(name="2 Eggs Any Style", description="", price=9.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/aeef0d48-b533-42e9-83a7-add14eecfa40-retina-large.jpg")
    db.session.add(item120)

    item121 = Item(name="Milano", description="Mozzarella, tomato, garlic and fresh basil.", price=12.95, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/c4944269-4875-4279-a2c0-4a0e2c767e57-retina-large-jpeg")
    db.session.add(item121)

    item122 = Item(name="Tofu Scramble", description="Eggs, smoked tofu, green pepper, onion and cilantro.", price=12.95, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/adc40018-72ab-45bd-af95-d9e172c51f93-retina-large.jpg")
    db.session.add(item122)

    item123 = Item(name="Acapulco", description="Cheddar, salsa, avocado, sour cream and black bean chili.", price=12.95, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/44c981ad-9973-485c-ae2c-6e1f89a0e5fc-retina-large-jpeg")
    db.session.add(item123)

    item124 = Item(name="Original", description="Cheddar and onion.", price=9.45, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/21d70717-a7ba-43b6-a140-79c7e379e630-retina-large.jpg")
    db.session.add(item124)

    item125 = Item(name="Pesto", description="Cheddar, tomato, spinach, pine nuts, cheese, pesto and avocado.", price=12.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/8548dfc2-2d61-4373-9ef7-a2d23b103b05-retina-large.jpg")
    db.session.add(item125)

    item126 = Item(name="New Orleans", description="Swiss cheese, chicken breast, mushroom, sundried tomato and salsa.", price=12.45, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/57150b3c-8f57-41d6-9054-e27989d8c349-retina-large.jpg")
    db.session.add(item126)

    item127 = Item(name="Salsa", description="Cheddar, onion, tomato, avocado, olives, salsa and sour cream.", price=12.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/043026ed-d365-490e-9e5a-0751b27d119c-retina-large-jpeg")
    db.session.add(item127)

    item128 = Item(name="Mediterranean", description="Cheddar, onion, tomato, feta, artichoke, olives and avocado.", price=12.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/f8c7f76d-f219-43c9-9b7f-a986743a57dc-retina-large.jpg")
    db.session.add(item128)

    item129 = Item(name="Almond Crescent", description="", price=1.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/ae4cbc8d-d28f-4d06-8012-e634dd89723b-retina-large-jpeg")
    db.session.add(item129)

    item130 = Item(name="SBK", description="Strawberry, banana, kiwi with cinnamon and brown sugar.", price=9, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/7ba1426f-24ab-4d41-b7d0-b86d2a6935fe-retina-large.jpg")
    db.session.add(item130)

    item131 = Item(name="Tuna", description="White albacore tuna, tomato, lettuce, sprout mustard and mayo.", price=13.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/5e3706dc-292c-425c-9f93-be8d8c944bad-retina-large.jpg")
    db.session.add(item131)

    item132 = Item(name="Crab Cake", description="Fresh crab cake, tomatoes, lettuce and mayo.", price=14.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/8d397ecd-e641-4367-ac16-0cbd5166c887-retina-large.jpg")
    db.session.add(item132)

    item133 = Item(name="Grilled Chicken", description="Chicken breast, tomato, lettuce, mozzarella cheese and pesto.", price=13.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/de4d4ddd-3eb4-4d1b-9f4e-e1d228aa4bf8-retina-large.jpg")
    db.session.add(item133)

    item134 = Item(name="Club", description="Smoked turkey, ham, bacon, tomato, lettuce and mayo.", price=13.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/5b058802-2df7-4254-87cc-44ff869c1be1-retina-large.jpg")
    db.session.add(item134)

    item135 = Item(name="Black Bean Chili", description="", price=3.95, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/fe8e6cf4-6684-47c2-8d4b-8178daed6f3f-retina-large-jpeg")
    db.session.add(item135)

    item136 = Item(name="Mexican", description="Chicken breast, black beans, corn torties, tomatoes, corn torties, cheddar cheese, sour cream, comes with its own dressing.", price=13.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/ded66326-cded-4f3a-9bac-341f4dbb94ab-retina-large.jpg")
    db.session.add(item136)

    item137 = Item(name="Caesar", description="Romaine lettuce, parmesan cheese and croutons.", price=11.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/6d287721-e3f8-4a2c-963c-66eb69cd5221-retina-large-jpeg")
    db.session.add(item137)

    item138 = Item(name="Rigatoni San Luca", description="Sundried tomato, chicken breast, tomato, garlic and fresh basil.", price=14.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/28277b41-020b-4c4f-8337-9a6b21cf5024-retina-large.jpg")
    db.session.add(item138)

    item139 = Item(name="Fettuccine", description="Tossed with mushroom and pesto or alfredo sauce.", price=14.45, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/ab107988-297d-4d1c-b21f-7455bfeacb47-retina-large-jpeg")
    db.session.add(item139)

    item140 = Item(name="Spaghetti Di Casa", description="Spaghetti with fresh tomato meat sauce.", price=14.25, restaurant_id=6,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/aacbad15-7291-499f-a92e-b30d0fe371ee-retina-large-jpeg")
    db.session.add(item140)

    db.session.commit()

def undo_items():
    db.session.execute('TRUNCATE items RESTART IDENTITY CASCADE;')
    db.session.commit()
