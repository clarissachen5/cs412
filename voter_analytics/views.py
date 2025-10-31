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
