# -*- coding: utf-8 -*-
"""medicine_dataset_extraction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BAHnzr1oOVzdhs7TNFt5bwSGAEtreP6W
"""

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def get_medicine(new_soups):

  content = ""

  try:

    medicine_section = new_soups.find('h2', class_='ddc-pronounce-title')

    if medicine_section:

        content = []

        for sibling in medicine_section.find_next_siblings():

            if sibling.name and sibling.name.startswith('h'):

                break

            content.append(sibling.text.strip())

  except AttributeError:

    content = ""

  return content

def get_uses(new_soups):

  content = ""

  try:

    uses_section = new_soups.find('h2', id='uses')

    if uses_section:

        content = []

        for sibling in uses_section.find_next_siblings():

            if sibling.name and sibling.name.startswith('h'):

                break

            content.append(sibling.text.strip())

  except AttributeError:

    content = ""

  return content

def get_side_effects(new_soups):

  content = ""

  try:

    side_effects_section = new_soups.find('h2', id='side-effects')

    if side_effects_section:

        content = []

        for sibling in side_effects_section.find_next_siblings():

            if sibling.name and sibling.name.startswith('h'):

                break

            content.append(sibling.text.strip())

  except AttributeError:

    content = ""

  return content

def get_warnings(new_soups):

  content = ""

  try:

    warnings_section = new_soups.find('h2', id='warnings')

    if warnings_section:

        content = []

        for sibling in warnings_section.find_next_siblings():

            if sibling.name and sibling.name.startswith('h'):

                break

            content.append(sibling.text.strip())

  except AttributeError:

    content = ""

  return content

def get_cost(new_soups):

  content = ""

  try:

    cost_section = new_soups.find('h2', id='cost')

    if cost_section:

        content = []

        for sibling in cost_section.find_next_siblings():

            if sibling.name and sibling.name.startswith('h'):

                break

            content.append(sibling.text.strip())

  except AttributeError:

    content = ""

  return content

def get_before_taking(new_soups):

  content = ""

  try:

    before_taking_section = new_soups.find('h2', id='before-taking')

    if before_taking_section :

        content = []

        for sibling in before_taking_section.find_next_siblings():

            if sibling.name and sibling.name.startswith('h'):

                break

            content.append(sibling.text.strip())

  except AttributeError:

    content = ""

  return content

def get_directions(new_soups):

  content = ""

  try:

    directions_section = new_soups.find('h2', id='directions')

    if directions_section:

        content = []

        for sibling in directions_section.find_next_siblings():

            if sibling.name and sibling.name.startswith('h'):

                break

            content.append(sibling.text.strip())

  except AttributeError:

    content = ""

  return content

def get_dosage(new_soups):

  content = ""

  try:

    dosage_section = new_soups.find('h2', id='dosage')

    if dosage_section:

        content = []

        for sibling in dosage_section.find_next_siblings():

            if sibling.name and sibling.name.startswith('h'):

                break

            content.append(sibling.text.strip())

  except AttributeError:

    content = ""

  return content

URL = "https://www.drugs.com/"

webpage = requests.get(URL)

d = {"medicine":[], "uses":[], "side effects":[], "warnings":[], "cost":[], "before taking":[], "directions":[], "dosage":[]}

soup = BeautifulSoup(webpage.content, "html.parser")

links=soup.find_all("a",attrs={'class':'ddc-paging-item'})

new_links = []

for link in links:

  link=link.get('href')

  product_list='https://www.drugs.com/'+link

  new_webpage=requests.get(product_list)

  new_soup=BeautifulSoup(new_webpage.content,'html.parser')

  new_links.extend(new_soup.select("ul.ddc-list-column-2 a"))

for new_link in new_links:

  new_href = new_link.get('href')

  new_product_list = 'https://www.drugs.com/' + new_href

  new_webpages=requests.get(new_product_list)

  new_soups=BeautifulSoup(new_webpages.content,'html.parser')

  d['medicine'].append(get_medicine(new_soups))

  d['uses'].append(get_uses(new_soups))

  d['side effects'].append(get_side_effects(new_soups))

  d['warnings'].append(get_warnings(new_soups))

  d['cost'].append(get_cost(new_soups))

  d['before taking'].append(get_before_taking(new_soups))

  d['directions'].append(get_directions(new_soups))

  d['dosage'].append(get_dosage(new_soups))

medicine_df = pd.DataFrame.from_dict(d)

medicine_df.to_csv('medicine_data.csv', index=False)

medicine_df

from google.colab import files
files.download("medicine_data.csv")

