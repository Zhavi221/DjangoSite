import requests
from django.shortcuts import render

def members_list(request):

    curMembers = ['loser', 'ok']

    return render(request, 'discordTool/discordTool.html', {
		'members_list': curMembers,
	})
