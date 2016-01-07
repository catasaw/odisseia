from django.shortcuts import render, render_to_response

def issueview(request, issue_id):
    return render_to_response('forum/issue_view.html')
