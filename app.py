import streamlit as st
import random

# ==========================================
# 1. THE 100-QUESTION BANK
# ==========================================
QUIZ_BANK = [
    # --- CAPITALS (30 Questions) ---
    {"question": "What is the capital of California?", "options": ["Sacramento", "Los Angeles", "San Francisco", "San Diego"], "answer": "Sacramento", "fact": "Sacramento became the capital in 1854."},
    {"question": "What is the capital of Texas?", "options": ["Austin", "Houston", "Dallas", "San Antonio"], "answer": "Austin", "fact": "Austin is known as the Live Music Capital of the World."},
    {"question": "What is the capital of New York?", "options": ["Albany", "New York City", "Buffalo", "Rochester"], "answer": "Albany", "fact": "Albany is one of the oldest surviving settlements in the original thirteen colonies."},
    {"question": "What is the capital of Florida?", "options": ["Tallahassee", "Miami", "Orlando", "Jacksonville"], "answer": "Tallahassee", "fact": "Tallahassee was chosen as the capital because it was halfway between Pensacola and St. Augustine."},
    {"question": "What is the capital of Illinois?", "options": ["Springfield", "Chicago", "Peoria", "Naperville"], "answer": "Springfield", "fact": "Abraham Lincoln lived in Springfield from 1837 until 1861."},
    {"question": "What is the capital of Pennsylvania?", "options": ["Harrisburg", "Philadelphia", "Pittsburgh", "Erie"], "answer": "Harrisburg", "fact": "Harrisburg played a notable role in the American Civil War."},
    {"question": "What is the capital of Ohio?", "options": ["Columbus", "Cleveland", "Cincinnati", "Toledo"], "answer": "Columbus", "fact": "Columbus is the most populous city in Ohio."},
    {"question": "What is the capital of Michigan?", "options": ["Lansing", "Detroit", "Grand Rapids", "Ann Arbor"], "answer": "Lansing", "fact": "Lansing is the only U.S. state capital located in a township of the same name."},
    {"question": "What is the capital of Georgia?", "options": ["Atlanta", "Savannah", "Augusta", "Athens"], "answer": "Atlanta", "fact": "Atlanta hosted the 1996 Summer Olympics."},
    {"question": "What is the capital of North Carolina?", "options": ["Raleigh", "Charlotte", "Durham", "Greensboro"], "answer": "Raleigh", "fact": "Raleigh is known as the 'City of Oaks'."},
    {"question": "What is the capital of Massachusetts?", "options": ["Boston", "Worcester", "Springfield", "Cambridge"], "answer": "Boston", "fact": "Boston is one of the oldest municipalities in the United States."},
    {"question": "What is the capital of Arizona?", "options": ["Phoenix", "Tucson", "Mesa", "Scottsdale"], "answer": "Phoenix", "fact": "Phoenix is the only state capital with a population over 1 million people."},
    {"question": "What is the capital of Washington?", "options": ["Olympia", "Seattle", "Spokane", "Tacoma"], "answer": "Olympia", "fact": "Olympia is located at the southern end of Puget Sound."},
    {"question": "What is the capital of Colorado?", "options": ["Denver", "Colorado Springs", "Aurora", "Boulder"], "answer": "Denver", "fact": "Denver is exactly one mile above sea level."},
    {"question": "What is the capital of Tennessee?", "options": ["Nashville", "Memphis", "Knoxville", "Chattanooga"], "answer": "Nashville", "fact": "Nashville is the center of the country music industry."},
    {"question": "What is the capital of Missouri?", "options": ["Jefferson City", "Kansas City", "St. Louis", "Springfield"], "answer": "Jefferson City", "fact": "Jefferson City was named after Thomas Jefferson."},
    {"question": "What is the capital of Maryland?", "options": ["Annapolis", "Baltimore", "Frederick", "Rockville"], "answer": "Annapolis", "fact": "Annapolis served as the temporary capital of the US in 1783–1784."},
    {"question": "What is the capital of Wisconsin?", "options": ["Madison", "Milwaukee", "Green Bay", "Kenosha"], "answer": "Madison", "fact": "Madison is built on an isthmus between Lake Mendota and Lake Monona."},
    {"question": "What is the capital of Minnesota?", "options": ["Saint Paul", "Minneapolis", "Duluth", "Rochester"], "answer": "Saint Paul", "fact": "Saint Paul and Minneapolis are known as the 'Twin Cities'."},
    {"question": "What is the capital of Louisiana?", "options": ["Baton Rouge", "New Orleans", "Shreveport", "Lafayette"], "answer": "Baton Rouge", "fact": "Baton Rouge means 'Red Stick' in French."},
    {"question": "What is the capital of Alabama?", "options": ["Montgomery", "Birmingham", "Mobile", "Huntsville"], "answer": "Montgomery", "fact": "Montgomery was the first capital of the Confederacy."},
    {"question": "What is the capital of Kentucky?", "options": ["Frankfort", "Louisville", "Lexington", "Bowling Green"], "answer": "Frankfort", "fact": "Frankfort is bisected by the Kentucky River."},
    {"question": "What is the capital of Oregon?", "options": ["Salem", "Portland", "Eugene", "Bend"], "answer": "Salem", "fact": "The Oregon State Capitol building is topped by a gold-leaf pioneer statue."},
    {"question": "What is the capital of Oklahoma?", "options": ["Oklahoma City", "Tulsa", "Norman", "Broken Arrow"], "answer": "Oklahoma City", "fact": "It is one of the few capitals that shares its name with the state."},
    {"question": "What is the capital of Connecticut?", "options": ["Hartford", "Bridgeport", "New Haven", "Stamford"], "answer": "Hartford", "fact": "Hartford is often called the 'Insurance Capital of the World'."},
    {"question": "What is the capital of Utah?", "options": ["Salt Lake City", "Provo", "West Valley City", "Orem"], "answer": "Salt Lake City", "fact": "It was founded in 1847 by Brigham Young and Mormon followers."},
    {"question": "What is the capital of Nevada?", "options": ["Carson City", "Las Vegas", "Reno", "Henderson"], "answer": "Carson City", "fact": "Carson City is an independent city, not part of any county."},
    {"question": "What is the capital of Arkansas?", "options": ["Little Rock", "Fort Smith", "Fayetteville", "Springdale"], "answer": "Little Rock", "fact": "Named for a rock formation on the Arkansas River."},
    {"question": "What is the capital of Mississippi?", "options": ["Jackson", "Gulfport", "Biloxi", "Hattiesburg"], "answer": "Jackson", "fact": "The city sits atop an extinct volcano."},
    {"question": "What is the capital of Kansas?", "options": ["Topeka", "Wichita", "Overland Park", "Kansas City"], "answer": "Topeka", "fact": "Topeka means 'a good place to dig potatoes' in Kansa-Osage."},

    # --- NATIONAL PARKS LOCATIONS (25 Questions) ---
    {"question": "In which state is Yosemite National Park located?", "options": ["California", "Wyoming", "Montana", "Colorado"], "answer": "California", "fact": "Yosemite is famous for its giant sequoia trees and Bridalveil Fall."},
    {"question": "In which state is Yellowstone National Park primarily located?", "options": ["Wyoming", "Montana", "Idaho", "Utah"], "answer": "Wyoming", "fact": "96% of the park is in Wyoming, 3% in Montana, and 1% in Idaho."},
    {"question": "Where is the Grand Canyon located?", "options": ["Arizona", "Nevada", "New Mexico", "Utah"], "answer": "Arizona", "fact": "The canyon is 277 miles long and up to 18 miles wide."},
    {"question": "Acadia National Park is located in which state?", "options": ["Maine", "Vermont", "New Hampshire", "Massachusetts"], "answer": "Maine", "fact": "Acadia was the first National Park created from private lands gifted to the public."},
    {"question": "Zion National Park is a famous landmark in which state?", "options": ["Utah", "Colorado", "Arizona", "Nevada"], "answer": "Utah", "fact": "Zion Canyon is 15 miles long and up to half a mile deep."},
    {"question": "Where would you find Glacier National Park?", "options": ["Montana", "Alaska", "Washington", "Idaho"], "answer": "Montana", "fact": "It borders Waterton Lakes National Park in Canada."},
    {"question": "Great Smoky Mountains National Park straddles the border of Tennessee and which other state?", "options": ["North Carolina", "Kentucky", "Virginia", "Georgia"], "answer": "North Carolina", "fact": "It is the most biodiverse park in the US system."},
    {"question": "Which state is home to Denali National Park?", "options": ["Alaska", "Washington", "Oregon", "Montana"], "answer": "Alaska", "fact": "It contains Denali, the highest mountain peak in North America."},
    {"question": "Everglades National Park is located in:", "options": ["Florida", "Louisiana", "Georgia", "Alabama"], "answer": "Florida", "fact": "It is the largest tropical wilderness in the US."},
    {"question": "Arches National Park, famous for over 2,000 natural stone arches, is in:", "options": ["Utah", "Arizona", "New Mexico", "Nevada"], "answer": "Utah", "fact": "Delicate Arch is the most famous feature."},
    {"question": "Olympic National Park is located in:", "options": ["Washington", "Oregon", "California", "Alaska"], "answer": "Washington", "fact": "It protects a vast temperate rainforest."},
    {"question": "Where is Shenandoah National Park located?", "options": ["Virginia", "West Virginia", "Kentucky", "Pennsylvania"], "answer": "Virginia", "fact": "It is long and narrow, with the Skyline Drive running its length."},
    {"question": "Hawaii Volcanoes National Park is on which island?", "options": ["Hawaii (The Big Island)", "Maui", "Oahu", "Kauai"], "answer": "Hawaii (The Big Island)", "fact": "It includes two active volcanoes: Kīlauea and Mauna Loa."},
    {"question": "Rocky Mountain National Park is in:", "options": ["Colorado", "Wyoming", "Utah", "Montana"], "answer": "Colorado", "fact": "The Continental Divide runs directly through the park."},
    {"question": "Joshua Tree National Park is located in:", "options": ["California", "Arizona", "Nevada", "New Mexico"], "answer": "California", "fact": "It is named after the Joshua trees (Yucca brevifolia) native to the Mojave Desert."},
    {"question": "Which state is home to Crater Lake National Park?", "options": ["Oregon", "Washington", "California", "Idaho"], "answer": "Oregon", "fact": "Crater Lake is the deepest lake in the United States."},
    {"question": "Where is Badlands National Park?", "options": ["South Dakota", "North Dakota", "Nebraska", "Wyoming"], "answer": "South Dakota", "fact": "It contains the world's richest fossil beds from the Oligocene epoch."},
    {"question": "Big Bend National Park is on the border of which state and Mexico?", "options": ["Texas", "Arizona", "New Mexico", "California"], "answer": "Texas", "fact": "It protects the largest protected area of Chihuahuan Desert topography."},
    {"question": "Where is Mammoth Cave National Park?", "options": ["Kentucky", "Tennessee", "Missouri", "West Virginia"], "answer": "Kentucky", "fact": "It is the longest known cave system in the world."},
    {"question": "Cuyahoga Valley National Park is in:", "options": ["Ohio", "Pennsylvania", "Michigan", "Indiana"], "answer": "Ohio", "fact": "It is the only national park in Ohio."},
    {"question": "Hot Springs National Park is in:", "options": ["Arkansas", "Missouri", "Oklahoma", "Tennessee"], "answer": "Arkansas", "fact": "It is nicknamed 'The American Spa'."},
    {"question": "Bryce Canyon National Park is found in:", "options": ["Utah", "Arizona", "Colorado", "Nevada"], "answer": "Utah", "fact": "It is famous for crimson-colored hoodoos (spire-shaped rock formations)."},
    {"question": "Where is Sequoia National Park?", "options": ["California", "Oregon", "Washington", "Nevada"], "answer": "California", "fact": "Home to General Sherman, the largest known living single-stem tree on Earth."},
    {"question": "Death Valley National Park is primarily in California and partially in:", "options": ["Nevada", "Arizona", "Utah", "Oregon"], "answer": "Nevada", "fact": "It holds the record for the highest air temperature ever recorded on Earth."},
    {"question": "Where is Haleakalā National Park?", "options": ["Hawaii (Maui)", "Hawaii (Oahu)", "Hawaii (Big Island)", "Hawaii (Kauai)"], "answer": "Hawaii (Maui)", "fact": "It protects the dormant Haleakalā volcano."},

    # --- NATIONAL PARK TRIVIA (20 Questions) ---
    {"question": "Which was the first National Park established in the US?", "options": ["Yellowstone", "Yosemite", "Acadia", "Grand Canyon"], "answer": "Yellowstone", "fact": "Established in 1872 by President Ulysses S. Grant."},
    {"question": "Which state has the MOST National Parks?", "options": ["California", "Alaska", "Utah", "Colorado"], "answer": "California", "fact": "California has 9 National Parks, Alaska has 8."},
    {"question": "Which National Park is the most visited annually?", "options": ["Great Smoky Mountains", "Grand Canyon", "Zion", "Yellowstone"], "answer": "Great Smoky Mountains", "fact": "It receives over 12 million visitors per year."},
    {"question": "Which National Park contains the geyser 'Old Faithful'?", "options": ["Yellowstone", "Yosemite", "Glacier", "Lassen Volcanic"], "answer": "Yellowstone", "fact": "It erupts every 44 to 125 minutes."},
    {"question": "Which park contains the monolithic rock 'El Capitan'?", "options": ["Yosemite", "Sequoia", "Zion", "Rocky Mountain"], "answer": "Yosemite", "fact": "El Capitan is about 3,000 feet from base to summit."},
    {"question": "Which park is known for its 'Hoodoos'?", "options": ["Bryce Canyon", "Arches", "Canyonlands", "Badlands"], "answer": "Bryce Canyon", "fact": "Hoodoos are tall, thin spires of rock."},
    {"question": "Which National Park protects the tallest trees in the world?", "options": ["Redwood", "Sequoia", "Yosemite", "Olympic"], "answer": "Redwood", "fact": "Hyperion, a coast redwood, stands over 379 feet tall."},
    {"question": "Which park is home to the 'Grand Prismatic Spring'?", "options": ["Yellowstone", "Hot Springs", "Lassen Volcanic", "Mammoth Cave"], "answer": "Yellowstone", "fact": "It is the largest hot spring in the US."},
    {"question": "What is the primary feature of Mesa Verde National Park?", "options": ["Cliff Dwellings", "Sand Dunes", "Glaciers", "Volcanoes"], "answer": "Cliff Dwellings", "fact": "It preserves the heritage of the Ancestral Pueblo people."},
    {"question": "Which park contains the lowest point in North America?", "options": ["Death Valley", "Joshua Tree", "Everglades", "Grand Canyon"], "answer": "Death Valley", "fact": "Badwater Basin is 282 feet below sea level."},
    {"question": "Which US National Park is the largest by area?", "options": ["Wrangell-St. Elias", "Death Valley", "Denali", "Yellowstone"], "answer": "Wrangell-St. Elias", "fact": "Located in Alaska, it is larger than Switzerland."},
    {"question": "Which US National Park is the smallest by area?", "options": ["Gateway Arch", "Hot Springs", "Indiana Dunes", "Virgin Islands"], "answer": "Gateway Arch", "fact": "Located in St. Louis, Missouri, it covers only 91 acres."},
    {"question": "Which park features the 'Going-to-the-Sun Road'?", "options": ["Glacier", "Rocky Mountain", "Shenandoah", "Mount Rainier"], "answer": "Glacier", "fact": "It is one of the most scenic drives in America."},
    {"question": "Which park is famous for the 'Narrows' hike?", "options": ["Zion", "Grand Canyon", "Bryce Canyon", "Arches"], "answer": "Zion", "fact": "Hikers travel through the Virgin River in a deep slot canyon."},
    {"question": "Which park preserves the 'General Sherman' tree?", "options": ["Sequoia", "Redwood", "Yosemite", "Kings Canyon"], "answer": "Sequoia", "fact": "By volume, it is the largest known living single-stem tree."},
    {"question": "Which park is home to 'Delicate Arch'?", "options": ["Arches", "Canyonlands", "Capitol Reef", "Zion"], "answer": "Arches", "fact": "It is depicted on the Utah license plate."},
    {"question": "Which park has a 'Rainforest' ecosystem within it?", "options": ["Olympic", "Yellowstone", "Grand Teton", "Badlands"], "answer": "Olympic", "fact": "The Hoh Rainforest receives 140 inches of rain a year."},
    {"question": "Which park is known for its bats and limestone formations?", "options": ["Carlsbad Caverns", "Wind Cave", "Mammoth Cave", "Acadia"], "answer": "Carlsbad Caverns", "fact": "It features the 'Big Room', a massive underground chamber."},
    {"question": "Which park contains 'Half Dome'?", "options": ["Yosemite", "Glacier", "Denali", "Grand Teton"], "answer": "Yosemite", "fact": "Hikers can use cables to ascend the final 400 feet."},
    {"question": "Which park is the only one located south of the equator?", "options": ["National Park of American Samoa", "Hawaii Volcanoes", "Virgin Islands", "Everglades"], "answer": "National Park of American Samoa", "fact": "It distributes across three islands: Tutuila, Ofu, and Ta‘ū."},

    # --- STATE GEOGRAPHY & POPULATION (25 Questions) ---
    {"question": "Which US state has the highest population?", "options": ["California", "Texas", "Florida", "New York"], "answer": "California", "fact": "California has approx 39 million residents."},
    {"question": "Which US state has the lowest population?", "options": ["Wyoming", "Vermont", "Alaska", "North Dakota"], "answer": "Wyoming", "fact": "Wyoming has fewer than 600,000 residents."},
    {"question": "Which is the largest US state by land area?", "options": ["Alaska", "Texas", "California", "Montana"], "answer": "Alaska", "fact": "Alaska is more than twice the size of Texas."},
    {"question": "Which is the smallest US state by land area?", "options": ["Rhode Island", "Delaware", "Connecticut", "Hawaii"], "answer": "Rhode Island", "fact": "Rhode Island is only about 1,214 square miles."},
    {"question": "Which state has the longest coastline?", "options": ["Alaska", "Florida", "California", "Hawaii"], "answer": "Alaska", "fact": "Alaska's coastline is longer than all other US states combined."},
    {"question": "Which state is known as the 'Sunshine State'?", "options": ["Florida", "California", "Arizona", "Hawaii"], "answer": "Florida", "fact": "Adopted as the official nickname by the legislature in 1970."},
    {"question": "Which state is known as the 'Golden State'?", "options": ["California", "Nevada", "Colorado", "Oregon"], "answer": "California", "fact": "Referring to the 1848 Gold Rush."},
    {"question": "Which state is known as the 'Lone Star State'?", "options": ["Texas", "Arizona", "New Mexico", "Oklahoma"], "answer": "Texas", "fact": "The single star represents Texas's history as an independent republic."},
    {"question": "Which state is known as the 'Empire State'?", "options": ["New York", "Virginia", "Pennsylvania", "Illinois"], "answer": "New York", "fact": "The Empire State Building is named after this nickname."},
    {"question": "Which state is nicknamed the 'Last Frontier'?", "options": ["Alaska", "Montana", "Wyoming", "Idaho"], "answer": "Alaska", "fact": "Due to its distance from the lower 48 and rugged terrain."},
    {"question": "Which state borders the most other states?", "options": ["Tennessee", "Texas", "California", "Nebraska"], "answer": "Tennessee", "fact": "Tennessee and Missouri both border 8 other states."},
    {"question": "Which state has the most active volcanoes?", "options": ["Alaska", "Hawaii", "Washington", "Oregon"], "answer": "Alaska", "fact": "Alaska has over 130 active volcanoes."},
    {"question": "Which state is the 'Aloha State'?", "options": ["Hawaii", "California", "Florida", "Alaska"], "answer": "Hawaii", "fact": "Aloha is a Hawaiian word for love, affection, peace, compassion and mercy."},
    {"question": "Which state is the 'Grand Canyon State'?", "options": ["Arizona", "Nevada", "Utah", "Colorado"], "answer": "Arizona", "fact": "The Grand Canyon is Arizona's most famous landmark."},
    {"question": "Which state is the 'Peach State'?", "options": ["Georgia", "South Carolina", "Alabama", "Florida"], "answer": "Georgia", "fact": "Georgia is famous for its high-quality peaches."},
    {"question": "Which state is nicknamed the 'Mount Rushmore State'?", "options": ["South Dakota", "North Dakota", "Montana", "Wyoming"], "answer": "South Dakota", "fact": "Mount Rushmore features the faces of four presidents."},
    {"question": "Which state is the 'Ocean State'?", "options": ["Rhode Island", "Massachusetts", "Maine", "Florida"], "answer": "Rhode Island", "fact": "Despite being the smallest state, it has over 400 miles of coastline."},
    {"question": "Which state is the 'Silver State'?", "options": ["Nevada", "Colorado", "California", "Montana"], "answer": "Nevada", "fact": "Named for the Comstock Lode silver discovery."},
    {"question": "Which state is the 'Beehive State'?", "options": ["Utah", "Idaho", "Ohio", "Kansas"], "answer": "Utah", "fact": "The beehive symbolizes industry and hard work."},
    {"question": "Which state is the 'Volunteer State'?", "options": ["Tennessee", "Kentucky", "Virginia", "North Carolina"], "answer": "Tennessee", "fact": "Earned during the War of 1812 due to the number of volunteer soldiers."},
    {"question": "Which state is the 'Magnolia State'?", "options": ["Mississippi", "Louisiana", "Alabama", "Georgia"], "answer": "Mississippi", "fact": "Named for the magnolia trees that grow there."},
    {"question": "Which state is the 'Gem State'?", "options": ["Idaho", "Montana", "Nevada", "Wyoming"], "answer": "Idaho", "fact": "Idaho produces 72 types of precious and semi-precious stones."},
    {"question": "Which state is the 'Treasure State'?", "options": ["Montana", "Idaho", "California", "Nevada"], "answer": "Montana", "fact": "Referring to its rich mineral reserves."},
    {"question": "Which state is the 'Land of 10,000 Lakes'?", "options": ["Minnesota", "Wisconsin", "Michigan", "Florida"], "answer": "Minnesota", "fact": "It actually has over 11,000 lakes."},
    {"question": "Which state is the 'Garden State'?", "options": ["New Jersey", "Delaware", "New York", "Connecticut"], "answer": "New Jersey", "fact": "Abraham Browning coined the term at the Centennial Exhibition in 1876."}
]

