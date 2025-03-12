# fastapi is a frame use for creating api in python
from fastapi import FastAPI
import random

app = FastAPI()              # we store all the function of fastapi in app variable 
# now we will build two  simple get endpoints side_hustles and money_quotes

side_hustles = [
   " Freelance Web Development :Build websites for clients using HTML, CSS, JavaScript, and frameworks like Next.js.",
   "App Development : Create mobile or desktop apps for businesses and startups.",
   "UI/UX Design : Design user-friendly interfaces for websites and apps using Figma or Adobe XD.",
   "SEO Services : Help businesses rank higher on Google by optimizing their websites.",
   "Content Writing : Write blog posts, articles, and website content for businesses.",
   "Virtual Assistant : Assist business owners with emails, scheduling, and admin work remotely.",
   "Online Tutoring : Teach students subjects like math, programming, or languages.",
   "Graphic Design : Create logos, social media posts, and branding materials.",
   "Dropshipping : Sell products online without holding inventory.",
   "Affiliate Marketing : Earn commissions by promoting products via blogs or social media.",
]

money_quotes = [
   "The only way to do great work is to love what you do.",
   "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
   "Money is like gasoline during a road trip. You don't want to run out of gas on your way to success.",
   "The best way to predict the future is to invent it.",
   "The only thing worse than starting something and failing... is not starting something.",
   "The only way to do great work is to love what you do.",
   "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
   "Money is like gasoline during a road trip. You don't want to run out of gas on your way to success.",
   "The best way to predict the future is to invent it.",
   "The only thing worse than starting something and failing... is not starting something.",
]

@app.get("/side_hustles")
# Now we are making a function which help us to live our api endpoint
def get_side_hustles():
    """ Return a random side hustle idea"""               # Docstring explain the functions of python
    # if apikey != "1234567890":
    #     return{"error": "Invalid API key"}
    return{"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
    """ Return a random money quote """
    # if apikey != "1234567890":
    #     return{"error": "Invalid API key"}
    return{"money_quote": random.choice(money_quotes)}