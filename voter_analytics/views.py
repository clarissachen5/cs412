# File: voter_analytics/views.py
# Author: Clarissa Chen (clchen5@bu.edu), 10/30/2025
# Description: Configures views specific to voter_analytics app.

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Voter

import plotly
import plotly.graph_objs as go

from django.db.models import Q

# Create your views here.


class VotersListView(ListView):
    """View to display voter results."""

    model = Voter
    template_name = "voter_analytics/voters.html"
    context_object_name = "voters"
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["years"] = list(range(1920, 2005))
        return context

    def get_queryset(self):
        """limit the voters queryset based on search."""
        voters = super().get_queryset()

        filters = []

        if "party_affiliation" in self.request.GET:
            party_affiliation = self.request.GET["party_affiliation"]

            if party_affiliation:
                filters.append(Q(party_affiliation=party_affiliation))

        if "voter_score" in self.request.GET:
            voter_score = self.request.GET["voter_score"]

            if voter_score:
                filters.append(Q(voter_score=voter_score))

        if "min_birth_year" in self.request.GET:
            min_birth_year = self.request.GET["min_birth_year"]

            if min_birth_year:
                filters.append(Q(date_of_birth__year__gte=min_birth_year))

        if "max_birth_year" in self.request.GET:
            max_birth_year = self.request.GET["max_birth_year"]

            if max_birth_year:
                filters.append(Q(date_of_birth__year__lte=max_birth_year))

        if len(filters) > 0:
            query = filters[0]
            for i in range(1, len(filters)):
                query |= filters[i]
            voters = Voter.objects.filter(query)

        return voters


class VoterDetailView(DetailView):
    """Display information for a single voter."""

    model = Voter
    context_object_name = "v"  # short for Voter
    template_name = "voter_analytics/voter_detail.html"

    def get_context_data(self, **kwargs):
        """Provide context variables for use in the template."""

        context = super().get_context_data(**kwargs)
        v = context["v"]  # Result for one votter

        return context


class GraphListView(ListView):
    """View for displaying graphs."""

    model = Voter
    template_name = "voter_analytics/graphs.html"
    context_object_name = "voters"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        voters = context["voters"]
        birth_years = {}
        party_affiliations = {}
        election_participation = {
            "v20state": 0,
            "v21town": 0,
            "v21primary": 0,
            "v22general": 0,
            "v23town": 0,
        }
        for voter in voters:
            if voter.date_of_birth.year in birth_years:
                birth_years[voter.date_of_birth.year] += 1
            else:
                birth_years[voter.date_of_birth.year] = 1

            if voter.party_affiliation in party_affiliations:
                party_affiliations[voter.party_affiliation] += 1
            else:
                party_affiliations[voter.party_affiliation] = 1

            if voter.v20state:
                election_participation["v20state"] += 1
            if voter.v21town:
                election_participation["v21town"] += 1
            if voter.v21primary:
                election_participation["v21primary"] += 1
            if voter.v22general:
                election_participation["v22general"] += 1
            if voter.v23town:
                election_participation["v23town"] += 1

        birthYears = list(birth_years.keys())
        birthYearCounts = list(birth_years.values())

        fig = go.Bar(x=birthYears, y=birthYearCounts)
        title_text = "Voter Distribution by Year of Birth"
        graph_birth_years = plotly.offline.plot(
            {"data": [fig], "layout_title_text": title_text},
            auto_open=False,
            output_type="div",
        )
        context["graph_birth_years"] = graph_birth_years

        labels = list(party_affiliations.keys())
        values = list(party_affiliations.values())

        # generate the Pie chart:
        fig = go.Pie(labels=labels, values=values)
        title_text = "Voter Distribution by Party Affiliation"
        # obtain the graph as an HTML div
        graph_pie = plotly.offline.plot(
            {"data": [fig], "layout_title_text": title_text},
            auto_open=False,
            output_type="div",
        )

        context["graph_pie"] = graph_pie

        elections = list(election_participation.keys())
        electionCounts = list(election_participation.values())

        fig = go.Bar(x=elections, y=electionCounts)
        title_text = "Voter Count by Election"
        graph_elections = plotly.offline.plot(
            {"data": [fig], "layout_title_text": title_text},
            auto_open=False,
            output_type="div",
        )
        context["graph_elections"] = graph_elections

        return context

    def get_queryset(self):
        """limit the voters queryset based on search."""
        voters = super().get_queryset()

        filters = []

        if "party_affiliation" in self.request.GET:
            party_affiliation = self.request.GET["party_affiliation"]

            if party_affiliation:
                filters.append(Q(party_affiliation=party_affiliation))

        if "voter_score" in self.request.GET:
            voter_score = self.request.GET["voter_score"]

            if voter_score:
                filters.append(Q(voter_score=voter_score))

        if "min_birth_year" in self.request.GET:
            min_birth_year = self.request.GET["min_birth_year"]

            if min_birth_year:
                filters.append(Q(date_of_birth__year__gte=min_birth_year))

        if "max_birth_year" in self.request.GET:
            max_birth_year = self.request.GET["max_birth_year"]

            if max_birth_year:
                filters.append(Q(date_of_birth__year__lte=max_birth_year))

        if len(filters) > 0:
            query = filters[0]
            for i in range(1, len(filters)):
                query |= filters[i]
            voters = Voter.objects.filter(query)

        return voters
