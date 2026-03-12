import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from restaurants.models import Restaurant, FoodItem
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def create_placeholder_image(filename, color=(200, 80, 80)):
    """Create a simple colored placeholder image"""
    img = Image.new('RGB', (300, 300), color=color)
    img_io = BytesIO()
    img.save(img_io, format='JPEG')
    img_io.seek(0)
    return ContentFile(img_io.read(), name=filename)

# Check if data exists, if not create it
if not Restaurant.objects.exists():
    print("Creating test data with images...")
    
    # Restaurant data
    restaurants_data = [
        {
            "name": "Pizza Palace",
            "location": "New York, NY",
            "rating": 4.5,
            "color": (210, 80, 60)  # Red/Orange
        },
        {
            "name": "Burger Barn",
            "location": "Los Angeles, CA",
            "rating": 4.7,
            "color": (220, 100, 50)  # Orange
        },
        {
            "name": "Sushi Supreme",
            "location": "San Francisco, CA",
            "rating": 4.8,
            "color": (100, 150, 200)  # Blue
        },
        {
            "name": "Taco Fiesta",
            "location": "Austin, TX",
            "rating": 4.6,
            "color": (200, 150, 50)  # Yellow/Brown
        },
    ]
    
    # Food items data
    food_items_data = {
        0: [  # Pizza Palace
            ("Margherita Pizza", 299),
            ("Pepperoni Pizza", 349),
            ("Vegetarian Pizza", 279),
        ],
        1: [  # Burger Barn
            ("Classic Burger", 199),
            ("Cheese Burger", 229),
            ("Deluxe Burger", 299),
        ],
        2: [  # Sushi Supreme
            ("California Roll", 349),
            ("Dragon Roll", 399),
            ("Salmon Sashimi", 449),
        ],
        3: [  # Taco Fiesta
            ("Beef Tacos", 199),
            ("Chicken Tacos", 179),
            ("Veggie Tacos", 159),
        ]
    }
    
    # Create restaurants with placeholder images
    restaurants = []
    for rest_data in restaurants_data:
        rest_name = rest_data['name']
        print(f"Creating {rest_name}...")
        
        restaurant = Restaurant.objects.create(
            name=rest_name,
            location=rest_data['location'],
            rating=rest_data['rating']
        )
        
        # Create and save placeholder image
        image_file = create_placeholder_image(
            f"restaurant_{rest_name.lower().replace(' ', '_')}.jpg",
            color=rest_data['color']
        )
        restaurant.image.save(
            f"restaurant_{rest_name.lower().replace(' ', '_')}.jpg",
            image_file,
            save=True
        )
        
        restaurants.append(restaurant)
    
    # Create food items with placeholder images
    total_items = 0
    for rest_idx, items in food_items_data.items():
        for item_name, price in items:
            print(f"  Creating {item_name}...")
            
            food_item = FoodItem.objects.create(
                restaurant=restaurants[rest_idx],
                name=item_name,
                price=price
            )
            
            # Create and save placeholder image with different color variations
            color_variants = [
                (200, 100, 80),   # Warm red
                (100, 180, 100),  # Green
                (150, 100, 200),  # Purple
            ]
            color = color_variants[total_items % len(color_variants)]
            
            image_file = create_placeholder_image(
                f"item_{item_name.lower().replace(' ', '_')}.jpg",
                color=color
            )
            food_item.image.save(
                f"item_{item_name.lower().replace(' ', '_')}.jpg",
                image_file,
                save=True
            )
            
            total_items += 1
    
    print(f"✓ Created {len(restaurants)} restaurants and {total_items} food items with images")
else:
    print("✓ Test data already exists")

print("Data seeding complete!")


