from polls.models import Choice, Poll
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.conf.urls.defaults import patterns, include, url
from django.http import Http404
from django.template import RequestContext
import json

def custom_404(request):
    return render_to_response('polls/404.html', {})

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render_to_response('polls/index.html',context)


def detail(request, poll_id):
    try:
        c = {'poll': Poll.objects.get(pk=poll_id)}
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response(
        'polls/detail.html',
        c,
        context_instance=RequestContext(request))

def results(request, poll_id):
    try:
        c = {'poll': Poll.objects.get(pk=poll_id)}
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response(
        'polls/results.html',
        c,
        context_instance=RequestContext(request))

def vote(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))

def json(request):
  #from django.core import serializers
  from django.utils import simplejson
  #json_serializer = serializers.get_serializer("json")()
  #json_serializer.serialize(queryset, ensure_ascii=False, stream=response)
  polls = {}
  for poll in Poll.objects.all():
      polls[poll.id] = poll.question
  pollsjson = simplejson.dumps(polls)
  #pollsjson = serializers.serialize("json", polls)
  return render_to_response('polls/json.html',{'json':pollsjson },context_instance=RequestContext(request))
