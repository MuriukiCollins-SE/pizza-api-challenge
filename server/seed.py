from server.app import db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from server.extensions import db

pizzas = [
    Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil"),
    Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni"),
    Pizza(name="Hawaiian", ingredients="Tomato, Mozzarella, Ham, Pineapple"),
    Pizza(name="Veggie", ingredients="Tomato, Mozzarella, Peppers, Onions, Mushrooms, Olives"),
    Pizza(name="BBQ Chicken", ingredients="BBQ Sauce, Mozzarella, Chicken, Red Onion, Cilantro"),
    Pizza(name="Four Cheese", ingredients="Mozzarella, Cheddar, Parmesan, Gorgonzola"),
    Pizza(name="Meat Lovers", ingredients="Tomato, Mozzarella, Pepperoni, Sausage, Ham, Bacon"),
    Pizza(name="Buffalo Chicken", ingredients="Buffalo Sauce, Mozzarella, Chicken, Blue Cheese"),
    Pizza(name="Mushroom", ingredients="Tomato, Mozzarella, Mushrooms, Garlic"),
    Pizza(name="Spinach Alfredo", ingredients="Alfredo Sauce, Mozzarella, Spinach, Garlic"),
    Pizza(name="Seafood", ingredients="Tomato, Mozzarella, Shrimp, Calamari, Garlic"),
    Pizza(name="Capricciosa", ingredients="Tomato, Mozzarella, Ham, Artichokes, Mushrooms, Olives"),
    Pizza(name="Diavola", ingredients="Tomato, Mozzarella, Spicy Salami, Chili Peppers"),
    Pizza(name="Prosciutto", ingredients="Tomato, Mozzarella, Prosciutto, Arugula"),
    Pizza(name="Truffle", ingredients="Truffle Oil, Mozzarella, Mushrooms, Parmesan"),
]

db.session.bulk_save_objects(pizzas)
db.session.commit()
print("Pizzas table populated!")

restaurants = [
    Restaurant(name="Demo Restaurant", address="Demo Address"),
    Restaurant(name="Pizza Palace", address="123 Main St"),
    Restaurant(name="Kiki's Pizza", address="456 Elm St"),
    Restaurant(name="Mama Mia", address="789 Oak Ave"),
    Restaurant(name="Slice of Heaven", address="321 Maple Rd"),
    Restaurant(name="The Italian Oven", address="654 Pine St"),
    Restaurant(name="Napoli Express", address="987 Cedar Blvd"),
    Restaurant(name="Cheesy Bites", address="246 Spruce Ln"),
    Restaurant(name="Urban Pie", address="135 Birch Dr"),
    Restaurant(name="Firehouse Pizza", address="864 Willow Ave"),
    Restaurant(name="Bella Roma", address="753 Aspen Ct"),
]

db.session.bulk_save_objects(restaurants)
db.session.commit()
print("Restaurants table populated!")