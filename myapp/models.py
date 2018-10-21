from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from enum import Enum

# Create your models here.

## Proerty Category

class PropertyCategory(Enum):
    Single_House = "Single House"
    Attached_House = "Attached House"
    Town_House = "Town House"
    Apartment = "Apartment"
    Store = "Store"
    Farm = "Farm"
    Factory = "Factory"
    Mall = "Mall"
    Building = "Building"
    Other = "Other"


class Property_Category(models.Model):
    propertyCategory = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in PropertyCategory]
    )

## Property Sector

class PropertySector(Enum):
    Private = "Private"
    Residential = "Residential"
    Commercial = "Commercial"
    Government = "Government"
    Rural = "Rural"
    Other = "Other"


class Property_Sector(models.Model):
    propertySector = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in PropertySector]
    )

## Property_Facing

class PropertyFacing(Enum):
    North = "North"
    South = "South"
    East = "East"
    West = "West"
    Other = "Other"

class Property_Facing(models.Model):
    propertyFacing = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in PropertyFacing]
    )

class Property(models.Model):
    propertyID = models.IntegerField(unique=True, primary_key=True, auto_created=True)
    propertyTitle = models.CharField(max_length=50)
    propertyCategory = models.ForeignKey(Property_Category, null=False)
    propertySector = models.ForeignKey(Property_Sector, null=False)
    propertyFacing = models.ForeignKey(Property_Facing, null=False)