# ==========================================
# 2. APP LOGIC
# ==========================================

# Initialize Session State
if 'selected_quiz' not in st.session_state:
    # Randomly select 10 unique questions from the bank of 100
    st.session_state.selected_quiz = random.sample(QUIZ_BANK, 10)
    st.session_state.score = 0
    st.session_state.current_question_index = 0
    st.session_state.game_over = False

st.title("🇺🇸 The Great US Geography Challenge")
st.markdown("10 Questions. Random Topics. Can you get a perfect score?")
st.divider()

if not st.session_state.game_over:
    # Get the current question data
    index = st.session_state.current_question_index
    question_data = st.session_state.selected_quiz[index]
    
    # Display Progress
    st.subheader(f"Question {index + 1} of 10")
    st.progress((index) / 10)
    
    # Display Question
    st.markdown(f"### {question_data['question']}")
    
    # Display Options
    options = question_data['options']
    # Shuffle options so the position of the correct answer changes every time
    random.shuffle(options)
    
    col1, col2 = st.columns(2)
    for i, option in enumerate(options):
        # Determine column placement
        col = col1 if i % 2 == 0 else col2
        
        if col.button(option, use_container_width=True):
            # Check Answer
            if option == question_data['answer']:
                st.session_state.score += 1
                st.toast(f"✅ Correct! {question_data['fact']}", icon="🎉")
            else:
                st.toast(f"❌ Wrong! The correct answer was **{question_data['answer']}**.", icon="⚠️")
            
            # Advance Logic
            if st.session_state.current_question_index + 1 < 10:
                st.session_state.current_question_index += 1
                st.rerun()
            else:
                st.session_state.game_over = True
                st.rerun()

else:
    # ==========================================
    # 3. GAME OVER SCREEN
    # ==========================================
    final_score = st.session_state.score
    percentage = int((final_score / 10) * 100)
    
    st.header("🏁 Quiz Complete!")
    st.progress(100)
    
    # Visual Score
    st.metric(label="Your Score", value=f"{percentage}%", delta=f"{final_score}/10 Correct")
    
    # Feedback Messages
    if percentage == 100:
        st.balloons()
        st.success("🌟 You got a perfect score! You are a Geography Master!")
    elif percentage >= 80:
        st.success("🥈 Excellent work! You really know your stuff.")
    elif percentage >= 50:
        st.info("🥉 Not bad! You know the basics.")
    else:
        st.warning("🏕️ Good try! Do you want to play again?")
        
    st.divider()
    
    # Play Again Button
    if st.button("🔄 Play New Round (New Questions)", type="primary", use_container_width=True):
        # Reset state and pick 10 NEW random questions
        st.session_state.selected_quiz = random.sample(QUIZ_BANK, 10)
        st.session_state.score = 0
        st.session_state.current_question_index = 0
        st.session_state.game_over = False
        st.rerun()
