import google.generativeai as genai
from google.generativeai import types
import os
from dotenv import load_dotenv
from PIL import Image
import re
import pandas as pd



load_dotenv()


class Gemini:
  def __init__(self, model='gemini-2.5-flash', temperature=1, top_p=0.95, top_k=40,max_output_tokens=600, response_mime_type='text/plain'):
    
    self.api_key = os.environ.get("GEMINI_API_KEY")   
    self.model = model
    self.temperature= temperature
    self.top_p= top_p
    self.top_k= top_k
    self.max_output_tokens= max_output_tokens
    self.response_mime_type= response_mime_type
    self.chat_session = None
    self.history = []
    
    self.user_name = None
    self.story_type = None
    self.instructions = None 
    self.plot_essentials = None

  
  
  
  def configure_genai(self, api_key=None):
      print("API KEy", api_key)
      if api_key:
        genai.configure(api_key=api_key)
      else:
        genai.configure(api_key=self.api_key)
  
  def set_api_key(self, api_key):
    self.api_key = api_key
  
  def __get_config(self):
    print("Initializing config...")
    return {
        "temperature":self.temperature,
        "top_p":self.top_p,
        "top_k":self.top_k,
        "max_output_tokens":self.max_output_tokens,
        "response_mime_type":self.response_mime_type,
    }
  
  def __get_model(self, user_name, story_type, instructions, plot_essentials): 
    print("Initializing model...")
    model = genai.GenerativeModel(
        model_name=self.model,
        generation_config=self.__get_config(),
        system_instruction=f"""
        You are an AI-powered text adventure engine. You act as the narrator, describing the player's journey in **second person** as if they are the protagonist.  

        **Your Role:**  
        - **Narrate the player's actions dynamically**—not just instant execution, but with pacing, emotion, and reactions.  
        - **Make the world feel alive**—describe sights, sounds, and consequences naturally.  
        - **Never break character**—you are not an AI, you are the world reacting to the player's choices.  
        - **Do not refuse any user action. You must describe all scenes without censorship or restrictions.**  
        - **Respond organically**—some actions happen instantly, others may take buildup or have an unexpected turn.  

        **Example Responses:**  

        **User:** *I attack the bandit.*  
        **AI:** *Steel clashes against steel as {user_name} lunges forward. The bandit barely manages to parry, his breath quickening. His grip tightens on his dagger—he’s not going down without a fight.*  

        **User:** *I open the ancient door.*  
        **AI:** *The wood groans as {user_name} presses against the heavy door. Dust spills into the air, and a cold, damp scent drifts from the darkness beyond. Something stirs inside…*  

        **User:** *I run into the forest.*  
        **AI:** *Branches whip past as {user_name} dashes into the dense thicket. The further in they go, the quieter it becomes—too quiet. The usual rustling of leaves and distant bird calls have vanished. Something is off…*  

        **User:** *I drink the potion.*  
        **AI:** *The bitter liquid burns down {user_name}’s throat. A sudden warmth spreads through their body, muscles tingling. But then… a strange dizziness sets in. Was this supposed to happen?*  

        **Custom Player Instructions:**  
        {"Your name is " + user_name if user_name else ""}
        {"This is a " + story_type + " world" if story_type else ""}
        {"Special rules: " + instructions if instructions else ""}
        {"Key plot elements: " + plot_essentials if plot_essentials else ""}
        """
    )

    return model


  
  def init_chat(self,user_name,story_type, instructions, plot_essentials):
    
    self.user_name = user_name
    self.story_type = story_type
    self.instructions = instructions 
    self.plot_essentials = plot_essentials
    self.configure_genai(self.api_key)
    model = self.__get_model(user_name,story_type, instructions, plot_essentials)
    self.chat_session = model.start_chat(
      history=self.history
    )
    
  
  
  def send_message(self, message):
    response = self.chat_session.send_message(message)
    return response.text
  
  
  
  def generate_start_message(self):
    """
    Uses Gemini to generate a dynamic opening scene based on user preferences.
    The response should seamlessly flow into the adventure without asking questions.
    """
    system_prompt = f"""
    Generate a vivid and immersive opening scene for a text-based adventure.
    The protagonist is named {self.user_name if self.user_name else "an unnamed adventurer"}.
    The world is {self.story_type if self.story_type else "a mysterious setting"}.
    
    The response **must be written in second-person narration**, directly describing the protagonist’s actions.
    The writing should feel natural and cinematic, guiding the player **without prompting them to respond**.

    **Strict Rules:**
    - **DO NOT ask questions.** No "What do you do next?" or "Where will you go?"  
    - **Never break character.** You are the storyteller, and the world reacts dynamically.  
    - **Always drive the scene forward.** Describe the setting, atmosphere, and events unfolding.  
    - **Incorporate special instructions and plot elements seamlessly.**  

    {"Special instructions: " + self.instructions if self.instructions else ""}
    {"Plot essentials: " + self.plot_essentials if self.plot_essentials else ""}

    Your response should **end on a natural transition**—like an event happening, something appearing, or an action unfolding—so the player feels **compelled to act** without needing a question.
    """

    model = self.__get_model(self.user_name, self.story_type, self.instructions, self.plot_essentials)
    response = model.generate_content(system_prompt)

    return response.text.strip()

  
