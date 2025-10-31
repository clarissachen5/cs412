# File: voter_analytics/views.py
# Author: Clarissa Chen (clchen5@bu.edu), 10/30/2025
# Description: Configures views specific to voter_analytics app.

from django.shortcuts import render
from django.views.generic import ListView
from .models import Voter

import plotly
import plotly.graph_objs as go

# Create your views here.


class VotersListView(ListView):
    """View to display voter results."""

    model = Voter
    template_name = "voter_analytics/voters.html"
    context_object_name = "voters"
    paginate_by = 100
