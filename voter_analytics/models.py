# File: voter_analytics/models.py
# Author: Clarissa Chen (clchen5@bu.edu), 10/30/2025
# Description: Defines the models for voter_analytics.
from django.db import models
from django.utils.dateparse import parse_date


# Create your models here.
class Voter(models.Model):
    """Store/represent the data from one voter in Newton, MA.
    Last Name, First Name,
    Residential Address (Street Number, Street Name, Apartment Number, Zip Code),
    Data of Birth, Date of Registration, Party Affiliation, Precinct Number,
    v20state, v21town, v21primary, v22general, v23town
    """

    last_name = models.TextField()
    first_name = models.TextField()
    res_add_street_num = models.TextField()
    res_add_street_name = models.TextField()
    res_add_apt_num = models.TextField(blank=True)
    res_add_zip_code = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_registration = models.DateField(null=True, blank=True)
    party_affiliation = models.CharField(max_length=2, blank=True)
    precinct_num = models.TextField(blank=True)

    v20state = models.BooleanField(default=False)
    v21town = models.BooleanField(default=False)
    v21primary = models.BooleanField(default=False)
    v22general = models.BooleanField(default=False)
    v23town = models.BooleanField(default=False)
    voter_score = models.TextField(blank=True)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"last_name: {self.last_name}, first_name: {self.first_name}"


def load_data():
    """Function to load data records from CSV file into the Django database."""
    Voter.objects.all().delete()
    filename = "/Users/clarissachen/Desktop/newton_voters.csv"
    f = open(filename, "r")
    f.readline()

    for line in f:
        try:
            fields = line.strip().split(",")
            # print(fields)
            voter = Voter(
                last_name=fields[1],
                first_name=fields[2],
                res_add_street_num=fields[3],
                res_add_street_name=fields[4],
                res_add_apt_num=fields[5],
                res_add_zip_code=fields[6],
                date_of_birth=parse_date(fields[7]),
                date_of_registration=parse_date(fields[8]),
                party_affiliation=fields[9],
                precinct_num=fields[10],
                v20state=True if fields[11] == "TRUE" else False,
                v21town=True if fields[12] == "TRUE" else False,
                v21primary=True if fields[13] == "TRUE" else False,
                v22general=True if fields[14] == "TRUE" else False,
                v23town=True if fields[15] == "TRUE" else False,
                voter_score=fields[16],
            )
            voter.save()  # commit this voter to the database
            print(f"Created voter: {voter}")

        except:
            print("Something went wrong")
            print(f"line={line}")
