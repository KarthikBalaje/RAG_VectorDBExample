# ============================================================
#  Sample documents for the RAG / Vector DB demo
#  2 clearly different topics so we can see clusters in PCA
# ============================================================

DOCUMENTS = [

    # ── CARS (10 docs) ──────────────────────────────────────
    {
        "id": "car_001",
        "text": (
            "Electric vehicles (EVs) are revolutionizing the automotive industry with zero tailpipe emissions. "
            "Modern EVs like Tesla Model 3 can travel over 400 km on a single charge. "
            "Battery technology continues to improve, with solid-state batteries promising even greater range and faster charging times."
        ),
        "metadata": {
            "title": "Electric Vehicles",
            "category": "Cars",
            "source": "EV Today",
            "year": 2023,
        },
    },
    {
        "id": "car_002",
        "text": (
            "The internal combustion engine has powered automobiles for over a century. "
            "Modern engines use fuel injection, turbocharging, and advanced ignition systems to maximize efficiency. "
            "Despite declining market share, combustion engines remain the dominant powertrain globally."
        ),
        "metadata": {
            "title": "Internal Combustion Engines",
            "category": "Cars",
            "source": "Automotive Engineering Review",
            "year": 2023,
        },
    },
    {
        "id": "car_003",
        "text": (
            "Autonomous vehicles use advanced sensors like LIDAR, radar, and cameras to navigate without human input. "
            "Machine learning algorithms process sensor data in real-time to make driving decisions. "
            "Companies like Waymo and Cruise are testing fully autonomous taxis in urban environments."
        ),
        "metadata": {
            "title": "Autonomous Vehicles",
            "category": "Cars",
            "source": "Self-Driving News",
            "year": 2023,
        },
    },
    {
        "id": "car_004",
        "text": (
            "Active safety systems in modern cars prevent accidents before they happen. "
            "Anti-lock braking (ABS), electronic stability control (ESC), and automatic emergency braking work together. "
            "These systems have reduced accident rates by up to 40% since their introduction."
        ),
        "metadata": {
            "title": "Active Safety Features",
            "category": "Cars",
            "source": "NHTSA Safety Database",
            "year": 2023,
        },
    },
    {
        "id": "car_005",
        "text": (
            "Luxury automobiles from brands like Rolls-Royce, Ferrari, and Lamborghini represent the pinnacle of automotive engineering. "
            "These cars feature hand-crafted interiors, exotic materials, and bespoke customization options. "
            "Some models command prices exceeding $1 million due to their exclusivity and performance."
        ),
        "metadata": {
            "title": "Luxury Cars",
            "category": "Cars",
            "source": "Luxury Auto Magazine",
            "year": 2023,
        },
    },
    {
        "id": "car_006",
        "text": (
            "Performance cars are engineered for speed and handling precision. "
            "The Bugatti Chiron holds the production car speed record at 490 km/h. "
            "Advanced aerodynamics, lightweight materials, and high-horsepower engines enable these extraordinary capabilities."
        ),
        "metadata": {
            "title": "Performance Cars",
            "category": "Cars",
            "source": "Top Gear",
            "year": 2023,
        },
    },
    {
        "id": "car_007",
        "text": (
            "Car maintenance is essential for longevity and safety. "
            "Regular oil changes, tire rotations, brake inspections, and filter replacements keep vehicles running smoothly. "
            "Preventive maintenance costs far less than emergency repairs from neglected upkeep."
        ),
        "metadata": {
            "title": "Car Maintenance",
            "category": "Cars",
            "source": "Mechanic's Handbook",
            "year": 2022,
        },
    },
    {
        "id": "car_008",
        "text": (
            "Fuel efficiency is measured in kilometers per liter (km/l) and depends on engine design and driving habits. "
            "Hybrid vehicles combine gasoline and electric power to achieve exceptional efficiency. "
            "Aerodynamic design, lightweight materials, and efficient transmissions all contribute to better fuel economy."
        ),
        "metadata": {
            "title": "Fuel Efficiency",
            "category": "Cars",
            "source": "Green Driving Guide",
            "year": 2023,
        },
    },
    {
        "id": "car_009",
        "text": (
            "The history of the automobile spans from Karl Benz's 1885 motorwagen to today's connected vehicles. "
            "The assembly line revolutionized production, making cars affordable for the masses. "
            "Today's cars are computers with wheels, featuring advanced infotainment and driver assistance systems."
        ),
        "metadata": {
            "title": "History of Automobiles",
            "category": "Cars",
            "source": "Auto History Archives",
            "year": 2022,
        },
    },
    {
        "id": "car_010",
        "text": (
            "Car transmission systems convert engine power into wheel rotation. "
            "Manual transmissions offer driver control but require skill; automatic transmissions provide convenience. "
            "Continuously variable transmissions (CVT) and dual-clutch systems optimize efficiency for different driving conditions."
        ),
        "metadata": {
            "title": "Transmission Systems",
            "category": "Cars",
            "source": "Automotive Technology Journal",
            "year": 2023,
        },
    },
    {
        "id": "car_011",
        "text": (
            "SUVs and crossovers dominate the global automotive market, accounting for over 40% of sales. "
            "These vehicles combine car comfort with truck practicality and higher seating positions. "
            "Modern SUVs offer all-wheel drive, advanced infotainment systems, and spacious interiors for families."
        ),
        "metadata": {
            "title": "SUVs and Crossovers",
            "category": "Cars",
            "source": "Auto Sales Report",
            "year": 2023,
        },
    },
    {
        "id": "car_012",
        "text": (
            "Compact cars are designed for urban environments and fuel efficiency. "
            "They feature tight turning radiuses, easier parking in crowded spaces, and excellent maneuverability. "
            "Despite smaller dimensions, modern compact cars offer comfortable interiors and surprisingly spacious cargo areas."
        ),
        "metadata": {
            "title": "Compact Cars",
            "category": "Cars",
            "source": "Urban Mobility Magazine",
            "year": 2023,
        },
    },
    {
        "id": "car_013",
        "text": (
            "Sedan vehicles are the traditional passenger car choice, offering balanced comfort and performance. "
            "With four doors and an enclosed trunk, sedans provide practicality for daily commuting and long trips. "
            "Modern sedans feature sophisticated suspension systems and advanced driver assistance technologies."
        ),
        "metadata": {
            "title": "Sedan Vehicles",
            "category": "Cars",
            "source": "Automotive Weekly",
            "year": 2023,
        },
    },
    {
        "id": "car_014",
        "text": (
            "Pickup trucks offer exceptional cargo capacity and towing capability for work and recreation. "
            "Modern trucks feature advanced trailering systems, reinforced suspension, and powerful engines. "
            "Truck beds can carry thousands of kilograms of payload, making them essential for construction and agriculture."
        ),
        "metadata": {
            "title": "Pickup Trucks",
            "category": "Cars",
            "source": "Truck & SUV Report",
            "year": 2023,
        },
    },
    {
        "id": "car_015",
        "text": (
            "Classic and vintage cars represent automotive history and engineering evolution. "
            "Vehicles from the 1960s and earlier feature mechanical simplicity and distinctive design aesthetics. "
            "Enthusiasts restore and preserve classic cars, maintaining them as rolling museums of automotive heritage."
        ),
        "metadata": {
            "title": "Classic Cars",
            "category": "Cars",
            "source": "Classic Auto Registry",
            "year": 2022,
        },
    },
    {
        "id": "car_016",
        "text": (
            "Sports cars represent the pinnacle of performance and engineering excellence. "
            "With 0-100 km/h times under 5 seconds and top speeds exceeding 300 km/h, they push automotive limits. "
            "Advanced suspension, track-focused tuning, and aggressive aerodynamics define the sports car category."
        ),
        "metadata": {
            "title": "Sports Cars",
            "category": "Cars",
            "source": "Performance Automotive",
            "year": 2023,
        },
    },
    {
        "id": "car_017",
        "text": (
            "Family cars prioritize safety, comfort, and practicality for households with children. "
            "They feature ample seating for five to seven passengers, advanced safety ratings, and multiple storage compartments. "
            "Minivans and three-row SUVs exemplify this category with sliding doors and modular interiors."
        ),
        "metadata": {
            "title": "Family Cars",
            "category": "Cars",
            "source": "Family Automotive Guide",
            "year": 2023,
        },
    },
    {
        "id": "car_018",
        "text": (
            "Eco-friendly vehicles minimize environmental impact through efficient engines and sustainable materials. "
            "Hybrid, plug-in hybrid, and fully electric vehicles reduce emissions compared to conventional cars. "
            "Government incentives encourage adoption of eco-friendly vehicles to combat climate change."
        ),
        "metadata": {
            "title": "Eco-Friendly Vehicles",
            "category": "Cars",
            "source": "Green Mobility Weekly",
            "year": 2023,
        },
    },
    {
        "id": "car_019",
        "text": (
            "NHTSA crash tests evaluate vehicle safety through front, side, and rollover tests. "
            "Five-star ratings indicate excellent protection in collisions, while multiple airbags and crumple zones absorb impact. "
            "Modern cars achieve a five-star rating by exceeding stringent safety requirements."
        ),
        "metadata": {
            "title": "Vehicle Safety Ratings",
            "category": "Cars",
            "source": "NHTSA Safety Reports",
            "year": 2023,
        },
    },
    {
        "id": "car_020",
        "text": (
            "Airbag systems deploy in milliseconds during collisions to protect passengers from impact injuries. "
            "Modern vehicles contain 10-15 airbags strategically placed around the cabin. "
            "Combined with seatbelts and crumple zones, airbags reduce serious injury rates by over 50%."
        ),
        "metadata": {
            "title": "Airbag Systems",
            "category": "Cars",
            "source": "Safety Technology Journal",
            "year": 2023,
        },
    },
    {
        "id": "car_021",
        "text": (
            "Engine displacement, measured in cubic centimeters (cc) or liters, indicates engine size and power potential. "
            "A 3.0-liter engine has three times the displacement of a 1.0-liter engine. "
            "Larger displacement typically means more power but reduced fuel efficiency unless paired with advanced technologies."
        ),
        "metadata": {
            "title": "Engine Displacement",
            "category": "Cars",
            "source": "Engine Specifications Database",
            "year": 2023,
        },
    },
    {
        "id": "car_022",
        "text": (
            "Turbocharging forces compressed air into the engine, increasing power without enlarging engine displacement. "
            "Modern turbochargers feature variable geometry and intercoolers to optimize performance and efficiency. "
            "Turbocharged engines provide superb torque delivery and responsiveness at various RPM ranges."
        ),
        "metadata": {
            "title": "Turbocharging Technology",
            "category": "Cars",
            "source": "Engine Modification Journal",
            "year": 2023,
        },
    },
    {
        "id": "car_023",
        "text": (
            "Hybrid powertrains combine gasoline engines with electric motors to maximize efficiency. "
            "The system seamlessly switches between power sources, capturing energy during braking. "
            "Hybrids achieve 30-50% better fuel economy than comparable conventional vehicles."
        ),
        "metadata": {
            "title": "Hybrid Technology",
            "category": "Cars",
            "source": "Green Engineering Review",
            "year": 2023,
        },
    },
    {
        "id": "car_024",
        "text": (
            "All-wheel drive (AWD) systems distribute power to all four wheels for enhanced traction and control. "
            "AWD excels in snow, rain, and off-road conditions by automatically adjusting power distribution. "
            "Modern AWD systems use electronic controls and limited-slip differentials for optimal performance."
        ),
        "metadata": {
            "title": "All-Wheel Drive Systems",
            "category": "Cars",
            "source": "Drivetrain Technology Guide",
            "year": 2023,
        },
    },
    {
        "id": "car_025",
        "text": (
            "Car insurance protects against financial losses from accidents, theft, and damages. "
            "Comprehensive coverage includes collision protection, theft coverage, and liability insurance. "
            "Insurance premiums depend on vehicle type, driver history, location, and coverage levels."
        ),
        "metadata": {
            "title": "Car Insurance",
            "category": "Cars",
            "source": "Insurance Industry Report",
            "year": 2023,
        },
    },

    # ── BIKES (10 docs) ─────────────────────────────────────
    {
        "id": "bike_001",
        "text": (
            "Mountain bikes are designed for off-road terrain with wide, knobby tires for traction. "
            "Full-suspension models absorb impact from rough surfaces, while hardtails are lighter and more efficient on climbs. "
            "Disc brakes provide superior stopping power in muddy and wet conditions."
        ),
        "metadata": {
            "title": "Mountain Bikes",
            "category": "Bikes",
            "source": "Mountain Bike Journal",
            "year": 2023,
        },
    },
    {
        "id": "bike_002",
        "text": (
            "Road bikes feature lightweight frames and thin, high-pressure tires for speed on pavement. "
            "Drop handlebars allow riders to assume an aerodynamic position, reducing wind resistance. "
            "These bikes excel at long-distance riding and racing on smooth road surfaces."
        ),
        "metadata": {
            "title": "Road Bikes",
            "category": "Bikes",
            "source": "Cycling Weekly",
            "year": 2023,
        },
    },
    {
        "id": "bike_003",
        "text": (
            "Electric bikes (e-bikes) combine pedal power with motor assistance for easier riding. "
            "Lithium-ion batteries provide 30-100 km of range depending on terrain and assistance level. "
            "E-bikes are transforming urban commuting, making cycling accessible to more people regardless of fitness level."
        ),
        "metadata": {
            "title": "Electric Bikes",
            "category": "Bikes",
            "source": "E-Bike Today",
            "year": 2023,
        },
    },
    {
        "id": "bike_004",
        "text": (
            "Bicycle maintenance ensures safety and performance. "
            "Regular chain lubrication, brake adjustments, tire pressure checks, and derailleur tuning are essential. "
            "A well-maintained bike can last decades and provides reliable transportation and recreation."
        ),
        "metadata": {
            "title": "Bike Maintenance",
            "category": "Bikes",
            "source": "Bike Mechanic's Guide",
            "year": 2023,
        },
    },
    {
        "id": "bike_005",
        "text": (
            "Cycling provides excellent cardiovascular benefits and builds muscle strength throughout the body. "
            "Regular cycling reduces heart disease risk, improves mental health, and builds endurance. "
            "It's a low-impact exercise suitable for all ages and can be enjoyed recreationally or competitively."
        ),
        "metadata": {
            "title": "Health Benefits of Cycling",
            "category": "Bikes",
            "source": "Sports Medicine Review",
            "year": 2023,
        },
    },
    {
        "id": "bike_006",
        "text": (
            "Motorcycles range from efficient commuter bikes to powerful sports bikes capable of 300+ km/h. "
            "Modern motorcycles feature advanced fuel injection, ABS braking, and traction control systems. "
            "Lightweight construction and high power-to-weight ratios make motorcycles thrilling and fuel-efficient."
        ),
        "metadata": {
            "title": "Motorcycles",
            "category": "Bikes",
            "source": "Motorcycle Enthusiast",
            "year": 2023,
        },
    },
    {
        "id": "bike_007",
        "text": (
            "Racing bikes are optimized for competitive cycling events and speed records. "
            "Professional race bikes weigh under 6.8 kg and feature cutting-edge materials like carbon fiber. "
            "Every component is engineered for aerodynamics, responsiveness, and minimal weight."
        ),
        "metadata": {
            "title": "Racing Bikes",
            "category": "Bikes",
            "source": "Pro Cycling Insider",
            "year": 2023,
        },
    },
    {
        "id": "bike_008",
        "text": (
            "Hybrid bikes combine features of road and mountain bikes for versatile performance. "
            "Upright seating positions and medium-width tires make them comfortable for casual riding. "
            "They're ideal for commuters who encounter mixed terrain including roads and light trails."
        ),
        "metadata": {
            "title": "Hybrid Bikes",
            "category": "Bikes",
            "source": "Bike Buyer's Guide",
            "year": 2023,
        },
    },
    {
        "id": "bike_009",
        "text": (
            "Bike safety requires proper equipment and awareness. "
            "Helmets reduce head injury risk by 85%; lights and reflectors increase visibility; and defensive riding techniques prevent accidents. "
            "Following traffic laws and wearing bright clothing significantly improves cyclist safety on roads."
        ),
        "metadata": {
            "title": "Bike Safety",
            "category": "Bikes",
            "source": "Road Safety Foundation",
            "year": 2023,
        },
    },
    {
        "id": "bike_010",
        "text": (
            "Motorcycle engines range from efficient singles to high-performance V4s and inline-6s. "
            "Advanced cooling systems, variable valve timing, and fuel injection maximize power and efficiency. "
            "Modern motorcycle engines combine reliability with thrilling performance characteristics."
        ),
        "metadata": {
            "title": "Motorcycle Engines",
            "category": "Bikes",
            "source": "Engine Technology Journal",
            "year": 2023,
        },
    },
    {
        "id": "bike_011",
        "text": (
            "BMX bikes are designed for trick riding and stunts with small, sturdy frames and single-speed drivetrains. "
            "Reinforced wheels and components withstand the impacts of landing tricks. "
            "BMX riders perform in competitions, street riding, and professional tours worldwide."
        ),
        "metadata": {
            "title": "BMX Bikes",
            "category": "Bikes",
            "source": "Action Sports Magazine",
            "year": 2023,
        },
    },
    {
        "id": "bike_012",
        "text": (
            "Cruiser bikes offer relaxed, upright geometry for comfortable casual riding. "
            "Wide, cushioned seats and swept-back handlebars reduce strain during leisurely rides. "
            "Cruisers are ideal for beach rides, neighborhood commuting, and social cycling."
        ),
        "metadata": {
            "title": "Cruiser Bikes",
            "category": "Bikes",
            "source": "Casual Cycling Guide",
            "year": 2023,
        },
    },
    {
        "id": "bike_013",
        "text": (
            "Touring bikes are built for long-distance travel with reinforced frames and racks for cargo. "
            "Drop bars and varied gearing allow efficient pedaling on different terrain. "
            "Touring cyclists traverse continents carrying camping gear and supplies."
        ),
        "metadata": {
            "title": "Touring Bikes",
            "category": "Bikes",
            "source": "Adventure Cycling Journal",
            "year": 2023,
        },
    },
    {
        "id": "bike_014",
        "text": (
            "Fixed-gear bikes have a direct drive with no freewheel, requiring continuous pedaling while moving. "
            "Riders control speed through pedaling cadence and use skidding for braking. "
            "Fixed-gear bikes offer a pure, minimalist riding experience popular in urban cycling."
        ),
        "metadata": {
            "title": "Fixed-Gear Bikes",
            "category": "Bikes",
            "source": "Urban Cycling Culture",
            "year": 2023,
        },
    },
    {
        "id": "bike_015",
        "text": (
            "Cargo bikes transport goods and children with large cargo boxes or platforms. "
            "Heavy-duty frames and low-speed gearing manage the extra weight effectively. "
            "Cargo bikes reduce vehicle emissions for urban delivery and family transportation."
        ),
        "metadata": {
            "title": "Cargo Bikes",
            "category": "Bikes",
            "source": "Sustainable Transport Weekly",
            "year": 2023,
        },
    },
    {
        "id": "bike_016",
        "text": (
            "Gravel bikes combine road bike speed with mountain bike capability for mixed terrain. "
            "Wider tires provide traction on gravel and dirt while maintaining efficiency on pavement. "
            "Gravel biking is a rapidly growing discipline connecting road and off-road riding."
        ),
        "metadata": {
            "title": "Gravel Bikes",
            "category": "Bikes",
            "source": "Gravel Cycling Report",
            "year": 2023,
        },
    },
    {
        "id": "bike_017",
        "text": (
            "Track bikes are engineered for velodrome racing with fixed gears and aerodynamic frames. "
            "Extremely lightweight construction and aggressive geometry maximize speed. "
            "Track cyclists achieve speeds exceeding 70 km/h during sprint events."
        ),
        "metadata": {
            "title": "Track Bikes",
            "category": "Bikes",
            "source": "Olympic Cycling Federation",
            "year": 2023,
        },
    },
    {
        "id": "bike_018",
        "text": (
            "Freestyle bikes are built for tricks, stunts, and acrobatic maneuvers in skate parks. "
            "Reinforced frames, pegs for grinding, and smooth tires enable complex tricks. "
            "Professional freestyle cyclists perform incredible aerial maneuvers and combinations."
        ),
        "metadata": {
            "title": "Freestyle Bikes",
            "category": "Bikes",
            "source": "Trick Sports Network",
            "year": 2023,
        },
    },
    {
        "id": "bike_019",
        "text": (
            "Bike frames are constructed from aluminum, steel, carbon fiber, or titanium materials. "
            "Carbon fiber offers superior weight-to-strength ratio; steel provides durability and comfort. "
            "Frame geometry affects handling, stability, and aerodynamics for different riding styles."
        ),
        "metadata": {
            "title": "Bike Frame Materials",
            "category": "Bikes",
            "source": "Frame Engineering Handbook",
            "year": 2023,
        },
    },
    {
        "id": "bike_020",
        "text": (
            "Gearing systems use chainrings and sprockets to optimize pedaling efficiency across speeds. "
            "Single-speed bikes offer simplicity; multi-speed systems provide 21-33 different gear combinations. "
            "Modern shifters enable smooth, precise gear changes with single-finger inputs."
        ),
        "metadata": {
            "title": "Gearing Systems",
            "category": "Bikes",
            "source": "Drivetrain Technology Guide",
            "year": 2023,
        },
    },
    {
        "id": "bike_021",
        "text": (
            "Brake types include rim brakes that squeeze the wheel rim and disc brakes that grip a rotor. "
            "Disc brakes provide superior stopping power in wet and muddy conditions. "
            "Mechanical, hydraulic, and electronic actuation systems offer varying levels of modulation and power."
        ),
        "metadata": {
            "title": "Brake Types",
            "category": "Bikes",
            "source": "Bicycle Component Guide",
            "year": 2023,
        },
    },
    {
        "id": "bike_022",
        "text": (
            "Tire technology includes tread patterns optimized for different surfaces and conditions. "
            "Slick tires minimize rolling resistance on pavement; knobbly tires provide traction on dirt. "
            "Tire pressure affects comfort, efficiency, and grip, requiring regular monitoring."
        ),
        "metadata": {
            "title": "Tire Technology",
            "category": "Bikes",
            "source": "Tire Science Journal",
            "year": 2023,
        },
    },
    {
        "id": "bike_023",
        "text": (
            "Pedal systems range from platform pedals to clipless systems that mechanically secure cycling shoes. "
            "Clipless pedals enable efficient power transfer and prevent foot slipping during intense efforts. "
            "Different pedal types suit various riding styles from casual to competitive racing."
        ),
        "metadata": {
            "title": "Pedal Systems",
            "category": "Bikes",
            "source": "Cyclist Equipment Review",
            "year": 2023,
        },
    },
    {
        "id": "bike_024",
        "text": (
            "Bike ergonomics optimize rider comfort and performance through proper frame sizing and adjustment. "
            "Correct saddle height, handlebar reach, and stem length prevent injuries and improve efficiency. "
            "Professional bike fitting analyzes body measurements and riding style for customized positioning."
        ),
        "metadata": {
            "title": "Bike Ergonomics",
            "category": "Bikes",
            "source": "Sports Medicine and Cycling",
            "year": 2023,
        },
    },
    {
        "id": "bike_025",
        "text": (
            "Bike accessories enhance comfort, safety, and functionality during rides. "
            "Essential items include helmets, lights, mirrors, bells, locks, and fenders. "
            "Advanced accessories like GPS computers, action cameras, and electronic shifting systems expand capabilities."
        ),
        "metadata": {
            "title": "Bike Accessories",
            "category": "Bikes",
            "source": "Cycling Accessory Guide",
            "year": 2023,
        },
    },
]

CATEGORIES = ["Cars", "Bikes"]
